'''method 1'''
# a=[]
# n=int(input("enter number of elements in list: "))
# for i in range(0,n):
#     element=int(input())
#     a.append(element)
# print(a)
# ele=int(input("enter an element: "))
# if ele in a:
#     print("element is in the list")
# else:
#     print("element is not in the list")

'''method 2'''
# n1=[int(x) for x in input('Enter some integer numbers:').split()]
# f=int(input("Which element you want to find? :"))
# for i in n1:
#     if (f in n1):
#         print("The Value",f,"is Found")
#         break
#     else:
#         print("The Value",f,"is Not Found")
#         break