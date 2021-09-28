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
	

    selectors.get("#contact").validate({
        errorPlacement: function () {
            return false;  // suppresses error message text
        }
    });
    
    /* =================================
    ===  CONTACT FORM               ====
    =================================== */
    selectors.get("#contact").submit(function (e) {
        e.preventDefault();
        var name = selectors.get("#form-name").val();
        var email = selectors.get("#form-email").val();
        var subject = selectors.get("#form-subject").val();
        var message = selectors.get("#form-message").val();
        var dataString = 'name=' + name + '&email=' + email + '&subject=' + subject + '&message=' + message;

        function validEmail(emailAddress) {
            var pattern = new RegExp(/^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i);
            return pattern.test(emailAddress);
        };

      

        if (validEmail(email) && (message.length > 1) && (name.length > 1)) {
            $.ajax({
                type: "POST",
                url: "send-mail.php",
                data: dataString,
                success: function () {
                    selectors.get('.successContent').fadeIn(1000);
                    selectors.get('.errorContent').fadeOut(500);
                }
            });
        }
        else {
            selectors.get('.errorContent').fadeIn(1000);
            selectors.get('.successContent').fadeOut(500);
        }
        return false;
    });



  
})(jQuery);


