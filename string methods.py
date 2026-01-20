Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a="machine learning"
a[2:14:3]
'cnlr'

a[3:15:2]
'hn eri'
a[1:11:4]
'ane'
#negative striding
a="python course"
a[-1:-9:-3]
'eu '
a[-2:-12:-4]
'sch'
a[-3:-13:-2]
'ro ot'
a[-4:-10:-3]
'u '
a[::-1]
'esruoc nohtyp'
#string methods
#len
a="codegnan"
len(a)
8
a="python course"
len(a)
13
a=""
len(c)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    len(c)
NameError: name 'c' is not defined
len(a)
0
a=" "
len(a)
1
a="hello python"
len(a)
12
#count
a="twinkle twinkle little star"
a.count(a)
1
a.count("twinkle")
2
a.count(" ")
3
b="jhonny jhonny yes pappa"
b.count("jhonny")
2
#find a string
a="code"
a[2]
'd'
a[4]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a[4]
IndexError: string index out of range
a[1]
'o'
b="codegnan"
b.find("n")
5
b.find("d")
2
b[5]+b[7]
'nn'
#escape sequences
\n->new line
SyntaxError: unexpected character after line continuation character
#\n->new line
#\t->tap space
a="name\nmobileno\tmailid\ncity"
print(a)
name
mobileno	mailid
city
b="name:akshita\nmobileno:9392682979\tmailid:akshita@2903.com\ncity:mtm"
print(b)
name:akshita
mobileno:9392682979	mailid:akshita@2903.com
city:mtm
#replace
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
#upper()
a="hello"
a.upper()
'HELLO'
a.lower()
'hello'
a="HI"
a.lower()
'hi'
a.upper()
'HI'
a="python"
a.capitalize()
'Python'
b="python course"
b.title()
'Python Course'
c="i am in class"
c.title()
'I Am In Class'
#true&flase
a="python"
a.startswith("p")
True
a.endswith('n")
           
SyntaxError: incomplete input
a.endswith("n")
           
True
a.isupper()
           
False
a.islower()
           
True
a.isdigits()
           
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    a.isdigits()
AttributeError: 'str' object has no attribute 'isdigits'. Did you mean: 'isdigit'?
a="1234"
           
a.isdigits()
           
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a.isdigits()
AttributeError: 'str' object has no attribute 'isdigits'. Did you mean: 'isdigit'?
a.isdigit()
           
True
#alpha&alnum
           
a="hello world"
           
a.isalpha()
           
False
a="helloworld"
           
a.isalpha()
           
True
b="akshi123"
           
b.isalnum()
           
True
c="akshita"
           
c.isalnum()
           
True
#strip()
           
a="   akshita     "
           
a.lstrip()
           
'akshita     '
a.rstrip()
           
'   akshita'
a.strip()
           
'akshita'
a.lstrip(),a.rstrip()
           
('akshita     ', '   akshita')
a.strip()
           
'akshita'
a="python java c c++"
           
a.strip()
           
'python java c c++'
>>> a.split()
...            
['python', 'java', 'c', 'c++']
>>> b="i am learning python course"
...            
>>> b.split()
...            
['i', 'am', 'learning', 'python', 'course']
>>> #join
...            
>>> a="python","java","c"
...            
>>> "".join(a)
...            
'pythonjavac'
>>> " ".join(a)
...            
'python java c'
>>> #concatenation
...            
>>> a="hello"
...            
>>> b="world"
...            
>>> print(a+b)
...            
helloworld
>>> print(a+""+b)
...            
helloworld
>>> print(a+" "+b)
...            
hello world
>>> fname="python"
...            
>>> lname="course"
...            
>>> print(fname+" "+lname)
...            
python course
>>> print(fname.title()+" "+lname.title())
...            
Python Course
>>> print((fname+" "+lname).title())
...            
Python Course
