$(document).ready( function() {

 function adjust_body_offset() {
    $('body').css('padding-top', $('.navbar-default').outerHeight(true) + 'px' );
}

$(window).resize(adjust_body_offset);

$(document).ready(adjust_body_offset);

$('.dropdown-toggle').dropdown();

$("ul.nav li  a").on("click", function(){
   $(".nav").find(".active").removeClass("active");
   $(this).addClass("active");
});



        
 });

 $('.multi-level-dropdown .dropdown-submenu > a').on("mouseenter", function(e) {
     var submenu = $(this);
     $('.multi-level-dropdown .dropdown-submenu .dropdown-menu').removeClass('show');
     submenu.next('.dropdown-menu').addClass('show');
     e.stopPropagation();
   });

   $('.multi-level-dropdown .dropdown').on("hidden.bs.dropdown", function() {
     // hide any open menus when parent closes
     $('.multi-level-dropdown .dropdown-menu.show').removeClass('show');
   });


