'''
Company Manager - Create an hierarchy of classes 
- abstract class Employee and subclasses HourlyEmployee,
SalariedEmployee, Manager and Executive. 
Every one's pay is calculated differently, research a bit about it. 
After you've established an employee hierarchy, 
create a Company class that allows you to manage the employees. 
You should be able to hire, fire and raise employees.
'''
class Employee:
    '''
    Contains Employee Details
    '''
    num_of_emps = 1
    emp_list = {}

    def __init__(self,first,last,emp_type,pay):
        self.first = first
        self.last = last
        self.emp_type = emp_type
        self.email = "{}_{}@abc.io".format(self.first,self.last)
        self.pay = pay
        self.emp_list[self.num_of_emps] = [emp_type,self.first,self.last,self.email,self.pay]
        self.num_of_emps += 1
    
    @property
    def fullname(self):
        return "{} {}".format(self.first,self.last)

    def __repr__(self):
        return "{}\n\tfirst: {} \n\tlast: {} \n\temail: {} \n\tpay: {}".format(self.emp_type,self.first,self.last,self.email,self.pay)


class HourlyEmployee(Employee):
    '''
    Hourly Employee
    '''
    hourly_rate = 5

    def __init__(self,first,last,hour):
        emp_type = 'hourly'
        self.hour = hour
        pay = int(self.hour * self.hourly_rate)
        super().__init__(first,last,emp_type,pay)
    


class SalariedEmployee(Employee):

    monthly_rate = 1000
    def __init__(self,first,last,month):
        emp_type = 'Salaried Employee'
        pay = month * self.monthly_rate
        super().__init__(first,last,emp_type,pay)
    

class Manager(Employee):

    def __init__(self,first,last,month):
        emp_type = 'Manager'
        pay = month * 10000
        super().__init__(first,last,emp_type,pay)
    

class Exective(Employee):
    def __init__(self,first,last,month):
        emp_type = 'Executive'
        pay = month * 90000
        super().__init__(first,last,emp_type,pay)


 
class Company:

    def __init__(self,first,last,state,emp_type,month):
        self.state = state
        self.fn = first
        self.ln = last
        self.emp_type = emp_type
        self.month = month

        if self.state == 'hire':
            self.hire()
        elif self.state == 'fire':
            pass

    def hire(self):
        
        if self.emp_type == 'H': HourlyEmployee(self.fn,self.ln,self.month)
        if self.emp_type == 'S': SalariedEmployee(self.fn,self.ln,self.month)
        if self.emp_type == 'M': Manager(self.fn,self.ln,self.month)
        if self.emp_type == 'E': Exective(self.fn,self.ln,self.month)


if __name__ == '__main__':
    
    state = str(input("Hire or Fire: "))
    
    emp_type = str(input("Employee Types \n \t\t 'H'-->'Hourly Employee' \n\t\t 'S'-->'Salaried Employee' \n\t\t 'M'-->'Manager' \n\t\t 'E'-->'Exective'\nEnter Employee Type: \t"))
    
    if emp_type == 'H':
        month = int(input("Contract 'Hours' >>: "))
    else:
        month = int(input("Contract Period >>: "))

    fn = str(input('Enter First Name: '))
    ln = str(input('Enter Last  Name: '))

    Company(fn,ln,state,emp_type,month)

    print(Employee.emp_list)
