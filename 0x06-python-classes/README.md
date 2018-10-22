# 0x06. Python - Classes and Objects

**What you should learn from this project**

    At the end of this project you are expected to be able to explain to anyone, without the help of Google:

* Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
* What is OOP
* “first-class everything”
* What is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
* What are and how to use public, protected and private attributes
* What is self
* What is a method
* What is the special __init__ method and how to use it
* What is Data Abstraction, Data Encapsulation, and Information Hiding
* What is a property
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What is and what does contain __dict__ of a class and of an instance of a class
* How does Python find the attributes of an object or class
* How to use the getattr function

## Exercises

[0-square.py](./0-square.py)
```
Write an empty class Square that defines a square:
```
* You are not allowed to import any module

[1-square.py](./1-square.py)
```
Write a class Square that defines a square by: (based on 0-square.py)

Why?
Why size is private attribute?
The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.
```
* Private instance attribute: size
* Instantiation with size (no type/value verification)
* Returns 0 otherwise

[2-mul.c](./2-mul.c )
```
Collaboration is multiplication
Write a function that multiplies two integers.
```
* Prototype: int mul(int a, int b);

[3-print_numbers.c](./3-print_numbers.c)
```
The numbers speak for themselves
Write a function that prints the numbers, from 0 to 9, followed by a new line.
```
* Prototype: void print_numbers(void);
* You can only use _putchar twice in your code

[4-print_most_numbers.c](./4-print_most_numbers.c)
```
I believe in numbers and signs
Write a function that prints the numbers, from 0 to 9, followed by a new line.
```
* Prototype: void print_most_numbers(void);
* Do not print 2 and 4
* You can only use _putchar twice in your code

[5-more_numbers.c](./5-more_numbers.c)
```
Numbers constitute the only universal language
Write a function that prints 10 times the numbers, from 0 to 14,
followed by a new line.
```
*  Prototype: void more_numbers(void);
* You can only use _putchar three times in your code

[6-print_line.c](./6-print_line.c)
```
The shortest distance between two points is a straight line
Write a function that draws a straight line in the terminal.
```
* Prototype: void print_line(int n);
* You can only use _putchar function to print
* Where n is the number of times the character _ should be printed
* The line should end with a \n
* If n is 0 or less, the function should only print \n

[7-print_diagonal.c](./7-print_diagonal.c)
```
I feel like I am diagonally parked in a parallel universe
Write a function that draws a diagonal line on the terminal.
```
* Prototype: void print_diagonal(int n);
* You can only use _putchar function to print
* Where n is the number of times the character \ should be printed
* The diagonal should end with a \n
* If n is 0 or less, the function should only print a \n

[8-print_square.c](./8-print_square.c)
```
You are so much sunshine in every square inch
Write a function that prints a square, followed by a new line.
```
* Prototype: void print_square(int size);
* You can only use _putchar function to print
* Where size is the size of the square
* If size is 0 or less, the function should print only a new line
* Use the character # to print the square

[9-fizz_buzz.c](./9-fizz_buzz.c)
```
The “Fizz-Buzz test” is an interview question designed to help filter out the
99.5% of programming job candidates who can’t seem to program their way out of
a wet paper bag.
Write a program that prints the numbers from 1 to 100, followed by a new line.
```
* But for multiples of three print Fizz instead of the number and for the
  multiples of five print Buzz. For numbers which are multiples of both three and
  five print FizzBuzz.

* Each number or word should be separated by a space
* You are allowed to use the standard library

[10-print_triangle.c](./10-print_triangle.c)
```
Write a function that prints a triangle, followed by a new line.
```
* Prototype: void print_triangle(int size);
* You can only use _putchar function to print
* Where size is the size of the triangle
* If size is 0 or less, the function should print only a new line
* Use the character # to print the triangle

[100-prime_factor.c](./100-prime_factor.c)
```
The problem of distinguishing prime numbers from composite numbers and of
resolving the latter into their prime factors is known to be one of the most
important and useful in arithmetic
The prime factors of 1231952 are 2, 2, 2, 2, 37 and 2081.
Write a program that finds and prints the largest prime factor of the number
612852475143, followed by a new line.
```
* You are allowed to use the standard library
* Your program will be compiled with this command: gcc -Wall -pedantic -Werror -
* Wextra 100-prime_factor.c -o 100-prime_factor -lm

[101-print_number.c](./101-print_number.c)
```
Numbers have life; they're not just symbols on paper
Write a function that prints an integer.
```
* Prototype: void print_number(int n);
* You can only use _putchar function to print
* You are not allowed to use long
* You are not allowed to use arrays or pointers
* You are not allowed to hard-code special values

## Author
### Kevin Yook 
Email: <yook00627@gmail.com> Twitter: [@yook00627](https://twitter.com/yook00627)
