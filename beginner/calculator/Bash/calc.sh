#!/bin/bash

declare -a op=(+ - '*' /)

while true
do
  read -p "enter first number: " n1
  read -p "enter second number: " n2
  echo "Expression List ${op[@]} "
  read -p "enter expression: " exp
  
  ans=$(echo "$n1 $exp $n2" |bc -l)
  printf "%s %s %s = %s\n\n" "$n1" "$exp" "$n2" "$ans" 

done
