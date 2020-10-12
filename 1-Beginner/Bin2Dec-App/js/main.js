// convert binary to decimal and "alert" the answer
function BinaryToDecimal(binary)
{
  return parseInt(binary,2);
};


function foo()
{
  let binary_value = document.getElementById("bin").value;
  alert("Binary Value is " + BinaryToDecimal(binary_value));
};

