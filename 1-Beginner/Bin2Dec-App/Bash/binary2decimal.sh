#!/bin/bash
printf "This is program converts binary numbers to decimal\n"

#reading the input
read input;


length=${#input}
#checking for digits greater than 9
if [[ $length -ge 9 ]] 
then
  echo "binary number cannot be greater than 8" 1>&2
  exit
fi

#checking for other digits
if [[ $input =~ [2-9] ]]
then
  echo "binary number cannot contain numbers other than 0 and 1" 1>&2
  exit
fi

decimal=`echo "ibase=2;obase=A;$input" | bc`
echo "decimal number is $decimal"
