$( document ).ready(function() {
    $('.fa-chevron-down').hide();
    $('h2, h4').on('click', function(){
        $(this).nextAll().slideToggle(800);
        $(this).children('.fa').toggleClass('fa-chevron-down fa-chevron-up');
    });
    function deferVideo() {

        //defer html5 video loading
      $("video source").each(function() {
        var sourceFile = $(this).attr("data-src");
        $(this).attr("src", sourceFile);
        var video = this.parentElement;
        video.load();
        // uncomment if video is not autoplay
        //video.play();
      });
    
    }
    window.onload = deferVideo;
});

