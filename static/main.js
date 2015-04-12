 // $.getJSON("assets/blob.json", function(data) {
 //    $("#content-template").html(tmpl({objects:data}));
 // });

//  $(document).ready("#pop", function() {
// 	$(this).animateCSS("shake", {delay: 5000})
// })

//  $( window ).load(function() {
//   // Run code
// });

//   $(document).on("click", "#pop", function() {
// 	$(this).animateCSS("shake")
// })

//   $(document).ready(function() {
//     // Stuff here
// });





$(document).ready( function(){
	var del = 0;
	$('.running .pop').each(function(i, el) {
		$(el).animateCSS('fadeIn', {delay: del});
		$(el).animateCSS('zoomIn', {delay: del});
		del += 250;
	});

	del = 0;
	$('.cycling .pop').each(function(i, el) {
		$(el).animateCSS('fadeIn', {delay: del});
		$(el).animateCSS('zoomIn', {delay: del});
		del += 250;
	});

	del = 0;
	$('.pop').each(function(i, el) {
		$(el).animateCSS('fadeIn', {delay: del});
		$(el).animateCSS('zoomIn', {delay: del});
		del += 250;
	});
});

/* 
* Test Locations
* Austin lat/long: 30.2676,-97.74298
* Austin WOEID: 2357536
*/
$(document).ready(function() {
	navigator.geolocation.getCurrentPosition(function(position) {
	  loadWeather(position.coords.latitude+','+position.coords.longitude); //load weather using your lat/lng coordinates
	});
});

function loadWeather(location, woeid) {
  $.simpleWeather({
    location: location,
    woeid: '',
    unit: 'f',
    success: function(weather) {
      html = '<h2><i class="icon-'+weather.code+'"></i> '+weather.temp+'&deg;'+weather.units.temp+'</h2>';
      $("#weather").html(html);
    },
    error: function(error) {
      $("#weather").html('<p>'+error+'</p>');
    }
  });
}

