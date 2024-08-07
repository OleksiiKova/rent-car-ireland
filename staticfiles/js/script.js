/**
 * Initializes Bootstrap tooltips for elements with the `data-bs-toggle="tooltip"` attribute.
 * 
 * This script selects all elements with the `data-bs-toggle="tooltip"` attribute and
 * creates Bootstrap tooltip instances for them. It runs after the DOM content is fully loaded.
 */
document.addEventListener('DOMContentLoaded', function () {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});