# AI Classroom Intelligence System

A computer vision based classroom monitoring application that automates student attendance and analyzes student attention in real time. The system uses face recognition for attendance and facial landmark analysis for attention monitoring. It also provides a dashboard for visualization and analytics.

Features

Automated Attendance
Detects and recognizes student faces using a trained face recognition model and automatically records attendance in the database.

Attention Monitoring
Analyzes facial landmarks to determine whether a student is attentive or inattentive and logs attention data for further analysis.

Model Training System
Allows capturing student face images and training a face recognition model for new students.

Dashboard and Analytics
Provides a Streamlit dashboard to visualize attendance records, attention logs, and student engagement.

Database Integration
Stores student information, attendance records, and attention logs using SQLite and CSV files.

Modular Architecture
Separate modules for face capture, model training, monitoring, dashboard, and database management.

Tech Stack

Backend
Python
OpenCV
MediaPipe
NumPy
Pandas
SQLite

Frontend / Dashboard
Streamlit

Machine Learning
OpenCV LBPH Face Recognizer
Face Landmark Detection


# 📁 Project Structure

```
ai-classroom-intelligence/

backend/
│
├── smart_monitor.py        # Main AI monitoring system
├── web_dashboard.py       # Streamlit dashboard
├── capture_faces.py      # Capture student images
├── train_model.py        # Train face recognition model
├── database.py           # Database setup
├── check_db.py           # Database checker
│
├── face_model.yml       # Trained face model
├── label_map.npy       # Label mapping

data/
│
├── attendance.db       # SQLite database
├── students.csv       # Student info

faces/
│
├── STU001/
├── STU002/

requirements.txt
README.md
```
Installation and Setup

1. Clone the Repository

git clone https://github.com/Akash4914/ai-classroom-intelligence.git

cd ai-classroom-intelligence

2. Create Virtual Environment

python -m venv .venv

3. Activate Virtual Environment

Windows:

.venv\Scripts\activate

Mac/Linux:

source .venv/bin/activate

4. Install Requirements

pip install -r requirements.txt

Running the Application

Step 1: Capture Student Faces

python backend/capture_faces.py

Step 2: Train Model

python backend/train_model.py

Step 3: Run Monitoring System

python backend/smart_monitor.py

Step 4: Run Dashboard

streamlit run backend/web_dashboard.py

Dashboard will open at:

http://localhost:8501

Database Files

attendance.db
Stores attendance records.

students.csv
Stores student information.

attention logs stored during monitoring.

Applications

Smart classrooms
Colleges and universities
Training institutes
Student engagement monitoring
Automated attendance systems

Future Improvements

Deep learning based face recognition
Cloud database integration
Web based deployment
Multi camera support
Real time alerts system

Author

Akash Prajapati

GitHub:
https://github.com/Akash4914
