#!/bin/bash

# color codes
expand_bg="\e[K"
blue_bg="\e[0;104m${expand_bg}"
red_bg="\e[0;101m${expand_bg}"
green_bg="\e[0;102m${expand_bg}"
yellow_bg="\e[0;103m${expand_bg}"
white_bg="\e[0;107m${expand_bg}"

#High Intensty backgrounds

blackhi="\e[0;100m${expand_bg}"
redhi="\e[0;101m${expand_bg}"
greenhi="\e[0;102m${expand_bg}"
yellowhi="\e[0;103m${expand_bg}"
bluehi="\e[0;104m${expand_bg}"
purplehi="\e[0;105m${expand_bg}"
cyanhi="\e[0;106m${expand_bg}"
whitehi="\e[0;107m${expand_bg}"

reset="\e[0m"


col=`tput cols`
lin=`tput lines`

color(){
  var=$1
  for (( c=1; c<=$lin; c++ ))
  do
  echo -e "${var}${reset}"
  done
  
  sleep 5
}

color $blue_bg
color $red_bg
color $green_bg
color $yellow_bg
color $white_bg
color $bluehi
color $redhi
color $greenhi
color $yellowhi
color $whitehi
color $blackhi
color $purplehi
color $cyanhi
