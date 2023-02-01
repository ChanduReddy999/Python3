'''
Types of Errors in Python
1- NameError
2- ValueError
3- TypeError
4- SyntaxError
5- AttributeError
6- KeyError
7- IndentationError
8- IndexError
9- ZerodivisionError
'''

'''Common Errors'''

# print(3/0)            # ZeroDivisionError: division by zero

# print(a)              # NameError: name 'a' is not defined

# print('hello'+7)      # TypeError: can only concatenate str (not "int") to str

# n='chandu'
# print(int(n))         # ValueError: invalid literal for int() with base 10: 'chandu'

# print(['Hello'].lower())        # AttributeError: 'list' object has no attribute 'lower'


"""Error Handling"""

# print(dir(__builtins__))

'''1'''

# print("hello chandu")
# print(57657)
# try:
#     print(9/0)
# except:
#     print("ZeroDivisionError: division by zero, You have divided by zero")
# print("Hello Python")
# print("Programming")

'''2'''

# print("Hello Pyhton")
# print("Hello World")
# try:
#     print(20/5)
# except:
#     print("You have not divided by zero so no ZeroDivisionError and except block is not executed")
# print("123")
# print("kailash")


'''3'''
# print("Hello Pyhton")
# print("Hello World")
# a=5
# try:
#     print(b)                            # NameError: name 'b' is not defined
# except ZeroDivisionError:
#     print("Not Ok Divided by Zero")
# print("123")
# print("kailash")


'''4'''
# print("Hello Pyhton")
# print("Hello World")
# a=5
# try:
#     print(a/5)
#     print(b)                # NameError: name 'b' is not defined
# except ZeroDivisionError:
#     print("Not Ok Divided by Zero")
# print("123")
# print("kailash")


'''5'''
# print("Hello Pyhton")
# print("Hello World")
# a=5
# try:
#     print(a/5)
#     print(a/0)
# except ZeroDivisionError:
#     print("You have not divided by zero")
# print("123")
# print("kailash")


'''6'''
# print("Hello Pyhton")
# print("Hello World")
# a=5
# try:
#     print(a/0)
#     print(7)
# except ZeroDivisionError:
#     print("Not Ok Divided by Zero")
# except NameError:
#     print("You have not defined the name")
# print("123")
# print("kailash")


'''7'''
# print("Hello Pyhton")
# print("Hello World")
# a=5
# try:
#     print(a/5)
#     print(a)
#     print(a/0)
# except ZeroDivisionError:
#     print("Not Ok Divided by Zero")
# print("123")
# print("kailash")



