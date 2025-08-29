### write
writefile=open("output.txt","w")

user_input=input("Enter text to write the file: ")
write=writefile.write( user_input +"\n")
writefile.close()

###read_write
readfile=open("output.txt","r")
read=readfile.read().strip()

if read==user_input:
    print("Data successfully written to output.txt")
readfile.close()


###append
appendfile=open("output.txt","a")

user_input2=input("enter additional text to write the file: ")

append=appendfile.write( user_input2 + "\n")

appendfile.close()


### read_append
readfile1=open("output.txt","r")
read=readfile1.read().strip()

if user_input2 in read:
    print("Data successfully appended to output.txt")
readfile1.close()


### read output.txt
readfile3=open("output.txt","r")
read=readfile3.read()
print("final content of the output.txt: ")
print(read)
readfile3.close()
readfile3.close()


