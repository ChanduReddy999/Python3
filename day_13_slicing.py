''' day 13 slicing in python'''

# print(len('python'))
# abc=['a','b'],[1,2,3]
# print(len(abc))
# print(abc[0][0])

# a="python"
# print(a,type(a))
# print(a[0])                  # is also same as             #print('python'[0])

# print('python'[0])
# print('python'[1])
# print('python'[2])
# print('python'[3])
# print('python'[4])
# print('python'[5])
# print('python'[6])               # IndexError: string index out of range

"""concatenation :- Used only for strings. Will combine more than one string together.
we use + sign to represent concatenation in the strings concept.
string is immutable, modifications cannot be made."""

# v='department'
# print(v[3]+v[2]+v[3]+v[4]+v[5]+v[6]+v[7]+v[8]+v[9])           #apartment


print('python'[-1])
print('python'[-2])
print('python'[-3])
print('python'[-4])
print('python'[-5])
print('python'[-6])
print('python'[-7])                 # IndexError: string index out of range


# w='python'
# print(w[:])               # python
# print(w[0:])              # python
# print(w[0:6])         # python
# print(w[0:0])         # empty line or blank line is given as output 
# print(w[0:1])         # p
# print(w[0:2])         # py
# print(w[0:3])            # pyt
# print(w[0:4])         # pyth
# print(w[0:5])             # pytho
# print(w[0:6])             # python
# print(w[0:7])             # python
# print(w[0:99])             # python
# print(w[0:0])         # empty line or blank line is given as output
# print(w[3:2])         # empty line or blank line is given as output
# print(w[5:3])         # empty line or blank line is given as output

# x='python'                    #  p y t h o n
# print(x[0:-1])                #  0 1 2 3 4 5         # pytho
                                # -6-5-4-3-2-1
# print(x[0:-2])          # pyth
# print(x[0:-3])          # pyt
# print(x[0:-4])          # py
# print(x[0:-5])          # p
# print(x[0:-6])          # empty line or blank line is given as output
# print(x[0:-7])          # empty line or blank line is given as output

# r='python'
# print(r[2:5])       # tho
# print(r[3:4])       # h
# print(r[5:2])       # empty line or blank line is given as output
# print(r[5:5])       # empty line or blank line is given as output

# y='python'
# print(y[-1:-6])         # empty line or blank line is given as output
# print(y[2:-5])          # empty line or blank line is given as output
# print(y[-6:])           # python


"""[  :   :  ]"""
'''left->(start=0)  middle->(end (or) -1 (or) n)   right->skip/step/difference(default value (1))'''
# f='python'
# print(f[::])        # is same as   # print(f[ : : ])    # python
# print(f[0::1])            # python
# print(f[::2])            # pto
# print(f[::3])            # ph
# print(f[::4])            # po
# print(f[::5])            # pn
# print(f[::6])            # p
"""reverse of a string [  :   :  ]"""
'''left->(end=n)  middle->(start=-1)   right->skip/step/difference(default value (1))'''
# print(f[::-1])            # nohtyp
# print(f[::-2])            # nhy
# print(f[::-3])            # nt
# print(f[::-4])            # ny
# print(f[::-5])            # np
# print(f[::-6])            # n
# print(f[1::])               # ython
# print(f[2::])               # thon
# print(f[3::])               # hon
# print(f[4::])               # on
# print(f[5::])               # n
# print(f[6::])               # empty line or blank line is given as output
# print(f[1:6:])          # ython
# print(f[2:5:])          # tho
# print(f[3:4:])          # h
# print(f[4:3:])          # empty line or blank line is given as output
# print(f[5:2:])          # empty line or blank line is given as output
# print(f[6:1:])          # empty line or blank line is given as output

