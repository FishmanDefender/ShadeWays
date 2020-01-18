$(document).ready(function () {

    let startLat;
    let startLong;

    let endLat;
    let endLong;

    function Position(lat, long){
        this.lat = lat;
        this.long = long;
    }


    $('#search').click(function(){
        let startLoc = $('#startLoc').val();
        let endLoc = $('#endLoc').val();

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

                let startObj = new Position(startLat, startLong);
                let endObj = new Position(endLat, endLong);

                console.log(startObj);
                console.log(endObj);
            });
        });


    });

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