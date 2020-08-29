$(document).ready(function (){
    function blinker() {
        $("#blink-me").fadeOut(500);
        $("#blink-me").fadeIn(500, blinker);
    }
blinker();

});

(function(){
   setTimeout(function(){
     window.location.href="/signup";
   },13000);
})()