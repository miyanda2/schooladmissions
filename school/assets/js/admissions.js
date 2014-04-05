/**
 * Created by Sandeep on 30/3/14.
 */

$('.institute').hover(function() {
        $(this).find('.institute-view').show();
    },
    function () {
        $(this).find('.institute-view').hide();
    }
);