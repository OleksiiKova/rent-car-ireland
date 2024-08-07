/**
 * Initializes star rating functionality for a given selector.
 * 
 * This script adds interactive star rating behavior to elements with a specified
 * selector. It updates the visual representation of stars based on user interactions.

 * The star rating functionality is applied to elements with the class 'star-rating'.
 */
document.addEventListener('DOMContentLoaded', function () {
    const starRating = (selector) => {
        const labels = document.querySelectorAll(selector + ' label');
        const inputs = document.querySelectorAll(selector + ' input');
        labels.forEach((label) => {
            label.addEventListener('mouseover', (event) => {
                const rating = event.target.previousElementSibling ? event.target
                    .previousElementSibling.value : event.target.querySelector('input')
                    .value;
            });
            label.addEventListener('mouseout', () => {
                const currentRating = document.getElementById('rating-hidden').value ||
                    0;
                updateStars(currentRating);
            });
        });
        inputs.forEach((input) => {
            input.addEventListener('change', (event) => {
                const rating = event.target.value;
                console.log('Выбран рейтинг:', rating);
                updateStars(rating);
                document.getElementById('rating-hidden').value = rating;
            });
        });
        const currentRating = document.getElementById('rating-hidden').value;
        updateStars(currentRating);
    };

    const updateStars = (rating) => {
        const labels = document.querySelectorAll('.star-rating label');
        labels.forEach((label) => {
            const input = label.querySelector('input');
            const value = parseInt(input.value, 10);
            if (value <= rating) {
                label.classList.add('checked');
            } else {
                label.classList.remove('checked');
            }
        });
    };

    starRating('.star-rating');
});