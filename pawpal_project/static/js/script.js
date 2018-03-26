function selectButton(element,species) {
    $(element).parent().find("button").removeClass("active");
    $(element).addClass("active");
    $("#images-left a").hide();
    $(".pet-species-"+species).show();
}

function selectPaws(paws) {
    images=$("#div-rating").find("img");
    for(i=0; i<images.length; i++) {
        if(i<=paws-1) {
            images[i].src="/static/images/paw-filled.png";
        }
        else {
            images[i].src="/static/images/paw-empty.png";
        }
    }
}

function unselectPaws() {
    images=$("#div-rating").find("img");
    for(i=0; i<images.length; i++) {
        if($(images[i]).hasClass("images-rating-empty")) {
            images[i].src="/static/images/paw-empty.png";
        }
        else {
            images[i].src="/static/images/paw-filled.png";
        }
    }
}
      var geocoder;
      var infowindow;
      var marker;
      var map;
function initMap() {
	geocoder = new google.maps.Geocoder();
    	infowindow = new google.maps.InfoWindow;
        var uluru = {lat: 55.8642, lng: 4.2518};
        map = new google.maps.Map(document.getElementById('map'), {
          zoom: 8,
          center: uluru
        });
        marker = new google.maps.Marker({
          position: uluru,
          map: map
        });
	google.maps.event.addListener(map, 'click', function(event) {
   		showAddressFromLatLng(geocoder, map, infowindow, event.latLng);
   		var latlng = new google.maps.LatLng(event.latLng.lat(), event.latLng.lng());
    		marker.setPosition(latlng);
		latitude_variable = event.latLng.lat();
		longitude_variable = event.latLng.lng();
		$("input[name='longtitude']").val(event.latLng.lat());
		$("input[name='latitude']").val(event.latLng.lng());
		getReverseGeocodingData(event.latLng.lat(), event.latLng.lng());
		});
}
    		

function showAddressFromLatLng(geocoder, map, infowindow, latLng){
		geocoder.geocode({'location': latLng}, function(results, status){
        	if (status === 'OK'){
            		if (results[0]) {
			
                	marker.setPosition(latLng);
                	infowindow.setContent(results[0].formatted_address);
                	city = results[0].address_components[2].long_name;
                	infowindow.open(map, marker);
            	} else{
                	console.log("no results found");
            	}
        } else{
            console.log("geocoder failed: " + status);
        }
    });
}	
function getReverseGeocodingData(lat, lng) {
    var latlng = new google.maps.LatLng(lat, lng);
    // This is making the Geocode request
    var geocoder = new google.maps.Geocoder();
    geocoder.geocode({ 'latLng': latlng }, function (results, status) {
        // This is checking to see if the Geoeode Status is OK before proceeding
        if (status == google.maps.GeocoderStatus.OK) {
            console.log(results);
            var address = (results[0].formatted_address);
	    //$("input[name='location']").val(address);
	    $("input[name='location']").val(address);
        }
    });
}
function userFunction() {
    $("#user_form").show();
    $("#pet_form").hide();
}

function petFunction() {
    $("#user_form").hide();
    $("#pet_form").show();
}
