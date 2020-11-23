$( document ).ready(function () {

    $('.url-holder').click(function () {

        var urlId = $(this).attr('data-id'),
            visitsHolder = $(this).children('.visits-holder')

        $.ajax({
            url: '/increase-visitors/',
            type: 'GET',
            data: {
                url_id: urlId
            },
            success: function (data) {

               var visits = data.visits

               $(visitsHolder).html(`Visits: (${visits})`)
            }
        })
    });

})
