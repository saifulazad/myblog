/**
 * Created by azad on 9/27/15.
 */




$(document).ready(function() {

    var pathname = window.location.pathname;

    if ( pathname === "/about_us") {
        $("#about_us").addClass("active");
      }
    if ( pathname === "/python") {
        $("#python").addClass("active");
      }

});
