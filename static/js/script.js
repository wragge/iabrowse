$(function() {

var $grid = $('.images').isotope({
    "layoutMode": 'fitRows',
    "itemSelector": ".image-cell",
    "sortBy" : "original-order",
    "fitRows": {"columnWidth": 200, "gutter": 5}
});
// layout Isotope after each image loads
$grid.imagesLoaded().progress( function() {
  $grid.isotope('layout');
});

    $("body").keydown(function(e){
    // left arrow
    if (e.which == 37) {
        var previous = $("#previous").attr('href');
        if (typeof previous !== "undefined") {
            window.location.href = previous;
        } 

    // right arrow
    } if (e.which == 39) {
        // do something
        var next = $("#next").attr('href');
        if (typeof next !== "undefined") {
            window.location.href = next;
        } 
    }   
});
});