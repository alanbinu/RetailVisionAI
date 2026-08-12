
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
