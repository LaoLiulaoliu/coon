$(document).ready(function() {
    $("#content .company .text").hover(function() {
        $(this).find("p.jsfloat").fadeIn(100);
    }, function() {
        $(this).find("p.jsfloat").fadeOut(100);
    });
});
