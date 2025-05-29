file=open('Text1.txt','r')
print(file.read())
file.close()

filewrite=open('Text1.txt','w')
filewrite.write("I AM LEARNING TO ADD MORE DATA TO THE EXISTING FILE")
filewrite.write("I am adding a new a new file to the existing file")
filewrite.close()

fileappend=open('Text1.txt','a')
fileappend.write("I am runig")
fileappend.close