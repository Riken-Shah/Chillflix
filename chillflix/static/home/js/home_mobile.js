let baseOwlCarouselSetting =
{
    items: 2,
    dots: false,
    nav: false,
    lazyLoad: true,
    margin: 20,
    smartSpeed: 1000,
    autoPlay: true,
    fluidSpeed: true,
    stagePadding: 10,
    responsive: {
        200: {
            items: 1,
        },
        300: {
            items: 2,
        }
    },
}

// Landscape Check
if (window.innerWidth > innerHeight) {
    // Increasing Height of
    $('.Bg-Test').css('min-height', '75vh')
    $('.Bg-Test').css('max-height', 'none')
    $('.Bg-Test').css('height', '85vh')
    // Hidding Potrait Content
    $('.potrait').hide()
    // Changing Background
    changeBackground({item: {index: 0}})
    $('.landscape-main').show()


    baseOwlCarouselSetting.items = 6
    baseOwlCarouselSetting.responsive = {}
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
        player.playVideo()
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

}


// Change Background && Play Trailer
function changeBackground(event) {
    // Getting Index Number
    let indexNum = event.item.index;
    // Getting Image URl
    let bgImageUrl = $('#bg-img-' + indexNum.toString()).val();
    // Applying Image Background
    // If device width is greater than 1400px than background cover will activate
    let backgroundSize = 'auto'
    if (window.innerWidth > 1400) backgroundSize = 'cover'
    css = {
      background: 'linear-gradient(100deg, rgba(1,19,29,1) 17%, rgba(45,73,88,0.7469362745098039) 20%, rgba(0,0,0,.15) 35%), url("' + bgImageUrl + '")',
      'background-position-x': '100%',
      'background-size': backgroundSize,
      'background-repeat': 'no-repeat',
      'background-postion': 'right',
    };
    $('.Bg-Test').css(css)
    console.log("Done");
  
    // Playing Trailer -> ith index elem
    // playTrailer(indexNum)
  }
  


$(function () {
    $('.owl-carousel').owlCarousel(baseOwlCarouselSetting);
});