// Get the modal
var modal = document.getElementById('assignmentModal');

// Get the button that opens the modal
var btn = document.getElementById('openModal');

// Get the <span> element that closes the modal
var span = document.getElementsByClassName('close')[0];

// Get the cancel button element
var cancelButton = document.getElementById('cancelButton');

// Get all edit buttons
var editButtons = document.getElementsByClassName('edit');

// Handle course and semester selection
var courseSelect = document.getElementById('course');
var semesterSelect = document.getElementById('semester');

// Function to populate the semester dropdown based on course
function populateSemesters(course, selectedSemester) {
    var semesters = [];

    switch(course) {
        case 'BTech':
            semesters = [1, 2, 3, 4, 5, 6, 7, 8];
            break;
        case 'MTech':
            semesters = [1, 2, 3, 4];
            break;
        case 'BSc CS':
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

    // Clear previous options
    semesterSelect.innerHTML = '<option value="" disabled>Select your semester</option>';

    // Add new options based on the selected course
    semesters.forEach(function(sem) {
        var option = document.createElement('option');
        option.value = sem;
        option.textContent = sem + ' Semester';
        if (sem === selectedSemester) {
            option.selected = true;
        }
        semesterSelect.appendChild(option);
    });
}

// When the user clicks the button, open the modal 
btn.onclick = function() {
    document.getElementById('assignmentForm').reset();
    document.getElementById('modalTitle').textContent = 'Upload Assignment';
    document.getElementById('assignmentId').value = '';
    var course = courseSelect.value;
    var selectedSemester = ''; // No selected semester initially
    populateSemesters(course, selectedSemester);
    modal.style.display = 'block';
}

// When the user clicks on <span> (x) or cancel button, close the modal
span.onclick = function() {
    modal.style.display = 'none';
}
cancelButton.onclick = function() {
    modal.style.display = 'none';
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}

// Handle course change event
courseSelect.addEventListener('change', function() {
    var course = courseSelect.value;
    var selectedSemester = semesterSelect.value; // Preserve the selected semester if available
    populateSemesters(course, selectedSemester);
});

// Handle editing of an assignment (populate fields when the modal is opened for editing)
editButtons.forEach(function(button) {
    button.onclick = function() {
        var assignmentId = this.getAttribute('data-id');
        var course = this.getAttribute('data-course');
        var semester = this.getAttribute('data-semester');

        // Populate form fields
        document.getElementById('assignmentId').value = assignmentId;
        document.getElementById('course').value = course;

        // Populate semesters based on course and pre-select the current semester
        populateSemesters(course, semester);

        // Show modal
        document.getElementById('modalTitle').textContent = 'Update Assignment';
        modal.style.display = 'block';
    }
});
