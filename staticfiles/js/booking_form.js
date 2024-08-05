document.addEventListener('DOMContentLoaded', function () {
    var startDateInput = document.getElementById('id_start_date');
    var endDateInput = document.getElementById('id_end_date');

    // When start_date changes
    startDateInput.addEventListener('change', function () {
        var startDate = new Date(startDateInput.value);
        // Set the minimum value end_date
        endDateInput.min = startDateInput.value;
        // If end_date is earlier than start_date, reset its value
        if (new Date(endDateInput.value) < startDate) {
            endDateInput.value = '';
        }
    });
});
