"""
Day 4
Topic: Format Specifiers
"""

"""
Note
int --> %d or %i
float --> %f
str --> %s
"""

# a=5; b=4.5; c='hello'
# print(type(a), type(b),type(c))
# print(a)
# print('%d' %a)
# print('%i' %a)
# print(float(a))
# print(b)
# print('%f' %b)
# print('%.1f' %b)
# print('%.2f' %b)
# print('%.3f' %b)
# print('%.13f' %b)

# a=5
# print(float(a))
# print(str(a))
# print('%f' %a)
# print('%.1f' %a)

# b=6.8
# print(int(b))
# print(str(b))

# c='hello'
# print(int(c))           #ValueError
# print(float(c))         #ValueError

# d='5'
# print(type(d))
# print(d)
# print(int(d))
# print(float(d))
# e=int(d)
# print(e,type(e))
# f=float(d)
# print(f,type(f))

# g='5.3'
# print(type(g))
# print(int(g))           #ValueError
# print(float(g))
# h=float(g)
# print(h,type(h))
# i=int(h)
# print(i,type(i))


# isidentifier() --> It is a method which helps us to know the variable declared is valid or invalid.
#                --> if the variable is valid we get the answer as True
#                --> if the variable is invalid we get the answer as False


# print('a'.isidentifier())           #True
# print('_'.isidentifier())           #True
# print('.'.isidentifier())           #False
# print('2'.isidentifier())           #False
# print('a b'.isidentifier())         #False
# print('3rt'.isidentifier())         #False
# print('age'.isidentifier())         #True
# print('a_r_t'.isidentifier())       #True
# print('a3e'.isidentifier())         #True
# print('_a3e'.isidentifier())        #True


