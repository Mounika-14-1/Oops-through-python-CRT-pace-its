// ==========================================
// AI-Powered Study Planner
// planner.js
// ==========================================

document.addEventListener("DOMContentLoaded", () => {

    // Form Elements
    const plannerForm = document.getElementById("plannerForm");
    const subject = document.getElementById("subject");
    const planType = document.getElementById("planType");
    const studyHours = document.getElementById("studyHours");
    const examDate = document.getElementById("examDate");

    const previewContainer = document.getElementById("planPreview");

    // ==========================
    // Form Validation
    // ==========================

    plannerForm.addEventListener("submit", function (event) {

        event.preventDefault();

        const subjectValue = subject.value.trim();
        const planTypeValue = planType.value;
        const studyHoursValue = studyHours.value;
        const examDateValue = examDate.value;

        // Subject Validation
        if (subjectValue === "") {
            alert("Please enter a subject.");
            subject.focus();
            return;
        }

        // Plan Type Validation
        if (planTypeValue === "") {
            alert("Please select a study plan type.");
            planType.focus();
            return;
        }

        // Study Hours Validation
        if (studyHoursValue === "" || studyHoursValue <= 0) {
            alert("Please enter valid study hours.");
            studyHours.focus();
            return;
        }

        // Exam Date Validation
        if (examDateValue === "") {
            alert("Please select an exam date.");
            examDate.focus();
            return;
        }

        // Display Preview
        previewContainer.innerHTML = `
            <div class="plan-card">
                <h3>📚 Study Plan Preview</h3>

                <p><strong>Subject:</strong> ${subjectValue}</p>

                <p><strong>Plan Type:</strong> ${planTypeValue}</p>

                <p><strong>Study Hours:</strong> ${studyHoursValue} Hours</p>

                <p><strong>Exam Date:</strong> ${examDateValue}</p>

                <p style="color:green; font-weight:bold;">
                    ✔ Ready to generate AI study plan.
                </p>
            </div>
        `;

        // Uncomment when Flask backend is ready
        // plannerForm.submit();

    });

    // ==========================
    // Clear Preview Button
    // ==========================

    const clearBtn = document.getElementById("clearBtn");

    if (clearBtn) {

        clearBtn.addEventListener("click", () => {

            plannerForm.reset();
            previewContainer.innerHTML = "";

        });

    }

});