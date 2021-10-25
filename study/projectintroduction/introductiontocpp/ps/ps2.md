2. A Simple Function
>    What would the following program print out?
>
>    ```cpp
>    void f(const int a = 5){
>        std::cout << a * 2 << "\n";
>    }
>    
>    int a = 123;
>    int main(){
>        f(1); // 2
>        f(a); // 246
>        int b = 3;
>        f(b); // 10
>        int a = 4;
>        f(a); // 8
>        f(); // 10
>    }
  ```

3. Fix the Function

   > Identify the errors in the following programs, and explain how you would correct them to make them do what they were apparently meant to do.
   >
   > 1. ```cpp
   >    #include <iostream>
   >    
   >    int main(){
   >        printNum(35);
   >        return 0;
   >    }
   >    void printNum(int number) { std::cout << number; }
   >    ```

   we can use the function declaration (prototyping) 

   ```cpp
   #include <iostream>
   
   void printNum(int number);
   
   int main(){
       printNum(35);
       return 0;
   }
   void printNum(int number) { std::cout << number; }
   ```

   we can move the `printNum` function above the `main` function.

   > 2. ```cpp
   >    #include <iostream>
   >    void printNum() { std::cout << number; }
   >    
   >    int main(){
   >    	int number = 35;
   >        printNum(number);
   >        return 0;
   >    }
   >    ```

   we need to make sure that the function accepts arguments.

   ```cpp
   void printNum(int number) { std::cout << number; }
   ```

   make  `number` variable a global variable. Move it outside the `main` function

   > 3. ```cpp
   >    #include <iostream>
   >    
   >    void doubleNumber(int num){num = num * 2;}
   >    
   >    int main(){
   >    	int num = 35;
   >        doubleNumber(num);
   >        std::cout << num; // should print 70
   >        return 0;
   >    }
   >    ```

   we can pass the address of the variable `num`

   ```cpp
   #include <iostream>
   
   void doubleNumber(int * num){num = num * 2;}
   
   int main(){
   	int num = 35;
       doubleNumber(&num);
       std::cout << num; // should print 70
       return 0;
   }
   ```

   > 4. ```cpp
   >    #include <iostream>
   >    #include <cstdlib> // contains some math functions
   >    
   >    int difference(const int x, const int y){
   >        int diff = abs(x - y); // abs(n) returns absolute value of n
   >    }
   >    
   >    int main(){
   >        std::cout << difference(24, 1238);
   >        return 0;
   >    }
   >    ```

   ```cpp
   #include <iostream>
   #include <cstdlib> // contains some math functions
   
   int difference(const int x, const int y){
       int diff = abs(x - y); // abs(n) returns absolute value of n
   	return diffl;
   }
   
   int main(){
       std::cout << difference(24, 1238);
       return 0;
   }
   ```

   > 5. ```c++
   >    #include <iostream>
   >    
   >    int sum(const int x, const int y){
   >        return x + y;
   >    }
   >    
   >    int main() {
   >        std::cout << sum(1,2,3); //should print 6
   >        return 0;
   >    }
   >    ```

   