document.addEventListener('DOMContentLoaded', function() {

    // document.querySelector('.edit-profile-btn').addEventListener('click', function() {
    //     window.location.href = "{% url 'edit_profile' %}?username={{ user.username }}";
    // });

    document.querySelector('.logout-btn').addEventListener('click', function() {
        if (confirm('Are you sure you want to log out?')) {
            window.location.href = "";
        }
    });

    document.querySelectorAll('.profile-nav a').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});
