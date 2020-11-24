$('#filterForm').on('submit',
    (e) => {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: './api/search/filter',
        data: $('#filterForm').serialize() + `&csrfmiddlewaretoken=${$("input[name=csrfmiddlewaretoken]").val()}` ,
        dataType: "html",
        success: onSuccess,
        error: () => {
            alert('Failed!!')
        }
    });
});

const onSuccess = (data) => {
    document.getElementById('toAdd').innerHTML = data;
    $('#menu-toggle').click();
    $('#filterForm').reset();
};
