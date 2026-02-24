import cv2
import os
import numpy as np

faces_dir = "faces"

recognizer = cv2.face.LBPHFaceRecognizer_create()

faces = []
labels = []

label_map = {}
current_label = 0


for student_id in os.listdir(faces_dir):

    path = os.path.join(faces_dir, student_id)

    if not os.path.isdir(path):
        continue

    label_map[current_label] = student_id

    for image_name in os.listdir(path):

        image_path = os.path.join(path, image_name)

        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        faces.append(img)

        labels.append(current_label)

    current_label += 1


labels = np.array(labels)

print("Training model...")

recognizer.train(faces, labels)

recognizer.save("backend/face_model.yml")

np.save("backend/label_map.npy", label_map)

print("Model trained and saved")