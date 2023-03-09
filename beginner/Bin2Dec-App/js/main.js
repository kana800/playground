// convert binary to decimal and "alert" the answer
function BinaryToDecimal(binary)
{
  return parseInt(binary,2);
};


function foo()
{
  let binary_value = document.getElementById("bin").value;
  document.getElementById("dec").value = BinaryToDecimal(binary_value);
  alert("Binary value of "+binary_value+" = "+BinaryToDecimal(binary_value));
};

function validateForm()
{
  let x = document.getElementById("bin").value;
  let regex=/^[0-1]+$/;
  if (x == "")
  {
    alert("input is empty")
    return false;
  }
  else if (x.match(regex))
    // number check
  {
    foo()
    return true;
  }
  alert("wrong input"+"="+x);
  return false;
};
