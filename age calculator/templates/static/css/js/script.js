// Wait until the page is fully loaded
document.addEventListener("DOMContentLoaded", () => {

    const dobInput = document.getElementById("dob");
    const form = document.querySelector("form");

    // Set the maximum selectable date to today
    const today = new Date().toISOString().split("T")[0];
    dobInput.setAttribute("max", today);

    // Validate the form before submitting
    form.addEventListener("submit", function (event) {

        if (dobInput.value === "") {
            event.preventDefault();
            alert("Please select your date of birth.");
            return;
        }

        const selectedDate = new Date(dobInput.value);
        const currentDate = new Date();

        if (selectedDate > currentDate) {
            event.preventDefault();
            alert("Date of birth cannot be in the future.");
            return;
        }
    });

    // Add a small animation to the result card
    const result = document.querySelector(".result");

    if (result) {
        result.style.opacity = "0";
        result.style.transform = "translateY(20px)";

        setTimeout(() => {
            result.style.transition = "all 0.6s ease";
            result.style.opacity = "1";
            result.style.transform = "translateY(0)";
        }, 100);
    }

});