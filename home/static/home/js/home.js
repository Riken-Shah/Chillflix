 // Adding JS For Responsive Carousel
// If Phone is Potrait
// let sliderOption = {"lazyLoad": 5, "wrapAround": true, "pageDots": false, "draggable": false, "prevNextButtons": true, "autoPlay": 3000, "initialIndex": 4, "contain": true, "pauseAutoPlayOnHover": true, "freeScrollFriction": 0.03};
// if (width < 450)
// {
//     // Removing Carousel Indicators
//     console.log('Potrait ');
//     document.getElementById('carousel-indicators').style.display = 'none';
//     document.getElementsByClassName('carousel-control-prev')[0].style.display = 'none';
//     document.getElementsByClassName('carousel-control-next')[0].style.display = 'none';
//
//     // Slider
//     sliderOption.draggable = true;
//     sliderOption.prevNextButtons = false;
//     sliderOption['selectedAttraction'] = 0.01;
//     sliderOption['friction'] = 0.15;
//
//
//     document.getElementById('slider1').setAttribute('data-flickity', JSON.stringify(sliderOption))
// }
// else if(width < 1000)
// {
//     document.getElementById('carousel-indicators').style.display = 'none';
//     // Slider
//     sliderOption.draggable = true;
//     sliderOption['selectedAttraction'] = 0.01;
//     sliderOption['friction'] = 0.15;
//
//     document.getElementById('slider1').setAttribute('data-flickity', JSON.stringify(sliderOption))
// }
// else{
//     // Loading Defalut Slider Option (Flickity)
//     sliderOption.autoPlay = false;
//     sliderOption['adaptiveHeight'] = true;
//     sliderOption.initialIndex = 0;
//     sliderOption.lazyLoad = 8;
//     document.getElementById('slider1').setAttribute('data-flickity', JSON.stringify(sliderOption))
// }
//
//
// // Example Slider
// $('.carousel-poster').mouseover(function () {
//     // $(this).children("div").children("div").css('display', 'block');
//     // alert('Hover')
// });
// $('.carousel-cell-image').mouseout(function () {
//     // $(this).children("div").css('display', 'none');
//
// });
//
// $(document).ready(function() {
//     let div = $("#carousel-container");
//     div.mouseenter(function() {
//       div.children('div').addClass("grow");
//       div.children('.carousel-poster').children('.details').children().css('display', 'unset')
//     });
//     div.mouseleave(function() {
//         div.children('div').removeClass("grow");
//         div.children('.carousel-poster').children('.details').children().css('display', 'none')
//
//     });
//   });
//
// // ./Example Slider
//

//Slider Default Options
baseFlickityOptions = {
    "lazyLoad": true, "draggable": false, "groupCells": true, fade: true, "cellAlign": "center", "freeScroll": true, "pageDots": false
}



