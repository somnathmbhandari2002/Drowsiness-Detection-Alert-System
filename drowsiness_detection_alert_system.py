import cv2
import mediapipe as mp
import time
import pyttsx3
import numpy as np

# Initialize Mediapipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to calculate Eye Aspect Ratio (EAR)
def eye_aspect_ratio(landmarks, eye_points):
    A = np.linalg.norm(np.array(landmarks[eye_points[1]]) - np.array(landmarks[eye_points[5]]))
    B = np.linalg.norm(np.array(landmarks[eye_points[2]]) - np.array(landmarks[eye_points[4]]))
    C = np.linalg.norm(np.array(landmarks[eye_points[0]]) - np.array(landmarks[eye_points[3]]))
    ear = (A + B) / (2.0 * C)
    return ear

# Eye landmark indices from Mediapipe
LEFT_EYE = [33, 160, 158, 133, 153, 144]  # Left eye landmarks
RIGHT_EYE = [362, 385, 387, 263, 373, 380]  # Right eye landmarks

# Thresholds
EAR_THRESHOLD = 0.25  # Eye closed threshold
CLOSED_TIME_THRESHOLD = 3  # Time in seconds

# Capture video
cap = cv2.VideoCapture(0)
start_time = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to RGB for Mediapipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            landmarks = {i: (int(pt.x * frame.shape[1]), int(pt.y * frame.shape[0])) 
                         for i, pt in enumerate(face_landmarks.landmark)}

            # Compute EAR for both eyes
            left_ear = eye_aspect_ratio(landmarks, LEFT_EYE)
            right_ear = eye_aspect_ratio(landmarks, RIGHT_EYE)
            avg_ear = (left_ear + right_ear) / 2.0

            # Check if eyes are closed
            if avg_ear < EAR_THRESHOLD:
                if start_time is None:
                    start_time = time.time()  # Start timer
                elapsed_time = time.time() - start_time

                if elapsed_time >= CLOSED_TIME_THRESHOLD:
                    print("Wake up! Don't sleep.")
                    engine.say("Wake up! Don't sleep.")
                    engine.runAndWait()
                    start_time = None  # Reset timer
            else:
                start_time = None  # Reset timer if eyes are open

            # Draw landmarks on eyes
            for point in LEFT_EYE + RIGHT_EYE:
                cv2.circle(frame, landmarks[point], 2, (0, 255, 0), -1)

    # Display output
    cv2.imshow("Eye Tracking", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
