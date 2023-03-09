#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// global variables

int hour = 10;
int minutes = 1;
int second = 10;
int flag = 0;


void delay(int ms){
  clock_t TimeDelay= ms + clock();
  while(TimeDelay > clock());
}

void print(){
  system("clear"); // clear screen
  printf("**************\n");
  printf("\t%d:%d:%d\t\n",hour,minutes,second);
  printf("**************\n");
}


int main(){

  
  while (1){
    if ((hour==0)&&(minutes==0)&&(second==0)){
      break;
    }
    second--;
    if (second < 0){
      minutes -= 1;
      second = 59;
    }
    if (minutes < 0){
      hour -= 1;
      minutes = 59;
    }
    print();
    delay(500000);
  }

  return 0;
}
