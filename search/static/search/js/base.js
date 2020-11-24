var reqr_page = 2

// Activation Tooltip
function reloadTooltip() {
  $(function () {
    $('button', '.row-item').tooltip()
  })
}


// Removing JS Effect for Tablet
function removeHoverOfRowItem() {
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

function sendReq(query, page, extra_data) {
  waypoint.disable()
  // alert('Scrolled to waypoint!')
  // let basic = $.extend()
  console.log(extra_data)
  data_ = $.extend({
      'query': query,
      'page': page,
      'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
      'for': 'data'
    }, extra_data)
  if(extra_data !== {}){
    // delete data_.query
  }
  var check = $.ajax({
    type: "post",
    url: "./api/search",
    data: data_ ,
    dataType: "html",
    success: addDatShit,
    error: function () {
      waypoint.enable()
      // alert(waypoint.enabled)
      waypoint.trigger()
      waypoint.trigger()
    },
  });
}

function addDatShit(respone) {
  console.log('Success')
  document.getElementById('toAdd').innerHTML += respone
  reqr_page += 1
  waypoint.enable()
  reloadTooltip();

}

// Navbar JS

$("#menu-toggle").click(function (e) {
  e.preventDefault();
  const isIE11 = !!navigator.userAgent.match(/Trident.*rv\:11\./);
  $("#toggleIcon").toggleClass("fa fa-angle-double-down fa fa-angle-double-up")
  $("#wrapper").toggleClass("toggled");

  // if (isIE11) {
  //   if ($("#wrapper").hasClass("toggled")) {
  //     $('#sidebar-wrapper').css("margin-left", "-268px")
  //   } else {
  //     $('#sidebar-wrapper').css("margin-left", "-250px")
  //   }
  // }
});

// NavBar Content JS

// Hiding Movie/TV Genres On Click
$(document).ready(function () {
  $('.navbar').addClass('fixed-top')
  toggleGenres();
//
  $(window).trigger('resize');
  reloadTooltip();

});

$('.type-selector span').click(function (e) {
  e.preventDefault();
  let type = $(this).attr('id');
  $('.genre-box').removeClass('genre-selected')
  $('.checked', '.genre-box-container').css('display', 'none')
  $('#genres').val('')
  if (type === 'movie') {
    $('#tv').removeClass('is-selected');
    $(this).addClass('is-selected');
    toggleGenres();
  }
  else {
    $('#movie').removeClass('is-selected');
    $(this).addClass('is-selected');
    toggleGenres();
  }
});

function toggleGenres() {
  let type = $('.is-selected').attr('id');
  if (type === 'movie') {
    $('.tv').hide();
    $('.movie').show();
    $('#type').val('movie')
  }
  else {
    $('.movie').hide();
    $('.tv').show();
    $('#type').val('tv')

  }
}
$('.genre-box-container').on('click', function () {
  let selectClass = 'genre-selected'
  let $genres = $('#genres')
  const val = $genres.val()
  console.log(val)
  let isSelected = $('.genre-box', this).hasClass(selectClass)
  if (isSelected) {
    $('.genre-box', this).removeClass(selectClass)
    $('.checked', this).hide()
    $genres.val(val.replace((',' + $(this).attr('id')), ''))


    
  }
  else {
    $('.genre-box', this).addClass(selectClass)
    $('.checked', this).show()
    $genres.val(val + ',' + $(this).attr('id'))
  }
})

$('.genres-container').on('show.bs.collapse', function () {
  $('#moreGenres').css('transform', 'rotate(180deg)')
});

$('.genres-container').on('hide.bs.collapse', function () {
  $('#moreGenres').css('transform', 'rotate(0deg)')
});


$('.age-grp span').on('click', function (){
  let selectClass = 'age-grp-selected'
  let $certification = $('#certification')
  let val = $certification.val()
  if($(this).hasClass(selectClass)){
    $(this).removeClass(selectClass)
    $certification.val(val.replace(',' + $(this).text(), ''))
  }
  else{
    $(this).addClass(selectClass)
    $certification.val(val + ',' + $(this).text())
  }
})




$('.rating').on('input', function (e) { 
  e.preventDefault();
  $('.liveScore', $(this).parent()).val($(this).val())
});

$(window).on('resize', () => {
  // Collapse Elem Id and Main Drawer Id
  const collapseId = 'Genres';
  const drawerId = 'allGenres';
  const collapseElem = document.getElementById(collapseId);
  const mainElem = document.getElementById(drawerId);
  const movieBoxClass= '.movie';
  const tvBoxClass = '.tv';
  const width =  window.innerWidth;
  const orientation = getOrientation();
  if(width < 717 && orientation === 'landscape'){
      addToElem($( movieBoxClass + '.genre-box-container', '.genres-container')[3], collapseElem);
      addToElem($( tvBoxClass + '.genre-box-container', '.genres-container')[3], collapseElem);

      mainElem.setAttribute('changed', '');
  }
  else if (mainElem.hasAttribute('changed')) {
    addToElem($(movieBoxClass + '.genre-box-container', '.genres-container')[4], mainElem);
    addToElem($( tvBoxClass + '.genre-box-container', '.genres-container')[3], mainElem);

    mainElem.removeAttribute('changed');
  }

})




const addToElem = (elem, addElem) => {
  elem.remove();
  addElem.insertBefore(elem, addElem.firstChild);
}


function getOrientation() {
if(window.matchMedia("(orientation: portrait)").matches) return 'portrait'
  return 'landscape';
}


$('.cross').on('click', () => document.getElementById('menu-toggle').click());

