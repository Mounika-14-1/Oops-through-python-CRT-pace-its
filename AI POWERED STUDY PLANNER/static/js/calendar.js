let currentDate = new Date();

const monthNames = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
];

function loadCalendar() {

    const calendarDays = document.getElementById("calendarDays");
    const monthYear = document.getElementById("monthYear");

    calendarDays.innerHTML = "";

    let year = currentDate.getFullYear();
    let month = currentDate.getMonth();

    monthYear.textContent = monthNames[month] + " " + year;

    let firstDay = new Date(year, month, 1).getDay();

    let daysInMonth = new Date(year, month + 1, 0).getDate();

    // Empty boxes before first day
    for (let i = 0; i < firstDay; i++) {

        let empty = document.createElement("div");
        empty.classList.add("empty");

        calendarDays.appendChild(empty);
    }

    // Dates
    for (let day = 1; day <= daysInMonth; day++) {

        let box = document.createElement("div");

        box.classList.add("day");

        let today = new Date();

        if (
            day === today.getDate() &&
            month === today.getMonth() &&
            year === today.getFullYear()
        ) {
            box.classList.add("today");
        }

        box.innerHTML = `
            <div class="date">${day}</div>
            <div class="study">Study</div>
        `;

        calendarDays.appendChild(box);
    }
}

// Previous Month
document.getElementById("prevMonth").addEventListener("click", function () {
    currentDate.setMonth(currentDate.getMonth() - 1);
    loadCalendar();
});

// Next Month
document.getElementById("nextMonth").addEventListener("click", function () {
    currentDate.setMonth(currentDate.getMonth() + 1);
    loadCalendar();
});

loadCalendar();