# 0x08. Python - More Classes and Objects

## Exercises

[0-rectangle.py](./0-rectangle.py)
```
Write an empty class Rectangle that defines a rectangle:
```
* You are not allowed to import any module

[1-rectangle.py](./1-rectangle.py)
```
Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
```
* Private instance attribute: width:
  * property def width(self): to retrieve it
  * property setter def width(self, value): to set it: 
    * width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
    * if width is less than 0, raise a ValueError exception with the message width must be >= 0
* Private instance attribute: height: 
  * property def height(self): to retrieve it
  * property setter def height(self, value): to set it: 
    * height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
    * if height is less than 0, raise a ValueError exception with the message height must be >= 0
* Instantiation with optional width and height: def __init__(self, width=0, height=0):
* You are not allowed to import any module

[2-rectangle.py](./2-rectangle.py)
```
Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)
```
* Private instance attribute: width: 
  * property def width(self): to retrieve it
  * property setter def width(self, value): to set it: 
    * width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
    * if width is less than 0, raise a ValueError exception with the message width must be >= 0
* Private instance attribute: height: 
  * property def height(self): to retrieve it
  * property setter def height(self, value): to set it: 
    * height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
    * if height is less than 0, raise a ValueError exception with the message height must be >= 0
* Instantiation with optional width and height: def __init__(self, width=0, height=0):
* Public instance method: def area(self): that returns the rectangle area
* Public instance method: def perimeter(self): that returns the rectangle perimeter: 
  * if width or height is equal to 0, perimeter is equal to 0
* You are not allowed to import any module

[3-rectangle.py](./3-rectangle.py)
```
Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)
```
* Private instance attribute: width:
  * property def width(self): to retrieve it
  * property setter def width(self, value): to set it: 
    * width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
    * if width is less than 0, raise a ValueError exception with the message width must be >= 0
* Private instance attribute: height:
  * property def height(self): to retrieve it
  * property setter def height(self, value): to set it: 
    * height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
    * if height is less than 0, raise a ValueError exception with the message height must be >= 0
* Instantiation with optional width and height: def __init__(self, width=0, height=0):
* Public instance method: def area(self): that returns the rectangle area
* Public instance method: def perimeter(self): that returns the rectangle perimeter: 
  * if width or height is equal to 0, perimeter has to be equal to 0
* print() and str() should print the rectangle with the character #: (see example below) 
  * if width or height is equal to 0, return an empty string
* You are not allowed to import any module

[4-rectangle.py](./4-rectangle.py)
```
Write a class Rectangle that defines a rectangle by: (based on 3-rectangle.py)
```
* Private instance attribute: width: 
  * property def width(self): to retrieve it
  * property setter def width(self, value): to set it: 
    * width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
    * if width is less than 0, raise a ValueError exception with the message width must be >= 0
* Private instance attribute: height: 
  * property def height(self): to retrieve it
  * property setter def height(self, value): to set it: 
    * height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
    * if height is less than 0, raise a ValueError exception with the message height must be >= 0
* Instantiation with optional width and height: def __init__(self, width=0, height=0):
* Public instance method: def area(self): that returns the rectangle area
* Public instance method: def perimeter(self): that returns the rectangle perimeter: 
  * if width or height is equal to 0, perimeter has to be equal to 0
* print() and str() should print the rectangle with the character #: (see example below) 
  * if width or height is equal to 0, return an empty string
* repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval() (see example below)
* You are not allowed to import any module

[5-rectangle.py](./5-rectangle.py)
```
Write a class Rectangle that defines a rectangle by: (based on 4-rectangle.py)
```
* Private instance attribute: width:
  * property def width(self): to retrieve it
  * property setter def width(self, value): to set it: 
    * width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
    * if width is less than 0, raise a ValueError exception with the message width must be >= 0
* Private instance attribute: height: 
  * property def height(self): to retrieve it
  * property setter def height(self, value): to set it: 
    * height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
    * if height is less than 0, raise a ValueError exception with the message height must be >= 0
* Instantiation with optional width and height: def __init__(self, width=0, height=0):
* Public instance method: def area(self): that returns the rectangle area
* Public instance method: def perimeter(self): that returns the rectangle perimeter: 
  * if width or height is equal to 0, perimeter has to be equal to 0
* print() and str() should print the rectangle with the character
  * if width or height is equal to 0, return an empty string
* repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval() 
* Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
* You are not allowed to import any module

[6-rectangle.py](./6-rectangle.py)
```
Write a class Rectangle that defines a rectangle by: (based on 5-rectangle.py)
```
* Private instance attribute: width:
  * property def width(self): to retrieve it
  * property setter def width(self, value): to set it: 
    * width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
    * if width is less than 0, raise a ValueError exception with the message width must be >= 0
* Private instance attribute: height:
  * property def height(self): to retrieve it
  * property setter def height(self, value): to set it: 
    * height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
    * if height is less than 0, raise a ValueError exception with the message height must be >= 0
* Public class attribute number_of_instances:
  * Initialized to 0
  * Incremented during each new instance instantiation
  * Decremented during each instance deletion
* Instantiation with optional width and height: def __init__(self, width=0, height=0):
* Public instance method: def area(self): that returns the rectangle area
* Public instance method: def perimeter(self): that returns the rectangle perimeter: 
  * if width or height is equal to 0, perimeter has to be equal to 0
* print() and str() should print the rectangle with the character #: 
  * if width or height is equal to 0, return an empty string
* repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval() 
* Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
* You are not allowed to import any module

[7-rectangle.py](./7-rectangle.py)
```
I feel like I am diagonally parked in a parallel universe
Write a function that draws a diagonal line on the terminal.
```
* Private instance attribute: width:
  * property def width(self): to retrieve it
  * property setter def width(self, value): to set it: 
    * width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
    * if width is less than 0, raise a ValueError exception with the message width must be >= 0
* Private instance attribute: height:
  * property def height(self): to retrieve it
  * property setter def height(self, value): to set it: 
    * height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
    * if height is less than 0, raise a ValueError exception with the message height must be >= 0
* Public class attribute number_of_instances:
  * Initialized to 0
  * Incremented during each new instance instantiation
  * Decremented during each instance deletion
* Public class attribute print_symbol: 
  * Initialized to #
  * Used as symbol for string representation
  * Can be any type
* Instantiation with optional width and height: def __init__(self, width=0, height=0):
* Public instance method: def area(self): that returns the rectangle area
* Public instance method: def perimeter(self): that returns the rectangle perimeter: 
  * if width or height is equal to 0, perimeter has to be equal to 0
* print() and str() should print the rectangle with the character #: 
  * if width or height is equal to 0, return an empty string
* repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval() 
* Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
* You are not allowed to import any module

[8-rectangle.py](./8-rectangle.py)
```
You are so much sunshine in every square inch
Write a function that prints a square, followed by a new line.
```
* Private instance attribute: width:
  * property def width(self): to retrieve it
  * property setter def width(self, value): to set it: 
    * width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
    * if width is less than 0, raise a ValueError exception with the message width must be >= 0
* Private instance attribute: height:
  * property def height(self): to retrieve it
  * property setter def height(self, value): to set it: 
    * height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
    * if height is less than 0, raise a ValueError exception with the message height must be >= 0
* Public class attribute number_of_instances:
  * Initialized to 0
  * Incremented during each new instance instantiation
  * Decremented during each instance deletion
* Public class attribute print_symbol: 
  * Initialized to #
  * Used as symbol for string representation
  * Can be any type
* Instantiation with optional width and height: def __init__(self, width=0, height=0):
* Public instance method: def area(self): that returns the rectangle area
* Public instance method: def perimeter(self): that returns the rectangle perimeter: 
  * if width or height is equal to 0, perimeter has to be equal to 0
* print() and str() should print the rectangle with the character #: 
  * if width or height is equal to 0, return an empty string
* repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval() 
* Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
* Static method def bigger_or_equal(rect_1, rect_2): that returns the biggest rectangle based on the area 
  * rect_1 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_1 must be an instance of Rectangle
  * rect_2 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_2 must be an instance of Rectangle
  * Returns rect_1 if both have the same area value
* You are not allowed to import any module

[9-rectangle.py](./9-rectangle.py)
```
The “Fizz-Buzz test” is an interview question designed to help filter out the
99.5% of programming job candidates who can’t seem to program their way out of
a wet paper bag.
Write a program that prints the numbers from 1 to 100, followed by a new line.
```
* Private instance attribute: width:
  * property def width(self): to retrieve it
  * property setter def width(self, value): to set it: 
    * width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
    * if width is less than 0, raise a ValueError exception with the message width must be >= 0
* Private instance attribute: height:
  * property def height(self): to retrieve it
  * property setter def height(self, value): to set it: 
    * height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
    * if height is less than 0, raise a ValueError exception with the message height must be >= 0
* Public class attribute number_of_instances:
  * Initialized to 0
  * Incremented during each new instance instantiation
  * Decremented during each instance deletion
* Public class attribute print_symbol: 
  * Initialized to #
  * Used as symbol for string representation
  * Can be any type
* Instantiation with optional width and height: def __init__(self, width=0, height=0):
* Public instance method: def area(self): that returns the rectangle area
* Public instance method: def perimeter(self): that returns the rectangle perimeter: 
  * if width or height is equal to 0, perimeter has to be equal to 0
* print() and str() should print the rectangle with the character #: 
  * if width or height is equal to 0, return an empty string
* repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval() 
* Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
* Static method def bigger_or_equal(rect_1, rect_2): that returns the biggest rectangle based on the area 
  * rect_1 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_1 must be an instance of Rectangle
  * rect_2 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_2 must be an instance of Rectangle
  * Returns rect_1 if both have the same area value
* Class method def square(cls, size=0): that returns a new Rectangle instance with width == height == size
* You are not allowed to import any module

## Author
### Kevin Yook 
Email: <yook00627@gmail.com> Twitter: [@yook00627](https://twitter.com/yook00627)
