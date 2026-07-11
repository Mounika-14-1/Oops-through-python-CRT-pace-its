// ==========================================
// AI-Powered Study Planner
// dashboard.js
// ==========================================

document.addEventListener("DOMContentLoaded", function () {

    // ==========================
    // Welcome Message
    // ==========================
    const welcomeMessage = document.getElementById("welcomeMessage");

    if (welcomeMessage) {
        const hour = new Date().getHours();

        if (hour < 12) {
            welcomeMessage.textContent = "🌞 Good Morning!";
        } else if (hour < 17) {
            welcomeMessage.textContent = "☀️ Good Afternoon!";
        } else {
            welcomeMessage.textContent = "🌙 Good Evening!";
        }
    }

    // ==========================
    // Current Date
    // ==========================
    const currentDate = document.getElementById("currentDate");

    if (currentDate) {
        const today = new Date();

        currentDate.textContent = today.toLocaleDateString("en-IN", {
            weekday: "long",
            year: "numeric",
            month: "long",
            day: "numeric"
        });
    }

    // ==========================
    // Live Clock
    // ==========================
    const currentTime = document.getElementById("currentTime");

    function updateClock() {
        if (currentTime) {
            currentTime.textContent = new Date().toLocaleTimeString();
        }
    }

    updateClock();
    setInterval(updateClock, 1000);

    // ==========================
    // Progress Bar Animation
    // ==========================
    const progressBar = document.querySelector(".progress-fill");

    if (progressBar) {
        const target = parseInt(progressBar.dataset.progress) || 70;

        let width = 0;

        const animation = setInterval(() => {

            if (width >= target) {
                clearInterval(animation);
            } else {
                width++;
                progressBar.style.width = width + "%";
                progressBar.textContent = width + "%";
            }

        }, 15);
    }

    // ==========================
    // Dark Mode Toggle
    // ==========================
    const darkModeBtn = document.getElementById("darkModeBtn");

    if (darkModeBtn) {

        darkModeBtn.addEventListener("click", function () {

            document.body.classList.toggle("dark-mode");

            if (document.body.classList.contains("dark-mode")) {
                darkModeBtn.textContent = "☀️ Light Mode";
            } else {
                darkModeBtn.textContent = "🌙 Dark Mode";
            }

        });

    }

    // ==========================
    // Logout Confirmation
    // ==========================
    const logoutBtn = document.getElementById("logoutBtn");

    if (logoutBtn) {

        logoutBtn.addEventListener("click", function (event) {

            const confirmLogout = confirm("Are you sure you want to logout?");

            if (!confirmLogout) {
                event.preventDefault();
            }

        });

    }

    // ==========================
    // Notification
    // ==========================
    const notificationBtn = document.getElementById("notificationBtn");

    if (notificationBtn) {

        notificationBtn.addEventListener("click", function () {

            alert("📚 Don't forget to complete today's study plan!");

        });

    }

});