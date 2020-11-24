    $(document).ready(function () {
    $.ajax({
        url: "https://cors-anywhere.herokuapp.com/https://www.soap2day.to/home/index/GetMInfoAjax",
        data: {
            pass: mId
        },
        dataType: "HTML",
        type: "POST",
        error: function () { },
        success: function (a) {
            b = eval('(' + a + ')')
            if (b["key"]) {
                subs = b["subs"];
                position = (b["pos"] >= 2) ? (b["pos"] - 2) : 0;
                video_inst_data = b;
                video_src = video_inst_data["val"];
                var video = videojs('my-player')
                // video.src(video_src)
               video.src({
                 src: video_src,
                  type: 'video/mp4'/*video type*/
                });

                alert('Success link' + video_src)

                // LoadJwPlayer()
            } else {
                const msg = b['val'];
                $('#error').html(msg)
            }
        }
    })
});

mId = $('#MId').val();
