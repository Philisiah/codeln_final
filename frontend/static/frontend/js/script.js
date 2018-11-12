document.addEventListener('DOMContentLoaded', function () {

    // Get all "navbar-burger" elements
    let $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

    // Check if there are any navbar burgers
    if ($navbarBurgers.length > 0) {

        // Add a click event on each of them
        $navbarBurgers.forEach(function ($el) {
            $el.addEventListener('click', function () {

                // Get the target from the "data-target" attribute
                let target = $el.dataset.target;
                let $target = document.getElementById(target);

                // Toggle the class on both the "navbar-burger" and the "navbar-menu"
                $el.classList.toggle('is-active');
                $target.classList.toggle('is-active');

            });
        });
    }

});

function goBack() {
    if (document.referrer.toString().length === 0) {
        window.location.href = '/';

    } else {
        window.location.href = document.referrer;
    }
    // window.history.go(-1)
}

$('.dismiss-notification').on('click', function () {
        $(this).parent().hide(100)
    }
);

/**
 * Created by cpkthompson on 1/15/2018.
 */
$('.quotes').slick({
    dots: true,
    infinite: true,
    autoplay: true,
    autoplaySpeed: 5000,
    speed: 800,
    slidesToShow: 1,
    adaptiveHeight: true
});