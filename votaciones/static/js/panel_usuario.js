function showonlyone(thechosenone) {

    $('.card-body').each(function(index) {

         if ($(this).attr("id") == thechosenone) {

              $(this).show(200);

         }

         else {

              $(this).hide(600);

         }

    });

}

$(document).ready(function () {
    $('.list-group a').click(function(e) {

        $('.list-group a.active').removeClass('active');

        var $parent = $(this).parent();
        $parent.addClass('active');
        e.preventDefault();
    });
});