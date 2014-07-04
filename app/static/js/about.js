$(document).ready(function() {
    $('.albums').find('img').fadeTo(200, 0.5);
    $('.albums').find('h1').fadeTo(250, 1);

    $("#about-header1").hide(0).delay(400).fadeIn(1000);
    $("#about-header2").hide(0).delay(800).fadeIn(1000);
    $("#about-header3").hide(0).delay(1200).fadeIn(1000);


    $('.albums').hover(function() {
        $(this).find('img').fadeTo(200, 1);
        $(this).find('h1').fadeTo(250, 0);
    }, function() {
        $(this).find('img').fadeTo(200, 0.5);
        $(this).find('h1').fadeTo(250, 1);
    });
});