Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> x,y,z = (3,4,5)
>>> my_tuple = (3,4,5)
>>> print(my_tuple+my_tuple)
(3, 4, 5, 3, 4, 5)
>>> print(x+y+z)
12
>>> print (x*3)
9
>>> print(my tuple
	  
SyntaxError: invalid syntax
>>> print(my_tuple*3)
	  
(3, 4, 5, 3, 4, 5, 3, 4, 5)
>>> print(my_tuple[0]==x)
	  
True
>>> print(x[0])
	  
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(x[0])
TypeError: 'int' object is not subscriptable
>>> my_tuple[0]=17
	  
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    my_tuple[0]=17
TypeError: 'tuple' object does not support item assignment
>>> print(mu_tuple)
	  
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(mu_tuple)
NameError: name 'mu_tuple' is not defined
>>> x=17
	  
>>> print(x)
	  
17
>>> import turtle
	  
>>> print(turtle.pos())
	  
(0.00,0.00)
>>> print(type(turtle.pos()))
	  
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(type(turtle.pos()))
  File "<string>", line 5, in pos
turtle.Terminator
>>> 
