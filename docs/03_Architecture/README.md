
---

# 🏗️ `03_Architecture/System_Architecture.md`

```markdown
# 🏗️ RetailVisionAI System Architecture

## 🎯 Architecture Overview

RetailVisionAI consists of several components that work together to capture customer attention data and convert it into meaningful analytics.

```text
                  🎥 Webcam
                      │
                      ▼
               ┌──────────────┐
               │    OpenCV    │
               └──────┬───────┘
                      │
                      ▼
               ┌──────────────┐
               │  MediaPipe   │
               │   Landmarks  │
               └──────┬───────┘
                      │
                      ▼
               ┌──────────────┐
               │  Head Pose   │
               │  Estimation  │
               └──────┬───────┘
                      │
                      ▼
               ┌──────────────┐
               │  Attention   │
               │    Logic     │
               └──────┬───────┘
                      │
                      ▼
               ┌──────────────┐
               │   Session    │
               │   Metrics    │
               └──────┬───────┘
                      │
                      ▼
               ┌──────────────┐
               │    SQLite    │
               │   Database   │
               └──────┬───────┘
                      │
                      ▼
               ┌──────────────┐
               │   Analytics  │
               └──────┬───────┘
                      │
                      ▼
               ┌──────────────┐
               │  Streamlit   │
               │   Dashboard  │
               └──────────────┘


🧩 System Components
🎥 OpenCV

Responsible for webcam access, video capture and frame processing.

🧠 MediaPipe

Responsible for detecting facial landmarks from the captured video frames.

🧭 Head Pose Estimation

Uses facial landmark information to estimate head orientation using yaw, pitch and roll.

👀 Attention Detection

Determines whether the person is attentive or looking away based on the estimated head direction.

⏱️ Session Tracking

Records attentive time, looking away time and overall session duration.

🗄️ SQLite Database

Stores completed monitoring sessions for later analysis.

📊 Analytics Module

Processes stored session data and calculates summary statistics.

📈 Streamlit Dashboard

Provides an interactive interface for viewing customer attention analytics.

🔁 Data Flow
🎥 Video Input
      ↓
🧠 Computer Vision Processing
      ↓
👀 Attention Detection
      ↓
⏱️ Session Measurement
      ↓
🗄️ Data Storage
      ↓
📊 Data Analysis
      ↓
📈 Business Dashboard
