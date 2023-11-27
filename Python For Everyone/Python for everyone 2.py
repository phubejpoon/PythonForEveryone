Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print('Hello World')
Hello World
print('Hello Poon')
Hello Poon
name = 'Poon'
lastname Asawanatwat
SyntaxError: incomplete input
name = 'Phubej'
lastname = 'Asawatanawat'
fullname = name + ' ' + lastname
>>> print(fullname)
Phubej Asawatanawat
>>> type(name)
<class 'str'>
>>> age = 10
>>> tpye(age)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    tpye(age)
NameError: name 'tpye' is not defined. Did you mean: 'tuple'?
>>> age = 10
... type(age)
SyntaxError: multiple statements found while compiling a single statement
>>> age = 10
>>> type(age)
<class 'int'>
>>> name = 'Poon'
>>> name.upper()
'POON'
>>> name = 'Poon'
>>> name.lower()
'poon'
>>> print(name)
Poon
>>> name = name.upper()
>>> print(name)
POON
>>> number = '1'
>>> number.zfill(5)
'00001'
>>> number = '15'
>>> number.zfill(5)
'00015'
