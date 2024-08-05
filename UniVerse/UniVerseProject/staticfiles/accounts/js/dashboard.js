// scripts.js
document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.nav-links a');
    const contentSections = document.querySelectorAll('.content');

    buttons.forEach(button => {
        button.addEventListener('click', function (e) {
            e.preventDefault();

            contentSections.forEach(section => {
                section.style.display = 'none';
            });

            const targetId = button.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);
            targetSection.style.display = 'block';
        });
    });
    
    // Show the first section by default
    if (contentSections.length > 0) {
        contentSections[0].style.display = 'block';
    }
});
