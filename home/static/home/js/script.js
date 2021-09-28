
// ==============================================
// Main Script
// ==============================================

    "use strict";
	
	function Selector_Cache() {
    var collection = {};

    function get_from_cache(selector) {
        if (undefined === collection[selector]) {
            collection[selector] = $(selector);
        }

        return collection[selector];
    }

    return {
        get: get_from_cache
    };
}

var selectors = new Selector_Cache();	
	

    function scroll_top() {
        selectors.get(".scroll-top").on('click', function() {
            return selectors.get("html, body").animate({
                scrollTop: 0
            }, 2e3), !1
        }), selectors.get('.scroll-down[href^="#"], .scroll-to-target[href^="#"]').on("click", function(scroll_top) {
            scroll_top.preventDefault();
            var e = this.hash,
                i = $(e);
            selectors.get("html, body").stop().animate({
                scrollTop: i.offset().top
            }, 900, "swing", function() {
                window.location.hash = e
            })
        })
    }

    function js_height() {
        var js_height = $(window).height();
        selectors.get(".js-fullscreen-height").css("height", js_height)
    }

    function header_prepare() {
        var header_prepare = $(window).scrollTop();
        $(window).height();
        header_prepare > 150 ? selectors.get(".header").addClass("header-prepare") : selectors.get(".header").removeClass("header-prepare"), header_prepare > 1 ? selectors.get(".header").addClass("header-fixed") : selectors.get(".header").removeClass("header-fixed")
    }

    function mobile_device() {
        nav_menu.css("max-height", $(window).height() - selectors.get(".header").height() - 20 + "px"), $(window).width() <= 1024 ? selectors.get(".header").addClass("mobile-device") : $(window).width() > 1024 && selectors.get(".header").removeClass("mobile-device")
    }

    function ini_owlCarousel() {
        selectors.get(".fullscreen-slider").owlCarousel({
            slideSpeed: 350,
            singleItem: !0,
            autoHeight: !1,
            navigation: !0,
            pagination: !0,
            navigationText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
            responsive: !0
        }), selectors.get(".intro-text-slider").owlCarousel({
            slideSpeed: 400,
            singleItem: !0,
            autoHeight: !1,
            navigation: !0,
            pagination: !0,
            navigationText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
            responsive: !0
        }), selectors.get(".team-carousel").owlCarousel({
            autoPlay: !0,
            stopOnHover: !0,
            items: 3,
            itemsDesktop: [1170, 3],
            itemsDesktopSmall: [1e3, 2],
            itemsTabletSmall: [768, 1],
            itemsMobile: [480, 1],
            pagination: !0,
            navigation: !1,
            navigationText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"]
        }), selectors.get(".testimonial-carousel").owlCarousel({
            autoPlay: !0,
            autoHeight: !0,
            stopOnHover: !0,
            singleItem: !0,
            slideSpeed: 350,
            pagination: !0,
            navigation: !1,
            navigationText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"]
        }), selectors.get(".client-carousel").owlCarousel({
            autoPlay: 2500,
            stopOnHover: !0,
            items: 6,
            itemsDesktop: [1170, 5],
            itemsDesktopSmall: [1024, 4],
            itemsTabletSmall: [768, 3],
            itemsMobile: [480, 2],
            pagination: !1,
            navigation: !1,
            navigationText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"]
        }), selectors.get(".image-carousel").owlCarousel({
            navigation: !0,
            pagination: !0,
            slideSpeed: 350,
            paginationSpeed: 400,
            singleItem: !0,
            navigationText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
            autoPlay: !1,
            autoHeight: !0,
            responsive: !0
        }), selectors.get(".post-carousel").owlCarousel({
            autoPlay: !1,
            autoHeight: !0,
            stopOnHover: !0,
            singleItem: !0,
            slideSpeed: 350,
            pagination: !0,
            navigation: !1,
            navigationText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
            responsive: !0
        })
    }

    function ini_wow() {
        
            var ini_wow = new WOW({
                boxClass: "wow",
                animateClass: "animated",
                offset: 90,
                mobile: !1,
                live: !0
            });
            selectors.get("body").hasClass("wow-animate") && ini_wow.init()
       
    }

    function ini_portfolio() {
        var ini_portfolio, subtract = selectors.get(".portfolio-grid");
        ini_portfolio = subtract.hasClass("masonry") ? "masonry" : "fitRows", subtract.isotope({
            itemSelector: ".portfolio-item",
            layoutMode: ini_portfolio,
            animationOptions: {
                duration: 750,
                easing: "linear",
                queue: !1
            }
        }), selectors.get(".portfolio-filter").on("click", ".categories", function() {
            var ini_portfolio = $(this).attr("data-filter");
            subtract.isotope({
                filter: ini_portfolio
            })
        }), selectors.get(".categories-filter").each(function(ini_portfolio, subtract) {
            var categories = $(subtract);
            categories.on("click", ".categories", function() {
                categories.find(".active").removeClass("active"), $(this).addClass("active")
            })
        })
    }

    function ini_parallax(substract) {
        var ini_window = $(window).scrollTop(),
            parallax_height = selectors.get(".parallax").height(),
            set1 = .5 * ini_window,
            set2 = -(.5 * ini_window),
            opacity = ini_window / parallax_height;
        selectors.get(".parallax").hasClass("parallax-section") && substract.css("top", set1), selectors.get(".parallax").hasClass("parallax-section2") && substract.css("top", set2), selectors.get(".parallax").hasClass("parallax-static") && substract.css("top", 1 * ini_window), selectors.get(".parallax").hasClass("parallax-opacity") && substract.css("opacity", 1 - 1 * opacity), selectors.get(".parallax").hasClass("parallax-background1") && substract.css("background-position", "left " + set1 + "px"), selectors.get(".parallax").hasClass("parallax-background2") && substract.css("background-position", "left " + -set1 + "px")
    }

    function popup() {
        selectors.get(".gallery-popup").magnificPopup({
            delegate: ".gallery-popup-link",
            type: "image",
            tLoading: "Loading image #%curr%...",
            mainClass: "mfp-img-mobile",
            gallery: {
                enabled: !0,
                navigateByImgClick: !0,
                preload: [0, 1]
            },
            image: {
                tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
                titleSrc: function(a) {
                    return a.el.attr("title")
                }
            }
        }), selectors.get(".popup-youtube, .popup-vimeo, .popup-gmaps, .video-popup").magnificPopup({
            disableOn: 700,
            type: "iframe",
            mainClass: "mfp-fade",
            removalDelay: 160,
            preloader: !1,
            fixedContentPos: !1
        })
    }

    function ini_settings() {
        selectors.get(".skillbar").appear(function() {
            selectors.get(".skillbar").each(function() {
                $(this).find(".skillbar-bar-child").animate({
                    width: $(this).attr("data-percent")
                }, 2e3)
            })
        }), selectors.get(".counter-num").appear(function() {
            var counter_num = $(this);
            counter_num.countTo({
                from: 0,
                to: counter_num.html(),
                speed: 1300,
                refreshInterval: 60
            })
        }), selectors.get(".tab-content > .tab-pane").hide(), selectors.get(".tab-content > .tab-pane:first-of-type").show(), selectors.get(".tabs a").on('click', function(ini_tab) {
            ini_tab.preventDefault();
            var active = $(this),
                tab_group = "#" + active.parents(".tabs").data("tabgroup"),
                child = active.closest("li").siblings().children("a"),
                active_href = active.attr("href");
            child.removeClass("active"), active.addClass("active"), $(tab_group).children(".tab-pane").hide(), $(active_href).fadeIn().show;
            var filter_href = selectors.get(".tab-content > .tab-pane").filter($(this).attr("href")).height();
            selectors.get(".tab-content").animate({
                height: filter_href
            }, function() {
                selectors.get(".tab-content").css("height", "auto")
            })
        });
        selectors.get(".toggle > .toggle-content").hide();
        selectors.get(".toggle > .toggle-title > a").on('click', function() {
            if ($(this).hasClass("active")) $(this).parent().next().slideUp("easeOutExpo"), $(this).removeClass("active");
            else {
                $(this).parent().next(".toggle-content");
                $(this).addClass("active"), $(this).parent().next().slideDown("easeOutExpo")
            }
            return !1
        });
        var accordion = selectors.get(".accordion > .accordion-content").hide();
        accordion.first().slideDown("easeOutExpo"), selectors.get(".accordion > .accordion-title > a").first().addClass("active"), selectors.get(".accordion > .accordion-title > a").on('click', function() {
            var accordion_content = $(this).parent().next(".accordion-content");
            return selectors.get(".accordion > .accordion-title > a").removeClass("active"), $(this).addClass("active"), accordion.not(accordion_content).slideUp("easeInExpo"), $(this).parent().next().slideDown("easeOutExpo"), !1
        })
    }
	
	
	
    $(document).ready(function() {
     
scroll_top(), js_height(), header_prepare(), mobile_device(), ini_owlCarousel(), ini_wow(), ini_portfolio(), popup(), ini_settings()
    }), 
	
	$(window).on('load', function() {
        ini_portfolio(), selectors.get("#preloader").fadeOut("slow", function() {
            $(this).remove()
        })
    }), $(window).resize(function() {
        js_height(), header_prepare(), mobile_device(), ini_owlCarousel()
    }), $(window).scroll(function() {
        header_prepare()
    });
    var slide_bg = selectors.get(".slide-bg-image, .bg-image");
    slide_bg.each(function(a) {
        $(this).attr("data-background-img") && $(this).css("background-image", "url(" + $(this).data("background-img") + ")")
    });
    var nav_mobile = selectors.get(".nav-mobile"),
        nav_menu = selectors.get(".nav-menu");
    nav_mobile.on('click', function() {
        $(this).hasClass("active") ? $(this).hasClass("active") && (nav_mobile.removeClass("active"), nav_menu.removeClass("active")) : (nav_mobile.addClass("active"), nav_menu.addClass("active"))
    });
    var menu_one, menu_two = $(".menu-has-sub");
    $(".mobile-device .menu-has-sub").find(".fa:first").removeClass("fa-angle-right").addClass("fa-angle-down"), menu_two.on('click', function() {
        return $(".header").hasClass("mobile-device") ? (menu_one = $(this).parent("li:first"), menu_one.hasClass("menu-opened") ? menu_one.find(".sub-dropdown:first").slideUp(function() {
            menu_one.removeClass("menu-opened"), menu_one.find(".menu-has-sub").find(".fa:first").removeClass("fa-angle-up").addClass("fa-angle-down")
        }) : ($(this).find(".fa:first").removeClass("fa-angle-down").addClass("fa-angle-up"), menu_one.addClass("menu-opened"), menu_one.find(".sub-dropdown:first").slideDown()), !1) : !1
    }), menu_one = menu_two.parent("li"), menu_one.hover(function() {
        $(".header").hasClass("mobile-device") || $(this).find(".sub-dropdown:first").stop(!0, !0).fadeIn("fast")
    }, function() {
        $(".header").hasClass("mobile-device") || $(this).find(".sub-dropdown:first").stop(!0, !0).delay(100).fadeOut("fast")
    });
    var overlay_m_btn = selectors.get(".overlay-menu-btn"),
        overlay_m = selectors.get(".overlay-menu"),
        overlay_m_close = selectors.get(".overlay-menu-close");
    overlay_m_btn.on('click', function() {
        $(this).hasClass("active") ? $(this).hasClass("active") && (overlay_m_btn.removeClass("active"), overlay_m.removeClass("active"), selectors.get("body").removeClass("overlay-menu-active")) : (overlay_m_btn.addClass("active"), overlay_m.addClass("active"), selectors.get("body").addClass("overlay-menu-active"))
    }), overlay_m_close.on('click', function() {
        overlay_m_btn.hasClass("active") && overlay_m.hasClass("active") && (overlay_m_btn.removeClass("active"), overlay_m.removeClass("active"), selectors.get("body").removeClass("overlay-menu-active"))
    }), selectors.get(".video-fit, .audio-fit, .post-media").fitVids();
    var C;
    C = $(window).width() >= 1024 ? "position" : "transform", $(window).stellar({
        responsive: !0,
        positionProperty: C,
        horizontalScrolling: !1
    }), selectors.get(".parallax").each(function() {
        var a = $(this);
        $(window).scroll(function() {
            ini_parallax(a)
        }), ini_parallax(a)
    }), selectors.get(".singlepage-nav").singlePageNav({
        offset: 0,
        currentClass: "current",
        filter: ":not(.external)",
        easing: "easeInOutExpo",
        speed: 1500,
        updateHash: !0,
        beforeStart: function() {
            nav_mobile.hasClass("active") && (nav_mobile.removeClass("active"), nav_menu.removeClass("active")), overlay_m_btn.hasClass("active") && (overlay_m_btn.removeClass("active"), overlay_m.removeClass("active"), selectors.get("body").removeClass("overlay-menu-active"))
        }
    })
