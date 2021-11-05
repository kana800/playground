#ifndef EMPLOYEE_H
#define EMPLOYEE_H

/*
 * contains the class employee and the subclass for 
 * employee
*/

class Employee{

    private:
        int employeeid;
        std::string firstname;
        std::string lastname;
        std::string employeetype;
        int pay;
    public:
        /*constructor*/
        Employee(const std::string a_firstname, const std::string a_lastname,
            const std::string a_employeetype, const int a_pay = 1){
                firstname = a_firstname;
                lastname = a_lastname;
                employeetype = a_employeetype;
                pay = a_pay;
        }

        const std::string getFullName() const {
            return firstname + " " + lastname;
        }

        const std::string getEmployeeType() const{
            return employeetype;
        }

        const std::string getemployeeDescription() const {
            return std::to_string(employeeid) + ": " + getFullName();
        }

        void setEmployeeType(const std::string a_employeetype){
            employeetype = a_employeetype;
        }

        void setPay(int a_pay){
            pay = a_pay;
        }

        int getPay(){
            return pay;
        }
};

class HourlyEmployee: public Employee {
    private:
        int hourlyrate = 5;    
        const std::string employeetype = "Hourly";
    public:
        HourlyEmployee(const std::string a_firstname, const std::string a_lastname,
            const std::string a_employeetype, const int hours):
            Employee(a_firstname, a_lastname, a_employeetype){
                // calculating the pay rate and 
                // setting the pay in the base class
                int tpay = hourlyrate * hours;  
                setPay(tpay);
                setEmployeeType(employeetype);
            }

        const int setHourlyRate(int a_hourlyrate){
            hourlyrate = a_hourlyrate;
            return hourlyrate;
        }
};


class SalariedEmployee: public Employee {
    private:
        int monthlyrate = 1000;
        const std::string employeetype = "Salaried";
    public:
        SalariedEmployee(const std::string a_firstname, const std::string a_lastname,
            const std::string a_employeetype, const int hours):
            Employee(a_firstname, a_lastname, a_employeetype){
                // calculating the pay rate and 
                // setting the pay in the base class
                int tpay = monthlyrate * hours;  
                setPay(tpay);
                setEmployeeType(employeetype);
            }

        const int setMonthlyRate(int a_monthlyrate){
            monthlyrate = a_monthlyrate;
            return monthlyrate;
        }
};

class Manager: public Employee {
    private:
        int monthlyrate = 5000;
        const std::string employeetype = "Manager";
    public:
        Manager(const std::string a_firstname, const std::string a_lastname,
            const std::string a_employeetype, const int hours):
            Employee(a_firstname, a_lastname, a_employeetype){
                // calculating the pay rate and 
                // setting the pay in the base class
                int tpay = monthlyrate * hours;  
                setPay(tpay);
                setEmployeeType(employeetype);
            }

        const int setMonthlyRate(int a_monthlyrate){
            monthlyrate = a_monthlyrate;
            return monthlyrate;
        }
    
};

class Executive: public Employee {
    private: 
        int monthlyrate = 10000;
        const std::string employeetype = "Executive";
    public:
        Executive(const std::string a_firstname, const std::string a_lastname,
            const std::string a_employeetype, const int hours):
            Employee(a_firstname, a_lastname, a_employeetype){
                // calculating the pay rate and 
                // setting the pay in the base class
                int tpay = monthlyrate * hours;  
                setPay(tpay);
                setEmployeeType(employeetype);
            }

        const int setMonthlyRate(int a_monthlyrate){
            monthlyrate = a_monthlyrate;
            return monthlyrate;
        }

};


#endif