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

    // When end_date changes
    // endDateInput.addEventListener('change', function () {
    //     // Parsing the start_date and end_date values
    //     var startDate = new Date(startDateInput.value);
    //     var endDate = new Date(endDateInput.value);
    //     // If end_date is earlier than start_date, reset its value
    //     if (endDate < startDate) {
    //         endDateInput.value = '';
    //     }
    // });

    // // Check on page load
    // var startDate = new Date(startDateInput.value);
    // var endDate = new Date(endDateInput.value);
    // if (endDate < startDate) {
    //     endDateInput.value = '';
    // }
});




// function toggleChildSeatOption(checkbox) {
//     const childSeatOptionField = document.querySelector('select[name="child_seat_option"]');
//     if (checkbox.checked) {
//         childSeatOptionField.disabled = false;
//     } else {
//         childSeatOptionField.disabled = true;
//         childSeatOptionField.value = '';
//     }
// }

// document.addEventListener('DOMContentLoaded', function() {
//     const childSeatCheckbox = document.querySelector('input[name="child_seat"]');
//     toggleChildSeatOption(childSeatCheckbox);
// });
