$(document).ready(function () {
    var sortBy = 'default';  //
    // Function for sending an AJAX request to update a list of cars
    function updateCarList() {
        var carType = $('#car-type').val();
        var transmission = $('#transmission').val();
        var airConditioning = $('#air-conditioning').prop('checked');
        var navigation = $('#navigation').prop('checked');

        $.ajax({
            url: '/update_car_list/',
            data: {
                'car_type': carType,
                'transmission': transmission,
                'sort_by': sortBy,
                'air_conditioning': airConditioning,
                'navigation': navigation
            },
            dataType: 'json',
            success: function (data) {
                $('#car-list-container').html(data.html);
            },
            error: function (xhr, status, error) {
                console.error('Error loading data:', error);
            }
        });
    }

    // Filter change handlers
    $('#car-type, #transmission, #sort, #air-conditioning, #navigation').change(function() {
        if ($(this).attr('id') === 'sort') {
            // Handling sort direction changes
            sortBy = $(this).val();
            updateCarList();
        } else {
            // Handling changes to other filters
            updateCarList();
        }
    });

    // Reset button handler
    $('#reset-filters').click(function() {
        $('#car-type').val('all');
        $('#transmission').val('all');
        $('#air-conditioning, #navigation').prop('checked', false);
        sortBy = 'default';  // Сброс сортировки по умолчанию
        updateCarList();
    });
    // Initializing the list of cars on page load
    updateCarList();
});