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
    responsiveClass:true,
    responsive:{
        0:{
            items:1,
            lazyLoad: false,
        },
        600:{
            items:3,
            nav:false
        },
        800:{
            items: 5,
        },
        1000:{
            items:6,            

        }
}
}
$(document).ready(function(){
  $(".owl-carousel").owlCarousel(baseOwlCarouselSetting);
});