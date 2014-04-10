/**
 * Created by Sandeep on 30/3/14.
 */

$('.institute').hover(function () {
        $(this).find('.institute-view').show();
    },
    function () {
        $(this).find('.institute-view').hide();
    }
);

/*
function apply_app_form(ins_id, app_form_id) {
    $.get('YOUR_VIEW_HERE/' + ins_id + '/' + app_form_id + '/', function (data) {
        //alert("counter updated!");
    });
}*/
