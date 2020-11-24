$(document).ready(function () {
    // Overview Init Collapse
    $('#overview').collapse({
    toggle: false
    });
    // Overview Div Logic
    $('#overview-more-info').click(function (e) { 
        e.preventDefault();
        let aria_expanded = $(this).attr('aria-expanded');
        if(aria_expanded === 'false')  {
            // Toggleing Overview div
            $('#overview').toggle()
            // Growing It
            $('.overview-container').addClass('grow');
            // Adding Close Button
            $('#close-button').css('display', 'initial');
            // More-info -> Less Info
            $(this).text('less info');

        }
        else {
            // Toggleing it again
            $('#overview').toggle()
            // Closing div
            $('.overview-container').removeClass('grow')
            // Removing Close Button
            $('#close-button').css('display', 'none');
            // Less Info -> More Info
            $(this).text('more info...')
        }
    });

    // Adding Logic for Close Overview button
    $('#close-button').click(function(){
          $('#overview-more-info').click() 
    });
});