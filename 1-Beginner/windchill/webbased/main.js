let calcbutton = document.getElementById("windchillcalc");
let windchillUnits = document.getElementById("answerUnits");
let airtempUnits = document.getElementById("airtempunits");
let windUnits = document.getElementById("windunits");

calcbutton.onclick = calculateWindChill;

function calculateWindChill(){
    let windspeed = document.getElementById("wind").value;
    let airtemperature = document.getElementById("airtemperature").value;
    console.log(airtemperature);
    let windchill = document.getElementById("windChill");
    windchill.value=(0.0817*(3.71*(Math.pow(windspeed, 0.5))+5.81-0.25*windspeed)*(airtemperature-91.4)+91.4);
}