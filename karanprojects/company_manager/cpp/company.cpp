#include <iostream>
#include <string>
#include "employee.h"

int main(int argc, char **argv){
    // creating an hourly employee
    HourlyEmployee hourlyemployee1 = HourlyEmployee("Jake", "Tame","Hourly", 5);
    std::cout << hourlyemployee1.getFullName();
    std::cout << hourlyemployee1.getPay();
}