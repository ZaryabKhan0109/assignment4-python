file1=open("file.txt","r+")
read=file1.readline()
read1=file1.readline()
print("Reading file content:")
print("Line1:",read.strip())
print("Line2:",read1.strip())
print()
file1.close()

try:
 file1=open("sample.txt","r+")
except FileNotFoundError:
    print("Error: The File 'sample.txt' not found")
