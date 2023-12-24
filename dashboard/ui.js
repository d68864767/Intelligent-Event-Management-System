```javascript
// Function to toggle visibility of a section
function toggleSectionVisibility(sectionId) {
    var section = document.getElementById(sectionId);
    if (section.style.display === "none") {
        section.style.display = "block";
    } else {
        section.style.display = "none";
    }
}

// Add click event listeners to headers
window.onload = function() {
    document.getElementById('scheduled-events').previousElementSibling.addEventListener('click', function() {
        toggleSectionVisibility('scheduled-events');
    });

    document.getElementById('attendee-analysis').previousElementSibling.addEventListener('click', function() {
        toggleSectionVisibility('attendee-analysis');
    });

    document.getElementById('feedback-analysis').previousElementSibling.addEventListener('click', function() {
        toggleSectionVisibility('feedback-analysis');
    });
};
```
