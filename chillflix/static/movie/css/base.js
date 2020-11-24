// Activation Tooltip
function reloadTooltip (){
  $(function () {
    $('button', '.row-item').tooltip()
  })
}

// Removing JS Effect for Tablet
function removeHoverOfRowItem(){
    $('.row-item').removeClass('row-item')
}


let forRows =
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
// Row Carousel
$(function () {

  // forRows.margin = 20
  // forRows.stagePadding = 10

  $('.rows').owlCarousel(forRows)
});
