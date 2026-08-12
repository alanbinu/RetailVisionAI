
---

# 🎤 `04_Interview_Questions/Interview_Questions.md`

```markdown
# 🎤 RetailVisionAI Interview Questions

This document contains common technical and project related questions that may be asked during a project presentation or viva.

## 🛍️ Project Understanding

### ❓ 1. What is RetailVisionAI?

RetailVisionAI is a computer vision based customer attention analytics system that estimates customer attention using facial landmarks and head pose information.

### ❓ 2. What problem does the project solve?

The project demonstrates how customer attention around retail displays can be monitored and converted into measurable analytics instead of relying only on manual observation.

## 🧠 Computer Vision

### ❓ 3. Why did you use MediaPipe?

MediaPipe provides facial landmark detection that can be used to identify important points on the face.

### ❓ 4. Why did you use OpenCV?

OpenCV is used for webcam access, video capture and image processing.

### ❓ 5. What are facial landmarks?

Facial landmarks are specific points detected on a person's face that describe important facial features and their positions.

## 🧭 Head Pose

### ❓ 6. What is head pose estimation?

Head pose estimation determines the orientation of a person's head.

### ❓ 7. What is yaw?

Yaw represents horizontal head rotation, such as turning the head left or right.

### ❓ 8. What is pitch?

Pitch represents vertical head movement, such as looking up or down.

### ❓ 9. What is roll?

Roll represents tilting the head toward the left or right shoulder.

## 👀 Attention

### ❓ 10. How does the system determine attention?

The system uses estimated head direction to determine whether the person is facing the monitoring area or looking away.

### ❓ 11. How is attention rate calculated?

```text
Attention Rate = Attentive Time / Total Session Time × 100


❓ 12. Does attention rate directly measure customer interest?

No. The current system estimates attention based primarily on head orientation. It does not directly measure psychological interest or purchase intention.

🗄️ Database
❓ 13. Why did you use SQLite?

SQLite is lightweight, does not require a separate database server and is suitable for this prototype.

❓ 14. What information is stored?

The database stores session information including start time, end time, attentive time, looking away time and attention rate.

📊 Dashboard
❓ 15. Why did you use Streamlit?

Streamlit allows Python based data and analytics applications to be converted into interactive web dashboards quickly.

❓ 16. What does the dashboard display?

The dashboard displays:

• 📌 Total sessions
• 📊 Average attention
• ⏱️ Average attentive time
• ↩️ Average looking away time
• 📈 Attention rate by session
• 📊 Attentive versus looking away time
• 📋 Session history

🚀 Future Improvements
❓ 17. What are the limitations?

The system can be affected by lighting conditions, camera position, face visibility and head movement.

❓ 18. What could be added in the future?

Future versions could include:

• 👥 Multiple person tracking
• 🔢 Customer counting
• 📍 Improved tracking
• ☁️ Cloud based analytics
• 📊 More advanced business intelligence
• 🤖 Improved attention estimation
