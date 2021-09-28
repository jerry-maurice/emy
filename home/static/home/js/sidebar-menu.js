
// ==============================================
// Right Sidemenu Bar
// ==============================================

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

$(document).ready(function () {
    $menuSidebar = selectors.get('.pushmenu-right');
    $menusidebarNav = selectors.get('#menu-sidebar-list-icon');
    $menuSidebarclose = selectors.get('#menu-sidebar-close-icon');

    //sidebar menu navigation icon toggle
    $menusidebarNav.on('click', function () {
        $(this).toggleClass('active');
        selectors.get('.pushmenu-push').toggleClass('pushmenu-push-toleft pushmenu-active');
        $menuSidebar.toggleClass('pushmenu-open');


    });

    //sidebar menu close icon
    $menuSidebarclose.on('click', function () {
        $menusidebarNav.removeClass('active');
        selectors.get('.pushmenu-push').removeClass('pushmenu-push-toleft');
        $menuSidebar.removeClass('pushmenu-open');

    });

    //Window Click Sidemenu Hide
    selectors.get('html').on('click', function (sMenuOutsite) {
        // Then find a target: element you clicked on.
        var target = $(sMenuOutsite.target);

        // Close your sidebar only if you clicked outside of this sidebar:
        if ((target.closest($menusidebarNav).length === 0) && (target.closest($menuSidebarclose).length === 0) && (target.closest('.pushmenu').length === 0)) {
            $menusidebarNav.removeClass('active');
            selectors.get('.pushmenu-push').removeClass('pushmenu-push-toleft');
            $menuSidebar.removeClass('pushmenu-open')
        }
    });

    //Achor Link Click Sidemenu Hide
    selectors.get('.side-menu .singlepage-nav li a').on('click', function (sMenuLink) {
        // Then find a target: element you clicked on.
        var targetLink = $(sMenuLink.target);

        // Close your sidebar only if you clicked outside of this sidebar:
        if (targetLink.closest($menusidebarNav).length === 0) {
            $menusidebarNav.removeClass('active');
            selectors.get('.pushmenu-push').removeClass('pushmenu-push-toleft');
            $menuSidebar.removeClass('pushmenu-open')
        }
    });

    if ($(document).find('#pushmenu-right').hasClass('pushmenu')) {
        selectors.get('body').addClass('pushmenu-push pushmenu-push-left');
        selectors.get('body').removeClass('pushmenu-push-right');
    }

});

// ==============================================
// Left Sidemenu Bar
// ==============================================

$(document).ready(function () {
    $menuLeftSidebar = selectors.get('.pushmenu-left');
    $menuLeftsidebarNav = selectors.get('#menu-left-sidebar-list-icon');
    $menuLeftSidebarclose = selectors.get('#menu-left-sidebar-close-icon');

    //sidebar menu navigation icon toggle
    $menuLeftsidebarNav.on('click', function () {
        $(this).toggleClass('active');
        selectors.get('.pushmenu-push').toggleClass('pushmenu-push-toright pushmenu-active');
        $menuLeftSidebar.toggleClass('pushmenu-open');


    });

    //sidebar menu close icon
    $menuLeftSidebarclose.on('click', function () {
        $menuLeftsidebarNav.removeClass('active');
        selectors.get('.pushmenu-push').removeClass('pushmenu-push-toright');
        $menuLeftSidebar.removeClass('pushmenu-open');

    });

    //Window Click Sidemenu Hide
    selectors.get('html').on('click', function (sMenuOutsite) {
        // Then find a target: element you clicked on.
        var target = $(sMenuOutsite.target);

        // Close your sidebar only if you clicked outside of this sidebar:
        if ((target.closest($menuLeftsidebarNav).length === 0) && (target.closest($menuLeftSidebarclose).length === 0) && (target.closest('.pushmenu').length === 0)) {
            $menuLeftsidebarNav.removeClass('active');
            selectors.get('.pushmenu-push').removeClass('pushmenu-push-toright');
            $menuLeftSidebar.removeClass('pushmenu-open')
        }
    });

    //Achor Link Click Sidemenu Hide
    selectors.get('.side-menu .singlepage-nav li a').on('click', function (sMenuLink) {
        // Then find a target: element you clicked on.
        var targetLink = $(sMenuLink.target);

        // Close your sidebar only if you clicked Link of this sidebar:
        if (targetLink.closest($menusidebarNav).length === 0) {
            $menuLeftsidebarNav.removeClass('active');
            selectors.get('.pushmenu-push').removeClass('pushmenu-push-toright');
            $menuLeftSidebar.removeClass('pushmenu-open')
        }
    });

    if ($(document).find('.pushmenu-left').hasClass('pushmenu')) {
        selectors.get('body').addClass('pushmenu-push pushmenu-push-right');
        selectors.get('body').removeClass('pushmenu-push-left');
    }


});

