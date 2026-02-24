import cv2
import os
import time

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

student_id = input("Enter Student ID: ")

folder = f"faces/{student_id}"
os.makedirs(folder, exist_ok=True)

cap = cv2.VideoCapture(0)

count = 0
max_images = 40

phase = 0

print("Smart Capture Started")

while count < max_images:

    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5
    )

    # Phase control
    if count == 0:
        message = "LOOK STRAIGHT"
        phase = 1
        show_instruction = True

    elif count == 10:
        message = "TURN LEFT"
        phase = 2
        show_instruction = True

    elif count == 20:
        message = "TURN RIGHT"
        phase = 3
        show_instruction = True

    elif count == 30:
        message = "LOOK UP / DOWN"
        phase = 4
        show_instruction = True

    else:
        show_instruction = False


    # Show instruction for 2 seconds
    if show_instruction:

        start = time.time()

        while time.time() - start < 2:

            ret, frame = cap.read()

            cv2.putText(
                frame,
                message,
                (50,50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,255),
                2
            )

            cv2.imshow("Smart Capture", frame)

            cv2.waitKey(1)

        print(message)


    for (x, y, w, h) in faces:

        margin = 30

        x1 = max(0, x-margin)
        y1 = max(0, y-margin)
        x2 = min(frame.shape[1], x+w+margin)
        y2 = min(frame.shape[0], y+h+margin)

        face = frame[y1:y2, x1:x2]

        file_path = f"{folder}/{count}.jpg"

        cv2.imwrite(file_path, face)

        count += 1

        print("Saved", count)

        cv2.rectangle(
            frame,
            (x1,y1),
            (x2,y2),
            (0,255,0),
            2
        )

        break


    cv2.imshow("Smart Capture", frame)

    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

print("Capture Complete")