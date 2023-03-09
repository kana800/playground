<br />
<p style="text-align: center" align="center">
  <a href="https://github.com/kana800/Side-Projects">
	:wind_chime:
  </a>
  <h3 align="center">WIND CHILL</h3>
  <p align="center">
    <br />
    <a href="https://github.com/kana800/Side-Projects/tree/master/1-Beginner">Project List</a>
    ·
    <a href="https://github.com/kana800/Side-Projects/issues">Report Bug</a>
    ·
    <a href="https://github.com/kana800/Side-Projects/issues">Request Feature</a>
  </p>
</p>

### [Web Based](webbased)

The userinterface looks really bad, just ignore it.

- [livepreview](https://codepen.io/kana800/pen/abwXaQO)

**Tier:** 1-Beginner

Windchill combines the actual temperature with the wind speed to calculate
the windchill factor, or what the perceived temperature is versus the actual
temperature.

## User Stories

-   [x] User can select the measurement system calculations will be performed in - Metric or English
-   [x] User can enter the actual temperature and the wind speed
-   [x] User can press the `Calculate` button to display the wind chill
-   [x] User will receive an error message when `Calculate` is clicked if data values are not entered

## Bonus features

-   [ ] User will receive an error message when `Calculate` is clicked if the resulting wind chill factor is greater than or equal to the actual temperature. Since this signifies an internal error in the calculation you may also satisfy this requirement using an assertion
-   [ ] User will be prompted to enter new data values if `Calculate` is pressed without first changing at least one of the input fields
-   [ ] User will see an updated wind chill factor whenever new actual temperature or wind speed values are entered, without being required to click the `Calculate` button

## Useful links and resources

-   [Wikipedia Wind Chill](https://en.wikipedia.org/wiki/Wind_chill)
-   [JavaScript Assert](https://developer.mozilla.org/en-US/docs/Web/API/console/assert)

## Example projects

-   [Wind Chill Calculator](http://www.jsmadeeasy.com/javascripts/Calculators/Wind%20Chill%20Calculator/index.htm)
-   [Svelte Wind Chill Index by Gabriele Corti](https://codepen.io/borntofrappe/pen/WNNrrJg)
