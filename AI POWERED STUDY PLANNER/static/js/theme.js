const themeButton = document.getElementById("themeToggle");

if (themeButton) {

    themeButton.onclick = function () {

        document.body.classList.toggle("dark");

        if (document.body.classList.contains("dark")) {

            themeButton.innerHTML = "☀️ Light Mode";
            localStorage.setItem("theme", "dark");

        } else {

            themeButton.innerHTML = "🌙 Dark Mode";
            localStorage.setItem("theme", "light");

        }

    };

    window.onload = function () {

        let savedTheme = localStorage.getItem("theme");

        if (savedTheme === "dark") {

            document.body.classList.add("dark");
            themeButton.innerHTML = "☀️ Light Mode";

        }

    };

}