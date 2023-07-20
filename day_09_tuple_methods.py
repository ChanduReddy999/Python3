''' day 9 Tuple Methods '''

# print(dir(str))
# print(dir(list))
# print(dir(tuple))

# a=(1)
# print(a,type(a))        # 1 <class 'int'>

# b=(1,)
# print(b,type(b))            # (1,) <class 'tuple'>

# c=1,2,3,'hey',2.8
# print(c,type(c))        # (1, 2, 3, 'hey', 2.8) <class 'tuple'>

# ab=('apple','banana','orange','asus','redmi','hp','jio')
# ab[1]='yellow'              # TypeError: 'tuple' object does not support item assignment
# print(ab)                  # in interpreter if we get error on previous line this line will not be executed as interpreter executes the programme step by step.

# n='hello','world'
# print(n,type(n))            # ('hello', 'world') <class 'tuple'>
# print(n[2])                 # IndexError: tuple index out of range

# print('hello','world')      # hello world

# v=(1,2,3.4,'hello',[2,'t'],('H',8),None,True)
# print(v,type(v))            # (1, 2, 3.4, 'h4llo', [2, 't'], ('H', 8), None, True) <class 'tuple'>

# v=(1,2,3.4,'hello',[2,'t'],('H',8))
# v[0]=23.3                   # TypeError: 'tuple' object does not support item assignment
# print(v)                  # in interpreter if we get error on previous line this line will not be executed as interpreter executes the programme step by step.

# v=(1,2,3.4,'hello',[2,'t'],('H',8))
# print(v.count(3.4))             # 1
# print(v.count(23.4))             # 0
# print(v.index([2,'t']))         # 4
# print(v.index([42,'h']))        # ValueError: tuple.index(x): x not in tuple


