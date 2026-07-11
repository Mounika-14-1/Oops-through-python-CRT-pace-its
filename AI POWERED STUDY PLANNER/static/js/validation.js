// ==========================================
// AI-Powered Study Planner
// validation.js
// ==========================================

document.addEventListener("DOMContentLoaded", () => {

    // -------------------------------
    // Email Validation
    // -------------------------------
    function isValidEmail(email) {
        const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return pattern.test(email);
    }

    // -------------------------------
    // Password Validation
    // -------------------------------
    function isValidPassword(password) {
        return password.length >= 6;
    }

    // -------------------------------
    // Register Form Validation
    // -------------------------------
    const registerForm = document.getElementById("registerForm");

    if (registerForm) {

        registerForm.addEventListener("submit", function (event) {

            const username = document.getElementById("username").value.trim();
            const email = document.getElementById("email").value.trim();
            const password = document.getElementById("password").value;
            const confirmPassword = document.getElementById("confirmPassword").value;

            if (username === "") {
                alert("Please enter your name.");
                event.preventDefault();
                return;
            }

            if (!isValidEmail(email)) {
                alert("Please enter a valid email address.");
                event.preventDefault();
                return;
            }

            if (!isValidPassword(password)) {
                alert("Password must contain at least 6 characters.");
                event.preventDefault();
                return;
            }

            if (password !== confirmPassword) {
                alert("Passwords do not match.");
                event.preventDefault();
                return;
            }

        });

    }

    // -------------------------------
    // Login Form Validation
    // -------------------------------
    const loginForm = document.getElementById("loginForm");

    if (loginForm) {

        loginForm.addEventListener("submit", function (event) {

            const email = document.getElementById("email").value.trim();
            const password = document.getElementById("password").value;

            if (!isValidEmail(email)) {
                alert("Please enter a valid email.");
                event.preventDefault();
                return;
            }

            if (!isValidPassword(password)) {
                alert("Password must be at least 6 characters.");
                event.preventDefault();
                return;
            }

        });

    }

    // -------------------------------
    // Planner Validation
    // -------------------------------
    const plannerForm = document.getElementById("plannerForm");

    if (plannerForm) {

        plannerForm.addEventListener("submit", function (event) {

            const subject = document.getElementById("subject").value.trim();
            const studyHours = document.getElementById("studyHours").value;
            const examDate = document.getElementById("examDate").value;

            if (subject === "") {
                alert("Please enter a subject.");
                event.preventDefault();
                return;
            }

            if (studyHours === "" || Number(studyHours) <= 0) {
                alert("Please enter valid study hours.");
                event.preventDefault();
                return;
            }

            if (examDate === "") {
                alert("Please select an exam date.");
                event.preventDefault();
                return;
            }

        });

    }

});