let baseOwlCarouselSetting =
{
    items: 8,
    dots: false,
    nav: false,
    lazyLoad: true,
    margin: 20,
    smartSpeed: 1000,
    autoPlay: true,
    fluidSpeed: true,
    // stagePadding: 10,
}

$(document).ready(function(){
  $(".owl-carousel").owlCarousel(baseOwlCarouselSetting);
});


$('.more-info').click(function (e) { 
  // e.preventDefault();
  if ($(this).text() === 'read more...') $(this).text('read less')
  else $(this).text('read more...');
  
});

// Fixing Overview
// $('.overview').hover(function () {
//     // over
//     $('.below-div').css('margin-top', '-11%');
    
//   }, function () {
//     // out
//     $('.below-div').css('margin-top', 'auto');

//   }
// );

$('iframe').click(function () {
    alert('Chan')
    $('.jw-player')[0].seek(100)
})
