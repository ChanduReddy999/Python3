'''method 1'''
# m=int(input())
# n=int(input())
# for i in range(m,n):
#     while(i%2==0):
#         print(i)
#         break
#     i+=2

'''method 2'''
# m,n=[int(i) for i in input("Enter Start Value, Stop Value: ").split()]
# x=m
# if x%2!=0: x=m+1
# while(x<=n):
#     print(x)
#     x+=2

""" using for loop """
# m=int(input())
# n=int(input())
# for i in range(m,n,2):
#     print(i)

""" using while loop """
# m=int(input())
# n=int(input())
# while(m<=n):
#      print(m)
#      m+=2