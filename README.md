# 🛍️ RetailVisionAI

## Smart Retail Customer Attention Analytics System

RetailVisionAI is a computer vision based customer attention analytics system designed to understand how long a person remains attentive to a retail display or visual area.

The system uses facial landmarks and head pose estimation to determine whether a person is facing the camera or looking away. Session results are stored in SQLite and presented through an interactive Streamlit dashboard.

---

## 🎯 Project Objective

The objective of RetailVisionAI is to demonstrate how computer vision can be used to collect customer attention related data and convert that data into meaningful business analytics.

The system can serve as a prototype for retail environments where businesses want to understand customer engagement around product displays, advertisements, counters, or promotional areas.

---

## ✨ Key Features

- 👤 Facial landmark detection using MediaPipe
- 🎥 Real time webcam based monitoring
- 🧭 Head direction detection
- 👀 Attention and looking away detection
- ⏱️ Attentive time calculation
- 📊 Attention rate calculation
- 💾 SQLite based session storage
- 📈 Interactive Streamlit analytics dashboard
- 📋 Session history and performance analysis

---

## 🧠 How It Works

The system follows a simple computer vision pipeline:

```text
Webcam
   ↓
OpenCV
   ↓
MediaPipe Facial Landmarks
   ↓
Head Pose Estimation
   ↓
Attention Detection
   ↓
Session Metrics
   ↓
SQLite Database
   ↓
Analytics
   ↓
Streamlit Dashboard

```

---

## 📊 Analytics Dashboard

The project includes an interactive Streamlit dashboard for analyzing the collected customer attention sessions.

The dashboard provides:

| Metric | Description |
|---|---|
| Total Sessions | Number of monitoring sessions |
| Average Attention | Average attention rate across sessions |
| Average Attentive Time | Average time spent attentive |
| Average Looking Away | Average time spent looking away |
| Attention Rate by Session | Attention performance across sessions |
| Session History | Detailed session records |

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| OpenCV | Webcam and image processing |
| MediaPipe | Facial landmark detection |
| NumPy | Numerical calculations |
| SQLite | Session data storage |
| Pandas | Data analysis |
| Streamlit | Interactive dashboard |

---

## 📁 Project Structure

```text
RetailVisionAI/
│
├── assets/
├── dashboard/
│   └── app.py
├── data/
│   └── database/
│       └── retailvision.db
├── docs/
├── modules/
│   ├── analytics.py
│   └── database.py
├── screenshots/
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/alanbinu/RetailVisionAI.git
cd RetailVisionAI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment on Windows

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install the required packages

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Start RetailVisionAI

```bash
python main.py
```

The webcam will open and the system will begin monitoring attention.

After the session ends, the collected session metrics are stored in the SQLite database.

### Start the Analytics Dashboard

Open another terminal while the virtual environment is active and run:

```bash
streamlit run dashboard/app.py
```

The Streamlit dashboard will open in your browser.

---

## 📈 Example Results

Example analytics generated during project testing:

```text
Total Sessions: 9

Average Attention Rate: 63.0%

Average Attentive Time: 18.1 seconds

Average Looking Away Time: 10.0 seconds

Highest Attention Rate: 100.0%

Lowest Attention Rate: 40.2%
```

These results are generated from actual monitoring sessions stored in the project's SQLite database.

---

## 💼 Business Use Case

RetailVisionAI demonstrates how computer vision can be used to collect customer attention data and convert it into useful business insights.

Potential applications include:

* Customer engagement analysis
* Product display evaluation
* Advertisement attention analysis
* Promotional area analysis
* Retail counter engagement
* Visual merchandising analysis

The current implementation is a prototype intended for educational and demonstration purposes.

---

## ⚠️ Limitations

The current system has some limitations:

* It is designed primarily for a webcam based environment.
* Head direction is used as an approximation of attention.
* Lighting conditions can affect facial landmark detection.
* The current system is not designed for large scale multi person tracking.
* Attention estimation should not be considered a precise measurement of human behaviour.

---

## 🔮 Future Improvements

Possible future improvements include:

* Multi person tracking
* Customer counting
* Dwell time analysis
* Product level attention analysis
* Customer behaviour heatmaps
* Historical trend analysis
* CSV export functionality
* Cloud deployment
* Real time business alerts
* Improved head pose estimation

---

## 🎓 Project Type

**Academic / Portfolio Project**

This project demonstrates the integration of:

**Computer Vision + Data Collection + Database Management + Data Analytics + Dashboard Development**

---

## 👨‍💻 Author

**Alan Binu**

RetailVisionAI was developed as a practical computer vision and analytics project using Python.

---

## ⭐ Project Summary

RetailVisionAI demonstrates a complete pipeline for converting computer vision observations into structured business analytics.

```text
Computer Vision
      ↓
Data Collection
      ↓
SQLite Database
      ↓
Analytics
      ↓
Streamlit Dashboard
```

---