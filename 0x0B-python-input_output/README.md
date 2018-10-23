# 0x0B. Python - Input/Output

**What you should learn from this project**

    At the end of this project you are expected to be able to explain to anyone, without the help of Google:

* Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
* How to open a file
* How to write text in a file
* How to read the full content of a file 
* How to read a file line by line
* How to move the cursor in a file
* How to make sure a file is closed after using it
* What is and how to use the with statement
* What is JSON
* What is serialization
* What is deserialization
* How to convert a Python data structure to a JSON string 
* How to convert a JSON string to a Python data structure

## Exercises

[0-read_file.py](./0-read_file.py)
```
Write a function that reads a text file (UTF8) and prints it to stdout:
```
* Prototype: def read_file(filename=""):
* You must use the with statement
* You don’t need to manage file permission/file doesn’t exist exceptions.
* You are not allowed to import any module

[1-number_of_lines.py](./1-number_of_lines.py)
```
Write a function that returns the number of lines of a text file:
```
* Prototype: def number_of_lines(filename=""):
* You must use the with statement
* You don’t need to manage file permission/file doesn’t exist exceptions.
* You are not allowed to import any module

[2-read_lines.py](./2-read_lines.py)
```
Write a function that reads n lines of a text file (UTF8) and prints it to stdout:
```
* Prototype: def read_lines(filename="", nb_lines=0):
* Read the entire file if nb_lines is lower or equal to 0 OR greater or equal to the total number of lines of the file
* You must use the with statement
* You don’t need to manage file permission/file doesn’t exist exceptions.
* You are not allowed to import any module

[3-write_file.py](./3-write_file.py)
```
Write a function that writes a string to a text file (UTF8) and returns the number of characters written:
```
* Prototype: def write_file(filename="", text=""):
* You must use the with statement
* You don’t need to manage file permission exceptions.
* Your function should create the file if doesn’t exist.
* Your function should overwrite the content of the file if it already exists.
* You are not allowed to import any module

[4-append_write.py](./4-append_write.py)
```
Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:
```
* Prototype: def append_write(filename="", text=""):
* If the file doesn’t exist, it should be created
* You must use the with statement
* You don’t need to manage file permission/file doesn’t exist exceptions.
* You are not allowed to import any module

[5-to_json_string.py](./5-to_json_string.py)
```
Write a function that returns the JSON representation of an object (string):
```
* Prototype: def to_json_string(my_obj):
* You don’t need to manage exceptions if the object can’t be serialized.

[6-from_json_string.py](./6-from_json_string.py)
```
Write a function that returns an object (Python data structure) represented by a JSON string:
```
* Prototype: def from_json_string(my_str):
* You don’t need to manage exceptions if the JSON string doesn’t represent an object.

[7-save_to_json_file.py](./7-save_to_json_file.py)
```
Write a function that writes an Object to a text file, using a JSON representation:
```
* Prototype: def save_to_json_file(my_obj, filename):
* You must use the with statement
* You don’t need to manage exceptions if the object can’t be serialized.
* You don’t need to manage file permission exceptions.

[8-load_from_json_file.py](./8-load_from_json_file.py)
```
Write a function that creates an Object from a “JSON file”:
```
* Prototype: def load_from_json_file(filename):
* You must use the with statement
* You don’t need to manage exceptions if the JSON string doesn’t represent an object.
* You don’t need to manage file permissions / exceptions.

[9-add_item.py](./9-add_item.py)
```
Write a script that adds all arguments to a Python list, and then save them to a file:
```
* You must use your function save_to_json_file from 7-save_to_json_file.py
* You must use your function load_from_json_file from 8-load_from_json_file.py
* The list must be saved as a JSON representation in a file named add_item.json
* If the file doesn’t exist, it should be created
* You don’t need to manage file permissions / exceptions.

[10-class_to_json.py](./10-class_to_json.py)
```
Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:
```
* Prototype: def class_to_json(obj):
* obj is an instance of a Class
* All attributes of the obj Class are serializable: list, dictionary, string, integer and boolean
* You are not allowed to import any module

[11-student.py](./11-student.py)
```
Write a class Student that defines a student by:
```
* Public instance attributes: 
  * first_name
  * last_name
  * age
* Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
* Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 10-class_to_json.py)
* You are not allowed to import any module

[12-student.py](./12-student.py)
```
Write a class Student that defines a student by: (based on 11-student.py)
```
* Public instance attributes: 
  * first_name
  * last_name
  * age
* Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
* Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 10-class_to_json.py)
  * If attrs is a list of strings, only attributes name contain in this list must be retrieved.
  * Otherwise, all attributes must be retrieved
* You are not allowed to import any module

[13-student.py](./13-student.py)
```
Write a class Student that defines a student by: (based on 11-student.py)
```
* Public instance attributes: 
  * first_name
  * last_name
  * age
* Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
* Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 10-class_to_json.py)
  * If attrs is a list of strings, only attributes name contain in this list must be retrieved.
  * Otherwise, all attributes must be retrieved
* Public method def reload_from_json(self, json): that replaces all attributes of the Student instance:
  * You can assume json will always be a dictionary
  * A dictionary key will be the public attribute name
  * A dictionary value will be the value of the public attribute
* You are not allowed to import any module

[14-pascal_triangle.py](./14-pascal_triangle.py)
```
Technical interview preparation:
Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:
```
* You are not allowed to google anything
* Whiteboard first
* Returns an empty list if n <= 0
* You can assume n will be always an integer


[100-append_after.py](./100-append_after.py)
```
Write a function that inserts a line of text to a file, after each line containing a specific string (see example):
```
* Prototype: def append_after(filename="", search_string="", new_string=""):
* You must use the with statement
* You don’t need to manage file permission/file doesn’t exist exceptions.
* You are not allowed to import any module

## Author
### Kevin Yook 
Email: <yook00627@gmail.com> Twitter: [@yook00627](https://twitter.com/yook00627)
