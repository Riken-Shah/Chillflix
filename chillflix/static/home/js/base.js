$('#search').keyup(function (event) {
    // If Pressed Enter
    if (event.keyCode === 13) {
        event.preventDefault();
    }
    $.ajax(
        {
            type: "POST",
            url: '/search/api',
            data: {
                'query': $(this).val(),
                'csrfmiddlewaretoken':$("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: 'html'
        })
})


function searchSuccess(data, textStatus, jqXHR) {
    // $nav = $(data).filter('nav')[0]
    // All the li item
    // let filtered_data = $('#search_result', $nav).children()
    console.log(data)
    $('#search_result').html(data)

}

