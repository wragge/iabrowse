$(function() {
    var $images = $('.images').isotope({
      // options
        "layoutMode": 'fitRows',
        "itemSelector": ".image-cell",
        "sortBy" : "original-order",
        "fitRows": {"columnWidth": 200, "gutter": 5}
    });
    $images.imagesLoaded().progress( function() {
        $images.isotope('layout');
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