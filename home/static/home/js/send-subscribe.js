(function ($) {

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

    /* =================================
    ===  SUBSCRIBE fORM             ====
    =================================== */
    selectors.get("#subscribe-form").validate({
        errorPlacement: function(){
            return false;  // suppresses error message text
        },
        submitHandler: function (form) {
            //$(form).find('.input-group-addon').find('.icon-email2').removeClass('icon-email2').addClass('icon-line-loader icon-spin');
            $(form).ajaxSubmit({
                target: '#subscribe-result',
                success: function () {
                    // $(form).find('.input-group-addon').find('.icon-line-loader').removeClass('icon-line-loader icon-spin').addClass('icon-email2');
                    selectors.get('#subscribe-form').find('.subscribe-form-control').val('');
                    selectors.get('#subscribe-result').attr('data-notify-msg', selectors.get('#subscribe-result').html()).html('');
                    SEMICOLON.widget.notifications(selectors.get('#subscribe-result'));
                }
            });
        }
    });




})(jQuery);


