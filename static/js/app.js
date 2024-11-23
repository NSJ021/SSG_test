$(function () {

    "use strict";

    // Made the left sidebar's min-height to window's height
    var winHeight = $(window).height();
    $(".dashboard-nav").css("min-height", winHeight);


    // Magnify activation
    $(".portfolio-item").magnificPopup({
        delegate: "a",
        gallery:{enabled:true},
        type: "image"
    });

    $(".game-magnify-gallery").lightGallery();

    $(document).on("click", ".compare-btn", function(event) {
        if($(event.currentTarget).hasClass("active")){
            $(event.currentTarget).removeClass("active");
            $.jnoty("Game has been removed from compare list", {
                header: "Warning",
                icon: "fa fa-check-circle",
                sticky: true,
                theme: "jnoty-warning"
            });

        } else {
            $(event.currentTarget).addClass("active");
            $.jnoty("Game has been added to compare list", {
                header: "Success",
                icon: "fa fa-check-circle",
                sticky: true,
                theme: "jnoty-success"
            });
        }
    });

    $(document).on("click", ".wishlist-btn", function(event) {
        if($(event.currentTarget).hasClass("active")){
            $(event.currentTarget).removeClass("active");
            $.jnoty("Game has been removed from wishlist list", {
                header: "Warning",
                icon: "fa fa-check-circle",
                sticky: true,
                theme: "jnoty-warning"
            });

        } else {
            $(event.currentTarget).addClass("active");
            $.jnoty("Game has been added to wishlist list", {
                header: "Success",
                icon: "fa fa-check-circle",
                sticky: true,
                theme: "jnoty-success"
            });
        }
    });

    // Header shrink while page scroll
    adjustHeader();
    doSticky();
    placedDashboard();
    $(window).on("scroll", function () {
        adjustHeader();
        doSticky();
        placedDashboard();
    });

    // Header shrink while page resize
    $(window).on("resize", function () {
        adjustHeader();
        doSticky();
        placedDashboard();
    });

    function adjustHeader()
    {
        var windowWidth = $(window).width();
        if(windowWidth > 0) {
            if ($(document).scrollTop() >= 100) {
                if($(".header-shrink").length < 1) {
                    $(".sticky-header").addClass("header-shrink");
                }
                if($(".do-sticky").length < 1) {
                    $(".company-logo img").attr(
                        "src", "static/img/logos/logo.jpg");
                }
            }
            else {
                $(".sticky-header").removeClass("header-shrink");
                if($(".do-sticky").length < 1 && $(
                    ".fixed-header").length == 0 && $(
                        ".fixed-header2").length == 0) {
                    $(".company-logo img").attr(
                        "src", "static/img/logos/logo.jpg");
                } else {
                    $(".company-logo img").attr(
                        "src", "static/img/logos/logo.jpg");
                }
            }
        } else {
            $(".company-logo img").attr("src", "static/img/logos/logo.jpg");
        }
    }

    function doSticky()
    {
        if ($(document).scrollTop() > 40) {
            $(".do-sticky").addClass("sticky-header");
            //$('.do-sticky').addClass('header-shrink');
        }
        else {
            $(".do-sticky").removeClass("sticky-header");
            //$('.do-sticky').removeClass('header-shrink');
        }
    }

    function placedDashboard() {
        var headerHeight = parseInt($(".main-header").height(), 10);
        $(".dashboard").css("top", headerHeight);
    }


    // Page scroller initialization.
    $.scrollUp({
        activeOverlay: false,
        animation: "fade",
        animationSpeed: 200,
        easingType: "linear",
        scrollDistance: 300,
        scrollFrom: "top",
        scrollImg: false,
        scrollName: "page_scroller",
        scrollSpeed: 500,
        scrollTarget: false,
        scrollText: "<i class='fa fa-chevron-up'></i>",
        scrollTitle: false,
        scrollTrigger: false,
        zIndex: 2147483647
    });

    // Select picket
    $(".selectpicker").selectpicker();


    // Carousel with partner initialization
    (function () {
        $("#ourPartners").carousel({interval: 3600});
    }());

    $(".our-partners .item").each(function(index, element) {
        var itemToClone = $(element);
        for (var i = 1; i < 4; i++) {
            itemToClone = itemToClone.next();
            if (!itemToClone.length) {
                itemToClone = $(this).siblings(":first");
            }
            itemToClone.children(":first-child").clone()
                .addClass("cloneditem-" + (i))
                .appendTo($(this));
        }
    })

    // Slick Sliders
    $(".slick-carousel").each(function () {
        var slider = $(this);
        $(this).slick({
            infinite: true,
            dots: false,
            arrows: false,
            centerMode: true,
            centerPadding: "0"
        });
        $(this).closest(".slick-slider-area").find(
            ".slick-prev").on("click", function () {
            slider.slick("slickPrev");
        });
        $(this).closest(".slick-slider-area").find(
            ".slick-next").on("click", function () {
            slider.slick("slickNext");
        });
    });

    // Alert Time Out
    setTimeout(function () {

        $("#message").fadeOut("slow");

    }, 4000); // <-- time in milliseconds
})(jQuery);