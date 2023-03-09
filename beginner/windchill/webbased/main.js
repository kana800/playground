let calcbutton = document.getElementById("windchillcalc");
let windchillUnits = document.getElementById("answerUnits");
let airtempUnits = document.getElementById("airtempunits");
let windUnits = document.getElementById("windunits");
let SIunit = document.getElementById("units");

calcbutton.onclick = calculateWindChill;
SIunit.onclick = changeUnits;

function calculateWindChill(){
    let windspeed = document.getElementById("wind").value;
    let airtemperature = document.getElementById("airtemperature").value;
    if ((windspeed == "") || (airtemperature == "")){
        alert("Missing Values");
        return;
    }
    let windchill = document.getElementById("windChill");
    windchill.value=(0.0817*(3.71*(Math.pow(windspeed, 0.5))+5.81-0.25*windspeed)*(airtemperature-91.4)+91.4);
}

function changeUnits(){
    if (SIunit.checked == true){
        airtempUnits.innerHTML = "Air Temperature (C)"
        windchillUnits.innerHTML = "C"
        windUnits.innerHTML = "Wind Speed (KMPH)"
    }else{
        airtempUnits.innerHTML = "Air Temperature (F)"
        windchillUnits.innerHTML = "F"
        windUnits.innerHTML = "Wind Speed (MPH)"
    }
}