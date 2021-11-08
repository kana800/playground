2. Catch that Bug

   In this section, the following snippets will have bugs. Identify them and indicate how to correct them. Do these without the use of a computer.

> 1. ```cpp
>    class Point{
>        private: 
>        	int x, y;
>        public:
>        	Point(int u, int v): x(u), y(v) {}
>        	int getX() {return x; }
>        	int getY() {return y; }
>        	void doubleVal(){
>                x *= 2;
>                y *= 2;
>            }
>    };
>    
>    int main(){
>        const Point myPoint(5, 3)
>        myPoint.doubleVal();
>        cout << myPoint.getX() << " " << myPoint.getY() << "\n";
>        return 0;
>    }
>    ```

- `const Point myPoint(5, 3)` should be `const Point myPoint(5, 3);` there should be a semi-colon present in the end of statement.
- `myPoint.doubleVal();` cannot be applied to `myPoint` because `myPoint` is `const`

> 2. ```cpp
>    class Point{
>      private:
>        int x, y;
>      public:
>        Point(int u, int v): x(u), y(v) {}
>        int getX() {return x;}
>        int getY() {return y;}
>        
>        void setX(int newX) const {x = newX; }
>    };
>    
>    int main(){
>       	Point p(5,3);
>        p.setX(9001);
>        	cout << p.getX() << ' ' << p.getY();
>        return 0;
>    }
>    ```

- `void setX(int newX) const {x = newX;}` is changing a variable because it declared as a `const` wee cannot modify any instance variables.

> 3. ```cpp
>    class Point{
>      private:
>        int x, y;
>      public:
>        Point(int u, int v): x(u), y(v) {}
>        int getX() {return x;}
>        int getY() {return y;}
>    };
>    
>    int main(){
>       	Point p(5,3);
>        cout << p.x( << " " << p.y << "\n";
>        return 0;
>    }
>    ```

- `p.x` and `p.y` cant access `x` and `y` variables in class `Point` because they are private

> 4. ```cpp
>    class Point{
>      private:
>        int x, y;
>      public:
>        Point(int u, int v): x(u), y(v) {}
>        int getX() {return x;}
>        int getY() {return y;}
>    };
>    
>    void setX(int newX) const {x = newX; }
>    
>    int main(){
>       	Point p(5,3);
>        p.setX(0);
>        cout << p.getX() << ' ' << p.getY();
>        return 0;
>    }
>    ```

- In the function `setX` the class variable `x` is not accessible. The function is not inside the class or declared in the class

> 5. ```cpp
>    int size;
>    cin >> size;
>    int *nums = new int[size];
>    for (int i = 0; i < size; ++i){
>        cin >> nums[i];
>    }
>    delete nums;
>    ```

- `delete nums` should be `delete[] nums`

> 6. ```cpp
>    class Point{
>      private:
>        int x, y;
>      public:
>        Point(int u, int v): x(u), y(v) {}
>        int getX() {return x;}
>        int getY() {return y;}
>    };
>    
>    int main(){
>       	Point *p = new Point(5,3);
>        cout << p->getX() << " " << p->getY();
>        return 0;
>    }
>    ```

- The point `p` needs to be deallocated

3. `Point`

   [geometry.h](codeps3/geometry.h)

   [geometry.cpp](codeps3/geometry.cpp)

4. `PointArray`

   [geometry.h](codeps3/geometry.h)

   [geometry.cpp](codeps3/geometry.cpp)

   > 5. Why do we need `const` and non-`const` version of `get`?

   The non-`const` version of the `get` can be used for a `PointArray` object and `const` version of the `get` can be used for `const PointArray` object. `const` version of the get returns only a read only version of the pointer. 

5. `Polygon`

   [polygon.h](codeps3/polygon.h)

   [polygon.cpp](codeps3/polygon.cpp)
   
6. `Triangle`

   [polygon.h](codeps3/polygon.h)

   [polygon.cpp](codeps3/polygon.cpp)

   > In the `Point` class, what would happen if the constructors were private?

   If the constructors were private we wont be able to instantiate a class with a `Point(x,y)`.s

   > Describe what happens to the fields of the `Polygon` object when the object is destroyed.

   The count of the polygons will decrement by one.

   > Why did we need to make the fields of `Polygon` protected?

   Let `Rectangle` and `Traingle` classes access the fields and not the other code.

   > Assume you are writing a function that takes as an argument a `Polygon *` called `polyPtr`
   >
   > Imagine that we had overridden `getNumSides` in each of `Rectangle` and `Triangle`. Which version of the function would be called if we wrote `polyPtr->getNumSides()`? Why?

   `getNumSides` isn't a virtual, `Polygon`'s `getNumSides()` will be called.

7. check `polygon.cpp` for answers

> Write a program the converts english into piglatin

[piglatin.cpp](codeps3/piglatin.cpp)





   