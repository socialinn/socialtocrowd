(function() {
    var Near = this.Near = {};
    Near.map = null;
    Near.geocoder = null;

    Near.initialize = function () {
      var mapOptions = {
        zoom: 8,
        center: new google.maps.LatLng(-34.397, 150.644)
      };
      Near.map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
      Near.geocoder = new google.maps.Geocoder();

      Near.geoloc();
    };

    Near.init = function() {
        google.maps.event.addDomListener(window, 'load', Near.initialize);
        $("#address").keypress(function(e) {
            if (e.which == 13) {
                Near.codeAddress();
            }
        });
    };

    Near.geoloc = function() {
        // Try HTML5 geolocation
        if(navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                var pos = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
                var infowindow = new google.maps.InfoWindow({
                  map: Near.map,
                  position: pos,
                  content: "You're here"
                });

                Near.map.setCenter(pos);
            }, function() {
              Near.handleNoGeolocation(true);
            });
        } else {
        // Browser doesn't support Geolocation
            Near.handleNoGeolocation(false);
        }
    };

    Near.handleNoGeolocation = function(errorFlag) {
        if (errorFlag) {
            var content = 'Error: The Geolocation service failed.';
        } else {
            var content = 'Error: Your browser doesn\'t support geolocation.';
        }

        var options = {
            map: Near.map,
            position: new google.maps.LatLng(60, 105),
            content: content
        };

        var infowindow = new google.maps.InfoWindow(options);
        Near.map.setCenter(options.position);
    };

    Near.codeAddress = function () {
        var address = document.getElementById('address').value;
        Near.geocoder.geocode( { 'address': address}, function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                Near.map.setCenter(results[0].geometry.location);
                var marker = new google.maps.Marker({
                    map: Near.map,
                    position: results[0].geometry.location
                });
            } else {
                alert('Geocode was not successful for the following reason: ' + status);
            }
        });
    };

}).call(this);
