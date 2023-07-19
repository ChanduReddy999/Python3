"""day 8"""

'''
list
-list is mutable
-list is sequence/ordered type
-represented by []
-it can even hold several datatypes
-it can even empty []
-ex1  a=1,2,3,4
-ex2  b=1,1.2,'hey',4
-ex3  c=1,1.2,'hello',[1,2]
'''

# a=[]
# print(type(a))      # <class 'list'>

# p=['ameerpet',5]
# print(p,type(p))        # ['ameerpet', 5] <class 'list'>
# print(p[0],type(p[0]))         # ameerpet <class 'str'>
# print(p[1],type(p[1]))         # 5 <class 'int'>
# print(p[2])         # IndexError: list index out of range

# a='hello'
# print(a[0])     # h
# print(a[4])         # o
# print(a[-1])         # o
# print(a[5])         # IndexError: string index out of range

# a=None
# print(type(a))      # <class 'NoneType'>

# b=[1,3.4,'hey',None,True]
# print(b,type(b))            # [1, 3.4, 'hey', None, True] <class 'list'>
# print(b[0],type(b[0]))        # 1 <class 'int'>
# print(b[1],type(b[1]))        # 3.4 <class 'float'>
# print(b[2],type(b[2]))        # hey <class 'str'>
# print(b[3],type(b[3]))        # None <class 'NoneType'>
# print(b[4],type(b[4]))        # True <class 'bool'>
# print(b[5],type(b[5]))        # IndexError: list index out of range

'''Note : modifications cannot be made inside the string'''
# s="python"
# s[0]='P'        # TypeError: 'str' object does not support item assignment

'''Note : List will allow the modifications'''
# r=[4,3.2,'python']
# r[0]=1
# print(r)            # [1, 3.2, 'python']
# r[-1]='program'
# print(r)            # [1, 3.2, 'program']

# x=[1,2.3,'hello',[10,12]]
# print(x,type(x))            # [1, 2.3, 'hello', [10, 12]] <class 'list'>
# print(x[0],type(x[0]))      # 1 <class 'int'>
# print(x[1],type(x[1]))      # 2.3 <class 'float'>
# print(x[2],type(x[2]))      # hello <class 'str'>
# print(x[3],type(x[3]))      # [10, 12] <class 'list'>
# print(x[4],type(x[4]))      # IndexError: list index out of range
# print(x[3][0],type(x[3][0]))    # 10 <class 'int'>
# print(x[3][1],type(x[3][1]))    # 12 <class 'int'>

# y=[1,2.3,'hello',[10,'hey']]
# print(y,type(y))            # [1, 2.3, 'hello', [10, 'hey']] <class 'list'>
# y[0]=23
# y[3][1]=24
# print(y,type(y))            # [23, 2.3, 'hello', [10, 24]] <class 'list'>
# print(y[0],type(y[0]))      # 23 <class 'int'>
# print(y[1],type(y[1]))      # 2.3 <class 'float'>
# print(y[2],type(y[2]))      # hello <class 'str'>
# print(y[3],type(y[3]))      # [10, 24] <class 'list'>
# print(y[4],type(y[4]))      # IndexError: list index out of range

# print(dir(list))

# n=[1,2,3.3,'hai',[19,121]]
# n.append(5)
# print(n)            # [1, 2, 3.3, 'hai', [19, 121], 5]

# n=[1,2,3.3,'hai',[19,121]]
# n.clear()
# print(n)            # []

# n=[1,2,3.3,'hai',[19,121]]
# print(n)            # [1,2,3.3,'hai',[19,121]]
# b=n.copy()
# print(b)            # [1,2,3.3,'hai',[19,121]]

# n=[5,10,'hello',10,'']
# print(n.count(''))      # 1
# print(n.count(6))       # 0
# print(n.count(10))      # 2

# v=[5,23,34]
# b=[1,2,3,5,7]
# v.extend(b)
# print(v)            # [5, 23, 34, 1, 2, 3, 5, 7]
# b.extend(v)
# print(b)            # [1, 2, 3, 5, 7, 5, 23, 34, 1, 2, 3, 5, 7]

# a='hello'
# print(a.index('w'))         # ValueError: substring not found

# n=[1,2,3.4,'hai',3.9,[67]]
# print(len(n))           # 6
# print(n.index(3.4))         # 2
# print(n.index('hai'))         # 3
# print(n.index(1.89))           # ValueError: 1.89 is not in list
# print(n.index([67]))         # 5
# print(n.index(3.9))         # 4
# print(n.rindex[2])         # AttributeError: 'list' object has no attribute 'rindex'


# d=[1,3,5,7,9,11,13,15]
# d.insert(1,'hello')
# print(d)              # [1, 'hello', 3, 5, 7, 9, 11, 13, 15]
# d.insert(2,4)
# print(d)              # [1, 'hello',4, 3, 5, 7, 9, 11, 13, 15]
# d.insert(-1,14)
# print(d)              # [1, 'hello', 4, 3, 5, 7, 9, 11, 13, 14, 15]
# d.insert(-2,'world')
# print(d)              # [1, 'hello', 4, 3, 5, 7, 9, 11, 13, 'world', 14, 15]

# d=[1,3,5,7,9,11,13,15,27,38,49]
# d.insert(1,'hello')
# d.insert(2,4)
# d.insert(-1,'king')
# d.insert(-2,'welcome to programming')
# print(d)              # [1, 'hello', 4, 3, 5, 7, 9, 11, 13, 15, 27, 38, 'welcome to programming', 'king', 49]


# n=[1,2,3,4,5,6]
# print(n.pop())          # 6

# n=[1,2,3,4,5,6]
# n.pop()
# print(n)            # [1, 2, 3, 4, 5]
# n.pop(0)
# print(n)            # [2, 3, 4, 5]
# n.pop(7)            # IndexError: pop index out of range
# print(n)            # Interpreter doesnot come to this line as error occured in above line no.138

# f=[12,13,14,14.5,'hey',30,50]
# f.remove('hey')
# print(f)                # [12, 13, 14, 14.5, 30, 50]
# f.index(100)
# print(f)            # ValueError: 100 is not in list

# n=[1,2,3,4,5]
# print(n[::-1])      # [5, 4, 3, 2, 1]
# n.reverse()
# print(n)            # [5, 4, 3, 2, 1]

# mn=[1,2,3,4,5]
# mn.reverse()
# print(mn)           # [5, 4, 3, 2, 1]


# n=[11,2,332,34,5,46]
# n.sort()
# print(n)            # [2, 5, 11, 34, 46, 332]
# n.sort(reverse=False)
# print(n)            # [2, 5, 11, 34, 46, 332]
# n.sort(reverse=True)
# print(n)            # [332, 46, 34, 11, 5, 2]


# k=[2.3,1.5,222,45,2.09,23]
# k.sort()
# print(k)                # [1.5, 2.09, 2.3, 23, 45, 222]

# print(chr(65))        # A
# print(chr(90))        # Z
# print(chr(97))        # a
# print(chr(122))       # z

# print(chr(91))        # [
# print(chr(92))        # \
# print(chr(93))        # ]
# print(chr(94))        # ^
# print(chr(95))        # _
# print(chr(96))        # `


# l=['HD','DF','EF','ZS','TH','s','PQ','UX','AH','DV']
# l.sort()
# print(l)        # ['AH', 'DF', 'DV', 'EF', 'HD', 'PQ', 'TH', 'UX', 'ZS', 's']


# print(dir(list))

# print(len(['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']))           # 11