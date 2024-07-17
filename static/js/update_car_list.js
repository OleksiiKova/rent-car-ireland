$(document).ready(function () {
    var sortBy = 'default';
    var isAuthenticated = "{{ user.is_authenticated|yesno:'true,false' }}";
    
    function updateCarList() {
        var carType = $('#car-type').val();
        var transmission = $('#transmission').val();
        var airConditioning = $('#air-conditioning').prop('checked');
        var navigation = $('#navigation').prop('checked');
        var startDate = $('#id_start_date').val();
        var endDate = $('#id_end_date').val();
        var pickUpTime = $('#id_pick_up_time').val();
        var dropOffTime = $('#id_drop_off_time').val();
        var pickupOffice = $('#id_pickup_office').val();
        var returnOffice = $('#id_return_office').val();

        $.ajax({
            url: '/update_car_list/',
            data: {
                'car_type': carType,
                'transmission': transmission,
                'sort_by': sortBy,
                'air_conditioning': airConditioning,
                'navigation': navigation,
                'start_date': startDate,
                'end_date': endDate,
                'pick_up_time': pickUpTime,
                'drop_off_time': dropOffTime,
                'pickup_office': pickupOffice,
                'return_office': returnOffice,
                'is_authenticated': isAuthenticated
            },
            dataType: 'json',
            success: function (data) {
                $('#car-list-container').html(data.html);
                if (data.is_authenticated === 'true') {
                    $('.reserve-button').show();
                    $('.login-to-continue').hide();
                } else {
                    $('.reserve-button').hide();
                    $('.login-to-continue').show();
                }
            },
            error: function (xhr, status, error) {
                console.error('Error loading data:', error);
            }
        });
    }

    // Filter change handlers
    $('#car-type, #transmission, #sort, #air-conditioning, #navigation').change(function() {
        if ($(this).attr('id') === 'sort') {
            sortBy = $(this).val();
            updateCarList();
        } else {
            updateCarList();
        }
    });

    // Reset button handler
    $('#reset-filters').click(function() {
        $('#car-type').val('all');
        $('#transmission').val('all');
        $('#air-conditioning, #navigation').prop('checked', false);
        sortBy = 'default';
        updateCarList();
    });

    updateCarList();
});