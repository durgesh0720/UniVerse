document.addEventListener('DOMContentLoaded', function() {
    var courseSelect = document.getElementById('course');
    var semesterSelect = document.getElementById('semester');

    courseSelect.addEventListener('change', function() {
        var course = courseSelect.value;
        var semesters;

        switch(course) {
            case 'BTech':
                semesters = [1, 2, 3, 4, 5, 6, 7, 8];
                break;
            case 'MTech':
                semesters = [1, 2, 3, 4];
                break;
            case 'BSc':
                semesters = [1, 2, 3, 4, 5, 6];
                break;
            case 'MSc':
                semesters = [1, 2, 3, 4];
                break;
            case 'BCA':
                semesters = [1, 2, 3, 4, 5, 6];
                break;
            case 'BBA':
                semesters = [1, 2, 3, 4, 5, 6];
                break;
            default:
                semesters = [];
        }

        semesterSelect.innerHTML = '<option value="" disabled>Select your semester</option>';

        semesters.forEach(function(sem) {
            var option = document.createElement('option');
            option.value = sem;
            option.textContent = sem;
            semesterSelect.appendChild(option);
        });

        // Set the existing semester if it's present in the array
        var currentSemester = parseInt(semesterSelect.dataset.currentSemester, 10);
        if (currentSemester && semesters.includes(currentSemester)) {
            semesterSelect.value = currentSemester;
        }
    });

    // Handle close modal button
    var closeModal = document.getElementById('closeModal');
    closeModal.addEventListener('click', function() {
        // Close the modal or redirect based on your requirements
        window.location.href = "{% url 'upload-assignment' %}?username={{username}}";
    });
});
