-- =====================================================
-- AI POWERED STUDY PLANNER
-- MySQL Database Schema
-- =====================================================


-- Create Database

CREATE DATABASE IF NOT EXISTS ai_study_planner;

USE ai_study_planner;



-- =====================================================
-- USERS TABLE
-- Stores login and student information
-- =====================================================

CREATE TABLE IF NOT EXISTS users (

    id INT AUTO_INCREMENT PRIMARY KEY,

    username VARCHAR(100) NOT NULL,

    email VARCHAR(150) UNIQUE NOT NULL,

    password VARCHAR(255) NOT NULL,

    college VARCHAR(150),

    course VARCHAR(100),

    study_year INT,

    daily_goal INT DEFAULT 4,

    about TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);



-- =====================================================
-- SUBJECTS TABLE
-- Student subjects
-- =====================================================

CREATE TABLE IF NOT EXISTS subjects (

    id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT NOT NULL,

    subject_name VARCHAR(100) NOT NULL,

    difficulty ENUM(
        'Easy',
        'Medium',
        'Hard'
    )
    DEFAULT 'Medium',

    priority ENUM(
        'Low',
        'Medium',
        'High'
    )
    DEFAULT 'Medium',

    target_hours DECIMAL(5,2)
    DEFAULT 0,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,


    FOREIGN KEY(user_id)
    REFERENCES users(id)
    ON DELETE CASCADE

);



-- =====================================================
-- STUDY PLANS TABLE
-- Stores AI generated plans
-- =====================================================

CREATE TABLE IF NOT EXISTS study_plans (

    id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT NOT NULL,

    subject_id INT NOT NULL,


    plan_type ENUM(
        'Daily',
        'Weekly',
        'Monthly'
    )
    NOT NULL,


    study_hours DECIMAL(5,2) NOT NULL,


    exam_date DATE,


    ai_schedule LONGTEXT,


    status ENUM(
        'Pending',
        'Completed'
    )
    DEFAULT 'Pending',


    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,


    FOREIGN KEY(user_id)
    REFERENCES users(id)
    ON DELETE CASCADE,


    FOREIGN KEY(subject_id)
    REFERENCES subjects(id)
    ON DELETE CASCADE

);



-- =====================================================
-- TIMETABLE TABLE
-- Generated timetable slots
-- =====================================================

CREATE TABLE IF NOT EXISTS timetable (

    id INT AUTO_INCREMENT PRIMARY KEY,


    plan_id INT NOT NULL,


    study_date DATE NOT NULL,


    start_time TIME,


    end_time TIME,


    topic VARCHAR(255),


    activity VARCHAR(255),


    status ENUM(
        'Pending',
        'Completed',
        'Skipped'
    )
    DEFAULT 'Pending',



    FOREIGN KEY(plan_id)
    REFERENCES study_plans(id)
    ON DELETE CASCADE

);



-- =====================================================
-- PROGRESS TABLE
-- Tracks subject progress
-- =====================================================

CREATE TABLE IF NOT EXISTS progress (

    id INT AUTO_INCREMENT PRIMARY KEY,


    user_id INT NOT NULL,


    subject_id INT NOT NULL,


    hours_completed DECIMAL(5,2)
    DEFAULT 0,


    target_hours DECIMAL(5,2)
    DEFAULT 0,


    completion_percentage INT
    DEFAULT 0,


    last_updated TIMESTAMP
    DEFAULT CURRENT_TIMESTAMP
    ON UPDATE CURRENT_TIMESTAMP,



    FOREIGN KEY(user_id)
    REFERENCES users(id)
    ON DELETE CASCADE,


    FOREIGN KEY(subject_id)
    REFERENCES subjects(id)
    ON DELETE CASCADE

);



-- =====================================================
-- STUDY SESSIONS TABLE
-- History of completed study sessions
-- =====================================================

CREATE TABLE IF NOT EXISTS study_sessions (

    id INT AUTO_INCREMENT PRIMARY KEY,


    user_id INT NOT NULL,


    subject_id INT NOT NULL,


    session_date DATE,


    duration DECIMAL(5,2),


    notes TEXT,


    FOREIGN KEY(user_id)
    REFERENCES users(id)
    ON DELETE CASCADE,


    FOREIGN KEY(subject_id)
    REFERENCES subjects(id)
    ON DELETE CASCADE

);



-- =====================================================
-- REMINDERS TABLE
-- Study reminders
-- =====================================================

CREATE TABLE IF NOT EXISTS reminders (

    id INT AUTO_INCREMENT PRIMARY KEY,


    user_id INT NOT NULL,


    title VARCHAR(150),


    message TEXT,


    reminder_date DATE,


    reminder_time TIME,


    status ENUM(
        'Pending',
        'Completed'
    )
    DEFAULT 'Pending',


    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,


    FOREIGN KEY(user_id)
    REFERENCES users(id)
    ON DELETE CASCADE

);



-- =====================================================
-- AI RECOMMENDATIONS TABLE
-- Stores AI analysis results
-- =====================================================

CREATE TABLE IF NOT EXISTS ai_recommendations (

    id INT AUTO_INCREMENT PRIMARY KEY,


    user_id INT NOT NULL,


    recommendation TEXT,


    generated_date TIMESTAMP
    DEFAULT CURRENT_TIMESTAMP,


    FOREIGN KEY(user_id)
    REFERENCES users(id)
    ON DELETE CASCADE

);



-- =====================================================
-- SAMPLE USER
-- =====================================================

INSERT INTO users
(
username,
email,
password,
college,
course,
study_year,
daily_goal
)

VALUES
(
'Admin',
'admin@gmail.com',
'admin123',
'PACE Institute of Technology and Science',
'Artificial Intelligence and Data Science',
3,
4
);



-- =====================================================
-- SAMPLE SUBJECTS
-- =====================================================

INSERT INTO subjects
(
user_id,
subject_name,
difficulty,
priority,
target_hours
)

VALUES

(
1,
'Artificial Intelligence',
'Hard',
'High',
40
),

(
1,
'Machine Learning',
'Hard',
'High',
50
),

(
1,
'Python Programming',
'Medium',
'High',
30
),

(
1,
'Database Management System',
'Medium',
'Medium',
25
);



-- =====================================================
-- SAMPLE STUDY PLAN
-- =====================================================

INSERT INTO study_plans
(
user_id,
subject_id,
plan_type,
study_hours,
exam_date,
ai_schedule
)

VALUES

(
1,
1,
'Daily',
2.5,
'2026-07-25',
'09:00-10:30 AI Theory | 10:45-11:45 Practice Questions'
);