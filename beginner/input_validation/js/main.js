// selectors

username = document.getElementById("username");
email = document.getElementById("email");
button = document.getElementById("btn");
password = document.getElementById("pass");

button.addEventListener("click",(e) => {
	e.preventDefault();
	console.log(e);
	// function to validate the string
	if (validateEmail(email.value) && validatePassword(str) && validateName(str)){
		alert("sucess");
	}else{
		alert("error")
	}

})

function validateEmail(str){
	let re = /.@gmail.com$/;
	var con = re.test(str);
	return con;
}

function validatePassword(str){
	let re = /^(?=.*[A-Z]{5})(?=.*[^/w]{6})(?=.*[-]{2})$/;
	var con = re.test(str);
	return con;
}

function validateName(str){
	let re = /[^\s]/;
	var con = re.test(str);
	return con;
}
