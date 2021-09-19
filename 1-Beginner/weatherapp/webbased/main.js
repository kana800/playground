var inputtext = document.getElementById("countryname");
var submitbutton = document.getElementById("submitbtn");
const url = `http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/{locationKey}`;
/*event listeners for submit button*/
submitbutton.addEventListener("click", checkCountry);

/*
 * return;
 * args: e -> event
 * summary: check if the country user entered is available
 * and grab its weather details
*/
function checkCountry(e){

}