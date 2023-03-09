const f1 = document.querySelector('#display');
const button = document.querySelectorAll('.bt');
const equal = document.querySelector('#equal_btn');
const clear = document.querySelector('.clearbtn');

// adding a event listener
f1.addEventListener('input',validate);
button.forEach((b)=>b.addEventListener('click',enterNumber));
equal.addEventListener('click',calculate);
clear.addEventListener('click',() => f1.value = 0);

let length_check = () => f1.value.length < 9;

function validate(e){
  let val = e.target.value;
  console.log(val);
}

function enterNumber(e){
  let val = e.target.value;
  let re  = /ERR/;
  if (length_check() == true && re.test(f1.value)== false){
    f1.value += val;
  }else if(re.test(f1.value)== true){
    f1.value = val;
  }
}

function calculate(e){
  console.log("works")
  try{
    let val = eval(f1.value);
    f1.value = val;
  } catch (error){
    f1.value = "ERR";
  }
}
