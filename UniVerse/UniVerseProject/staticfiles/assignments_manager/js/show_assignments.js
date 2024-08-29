document.addEventListener('DOMContentLoaded', function() {
    const uploadButtons = document.querySelectorAll('.upload-btn');
    const modal = document.getElementById('upload-modal');
    const closeModalButton = document.querySelector('.close-btn');
    const uploadForm = document.getElementById('upload-form');
    const statusMessage = document.getElementById('status-message');
    const assignmentIdInput = document.getElementById('assignment-id');

    // Show modal on upload button click
    uploadButtons.forEach(button => {
        button.addEventListener('click', function() {
            assignmentIdInput.value = this.getAttribute('data-assignment-id');
            modal.style.display = 'block';
        });
    });

    closeModalButton.addEventListener('click', function() {
        modal.style.display = 'none';
    });

    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });

    // Handle form submission
    uploadForm.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const formData = new FormData(this);

        fetch("{% url 'saveStudentAssignment' %}?username={{username}}",{
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                statusMessage.textContent = 'Assignment uploaded successfully!';
                statusMessage.style.color = 'green';
                // Optionally close modal or reset form
                setTimeout(() => modal.style.display = 'none', 2000);
            } else {
                statusMessage.textContent = 'Upload failed. Please try again.';
                statusMessage.style.color = 'red';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            statusMessage.textContent = 'An error occurred. Please try again.';
            statusMessage.style.color = 'red';
        });
    });
});
