
---

# 🔄 `02_Flowcharts/System_Flow.md`

```markdown
# 🔄 RetailVisionAI System Flow

## 🎯 Processing Pipeline

The RetailVisionAI system follows the pipeline below:

```text
🎥 Webcam
     ↓
🖼️ Capture Video Frame
     ↓
👤 Face Detection
     ↓
📍 Facial Landmark Detection
     ↓
🧭 Head Pose Estimation
     ↓
👀 Attention Detection
     ↓
⏱️ Session Metrics
     ↓
🗄️ SQLite Database
     ↓
📊 Analytics
     ↓
📈 Streamlit Dashboard


🔍 Attention Detection Flow

🎥 Capture Frame
       ↓
👤 Detect Face
       ↓
📍 Detect Facial Landmarks
       ↓
🧭 Estimate Head Direction
       ↓
❓ Is the person facing the monitoring area?
       ↓
   ┌───────────┴───────────┐
   ↓                       ↓
✅ Yes                    ❌ No
   ↓                       ↓
⏱️ Record                 ⏱️ Record
Attentive Time            Looking Away Time
   ↓                       ↓
   └───────────┬───────────┘
               ↓
        📊 Calculate Metrics
               ↓
        🗄️ Save Session
               ↓
        📈 Display Analytics
