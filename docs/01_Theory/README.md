# 🧠 RetailVisionAI Theory

## 👁️ 1. Computer Vision

Computer vision allows a computer to understand and analyze visual information from images and video.

In RetailVisionAI, computer vision is used to analyze a person's face and head direction through a webcam.

## 🎥 2. OpenCV

OpenCV is used to capture live video from the webcam and process individual video frames.

The webcam provides the visual input that is analyzed by the system.

## 🧩 3. MediaPipe

MediaPipe is used for facial landmark detection.

These landmarks provide important points around the face that help the system understand the position and orientation of the head.

## 📍 4. Facial Landmarks

Facial landmarks are specific points detected on a person's face.

RetailVisionAI uses these points as input for determining the orientation of the person's head.

## 🧭 5. Head Pose Estimation

Head pose estimation determines the direction and orientation of a person's head.

The system analyzes values such as:

• Yaw → horizontal head rotation  
• Pitch → vertical head movement  
• Roll → head tilt  

These values help estimate whether the person is facing the monitoring area or looking away.

## 👀 6. Attention Detection

The project considers a person attentive when the detected head direction indicates that they are facing the monitoring area.

When the person turns away, the system records this as looking away time.

## ⏱️ 7. Attention Rate

Attention rate represents the percentage of the monitoring session during which the person was attentive.

### Formula

```text
Attention Rate = Attentive Time / Total Session Time × 100
