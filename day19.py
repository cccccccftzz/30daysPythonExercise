#File Handling

print("Catch up in Preview".center(80, "-"))
#File Handling by using open() function
f = open('reading_file_example.txt') # mode(r, a, w, x, t,b)  could be to read, write, update
print(f)

#To read the whole file
txt = f.read()
print(type(txt))

print(txt)
f.close()

#read(XX): To read the limited characters
f = open('reading_file_example.txt') 
txt = f.read(10)
print(txt)
f.close()

#readline(): To only read the first line
f = open('reading_file_example.txt') 
line = f.readline()
print(line)
f.close()

#readlines(): To only read the whole txt LINE BY LINE
f = open('reading_file_example.txt') 
lines = f.readlines()
print(lines)
f.close() #['This is a sample file to try open a file\n', 'the second line of the file\n', '\n']


