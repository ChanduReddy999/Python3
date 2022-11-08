# f1=open("chandu_reddy.txt",'x')
# f2=open("chandu_reddy_v.txt",'x')
# f3=open("chandu_reddy2.txt",'x')

# f1=open("chandu_reddy.txt",'w')
# f1.write("chandu loves amma, nanna and anna")
# f1.close()

# f2=open("chandu_reddy_v.txt",'w')
# f2.write("chandu is good at coding")
# f2.write("chandu is practicing daily")
# f2.close()

# f2=open("chandu_reddy_v.txt",'w')
# f2.write("chandu is good at coding")
# f2.write("chandu is practicing daily")
# f2=open("chandu_reddy_v.txt",'w')                 # after this line the text rewritten/vanished and writes the new text in the file
# f2.write("chandu is good at coding")
# f2.write("\nchandu is practicing daily")
# f2.close()

# f3=open("chandu_reddy2.txt",'w')
# f3.write("chandu loves amma, nanna and anna")
# f3=open("chandu_reddy2.txt",'a')                  # a=append means that a text is inserted into the existing file with continuation
# f3.write("welcome to my world")                   # if the file doesnot exists then creates a file and then insert the text/data into it
# f3.write("\nlove you")
# f3.close()

# f1=open("chandu_reddy.txt",'r')
# print(f1.read())                      # it reads the files and outputs the data present in it
# f1.close()

# f1.close()            #close every file after opening/writing into file/appending text to file/reading the file