function toggleChildSeatOption(checkbox) {
    const childSeatOptionField = document.querySelector('select[name="child_seat_option"]');
    if (checkbox.checked) {
        childSeatOptionField.disabled = false;
    } else {
        childSeatOptionField.disabled = true;
        childSeatOptionField.value = '';
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const childSeatCheckbox = document.querySelector('input[name="child_seat"]');
    toggleChildSeatOption(childSeatCheckbox);
});