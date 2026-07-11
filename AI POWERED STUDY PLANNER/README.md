# 📚 AI-Powered Study Planner

An AI-powered web application that helps students create personalized study plans based on their subjects, available study hours, exam dates, and study goals.

The application automatically generates **Daily**, **Weekly**, and **Monthly** study schedules using Artificial Intelligence to help students manage their time effectively.

---

## 🎯 Objectives

- Generate personalized study plans.
- Help students manage study time efficiently.
- Prioritize difficult subjects.
- Track study progress.
- Improve productivity using AI.

---

## ✨ Features

- 🔐 User Registration & Login
- 👤 User Profile Management
- 📚 Add, Edit & Delete Subjects
- 🤖 AI-Powered Study Plan Generator
- 📅 Daily Study Planner
- 📆 Weekly Study Planner
- 🗓️ Monthly Study Planner
- 📊 Progress Tracking
- 📈 Study Analytics Dashboard
- 🎯 Subject Priority Management
- ⏰ Study Reminders
- 📱 Responsive Design

---

# 🛠 Technology Stack

## Frontend

- HTML5
- CSS3
- JavaScript

## Backend

- Python
- Flask

## Database

- MySQL

## Artificial Intelligence

- Google Gemini API

## Libraries

- Flask
- Flask-Login
- Flask-WTF
- Flask-SQLAlchemy
- PyMySQL
- python-dotenv
- Werkzeug

---

# 📂 Project Structure

```
AI-Study-Planner/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .env
│
├── database/
│   ├── schema.sql
│   └── seed.sql
│
├── models/
│   ├── user.py
│   ├── subject.py
│   ├── study_plan.py
│   └── progress.py
│
├── routes/
│   ├── auth.py
│   ├── dashboard.py
│   ├── planner.py
│   ├── subjects.py
│   └── profile.py
│
├── services/
│   ├── ai_service.py
│   └── planner_service.py
│
├── utils/
│
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── icons/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── planner.html
│   ├── subjects.html
│   ├── progress.html
│   └── profile.html
│
└── tests/
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Study-Planner.git
```

---

## 2. Open the Project Folder

```bash
cd AI-Study-Planner
```

---

## 3. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Install Required Packages

```bash
pip install -r requirements.txt
```

---

## 5. Create `.env`

```env
SECRET_KEY=your_secret_key

MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DB=study_planner

GEMINI_API_KEY=your_gemini_api_key
```

---

## 6. Create Database

```sql
CREATE DATABASE study_planner;
```

Import your SQL file.

---

## 7. Run the Application

```bash
python app.py
```

Visit:

```
http://127.0.0.1:5000
```

---

# 🤖 AI Workflow

```
User Login
      │
      ▼
Add Subjects
      │
      ▼
Select Planner Type
(Daily / Weekly / Monthly)
      │
      ▼
Enter Available Study Hours
      │
      ▼
Enter Exam Dates
      │
      ▼
AI Processes Data
      │
      ▼
Generate Personalized Study Plan
      │
      ▼
Save Plan in MySQL
      │
      ▼
Display Dashboard
```

---

# 🗄 Database Tables

## Users

| Column | Type |
|---------|------|
| id | INT |
| username | VARCHAR |
| email | VARCHAR |
| password | VARCHAR |
| created_at | DATETIME |

---

## Subjects

| Column | Type |
|---------|------|
| id | INT |
| user_id | INT |
| subject_name | VARCHAR |
| difficulty | VARCHAR |
| priority | VARCHAR |

---

## Study Plans

| Column | Type |
|---------|------|
| id | INT |
| user_id | INT |
| plan_type | VARCHAR |
| study_date | DATE |
| subject | VARCHAR |
| duration | FLOAT |
| status | VARCHAR |

---

## Progress

| Column | Type |
|---------|------|
| id | INT |
| user_id | INT |
| completed_hours | FLOAT |
| completion_percentage | FLOAT |

---

# 📋 Modules

### Authentication

- Register
- Login
- Logout

### Dashboard

- Today's Study Plan
- Weekly Progress
- AI Suggestions

### Subject Management

- Add Subject
- Edit Subject
- Delete Subject

### AI Planner

- Daily Planner
- Weekly Planner
- Monthly Planner

### Progress

- Track Completed Tasks
- View Statistics

### Profile

- Update Profile
- Change Password

---

# 🚀 Future Enhancements

- AI Chatbot
- Voice Assistant
- Google Calendar Integration
- Pomodoro Timer
- PDF Export
- Email Notifications
- Mobile App
- Smart Revision Planning
- Performance Prediction

---

# 📸 Screenshots

Add screenshots of:

- Home Page
- Login Page
- Dashboard
- AI Planner
- Progress Dashboard

---

# 👨‍💻 Author

**mounika yarram**

Department of Artificial Intelligence and Data Science

PACE Institute of Technology and Science

---

# 📄 License

This project is developed for educational purposes.

---

# 🙏 Acknowledgements

- Python
- Flask
- MySQL
- Google Gemini API
- HTML
- CSS
- JavaScript
- Bootstrap

---

## ⭐ Thank You

Thank you for visiting this project.

If you like this project, consider giving it a ⭐ on GitHub.
