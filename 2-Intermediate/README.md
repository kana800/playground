# Project List

## Progress Bar

- Numbers ![0%](https://progress-bar.dev/0)
- Classic Algorithms![0%](https://progress-bar.dev/0)
- Classes ![0%](https://progress-bar.dev/0)
- Text ![16%](https://progress-bar.dev/16)



Numbers
---------

- [ ] **Mortgage Calculator** - Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. Also figure out how long it will take the user to pay back the loan. For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).
- [ ] **Alarm Clock** - A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.
- [ ] **Distance Between Two Cities** - Calculates the distance between two cities and allows the user to specify a unit of distance. This program may require finding coordinates for the cities like latitude and longitude.
- [x] **Happy Numbers** - A happy number is defined by the following process. Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers. Display an example of your output here. Find first 8 happy numbers.
- [x] **Number Names** - Show how to spell out a number in English. You can use a preexisting implementation or roll your own, but you should support inputs up to at least one million (or the maximum value of your language's default bounded integer type, if that's less). *Optional: Support for inputs other than positive integers (like zero, negative integers, and floating-point numbers).*

Classes
---------

- [x] [**Product Inventory Project**](https://github.com/kana800/expense_tracker) - Create an application which manages an inventory of products. Create a product class which has a price, id, and quantity on hand. Then create an *inventory* class which keeps track of various products and can sum up the inventory value.
- [x] [**Airline / Hotel Reservation System**](https://github.com/kana800/Side-Projects/blob/master/2-Intermediate/airline_hotel_reservation_system/reserve.py) - Create a reservation system which books airline seats or hotel rooms. It charges various rates for particular sections of the plane or hotel. Example, first class is going to cost more than coach. Hotel rooms have penthouse suites which cost more. Keep track of when rooms will be available and can be scheduled.
- [x] [**Company Manager**](https://github.com/kana800/Side-Projects/tree/master/2-Intermediate/company_manager) - Create an hierarchy of classes - abstract class Employee and subclasses HourlyEmployee, SalariedEmployee, Manager and Executive. Every one's pay is calculated differently, research a bit about it.
After you've established an employee hierarchy, create a Company class that allows you to manage the employees. You should be able to hire, fire and raise employees. 
- [x] [**Bank Account Manager**](https://github.com/kana800/Side-Projects/tree/master/2-Intermediate/bank_manager) - Create a class called Account which will be an abstract class for three other classes called CheckingAccount, SavingsAccount and BusinessAccount. Manage credits and debits from these accounts through an ATM style program.
- [x] [**Patient / Doctor Scheduler**](https://github.com/kana800/Side-Projects/tree/master/2-Intermediate/patient_doctor_scheduler) - Create a patient class and a doctor class. Have a doctor that can handle multiple patients and setup a scheduling program where a doctor can only handle 16 patients during an 8 hr work day.
- [x] [**Recipe Creator and Manager**](https://github.com/kana800/Side-Projects/tree/master/2-Intermediate/recipe_creator_manager) - Create a recipe class with ingredients and a put them in a recipe manager program that organizes them into categories like deserts, main courses or by ingredients like chicken, beef, soups, pies etc.
- [x] [**Image Gallery**](https://github.com/kana800/Side-Projects/tree/master/2-Intermediate/image_gallery) - Create an image abstract class and then a class that inherits from it for each image type. Put them in a program which displays them in a gallery style format for viewing.
- [x] [**Shape Area and Perimeter Classes**](https://github.com/kana800/Side-Projects/tree/master/2-Intermediate/shapes) - Create an abstract class called Shape and then inherit from it other shapes like diamond, rectangle, circle, triangle etc. Then have each class override the area and perimeter functionality to handle each shape type.
- [x] [**Flower Shop Ordering To Go**](https://github.com/kana800/Side-Projects/tree/master/2-Intermediate/flowershops)- Create a flower shop application which deals in flower objects and use those flower objects in a bouquet object which can then be sold. Keep track of the number of objects and when you may need to order more.
- [ ] **Family Tree Creator** - Create a class called Person which will have a name, when they were born and when (and if) they died. Allow the user to create these Person classes and put them into a family tree structure. Print out the tree to the screen.

Classic Algorithms
-----------------

- [ ] **Closest pair problem** - The closest pair of points problem or closest pair problem is a problem of computational geometry: given *n* points in metric space, find a pair of points with the smallest distance between them.
- [ ] **Collatz Conjecture** - Start with a number *n > 1*. Find the number of steps it takes to reach one using the following process: If *n* is even, divide it by 2. If *n* is odd, multiply it by 3 and add 1.


Text
---------

- [x] **Text Editor** - Notepad style application that can open, edit, and save text documents. *Optional: Add syntax highlighting and other features.*
- [ ] **RSS Feed Creator** - Given a link to RSS/Atom Feed, get all posts and display them.
- [ ] **Quote Tracker (market symbols etc)** - A program which can go out and check the current value of stocks for a list of symbols entered by the user. The user can set how often the stocks are checked. For CLI, show whether the stock has moved up or down. *Optional: If GUI, the program can show green up and red down arrows to show which direction the stock value has moved.*
- [ ] **Guestbook / Journal** - A simple application that allows people to add comments or write journal entries. It can allow comments or not and timestamps for all entries. Could also be made into a shout box. *Optional: Deploy it on Google App Engine or Heroku or any other PaaS (if possible, of course).*
- [ ] **Vigenere / Vernam / Ceasar Ciphers** - Functions for encrypting and decrypting data messages. Then send them to a friend.
- [ ] **Regex Query Tool** - A tool that allows the user to enter a text string and then in a separate control enter a regex pattern. It will run the regular expression against the source text and return any matches or flag errors in the regular expression.
