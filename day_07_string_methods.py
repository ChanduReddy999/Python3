"""
Day 7
Topic: string methods
"""

"""1"""
# print('chandu reddy'.capitalize())  #Chandu reddy

# text='chandu reddy'
# a=text.capitalize()
# print(a)

"""2"""
# print('sampath'.upper())      #SAMPATH

# text='sampath'
# a=text.upper()
# print(a)

"""3"""
# print('RAJ'.lower())          #raj

# text='RAJ'
# a=text.lower()
# print(a)

"""4"""
# print('Chandu is learning Python in Josh Innovations and it is located in Ameerpet'.count('is'))       #2

# text="I am chandu from Hyderabad and it is located in Telangana. Hyderabad is specially known for Biryani and Charminar."
# x=text.count('Hyderabad')
# print(x)                     #2

"""5"""
# print('Chandu is learning Python in Josh Innovations and it is located in Ameerpet'.casefold())         #chandu is learning python in josh innovations and it is located in ameerpet

# text='Chandu is learning Python in Josh Innovations and it is located in Ameerpet'
# a=text.casefold()
# print(a)

"""6"""
# print('Python'.center(20,'0'))            #0000000Python0000000

# text='Python'
# a=text.center(20,'0')
# print(a)

"""7"""
# print('hello world'.endswith('d'))                  #True

# text='hello world'
# a=text.endswith('d')
# print(a)

"""8"""
# print('C\th\ta\tn\td\tu'.expandtabs())      #C       h       a       n       d       u
# print('C\th\ta\tn\td\tu'.expandtabs(6))     #C     h     a     n     d     u
# print('C\th\ta\tn\td\tu'.expandtabs(3))     #C  h  a  n  d  u

# text='C\th\ta\tn\td\tu'
# a=text.expandtabs(6)
# print(a)

"""9"""
# print('Hello, Welcome to Python classes.'.find('to'))       #15
# print('Hello, Welcome to Python classes.'.find('welcome'))       #-1
# print('Hello, Welcome to Python classes.'.find('classes'))       #25

# text='Hello, Welcome to Python classes'
# a=text.find('to')
# print(a)

"""10"""
# print('hi, welcome to my world'.index('my'))        #15
# print('hi, welcome to my world'.index('hI'))        #ValueError: substring not found

# text='hi, welcome to my world'
# a=text.index('my')
# print(a)

"""11"""
# print('chandu1999'.isalnum())           #True
# print('chandu 1999'.isalnum())           #False

# text='chandu1999'
# a=text.isalnum()
# print(a)

"""12"""
# print('hameedsir'.isalpha())            #True
# print('hameed sir'.isalpha())           #False

# text='hameedsir'
# a=text.isalpha()
# print(a)

"""13"""
# print('_abcdef_12A'.isidentifier())          #True

# text='abcdef_12'
# a=text.isidentifier()
# print(a)

"""14"""
# print('raj'.islower())              #True
# print('rajSam'.islower())              #False

# text='raj'
# a=text.islower()
# print(a)

"""15"""
# print('12345'.isnumeric())          #True

# text='12345'
# a=text.isnumeric()
# print(a)

"""16"""
# print('994'.isdigit())              #True

# text='994'
# a=text.isdigit()
# print(a)

"""17"""
# print('abcd789'.isprintable())          #True

# text='abcd789'
# a=text.isprintable()
# print(a)

"""18"""
# print('   '.isspace())                #True

# text='   '
# a=text.isspace()
# print(a)

"""19"""
# print('C V Raman'.istitle())            #True
# print('C v Raman'.istitle())            #False

# text='C V Raman'
# a=text.istitle()
# print(a)

"""20"""
# print('CHANDU'.isupper())           # True

# text='CHANDU'
# a=text.isupper()
# print(a)

"""21"""
# print('       banana      '.lstrip())     #banana      

# text='       banana      '
# a=text.lstrip()
# print(a)

"""22"""
# print('chandureddyvadala'.partition('reddy'))       #('chandu', 'reddy', 'vadala')
# print('chandureddyvadala'.partition(' '))       #('chandureddyvadala', '', '')
# print('chandureddyvadala'.partition('2'))       #('chandureddyvadala', '', '')

# text='chandureddyvadala'
# a=text.partition('reddy')
# print(a)

"""23"""
# print('chandu cares all his friends'.replace('cares','loves'))      #chandu loves all his friends

# text='chandu cares all his friends'
# a=text.replace('cares','loves')
# print(a)

"""24"""
# print('chandu is very good in coding and he performing well in his tasks'.rfind('in'))          #53

# text='chandu is very good in coding and he performing well in his tasks'
# a=text.rfind('in')
# print(a)

"""25"""
# print('chandu is very good in coding and he performing well in his tasks'.rindex('and'))    #30

# text='chandu is very good in coding and he performing well in his tasks'
# a=text.rindex('and')
# print(a)

"""26"""
# print('chandureddyvadala'.rpartition('reddy'))      #('chandu', 'reddy', 'vadala')
# print('chandureddyvadala'.rpartition(' '))          #('', '', 'chandureddyvadala')

# text='chandureddyvadala'
# a=text.rpartition('reddy')
# print(a)

"""27"""
# print('    chandu      '.rstrip())      #    chandu

# text='    chandu     '
# a=text.rstrip()
# print(a)

"""28"""
# print('     chandu      '.split())      #['chandu']

# text='     chandu      '
# a=text.split()
# print(a)

"""29"""
# print('I am going to Hyderabad\nWanna join me'.splitlines())            #['I am going to Hyderabad', 'Wanna join me']

# text='I am going to Hyderabad\nWanna join me'
# a=text.splitlines()
# print(a)

"""30"""
# print('I am now at sanath nagar'.startswith('I'))           #True

# text='I am now at sanath nagar'
# a=text.startswith('I')
# print(a)

"""31"""
# print('     I am Alone     '.strip())           #I am Alone

# text='     I am Alone     '
# a=text.strip()
# print(a)

"""32"""
# print('i am at Work in my Office'.swapcase())           #I AM AT wORK IN MY oFFICE

# text='i am at Work in my Office'
# a=text.swapcase()
# print(a)

"""33"""
# print('I am a Software Developer'.title())          ##I Am A Software Developer

# text=('I am a Software Developer')
# a=text.title()
# print(a)

"""34"""
# print('chandu'.zfill(10))           #0000chandu

# text='chandu'
# a=text.zfill(10)
# print(a)

"""35"""
# print('abcd102_'.isascii())             #True

# text='abcd102_'
# a=text.isascii()
# print(a)


