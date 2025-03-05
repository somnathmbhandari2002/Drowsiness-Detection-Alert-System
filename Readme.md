# 💤 Drowsiness Detection Alert System

## 📌 Overview
This project detects **eye closure** using Mediapipe FaceMesh and calculates the **Eye Aspect Ratio (EAR)**.  
If the user's eyes remain **closed for more than 3 seconds**, the system will **play a voice alert** to wake them up.  

## 🚀 Features
- 👁️ **Tracks eye movements** in real-time  
- ⏳ **Detects prolonged eye closure (3 sec)**  
- 🔊 **Voice alert: "Wake up! Don't sleep."**  
- 🎯 Uses **Mediapipe**, **OpenCV**, and **pyttsx3**  

---

## 🛠️ Installation

### 1️⃣ Install Dependencies  
Run the following command:  

```bash
pip install opencv-python mediapipe pyttsx3 numpy

⚙️ Workflow
Capture webcam video using OpenCV.
Detect facial landmarks with Mediapipe.
Extract eye landmarks and calculate the Eye Aspect Ratio (EAR).
If EAR drops below 0.25 (eyes closed):
Start the timer
If closed for 3 seconds, play voice alert
If eyes open before 3 seconds, the timer resets.

#---------------------------------------------------------------------------------------------------------------------------------------

📜 Code Explanation
1️⃣ Eye Tracking Setup
Uses Mediapipe FaceMesh to track 468 facial landmarks.
Identifies left and right eye landmarks for EAR calculation.
2️⃣ Eye Aspect Ratio (EAR) Calculation
Formula:
EAR = (vertical_distance_1 + vertical_distance_2) / (2 * horizontal_distance)
If EAR < 0.25, it indicates closed eyes.

3️⃣ Alert Mechanism
Timer starts when eyes close.
If eyes remain closed for ≥3 seconds, it triggers:
engine.say("Wake up! Don't sleep.")
engine.runAndWait()
Timer resets when eyes reopen.

🏆 Use Cases
🚗 Driver Drowsiness Detection
🖥️ Computer User Fatigue Alert
🏫 Student Attention Monitoring
📌 Controls
Press ESC to exit.

📧 Contact
🔗 GitHub: (https://github.com/somnathmbhandari2002/Drowsiness-Detection-Alert-System)
✉️ Email: somnathjogi20@gmail.com
