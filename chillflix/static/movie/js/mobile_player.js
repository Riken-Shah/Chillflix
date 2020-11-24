let baseOwlCarouselSetting = 
{
    items: 3,
    dots: false,
    nav: false,
    lazyLoad: true,
    margin: 20,
    smartSpeed: 1000,
    autoPlay: true,
    fluidSpeed: true,
    stagePadding: 10,
}

$(document).ready(function(){
  $(".owl-carousel").owlCarousel(baseOwlCarouselSetting);
});

// Adding Settting for Horizontal Image
$(document).ready(function () {
    // To Check if Viewport is in Landscape
    let colorThief;
    if (window.innerHeight < window.innerWidth) {
        $card = $('#main-card');
        $card.addClass('card-landscape');
        // Disabling Horizontal Image
        $('#blockLandscape', $card).css('display', 'none');
        // Disabling Potrait Content Image
        $('#potraitContent').css('display', 'none');
        // Enabling Background Blur Image
        $('#background', $card).css('display', 'block');
        // Enabling Background Content
        $('.for-landscape', $card).css('display', 'inline-flex');

        // Reinit OwlCarousel with 6 items
        baseOwlCarouselSetting.items = 6;
        var $owl = $('.owl-carousel')
        $owl.trigger('destroy.owl.carousel');
        $owl.owlCarousel(baseOwlCarouselSetting);
        


    }
});

// Dosen't need these things now

/*
        // Fixing Background Content Color

        // Source img
        ct = new ColorThief;
        let img = document.getElementById('secondImg')
        fixHeader(img);


// Only for Horizontal
function fixHeader(sourceImg) {
    console.log(sourceImg)
    // Getting Dominant Color First
    let dominantColor;
    if (sourceImg.complete) {
        dominantColor = ct.getColor(sourceImg);
    }
    else {
        sourceImg.addEventListener('load', function () {
            dominantColor = ct.getColor(sourceImg);
        });
    }
    console.log('Dominant Color: ' + dominantColor)
    // Checking if its bright or light
    let rgb = 'rgb(' + dominantColor + ')';
    console.log(rgb)
    let imgIs = lightOrDark(rgb);

    // If Image is Light
    if (imgIs === 'light'){
        console.log('Image is Light');
        $('h1', $card).css('color', 'black');
        $('.list-inline-item', $card).css('color', '#2a2a2a');
        $('#trailer-btn', $card).css('color', 'black');
        $('#plat-btn', $card).css('color', 'black');
    }


}

// Tells if Bg Image is light or dark
function lightOrDark(color) {

    // Variables for red, green, blue values
    var r, g, b, hsp;

    // Check the format of the color, HEX or RGB?
    if (color.match(/^rgb/)) {

        // If HEX --> store the red, green, blue values in separate variables
        color = color.match(/^rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*(\d+(?:\.\d+)?))?\)$/);

        r = color[1];
        g = color[2];
        b = color[3];
    }
    else {

        // If RGB --> Convert it to HEX: http://gist.github.com/983661
        color = +("0x" + color.slice(1).replace(
        color.length < 5 && /./g, '$&$&'));

        r = color >> 16;
        g = color >> 8 & 255;
        b = color & 255;
    }

    // HSP (Highly Sensitive Poo) equation from http://alienryderflex.com/hsp.html
    hsp = Math.sqrt(
    0.299 * (r * r) +
    0.587 * (g * g) +
    0.114 * (b * b)
    );

    // Using the HSP value, determine whether the color is light or dark
    // if (hsp>127.5) {
    console.log('HSP' + hsp.toString())
    if (hsp > 150){

        return 'light';
    }
    else {

        return 'dark';
    }
}
*/
