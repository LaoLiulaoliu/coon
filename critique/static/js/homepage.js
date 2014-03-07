$(document).ready(function() {
    $("#content .company .text").hover(function() {
        $(this).find(".jsfloat").fadeIn(100);
    }, function() {
        $(this).find(".jsfloat").fadeOut(100);
    });
});
