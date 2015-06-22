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
});