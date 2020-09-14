$(document).ready(function(){
    //To initialise the Accordion
    $('.collapsible').collapsible();
    //To initialise dropdown selection
    $("select").material_select();
    //To initialise side nav
    $(".button-collapse").sideNav();
    //To initialise carousel image slider
    $('.carousel.carousel-slider').carousel({fullWidth: true});
    setInterval(function() {
        $(".carousel").carousel("next");
    }, 2500);
  });
//To initialise datepicker
$('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15, // Creates a dropdown of 15 years to control year,
    today: 'Today',
    clear: 'Clear',
    close: 'Ok',
    closeOnSelect: false // Close upon selecting a date,
  });
//To ensure the datepicker works
  document.getElementById("matfix").addEventListener("click", function(e) {
	e.stopPropagation();
});