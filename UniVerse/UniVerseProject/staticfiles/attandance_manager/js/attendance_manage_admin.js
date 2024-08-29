document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById('requirement');
    var btnAdd = document.getElementById('btn-add');
    var span = document.getElementsByClassName('close')[0];

    // Show the modal
    modal.style.display = 'none';
    btnAdd.onclick = function() {
        modal.style.display = 'flex'; // Change to 'flex' to center the modal content
    }

    // Hide the modal when the user clicks on <span> (x)
    span.onclick = function() {
        modal.style.display = 'none';
    }

    // Hide the modal when the user clicks anywhere outside of the modal content
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }
});

