$(document).ready(function () {

    $('#search').click(function(){
        let startLoc = $('#startLoc').val();
        let endLoc = $('#endLoc').val();

        console.log(startLoc);

        console.log(endLoc);
    });

    // option for current location
    navigator.geolocation.getCurrentPosition(function(pos){
        console.log(pos);
        // convert coords to city name
        $.ajax({
            url : "https://api.opencagedata.com/geocode/v1/json?q=" + pos.coords.latitude + "+" + pos.coords.longitude + "&key=e16da4bde78f454b9bbb8c21599196e6",
            method : "GET"
        }).then(function(response){
            if(!pastCities.includes(response.results[0].components.city)){
                city = response.results[0].components.city;
                pastCities.unshift(city);
                localStorage.setItem("pastCities", JSON.stringify(pastCities));
                getCity();
            }
        });
    });

});