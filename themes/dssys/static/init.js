SlideSync.init(SlideDeck);
SlideController.init(SlideSync);

var writeNumberOfSlidesInSlideFooter = function(ev) {

    var all_the_slides = document.querySelectorAll('.slide_count');
    var i;
    for (i = 0; i < all_the_slides.length; i++) {
            all_the_slides[i].innerHTML = slideEls.length;

    }
};

document.addEventListener("DOMContentLoaded", writeNumberOfSlidesInSlideFooter, false);

