// Base Config for Owl Carousel
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
  lazyLoadEager: 1,
  stagePadding: null,

  // stagePadding: 10,
}
// let forRows = {}
// Object.assign(forRows, baseOwlCarouselSetting)


// When Document is Ready -> All Other Effect
$(document).ready(function () {
  // Resize Carousel Size


  // Init Owl Carousel for -> Main Carousel
  // Changing Some Setting for Trailer in Carousel

  baseOwlCarouselSetting.items = 1
  baseOwlCarouselSetting.singleItem = true
  baseOwlCarouselSetting.margin = null
  baseOwlCarouselSetting.autoPlay = true
  baseOwlCarouselSetting.navText = [
    "<i class='fa fa-arrow-left'></i><span style='margin-left: .5em'>Prev Item</span>",
    "<span style='margin-right: 0.5em;'>Next Item</span><i class=\"fa fa-arrow-right\" aria-hidden=\"true\"></i>"
  ]
  baseOwlCarouselSetting.nav = true
  // Init
  $("#main-carousel").owlCarousel(baseOwlCarouselSetting);
  owl = $('#main-carousel')

  // Setting for first elem
  changeBackground({ 'item': { 'index': 0 } })
  playTrailer(0)

  // Change Background && Play Trailer If Background is Changedd
  owl.on('changed.owl.carousel', changeBackground);


});

// Change Background && Play Trailer
function changeBackground(event) {
  console.log('Event', event)
  // Getting Index Number
  let indexNum = event.item.index;
    // Logic for Tablet
    let isTablet = $('#isTablet').val()
    let baseImgUrl = 'https://image.tmdb.org/t/p/w'
    let quality = '1280';
    if (isTablet==='True') quality = '780'
  
  // Getting Image URl
  let bgImageUrl = $('#bg-img-' + indexNum.toString()).val();
  bgImageUrl = baseImgUrl + quality + bgImageUrl

  // Applying Image Background
  // If device width is greater than 1400px than background cover will activate
  let backgroundSize = 'auto'
  if (window.innerWidth > 1400||isTablet === 'True') backgroundSize = 'cover'
  css = {
//    background: 'linear-gradient(100deg, rgba(1,19,29,1) 17%, rgba(45,73,88,0.7469362745098039) 20%, rgba(0,0,0,.15) 35%), url("' + bgImageUrl + '")',
    background: 'linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.2  )), url("' + bgImageUrl + '")',

    'background-position-x': '100%',
    'background-size': backgroundSize,
    'background-repeat': 'no-repeat',
    'background-postion': 'right',
  };
  $('.Bg-Test').css(css)
  console.log("Done");

  // Playing Trailer -> ith index elem
  playTrailer(indexNum)
}


// Play Trailer in background carousel
function playTrailer(indexNum) {
  // Checking if player is definined
  if (player && player.cueVideoById !== undefined) {
    // alert('Called Play Trailer')
    stopVideo();
    player.cueVideoById($('#carousel-trailer-' + indexNum.toString()).val());
    // It would start trailer after -> 2 sec + loading time 
    setTimeout(function () {
      player.playVideo();
    }, 2000);
    // infinite.waypoint.trigger()
  }
}

// Mute Functionality For 
$(function () {
  $('#mute').click(function (e) {
    e.preventDefault();
    $i = $($(this).children()[0])
    let forMute = 'fa-volume-mute'
    let forSound = 'fa-volume-up'
    if (!player.isMuted()) {
      player.mute()
      // Change the Icon
      $i.removeClass(forMute);
      $i.addClass(forSound)
    }
    else {
      player.unMute();
      // Change the Icon
      $i.removeClass(forSound)
      $i.addClass(forMute)
    }
  });
});




// Youtube Player JS Started...

var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// Base Config for Youtube
var youtubePlayerConfig = {
  autoplay: 1,
  cc_load_policy: 1,
  controls: 0,
  disablekb: 1,
  fs: 0,
  enablejsapi: 1,
  rel: 0,
  origin: 'http://localhost:8000',
  widget_referrer: 0,
  mute: 1
}

var player;
function onYouTubePlayerAPIReady() {
  player = new YT.Player('Bg-Trailer', {
    height: '360',
    width: '640',
    videoId: $('#carousel-trailer-0').val(),
    playerVars: youtubePlayerConfig,
    events: {
      'onReady': onPlayerReady,
      'onStateChange': onPlayerStateChange,
    }
  });
}

// When Youtube Player is Ready to Play
function onPlayerReady(event) {
  infinite.waypoint.trigger()

  // $('#mute').click()
  // $('#mute').click()

  // setTimeout(function(){
  // player.unMute();
  // alert('Happeing')
  // },1000)
}

// When any state of youtube player changes 
function onPlayerStateChange(event) {
  let playerStatus = event.data;
  // If Youtube Player is Started Playing -> Will Appear

  if (playerStatus === 1) {

    // Changing CSS
    $('#Bg-Trailer').addClass('bgVisible')
    $('.hide').css('opacity', '0')
    $('.title-container').addClass('main-title-grow')
    $('.main-title').css('-webkit-line-clamp', "1")
    $('#trailerOptions').css('opacity', 1)
    // player.unMute()
    // console.log('Started')

  }

  // If Anything else than Q-ing Video -> Will Disappear
  else if (playerStatus !== 5) {

    // Revert Backing CSS
    $('#Bg-Trailer').removeClass('bgVisible')
    $('.hide').css('opacity', '1')
    $('.title-container').removeClass('main-title-grow')
    $('.main-title').css('-webkit-line-clamp', "2")

  }
}

// Function to Stop Video
function stopVideo() {
  if (player.stopVideo !== undefined)
    player.stopVideo();
}

// Youtube Trailer JS Finished


// onPlayerReady(null)

let forRows =
{
  items: 8,
  dots: false,
  nav: true,
  navText : ["<div class='nav-btn'><div class='prev-slide'></div></div>","<div class='nav-btn next'><div class='next-slide'></div></div>"],
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



// Activation Tooltip
function reloadTooltip (){
  $(function () {
    $('button', '.row-item').tooltip()
  })
}
