# 🎓 RetailVisionAI Presentation Notes

## 🏷️ Project Title

# 🛍️ RetailVisionAI

### Smart Retail Customer Attention Analytics System

---

## 🎯 Problem Statement

Retail businesses need ways to understand whether customers are paying attention to displays, advertisements and promotional areas.

Traditional observation can be manual and difficult to quantify.

RetailVisionAI demonstrates how computer vision can be used to collect customer attention related measurements automatically.

---

## 💡 Proposed Solution

The system uses a webcam, OpenCV and MediaPipe to analyze facial landmarks and estimate head direction.

The system records attentive time and looking away time during each monitoring session.

The results are stored in SQLite and presented through an interactive Streamlit dashboard.

---

## 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Core programming language |
| 👁️ OpenCV | Webcam and image processing |
| 🧠 MediaPipe | Facial landmark detection |
| 🔢 NumPy | Numerical processing |
| 🐼 Pandas | Data analysis |
| 🗄️ SQLite | Session data storage |
| 📈 Streamlit | Analytics dashboard |

---

## 📊 Main Outputs

The system produces:

• ⏱️ Attentive time  
• ↩️ Looking away time  
• 📊 Attention rate  
• 🕐 Session duration  
• 📋 Session history  
• 📈 Overall analytics  

---

## 📈 Dashboard

The Streamlit dashboard provides:

• 📌 Total sessions  
• 📊 Average attention  
• ⏱️ Average attentive time  
• ↩️ Average looking away time  
• 📈 Attention rate by session  
• 📊 Attentive versus looking away time  
• 📋 Session history  

---

## 🏢 Potential Business Applications

The concept could be extended to:

🛍️ Retail product displays

📺 Advertising screens

🏷️ Promotional counters

🛒 Customer engagement analysis

📊 Store level analytics

---

## 🚀 Future Scope

Future versions could include:

• 👥 Multiple person tracking  
• 🔢 Customer counting  
• 🧭 Improved head pose estimation  
• 📊 Advanced business intelligence  
• ☁️ Cloud based storage  
• 🤖 More advanced attention models  

---

## 🏁 Conclusion

RetailVisionAI demonstrates how computer vision can transform visual observations into measurable customer attention analytics.

The project provides a working prototype that connects computer vision, data storage and business analytics into a single system.
