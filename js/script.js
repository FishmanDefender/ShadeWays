$(document).ready(function () {

    let startLat;
    let startLong;

    let endLat;
    let endLong;

    function calcRoute(start,end) {
        let request = {
          origin:start,
          destination:end,
          travelMode: google.maps.TravelMode.DRIVING,
          provideRouteAlternatives : false
        };
        directionsService.route(request, function(result, status) {
          if (status == google.maps.DirectionsStatus.OK) {
            directionsDisplay.setDirections(sampleObj);
            //displayDirections(result);
          }
        });
    }


    $('#search').click(function(){
        let startLoc = $('#startLoc').val();
        let endLoc = $('#endLoc').val();

        // convert address to coords
        $.ajax({
            url : `https://maps.googleapis.com/maps/api/geocode/json?address=${startLoc}&key=${apiKey}`,
            method : "GET"
        }).then(function(response){
            startLat = response.results[0].geometry.location.lat;
            startLong = response.results[0].geometry.location.lng;

            $.ajax({
                url : `https://maps.googleapis.com/maps/api/geocode/json?address=${endLoc}&key=${apiKey}`,
                method : "GET"
            }).then(function(response){
                endLat = response.results[0].geometry.location.lat;
                endLong = response.results[0].geometry.location.lng;

                let startObj = new google.maps.LatLng(startLat, startLong);
                let endObj = new google.maps.LatLng(endLat, endLong);

                let routeThing = calcRoute(startObj, endObj);

                console.log(startObj);
                console.log(endObj);

                // ajax request to python server
                // `https://maps.googleapis.com/maps/api/directions/json?origin=${startLat},${startLong}&destination=${endLat},${engLong}&key=AIzaSyCCKpKX4eqJYPKQOB-HlcuxdlOArp_0nNg`

                // $.ajax({
                //     url : `https://maps.googleapis.com/maps/api/directions/json?origin=${startLat},${startLong}&destination=${endLat},${endLong}&key=AIzaSyCCKpKX4eqJYPKQOB-HlcuxdlOArp_0nNg`,
                //     method : "GET"
                // }).then(function(response){
                //     console.log(response);
                // });


                // $.ajax({
                //     url : `https://maps.googleapis.com/maps/api/directions/json?origin=${startLat},${startLong}&destination=${endLat},${endLong}&key=AIzaSyCCKpKX4eqJYPKQOB-HlcuxdlOArp_0nNg`,
                //     method : "GET"
                // }).then(function(response){
                //     console.log(response);
                // });

                calculateAndDisplayRoute(directionsService, directionsRenderer);

                $(".change").attr({
                    class: "change min addy"
                });

                $(".container").attr({
                    class: "container move"
                });

                $("#currentLoc").hide();

                $(".logo").hide();

                $("#search").hide();

                $(".addy").css("width", "40vw");

            });
        });


    });

    function calculateAndDisplayRoute(directionsService, directionsRenderer) {
        let start = document.getElementById('start').value;
        let end = document.getElementById('end').value;
        directionsService.route({
          origin: start,
          destination: end,
          travelMode: 'DRIVING'
        }, function(response, status) {
          if (status === 'OK') {
            directionsRenderer.setDirections(response);
          } else {
            window.alert('Directions request failed due to ' + status);
          }
        });
    }

    // option for current location
    $('#currentLoc').click(function(){
        navigator.geolocation.getCurrentPosition(function(pos){
            console.log(pos);
            startLat = pos.coords.latitude;
            startLong = pos.coords.longitude;
            // convert coords to address
            $.ajax({
                url : `https://maps.googleapis.com/maps/api/geocode/json?latlng=${pos.coords.latitude},${pos.coords.longitude}&key=${apiKey}`,
                method : "GET"
            }).then(function(response){
                // console.log(response.results[0].formatted_address);
                $('#startLoc').val(response.results[0].formatted_address);
            });
        });
    });

});