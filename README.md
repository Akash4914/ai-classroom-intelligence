# 🎓 AI Classroom Intelligence System

An AI-powered smart classroom monitoring system that automatically tracks **student attendance and attention levels** using **Face Recognition, Computer Vision, and Machine Learning**, and provides **real-time analytics through a live dashboard**.

---

# 🚀 Features

## ✅ Automatic Face Recognition

* Detects and identifies students using webcam
* Marks attendance automatically
* Uses OpenCV LBPH Face Recognizer

## ✅ Attention Detection (AI-based)

* Detects whether student is:

  * Attentive 👀
  * Sleeping 😴
* Uses MediaPipe Face Mesh
* Eye Aspect Ratio based detection

## ✅ Real-time Dashboard

* Live attention score
* Engagement score
* Attention vs Sleeping charts
* Class ranking system

## ✅ Class Overview Analytics

* Top performing student 🏆
* Lowest attention student ⚠
* Full class performance graph

## ✅ Database Storage

* Uses SQLite database
* Stores:

  * Student ID
  * Attention Status
  * Duration
  * Time

## ✅ Fully Automatic System

No manual input required.

System flow:

Face → Recognition → Attention → Database → Dashboard

---

# 🧠 Technologies Used

| Technology | Purpose             |
| ---------- | ------------------- |
| Python     | Core programming    |
| OpenCV     | Face Recognition    |
| MediaPipe  | Attention Detection |
| Streamlit  | Dashboard           |
| SQLite     | Database            |
| NumPy      | Data Processing     |
| Pandas     | Data Analysis       |
| Matplotlib | Graphs              |
| Seaborn    | Visualization       |

---

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

---

# ⚙️ Installation

## Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/ai-classroom-intelligence.git

cd ai-classroom-intelligence
```

---
## Step 2: Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

Windows:
```bash
.venv\Scripts\activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ How to Run

## Step 1: Start AI Monitoring System

```bash
python backend/smart_monitor.py
```

---

## Step 2: Start Dashboard

```bash
streamlit run backend/web_dashboard.py
```

---

## Step 3: Open browser

```
http://localhost:8501
```

---

# 📊 Dashboard Features

Shows:

* Attention Score
* Engagement Score
* Class Ranking
* Live graphs
* Performance analytics

---

# 🧪 How It Works

1. Camera captures student face
2. System identifies student
3. Detects eye movement
4. Classifies attention state
5. Saves into database
6. Dashboard shows analytics

---

# 🎯 Applications

* Smart Classrooms
* Online Learning Monitoring
* Schools and Colleges
* Training Institutes
* Corporate Training

---

# 🧑‍💻 Author

Akash Prajapati

Computer Science Student
AI and Data Science Enthusiast

---

# 📈 Future Improvements

* Email alerts to teachers
* Cloud deployment
* Mobile app integration
* Emotion detection
* Multi-camera support

---

# ⭐ GitHub

If you like this project, give it a star ⭐

---

# 📜 License

This project is for educational purposes.
