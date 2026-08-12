# RetailVisionAI

## Smart Retail Customer Attention Analytics System

RetailVisionAI is a computer vision based customer attention analytics system built using Python, MediaPipe, OpenCV, SQLite, and Streamlit.

The system uses facial landmarks and head pose estimation to estimate whether a person is facing the camera or looking away. It measures attentive time, looking away time, and calculates an overall attention rate for each monitoring session.

The collected session data is stored in a SQLite database and presented through an interactive Streamlit analytics dashboard.

---

## Project Objective

The main objective of RetailVisionAI is to demonstrate how computer vision can be used to collect customer attention related data and convert it into useful analytics.

The system can be used as a prototype for retail environments where businesses may want to understand customer engagement patterns around displays, counters, advertisements, or product areas.

---

## How the System Works

The system follows this process:

Webcam

↓

MediaPipe Facial Landmarks

↓

Head Pose Estimation using solvePnP

↓

Head Direction Detection

↓

Attention Estimation

↓

Session Time Tracking

↓

SQLite Database

↓

Analytics

↓

Streamlit Dashboard

---

## Main Features

### 1. Face Landmark Detection

MediaPipe is used to detect facial landmarks from the webcam feed.

### 2. Head Pose Estimation

OpenCV solvePnP is used with selected facial landmarks to estimate head orientation.

The system calculates:

- Yaw
- Pitch
- Roll

### 3. Head Direction Detection

The system classifies the detected head orientation into:

- CENTER
- LEFT
- RIGHT

### 4. Attention Estimation

When the person is facing the camera, the system considers the person attentive.

When the person turns away, the system considers the person to be looking away.

### 5. Time Tracking

The system records:

- Attentive time
- Looking away time
- Total session time

### 6. Attention Rate

The system calculates attention rate using:

Attention Rate = Attentive Time / Total Session Time × 100

### 7. SQLite Database

Each monitoring session is stored in a SQLite database.

The database stores:

- Session ID
- Start time
- End time
- Attentive time
- Looking away time
- Attention rate

### 8. Analytics

The analytics module calculates:

- Total sessions
- Average attention rate
- Average attentive time
- Average looking away time
- Highest attention rate
- Lowest attention rate

### 9. Streamlit Dashboard

The dashboard provides:

- Total session count
- Average attention rate
- Average attentive time
- Average looking away time
- Attention rate by session
- Attentive time versus looking away time
- Session history

---

## Technology Stack

- Python
- OpenCV
- MediaPipe
- NumPy
- Pandas
- SQLite
- Streamlit

---

## Project Structure

```text
RetailVisionAI/
│
├── assets/
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── csv/
│   └── database/
│       └── retailvision.db
│
├── docs/
│   ├── 01_Theory/
│   ├── 02_Flowcharts/
│   ├── 03_Architecture/
│   ├── 04_Interview_Questions/
│   ├── 05_Development_Log/
│   └── 06_Presentation/
│
├── modules/
│   ├── analytics.py
│   ├── camera.py
│   ├── config.py
│   ├── database.py
│   ├── developer_mode.py
│   ├── face_detector.py
│   ├── hand_detector.py
│   ├── heatmap.py
│   ├── pose_detector.py
│   ├── tracker.py
│   └── utils.py
│
├── screenshots/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore