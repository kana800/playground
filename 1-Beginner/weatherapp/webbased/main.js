var inputtext = document.getElementById("countryname");
var submitbutton = document.getElementById("submitbtn");

/*event listeners for submit button*/
submitbutton.addEventListener("click", checkCountry);

/*weather app information*/
let apikey = '';
let unit = 'standard';

/*
 * return;
 * args: e -> event
 * summary: check if the country user entered is available
 * and grab its weather details
*/
function checkCountry(e){
    let cityname = inputtext.value;
    fetch(`http://api.openweathermap.org/data/2.5/weather?q=${cityname}&appid=${apikey}&units=${unit}`).then(result => {
        return result.json();
        }).then(result => {
            decodeInformation(result);
       }).catch((result) => {
           alert("cant find city");
           return;
       })
}

function decodeInformation(result){
    console.log(result);
    /*change the background color according to the weather*/
    /*
    switch (result.weather[0].main){
        case 'Clear':
            document.body.style.backgroundImage = 'url("clearsky.jpg")';
            break;
        case 'Clouds':
            document.body.style.backgroundImage = 'url("cloudy.jpg")';
            break;
        case 'Rain':
        case 'Drizzle':
        case 'Mist':
            document.body.style.backgroundImage = 'url("rainsky.jpg")';
            break;
        case 'Snow':
            document.body.style.backgroundImage = 'url("snowsky.jpg")';
        default:
            break;
    }
    */

    /*grabbing the widgets*/
    let weathericon = document.getElementById("weathericon");
    let weathertype = document.getElementById("weathertype");
    let weatherdesc = document.getElementById("weatherdesc");
    let weathertemp = document.getElementById("weathertemp");

    /*setting the weather icon*/
    weathericon.src = "http://openweathermap.org/img/wn/" + result.weather[0].icon + ".png";
    weathertype.textContent = 'weather: ' + result.weather[0].main;
    weathertemp.textContent = 'temperature: ' + result.main.temp + 'K';
}
