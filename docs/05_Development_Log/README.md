
---

# 🛠️ `05_Development_Log/Development_Log.md`

```markdown
# 🛠️ RetailVisionAI Development Log

## 📅 Phase 1: Project Planning

Defined the objective of building a computer vision based system for analyzing customer attention in a retail environment.

## ⚙️ Phase 2: Project Setup

Created the Python project structure and configured the virtual environment and required packages.

## 🎥 Phase 3: Webcam Integration

Implemented webcam capture using OpenCV.

The system was tested to ensure that live video frames could be captured successfully.

## 🧠 Phase 4: Facial Landmark Detection

Integrated MediaPipe for facial landmark detection.

Facial landmarks were used as the basis for further head pose analysis.

## 🧭 Phase 5: Head Pose Estimation

Implemented head orientation analysis using facial landmark information.

Yaw, pitch and roll values were used to estimate head direction.

## 👀 Phase 6: Attention Detection

Implemented logic to determine whether the person was attentive or looking away.

The system records the amount of time spent in each state.

## ⏱️ Phase 7: Session Tracking

Added session tracking to calculate:

• ⏱️ Attentive time  
• ↩️ Looking away time  
• 🕐 Session duration  
• 📊 Attention rate  

## 🗄️ Phase 8: Database Integration

Implemented SQLite database storage for completed monitoring sessions.

## 📊 Phase 9: Analytics

Created the analytics module to calculate overall statistics from stored sessions.

The analytics include:

• Total sessions  
• Average attention rate  
• Average attentive time  
• Average looking away time  
• Highest attention rate  
• Lowest attention rate  

## 📈 Phase 10: Streamlit Dashboard

Created an interactive Streamlit dashboard displaying key metrics, attention trends, attentive versus looking away time and session history.

## 🧪 Phase 11: Testing

Tested the complete system using multiple monitoring sessions.

Verified that session results were successfully stored in SQLite and displayed correctly in the dashboard.

## 🧹 Phase 12: Final Cleanup

Removed unused Python modules and unnecessary project files.

Updated the README and requirements file and prepared the GitHub repository for submission.

## ✅ Final Status

RetailVisionAI is successfully running with:

• 🎥 Working webcam monitoring  
• 🧠 MediaPipe facial landmark processing  
• 🧭 Head direction estimation  
• 👀 Attention detection  
• ⏱️ Session tracking  
• 🗄️ SQLite storage  
• 📊 Analytics  
• 📈 Streamlit dashboard
