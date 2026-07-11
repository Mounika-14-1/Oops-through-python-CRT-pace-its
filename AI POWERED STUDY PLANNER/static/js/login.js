// ==========================================
// AI-Powered Study Planner
// login.js
// ==========================================

// Wait until the page is fully loaded
document.addEventListener("DOMContentLoaded", function () {

    // Form elements
    const loginForm = document.getElementById("loginForm");
    const email = document.getElementById("email");
    const password = document.getElementById("password");
    const loginBtn = document.getElementById("loginBtn");
    const togglePassword = document.getElementById("togglePassword");

    // ==========================
    // Show / Hide Password
    // ==========================

    if (togglePassword) {

        togglePassword.addEventListener("click", function () {

            if (password.type === "password") {
                password.type = "text";
                togglePassword.innerHTML = "🙈 Hide";
            } else {
                password.type = "password";
                togglePassword.innerHTML = "👁 Show";
            }

        });

    }

    // ==========================
    // Login Validation
    // ==========================

    if (loginForm) {

        loginForm.addEventListener("submit", function (event) {

            event.preventDefault();

            const emailValue = email.value.trim();
            const passwordValue = password.value.trim();

            // Empty Validation
            if (emailValue === "" || passwordValue === "") {

                alert("Please fill in all fields.");

                return;
            }

            // Email Validation
            const emailPattern =
                /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            if (!emailPattern.test(emailValue)) {

                alert("Please enter a valid email address.");

                email.focus();

                return;
            }

            // Password Validation
            if (passwordValue.length < 6) {

                alert("Password must be at least 6 characters.");

                password.focus();

                return;
            }

            // Loading Button

            loginBtn.innerHTML = "Logging in...";
            loginBtn.disabled = true;

            // Submit form after validation
            setTimeout(() => {

                loginForm.submit();

            }, 1000);

        });

    }

});