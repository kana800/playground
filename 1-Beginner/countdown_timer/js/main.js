// selectors
frame = document.getElementById("frame");
startdate = document.getElementById("start");
startbtn = document.getElementById("startbtn");



startbtn.addEventListener("click",(e) => {
	e.preventDefault();
	// change the value from start to pause and vice versa
	let content = startbtn.textContent;
	if (content === "start"){
		starttimer();
	}
})


function getDate(){
	// obtaining and setting up the date.
	let today = new Date();
	let today_ISO = today.toISOString().slice(0,10);
	let enddate = new Date(startdate.valueAsNumber);
	let enddate_ISO = enddate.toISOString().slice(0,10);

	if (enddate - today  < 0){
		frame.textContent = "Long Gone!";
	}else{
		// convert milliseconds to days
		let diff = enddate - today;
		let seconds,minutes,hours,days;

		seconds = parseInt(Math.floor(diff / 1000));
		minutes = parseInt(Math.floor(seconds / 60));
		hours = parseInt(Math.floor(minutes / 60));
		days = parseInt(Math.floor(hours / 24));

		s = parseInt(seconds % 60);
		m = parseInt(minutes % 60);
		h = parseInt(hours % 24);
		
		return  [h,m,s];
	}
}

function starttimer(){
  let datearray = getDate();
  function timer(){
	datearray[2]--;
	// if seconds == 0
	if (datearray[2] < 0){
		datearray[1] -= 1;
		datearray[2] = 59;
	}
	if (datearray[1] < 0){
		datearray[2] -= 1;
		datearray[1] = 59;
	}
	
	if ((datearray[2] == 0)&&(datearray[1] == 0)&&datearray[2] == 0){
		frame.textContent = "END";
		return;
	}
    frame.textContent = datearray[0]+":"+datearray[1]+":"+datearray[2];
  }

  // using set interval function
  setInterval(timer,1000);
}


