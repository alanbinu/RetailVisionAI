import cv2
import mediapipe as mp
import numpy as np
import time

from datetime import datetime
from modules.database import create_database, save_session


mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)


camera = cv2.VideoCapture(0 , cv2.CAP_DSHOW)

# Create the database if it doesn't already exist
create_database()

session_start_time = time.time()
last_frame_time = time.time()

attentive_time = 0
away_time = 0
session_start_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


face_3d = np.array([
    [0.0, 0.0, 0.0],          # Nose
    [0.0, -63.6, -12.5],      # Chin
    [-43.3, 32.7, -26.0],     # Left eye
    [43.3, 32.7, -26.0],      # Right eye
    [-28.9, -28.9, -24.1],    # Left mouth
    [28.9, -28.9, -24.1]      # Right mouth
], dtype=np.float64)


while True:

    success, frame = camera.read()

    if not success:
        print("Could not read from the camera.")
        break

    height, width, _ = frame.shape

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect face landmarks
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:

        for face_landmarks in results.multi_face_landmarks:

            # Landmark indexes we need
            landmark_ids = [1, 152, 33, 263, 61, 291]

            face_2d = []

            for landmark_id in landmark_ids:

                landmark = face_landmarks.landmark[landmark_id]

                x = int(landmark.x * width)
                y = int(landmark.y * height)

                face_2d.append([x, y])

                # Draw the selected landmarks
                cv2.circle(
                    frame,
                    (x, y),
                    5,
                    (0, 255, 0),
                    -1
                )

            # Convert the points into NumPy format
            face_2d = np.array(face_2d, dtype=np.float64)

            # Camera focal length
            focal_length = width

            camera_matrix = np.array([
                [focal_length, 0, width / 2],
                [0, focal_length, height / 2],
                [0, 0, 1]
            ], dtype=np.float64)

            # Assume no lens distortion
            distortion_matrix = np.zeros((4, 1))

            # Estimate head pose
            success_pnp, rotation_vector, translation_vector = cv2.solvePnP(
                face_3d,
                face_2d,
                camera_matrix,
                distortion_matrix
            )

            if success_pnp:

                # Convert rotation vector into rotation matrix
                rotation_matrix, _ = cv2.Rodrigues(rotation_vector)

                # Convert rotation matrix into angles
                angles, _, _, _, _, _ = cv2.RQDecomp3x3(
                    rotation_matrix
                )

                yaw = angles[1]
                pitch = angles[0]
                roll = angles[2]

                # Decide which direction the customer is facing
                if yaw < -15:
                     head_direction = "LEFT"

                elif yaw > 15:
                    head_direction = "RIGHT"

                else:
                    head_direction = "CENTER"

                if head_direction == "CENTER":
                    attention_status = "ATTENTIVE"

                else:
                    attention_status = "LOOKING AWAY"

                # Calculate the time since the previous frame
                current_time = time.time()
                frame_time = current_time - last_frame_time
                last_frame_time = current_time

                # Add the time to the correct attention category
                if attention_status == "ATTENTIVE":
                 attentive_time += frame_time

                else:
                    away_time += frame_time

                total_attention_time = attentive_time + away_time
                if total_attention_time > 0:
                    attention_rate = (attentive_time / total_attention_time) * 100
                else:
                    attention_rate = 0


                # Display the angles
                cv2.putText(
                    frame,
                    f"Yaw: {yaw:.1f}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    f"Pitch: {pitch:.1f}",
                    (20, 70),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    f"Roll: {roll:.1f}",
                    (20, 100),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    f"Head Direction: {head_direction}",
                    (20, 140),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    f"Attention: {attention_status}",
                    (20, 180),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    f"Attentive Time: {attentive_time:.1f}s",
                    (20, 220),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    f"Looking Away: {away_time:.1f}s",
                    (20, 260),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 255),
                    2
                )

                cv2.putText(
                    frame,
                    f"Attention Rate: {attention_rate:.1f}%",
                    (20, 300),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255, 255, 0),
                    2
                )

    # Display camera
    cv2.imshow("RetailVisionAI", frame)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):

    # Record the session end time
     session_end_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Calculate final attention rate
     total_time = attentive_time + away_time

     if total_time > 0:
        final_attention_rate = (attentive_time / total_time) * 100
     else:
        final_attention_rate = 0

    # Save the session
     save_session(
        session_start_datetime,
        session_end_datetime,
        attentive_time,
        away_time,
        final_attention_rate
    )

     print()
     print("Session saved successfully.")
     print(f"Attentive time: {attentive_time:.1f} seconds")
     print(f"Looking away: {away_time:.1f} seconds")
     print(f"Attention rate: {final_attention_rate:.1f}%")

     break

camera.release()
cv2.destroyAllWindows()