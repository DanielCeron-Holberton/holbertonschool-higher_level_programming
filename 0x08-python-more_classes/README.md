# 0x08. Python - More Classes and Objects
## Details
      By Guillaume          Weight: 1                Ongoing project - started 01-24-2022, must end by 01-25-2022 (in about 9 hours)          - you're done with 0% of tasks.              Checker will be released at 01-24-2022 06:00 PM      Manual QA review must be done          (request it when you are done with the project)              QA review fully automated.      ## Resources
Read or watch :
* [Object Oriented Programming](https://intranet.hbtn.io/rltoken/VlISluyXK-teEwwPCu2tlg) 
 (Read everything until the paragraph “Inheritance” (excluded))
* [Object-Oriented Programming](https://intranet.hbtn.io/rltoken/zerKovWZrKMKWx0OVZBchw) 
 (Please be careful: in most of the following paragraphs, the author shows the way you should not use or write a class, in order to help you better understand some concepts and how everything works in Python 3. Make sure you read only the following paragraphs: “General Introduction,” “First-class Everything,” “A Minimal Class in Python,” “Attributes,” “Methods,” “The  ` __init__ `  Method,”  “Data Abstraction, Data Encapsulation, and Information Hiding,” “ ` __str__ ` - and  ` __repr__ ` -Methods,” “Public- Protected- and Private Attributes,” & “Destructor”)
* [Class and Instance Attributes](https://intranet.hbtn.io/rltoken/tBuuWfzA2PIFAmX8X65YZg) 

* [classmethods and staticmethods](https://intranet.hbtn.io/rltoken/ce7aZMwzugNBFgfYxNxwCw) 

* [Properties vs. Getters and Setters](https://intranet.hbtn.io/rltoken/sOlKSeY2hI6Ppf_hExxJvw) 
 (Mainly the last part “Public instead of Private Attributes”)
* [str vs repr](https://intranet.hbtn.io/rltoken/BnqS9rZ4oYsX_QMzgHNa8A) 

## Learning Objectives
At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/XAZQeGUjBYlhagBCUHKasQ) 
 ,  without the help of Google :
### General
* Why Python programming is awesome 
* What is OOP
* “first-class everything”
* What is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
* What are and how to use public, protected and private attributes
* What is  ` self ` 
* What is a method
* What is the special  ` __init__ `  method and how to use it
* What is Data Abstraction, Data Encapsulation, and Information Hiding
* What is a property
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python
* What are the special  ` __str__ `  and  ` __repr__ `  methods and how to use them
* What is the difference between  ` __str__ `  and  ` __repr__ ` 
* What is a class attribute
* What is the difference between a object attribute and a class attribute
* What is a class method
* What is a static method
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What is and what does contain  ` __dict__ `  of a class and of an instance of a class
* How does Python find the attributes of an object or class
* How to use the  ` getattr `  function
## Requirements
### General
* Allowed editors:  ` vi ` ,  ` vim ` ,  ` emacs ` 
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly  ` #!/usr/bin/python3 ` 
* A  ` README.md `  file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using  ` wc ` 
## Quiz questions
Show
#### 
        
        Question #0
    
 Quiz question Body What is   ` __init__ `  ? 
 Quiz question Answers * A class attribute

* A class method

* The instance method called when a new object is created 

* The instance method called when a class is called for the first time

 Quiz question Tips #### 
        
        Question #1
    
 Quiz question Body What is   ` __str__ `  ?
 Quiz question Answers * Instance method that returns an “informal” and nicely printable string representation of an instance

* Instance method that returns the dictionary representation of an instance

* Instance method that prints an “informal” and nicely printable string representation of an instance

 Quiz question Tips #### 
        
        Question #2
    
 Quiz question Body What is   ` __repr__ `  ?
 Quiz question Answers * Instance method that prints an “official” string representation of an instance

* Instance method that returns an “official” string representation of an instance

* Instance method that returns the dictionary representation of an instance

 Quiz question Tips #### 
        
        Question #3
    
 Quiz question Body What is   ` __del__ `  ?
 Quiz question Answers * Instance method that removes the last character of an instance

* Instance method that prints the memory address of an instance

* Instance method called when an instance is deleted

 Quiz question Tips #### 
        
        Question #4
    
 Quiz question Body What is   ` __doc__ `  ?
 Quiz question Answers * The string documentation of an object (based on docstring)

* Prints the documentation of an object

* Creates man file

 Quiz question Tips #### 
        
        Question #5
    
 Quiz question Body What do these lines print?
 ` class User:
    id = 1

print(User.id)
 `  Quiz question Answers * None

* 1

* 89

* 98

 Quiz question Tips #### 
        
        Question #6
    
 Quiz question Body What do these lines print?
 ` class User:
    id = 1

u = User()
print(u.id)
 `  Quiz question Answers * None

* 1

* 89

* 98

 Quiz question Tips #### 
        
        Question #7
    
 Quiz question Body What do these lines print?
 ` class User:
    id = 1

u = User()
u.id = 89
print(u.id)
 `  Quiz question Answers * None

* 1

* 89

* 98

 Quiz question Tips #### 
        
        Question #8
    
 Quiz question Body What do these lines print?
 ` class User:
    id = 1

User.id = 98
u = User()
print(u.id)
 `  Quiz question Answers * None

* 1

* 89

* 98

 Quiz question Tips #### 
        
        Question #9
    
 Quiz question Body What do these lines print?
 ` class User:
    id = 1

u = User()
User.id = 98
print(u.id)
 `  Quiz question Answers * None

* 1

* 89

* 98

 Quiz question Tips #### 
        
        Question #10
    
 Quiz question Body What do these lines print?
 ` class User:
    id = 1

User.id = 98
u = User()
u.id = 89
print(u.id)
 `  Quiz question Answers * None

* 1

* 89

* 98

 Quiz question Tips #### 
        
        Question #11
    
 Quiz question Body What do these lines print?
 ` class User:
    id = 1

User.id = 98
u = User()
u.id = 89
print(User.id)
 `  Quiz question Answers * None

* 1

* 89

* 98

 Quiz question Tips #### 
        
        Question #12
    
 Quiz question Body What do these lines print?
 ` class User:
    id = 1

u = User()
u.id = 89
User.id = 98
print(User.id)
 `  Quiz question Answers * None

* 1

* 89

* 98

 Quiz question Tips #### 
        
        Question #13
    
 Quiz question Body What do these lines print?
 ` class User:
    id = 1

u = User()
u.id = 89
User.id = 98
print(u.id)
 `  Quiz question Answers * None

* 1

* 89

* 98

 Quiz question Tips ## Tasks
### 0. Simple rectangle
          mandatory         Progress vs Score  Task Body Write an empty class   ` Rectangle `   that defines a rectangle:
* You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x08$ cat 0-main.py
#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)

guillaume@ubuntu:~/0x08$ ./0-main.py
<class '0-rectangle.Rectangle'>
{}
guillaume@ubuntu:~/0x08$ 

```
No test cases needed
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x08-python-more_classes ` 
* File:  ` 0-rectangle.py ` 
 Self-paced manual review  Panel footer - Controls 
### 1. Real definition of a rectangle
          mandatory         Progress vs Score  Task Body Write a class   ` Rectangle `   that defines a rectangle by: (based on   ` 0-rectangle.py `  )
* Private instance attribute:  ` width ` :* property  ` def width(self): `  to retrieve it
* property setter  ` def width(self, value): `  to set it:*  ` width `  must be an integer, otherwise raise a  ` TypeError `  exception with the message  ` width must be an integer ` 
* if  ` width `  is less than  ` 0 ` , raise a  ` ValueError `  exception with the message  ` width must be >= 0 ` 


* Private instance attribute:  ` height ` :* property  ` def height(self): `  to retrieve it
* property setter  ` def height(self, value): `  to set it:*  ` height `  must be an integer, otherwise raise a  ` TypeError `  exception with the message  ` height must be an integer ` 
* if  ` height `  is less than  ` 0 ` , raise a  ` ValueError `  exception with the message  ` height must be >= 0 ` 


* Instantiation with optional  ` width `  and  ` height ` :  ` def __init__(self, width=0, height=0): ` 
* You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x08$ cat 1-main.py
#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)

guillaume@ubuntu:~/0x08$ ./1-main.py
{'_Rectangle__height': 4, '_Rectangle__width': 2}
{'_Rectangle__height': 3, '_Rectangle__width': 10}
guillaume@ubuntu:~/0x08$ 

```
No test cases needed
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x08-python-more_classes ` 
* File:  ` 1-rectangle.py ` 
 Self-paced manual review  Panel footer - Controls 
### 2. Area and Perimeter
          mandatory         Progress vs Score  Task Body Write a class   ` Rectangle `   that defines a rectangle by: (based on   ` 1-rectangle.py `  )
* Private instance attribute:  ` width ` :* property  ` def width(self): `  to retrieve it
* property setter  ` def width(self, value): `  to set it:*  ` width `  must be an integer, otherwise raise a  ` TypeError `  exception with the message  ` width must be an integer ` 
* if  ` width `  is less than  ` 0 ` , raise a  ` ValueError `  exception with the message  ` width must be >= 0 ` 


* Private instance attribute:  ` height ` :* property  ` def height(self): `  to retrieve it
* property setter  ` def height(self, value): `  to set it:*  ` height `  must be an integer, otherwise raise a  ` TypeError `  exception with the message  ` height must be an integer ` 
* if  ` height `  is less than  ` 0 ` , raise a  ` ValueError `  exception with the message  ` height must be >= 0 ` 


* Instantiation with optional  ` width `  and  ` height ` :  ` def __init__(self, width=0, height=0): ` 
* Public instance method:  ` def area(self): `  that returns the rectangle area
* Public instance method:  ` def perimeter(self): `  that returns the rectangle perimeter:* if  ` width `  or  ` height `  is equal to  ` 0 ` , perimeter is equal to  ` 0 ` 

* You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x08$ cat 2-main.py
#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

guillaume@ubuntu:~/0x08$ ./2-main.py
Area: 8 - Perimeter: 12
--
Area: 30 - Perimeter: 26
guillaume@ubuntu:~/0x08$ 

```
No test cases needed
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x08-python-more_classes ` 
* File:  ` 2-rectangle.py ` 
 Self-paced manual review  Panel footer - Controls 
### 3. String representation
          mandatory         Progress vs Score  Task Body Write a class   ` Rectangle `   that defines a rectangle by: (based on   ` 2-rectangle.py `  )
* Private instance attribute:  ` width ` :* property  ` def width(self): `  to retrieve it
* property setter  ` def width(self, value): `  to set it:*  ` width `  must be an integer, otherwise raise a  ` TypeError `  exception with the message  ` width must be an integer ` 
* if  ` width `  is less than  ` 0 ` , raise a  ` ValueError `  exception with the message  ` width must be >= 0 ` 


* Private instance attribute:  ` height ` :* property  ` def height(self): `  to retrieve it
* property setter  ` def height(self, value): `  to set it:*  ` height `  must be an integer, otherwise raise a  ` TypeError `  exception with the message  ` height must be an integer ` 
* if  ` height `  is less than  ` 0 ` , raise a  ` ValueError `  exception with the message  ` height must be >= 0 ` 


* Instantiation with optional  ` width `  and  ` height ` :  ` def __init__(self, width=0, height=0): ` 
* Public instance method:  ` def area(self): `  that returns the rectangle area
* Public instance method:  ` def perimeter(self): `  that returns the rectangle perimeter:* if  ` width `  or  ` height `  is equal to  ` 0 ` , perimeter has to be equal to  ` 0 ` 

*  ` print() `  and  ` str() `  should print the rectangle with the character  ` # ` : (see example below)* if  ` width `  or  ` height `  is equal to 0, return an empty string

* You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x08$ cat 3-main.py
#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))

guillaume@ubuntu:~/0x08$ ./3-main.py
Area: 8 - Perimeter: 12
##
##
##
##
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
--
##########
##########
##########
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
guillaume@ubuntu:~/0x08$ 

```
Object address can be different
No test cases needed
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x08-python-more_classes ` 
* File:  ` 3-rectangle.py ` 
 Self-paced manual review  Panel footer - Controls 
### 4. Eval is magic
          mandatory         Progress vs Score  Task Body Write a class   ` Rectangle `   that defines a rectangle by: (based on   ` 3-rectangle.py `  )
* Private instance attribute:  ` width ` :* property  ` def width(self): `  to retrieve it
* property setter  ` def width(self, value): `  to set it:*  ` width `  must be an integer, otherwise raise a  ` TypeError `  exception with the message  ` width must be an integer ` 
* if  ` width `  is less than  ` 0 ` , raise a  ` ValueError `  exception with the message  ` width must be >= 0 ` 


* Private instance attribute:  ` height ` :* property  ` def height(self): `  to retrieve it
* property setter  ` def height(self, value): `  to set it:*  ` height `  must be an integer, otherwise raise a  ` TypeError `  exception with the message  ` height must be an integer ` 
* if  ` height `  is less than  ` 0 ` , raise a  ` ValueError `  exception with the message  ` height must be >= 0 ` 


* Instantiation with optional  ` width `  and  ` height ` :  ` def __init__(self, width=0, height=0): ` 
* Public instance method:  ` def area(self): `  that returns the rectangle area
* Public instance method:  ` def perimeter(self): `  that returns the rectangle perimeter:* if  ` width `  or  ` height `  is equal to  ` 0 ` , perimeter has to be equal to  ` 0 ` 

*  ` print() `  and  ` str() `  should print the rectangle with the character  ` # ` : (see example below)* if  ` width `  or  ` height `  is equal to 0, return an empty string

*  ` repr() `  should return a string representation of the rectangle to be able to recreate a new instance by using  ` eval() `  (see example below)
* You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x08$ cat 4-main.py
#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("--")
print(new_rectangle)
print("--")
print(repr(new_rectangle))
print("--")
print(hex(id(new_rectangle)))
print("--")

print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))

guillaume@ubuntu:~/0x08$ ./4-main.py
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7cc88
--
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7ccc0
--
False
True
guillaume@ubuntu:~/0x08$ 

```
No test cases needed
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x08-python-more_classes ` 
* File:  ` 4-rectangle.py ` 
 Self-paced manual review  Panel footer - Controls 
### 5. Detect instance deletion
          mandatory         Progress vs Score  Task Body Write a class   ` Rectangle `   that defines a rectangle by: (based on   ` 4-rectangle.py `  )
* Private instance attribute:  ` width ` :* property  ` def width(self): `  to retrieve it
* property setter  ` def width(self, value): `  to set it:*  ` width `  must be an integer, otherwise raise a  ` TypeError `  exception with the message  ` width must be an integer ` 
* if  ` width `  is less than  ` 0 ` , raise a  ` ValueError `  exception with the message  ` width must be >= 0 ` 


* Private instance attribute:  ` height ` :* property  ` def height(self): `  to retrieve it
* property setter  ` def height(self, value): `  to set it:*  ` height `  must be an integer, otherwise raise a  ` TypeError `  exception with the message  ` height must be an integer ` 
* if  ` height `  is less than  ` 0 ` , raise a  ` ValueError `  exception with the message  ` height must be >= 0 ` 


* Instantiation with optional  ` width `  and  ` height ` :  ` def __init__(self, width=0, height=0): ` 
* Public instance method:  ` def area(self): `  that returns the rectangle area
* Public instance method:  ` def perimeter(self): `  that returns the rectangle perimeter:* if  ` width `  or  ` height `  is equal to  ` 0 ` , perimeter has to be equal to  ` 0 ` 

*  ` print() `  and  ` str() `  should print the rectangle with the character  ` # ` : * if  ` width `  or  ` height `  is equal to 0, return an empty string

*  ` repr() `  should return a string representation of the rectangle to be able to recreate a new instance by using  ` eval() ` 
* Print the message  ` Bye rectangle... `  ( ` ... `  being 3 dots not ellipsis) when an instance of  ` Rectangle `  is deleted
* You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x08$ cat 5-main.py
#!/usr/bin/python3
Rectangle = __import__('5-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

del my_rectangle

try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x08$ ./5-main.py
Area: 8 - Perimeter: 12
Bye rectangle...
[NameError] name 'my_rectangle' is not defined
guillaume@ubuntu:~/0x08$ 

```
No test cases needed
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x08-python-more_classes ` 
* File:  ` 5-rectangle.py ` 
 Self-paced manual review  Panel footer - Controls 
### 6. How many instances
          mandatory         Progress vs Score  Task Body Write a class   ` Rectangle `   that defines a rectangle by: (based on   ` 5-rectangle.py `  )
* Private instance attribute:  ` width ` :* property  ` def width(self): `  to retrieve it
* property setter  ` def width(self, value): `  to set it:*  ` width `  must be an integer, otherwise raise a  ` TypeError `  exception with the message  ` width must be an integer ` 
* if  ` width `  is less than  ` 0 ` , raise a  ` ValueError `  exception with the message  ` width must be >= 0 ` 


* Private instance attribute:  ` height ` :* property  ` def height(self): `  to retrieve it
* property setter  ` def height(self, value): `  to set it:*  ` height `  must be an integer, otherwise raise a  ` TypeError `  exception with the message  ` height must be an integer ` 
* if  ` height `  is less than  ` 0 ` , raise a  ` ValueError `  exception with the message  ` height must be >= 0 ` 


* Public class attribute  ` number_of_instances ` :* Initialized to  ` 0 ` 
* Incremented during each new instance instantiation
* Decremented during each instance deletion

* Instantiation with optional  ` width `  and  ` height ` :  ` def __init__(self, width=0, height=0): ` 
* Public instance method:  ` def area(self): `  that returns the rectangle area
* Public instance method:  ` def perimeter(self): `  that returns the rectangle perimeter:* if  ` width `  or  ` height `  is equal to  ` 0 ` , perimeter has to be equal to  ` 0 ` 

*  ` print() `  and  ` str() `  should print the rectangle with the character  ` # ` : * if  ` width `  or  ` height `  is equal to 0, return an empty string

*  ` repr() `  should return a string representation of the rectangle to be able to recreate a new instance by using  ` eval() ` 
* Print the message  ` Bye rectangle... `  ( ` ... `  being 3 dots not ellipsis) when an instance of  ` Rectangle `  is deleted
* You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x08$ cat 6-main.py
#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

guillaume@ubuntu:~/0x08$ ./6-main.py
2 instances of Rectangle
Bye rectangle...
1 instances of Rectangle
Bye rectangle...
0 instances of Rectangle
guillaume@ubuntu:~/0x08$ 

```
No test cases needed
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x08-python-more_classes ` 
* File:  ` 6-rectangle.py ` 
 Self-paced manual review  Panel footer - Controls 
### 7. Change representation
          mandatory         Progress vs Score  Task Body Write a class   ` Rectangle `   that defines a rectangle by: (based on   ` 6-rectangle.py `  )
* Private instance attribute:  ` width ` :* property  ` def width(self): `  to retrieve it
* property setter  ` def width(self, value): `  to set it:*  ` width `  must be an integer, otherwise raise a  ` TypeError `  exception with the message  ` width must be an integer ` 
* if  ` width `  is less than  ` 0 ` , raise a  ` ValueError `  exception with the message  ` width must be >= 0 ` 


* Private instance attribute:  ` height ` :* property  ` def height(self): `  to retrieve it
* property setter  ` def height(self, value): `  to set it:*  ` height `  must be an integer, otherwise raise a  ` TypeError `  exception with the message  ` height must be an integer ` 
* if  ` height `  is less than  ` 0 ` , raise a  ` ValueError `  exception with the message  ` height must be >= 0 ` 


* Public class attribute  ` number_of_instances ` :* Initialized to  ` 0 ` 
* Incremented during each new instance instantiation
* Decremented during each instance deletion

* Public class attribute  ` print_symbol ` :* Initialized to  ` # ` 
* Used as symbol for string representation
* Can be any type

* Instantiation with optional  ` width `  and  ` height ` :  ` def __init__(self, width=0, height=0): ` 
* Public instance method:  ` def area(self): `  that returns the rectangle area
* Public instance method:  ` def perimeter(self): `  that returns the rectangle perimeter:* if  ` width `  or  ` height `  is equal to  ` 0 ` , perimeter has to be equal to  ` 0 ` 

*  ` print() `  and  ` str() `  should print the rectangle with the character(s) stored in   ` print_symbol ` : * if  ` width `  or  ` height `  is equal to 0, return an empty string

*  ` repr() `  should return a string representation of the rectangle to be able to recreate a new instance by using  ` eval() ` 
* Print the message  ` Bye rectangle... `  ( ` ... `  being 3 dots not ellipsis) when an instance of  ` Rectangle `  is deleted
* You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x08$ cat 7-main.py
#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print("--")
my_rectangle_1.print_symbol = "&"
print(my_rectangle_1)
print("--")

my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
print("--")
Rectangle.print_symbol = "C"
print(my_rectangle_2)
print("--")

my_rectangle_3 = Rectangle(7, 3)
print(my_rectangle_3)

print("--")

my_rectangle_3.print_symbol = ["C", "is", "fun!"]
print(my_rectangle_3)

print("--")

guillaume@ubuntu:~/0x08$ ./7-main.py
########
########
########
########
--
&&&&&&&&
&&&&&&&&
&&&&&&&&
&&&&&&&&
--
##
--
CC
--
CCCCCCC
CCCCCCC
CCCCCCC
--
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
--
Bye rectangle...
Bye rectangle...
Bye rectangle...
guillaume@ubuntu:~/0x08$ 

```
No test cases needed
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x08-python-more_classes ` 
* File:  ` 7-rectangle.py ` 
 Self-paced manual review  Panel footer - Controls 
### 8. Compare rectangles
          mandatory         Progress vs Score  Task Body Write a class   ` Rectangle `   that defines a rectangle by: (based on   ` 7-rectangle.py `  )
* Private instance attribute:  ` width ` :* property  ` def width(self): `  to retrieve it
* property setter  ` def width(self, value): `  to set it:*  ` width `  must be an integer, otherwise raise a  ` TypeError `  exception with the message  ` width must be an integer ` 
* if  ` width `  is less than  ` 0 ` , raise a  ` ValueError `  exception with the message  ` width must be >= 0 ` 


* Private instance attribute:  ` height ` :* property  ` def height(self): `  to retrieve it
* property setter  ` def height(self, value): `  to set it:*  ` height `  must be an integer, otherwise raise a  ` TypeError `  exception with the message  ` height must be an integer ` 
* if  ` height `  is less than  ` 0 ` , raise a  ` ValueError `  exception with the message  ` height must be >= 0 ` 


* Public class attribute  ` number_of_instances ` :* Initialized to  ` 0 ` 
* Incremented during each new instance instantiation
* Decremented during each instance deletion

* Public class attribute  ` print_symbol ` :* Initialized to  ` # ` 
* Used as symbol for string representation
* Can be any type

* Instantiation with optional  ` width `  and  ` height ` :  ` def __init__(self, width=0, height=0): ` 
* Public instance method:  ` def area(self): `  that returns the rectangle area
* Public instance method:  ` def perimeter(self): `  that returns the rectangle perimeter:* if  ` width `  or  ` height `  is equal to  ` 0 ` , perimeter has to be equal to  ` 0 ` 

*  ` print() `  and  ` str() `  should print the rectangle with the character  ` # ` : * if  ` width `  or  ` height `  is equal to 0, return an empty string

*  ` repr() `  should return a string representation of the rectangle to be able to recreate a new instance by using  ` eval() ` 
* Print the message  ` Bye rectangle... `  ( ` ... `  being 3 dots not ellipsis) when an instance of  ` Rectangle `  is deleted
* Static method  ` def bigger_or_equal(rect_1, rect_2): `  that returns the biggest rectangle based on the area*  ` rect_1 `  must be an instance of  ` Rectangle ` , otherwise raise a  ` TypeError `  exception with the message  ` rect_1 must be an instance of Rectangle ` 
*  ` rect_2 `  must be an instance of  ` Rectangle ` , otherwise raise a  ` TypeError `  exception with the message  ` rect_2 must be an instance of Rectangle ` 
* Returns  ` rect_1 `  if both have the same area value

* You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x08$ cat 8-main.py
#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")


my_rectangle_2.width = 10
my_rectangle_2.height = 5
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")

guillaume@ubuntu:~/0x08$ ./8-main.py
my_rectangle_1 is bigger or equal to my_rectangle_2
my_rectangle_2 is bigger than my_rectangle_1
Bye rectangle...
Bye rectangle...
guillaume@ubuntu:~/0x08$ 

```
No test cases needed
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x08-python-more_classes ` 
* File:  ` 8-rectangle.py ` 
 Self-paced manual review  Panel footer - Controls 
### 9. A square is a rectangle
          mandatory         Progress vs Score  Task Body Write a class   ` Rectangle `   that defines a rectangle by: (based on   ` 8-rectangle.py `  )
* Private instance attribute:  ` width ` :* property  ` def width(self): `  to retrieve it
* property setter  ` def width(self, value): `  to set it:*  ` width `  must be an integer, otherwise raise a  ` TypeError `  exception with the message  ` width must be an integer ` 
* if  ` width `  is less than  ` 0 ` , raise a  ` ValueError `  exception with the message  ` width must be >= 0 ` 


* Private instance attribute:  ` height ` :* property  ` def height(self): `  to retrieve it
* property setter  ` def height(self, value): `  to set it:*  ` height `  must be an integer, otherwise raise a  ` TypeError `  exception with the message  ` height must be an integer ` 
* if  ` height `  is less than  ` 0 ` , raise a  ` ValueError `  exception with the message  ` height must be >= 0 ` 


* Public class attribute  ` number_of_instances ` :* Initialized to  ` 0 ` 
* Incremented during each new instance instantiation
* Decremented during each instance deletion

* Public class attribute  ` print_symbol ` :* Initialized to  ` # ` 
* Used as symbol for string representation
* Can be any type

* Instantiation with optional  ` width `  and  ` height ` :  ` def __init__(self, width=0, height=0): ` 
* Public instance method:  ` def area(self): `  that returns the rectangle area
* Public instance method:  ` def perimeter(self): `  that returns the rectangle perimeter:* if  ` width `  or  ` height `  is equal to  ` 0 ` , perimeter has to be equal to  ` 0 ` 

*  ` print() `  and  ` str() `  should print the rectangle with the character  ` # ` : * if  ` width `  or  ` height `  is equal to 0, return an empty string

*  ` repr() `  should return a string representation of the rectangle to be able to recreate a new instance by using  ` eval() ` 
* Print the message  ` Bye rectangle... `  ( ` ... `  being 3 dots not ellipsis) when an instance of  ` Rectangle `  is deleted
* Static method  ` def bigger_or_equal(rect_1, rect_2): `  that returns the biggest rectangle based on the area*  ` rect_1 `  must be an instance of  ` Rectangle ` , otherwise raise a  ` TypeError `  exception with the message  ` rect_1 must be an instance of Rectangle ` 
*  ` rect_2 `  must be an instance of  ` Rectangle ` , otherwise raise a  ` TypeError `  exception with the message  ` rect_2 must be an instance of Rectangle ` 
* Returns  ` rect_1 `  if both have the same area value

* Class method  ` def square(cls, size=0): `  that returns a new Rectangle instance with  ` width == height == size ` 
* You are not allowed to import any module
```bash
guillaume@ubuntu:~/0x08$ cat 9-main.py
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)

guillaume@ubuntu:~/0x08$ ./9-main.py
Area: 25 - Perimeter: 20
#####
#####
#####
#####
#####
Bye rectangle...
guillaume@ubuntu:~/0x08$ 

```
No test cases needed
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-higher_level_programming ` 
* Directory:  ` 0x08-python-more_classes ` 
* File:  ` 9-rectangle.py ` 
 Self-paced manual review  Panel footer - Controls 
