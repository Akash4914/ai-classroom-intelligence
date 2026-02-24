import cv2
import mediapipe as mp
import numpy as np
import pandas as pd
import sqlite3
import time
from datetime import datetime


# ================= DATABASE =================

conn = sqlite3.connect("data/attendance.db")

cursor = conn.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS attention (

id INTEGER PRIMARY KEY AUTOINCREMENT,

student_id TEXT,

status TEXT,

start_time TEXT,

end_time TEXT,

duration REAL

)

""")

conn.commit()



# ================= LOAD FACE MODEL =================

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read("backend/face_model.yml")

label_map = np.load(
    "backend/label_map.npy",
    allow_pickle=True
).item()


students = pd.read_csv("data/students.csv")

students["id"] = students["id"].astype(str)



# ================= MEDIAPIPE =================

mp_face_mesh = mp.solutions.face_mesh.FaceMesh(

    max_num_faces=1,

    refine_landmarks=True

)


LEFT = [33,160,158,133,153,144]

RIGHT = [362,385,387,263,373,380]



def eye_ratio(landmarks, eye, w, h):

    points = [

        (int(landmarks[i].x*w),

         int(landmarks[i].y*h))

        for i in eye

    ]


    vertical = np.linalg.norm(

        np.array(points[1]) - np.array(points[5])

    )


    horizontal = np.linalg.norm(

        np.array(points[0]) - np.array(points[3])

    )


    return vertical / horizontal



# ================= FACE CASCADE =================

face_cascade = cv2.CascadeClassifier(

    cv2.data.haarcascades +

    "haarcascade_frontalface_default.xml"

)



# ================= CAMERA =================

cap = cv2.VideoCapture(0)



# ================= STATE VARIABLES =================

current_student = None

current_status = "Attentive"

status_start = time.time()

sleep_start = None



print("Smart AI Monitor Started")



# ================= MAIN LOOP =================

while True:


    ret, frame = cap.read()

    if not ret:

        break


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    h, w, _ = frame.shape



    # ================= FACE RECOGNITION =================

    faces = face_cascade.detectMultiScale(

        gray,

        1.3,

        5

    )


    student_name = "Unknown"


    for (x,y,wf,hf) in faces:


        face = gray[y:y+hf, x:x+wf]


        label, confidence = recognizer.predict(face)


        if confidence < 70:


            student_id = label_map[label]


            student = students[

                students["id"] == student_id

            ]


            if not student.empty:


                student_name = student.iloc[0]["name"]

                current_student = student_id


        cv2.rectangle(

            frame,

            (x,y),

            (x+wf,y+hf),

            (0,255,0),

            2

        )



    # ================= ATTENTION DETECTION =================

    detected_status = "Attentive"


    result = mp_face_mesh.process(rgb)


    if result.multi_face_landmarks:


        landmarks = result.multi_face_landmarks[0].landmark


        ratio = (

            eye_ratio(landmarks, LEFT, w, h) +

            eye_ratio(landmarks, RIGHT, w, h)

        ) / 2


        if ratio < 0.20:


            if sleep_start is None:

                sleep_start = time.time()


            elif time.time() - sleep_start > 2:

                detected_status = "Sleeping"


        else:

            sleep_start = None



    # ================= SAVE TO DATABASE =================

    if current_student is not None:


        if detected_status != current_status:


            now = datetime.now()


            duration = round(

                time.time() - status_start,

                1

            )


            cursor.execute("""

            INSERT INTO attention

            (student_id, status, start_time, end_time, duration)

            VALUES (?, ?, ?, ?, ?)

            """,

            (

                current_student,

                current_status,

                str(datetime.fromtimestamp(status_start)),

                str(now),

                duration

            ))


            conn.commit()


            print(

                current_student,

                current_status,

                duration

            )


            current_status = detected_status

            status_start = time.time()



    # ================= DISPLAY =================

    cv2.putText(

        frame,

        f"{student_name}",

        (30,50),

        cv2.FONT_HERSHEY_SIMPLEX,

        1,

        (0,255,0),

        2

    )


    cv2.putText(

        frame,

        f"{current_status}",

        (30,100),

        cv2.FONT_HERSHEY_SIMPLEX,

        1,

        (0,255,255),

        2

    )


    cv2.imshow(

        "AI Classroom Intelligence",

        frame

    )



    if cv2.waitKey(1) == ord("q"):

        break



# ================= CLEANUP =================

cap.release()

cv2.destroyAllWindows()

conn.close()