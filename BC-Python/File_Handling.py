#Syntext
# var_name = open('file_name.txt', 'mode/file format')
#rg f=open('my_file.txt','rt'  --> mode=r- read (default cmd) and t=text (is default)- fileformat, b-for binary

#Reading a file
file=open('myfile.txt','rt')

# file.read()       # Reading the entire file
# file.readline()   # Reading line by line
# file.readlines()  # Reading all lines into a list


#Reading 2nd line of the file
file.readline()  #skips the first line, or till \n comes.
file.readline()  #prints 2nd line within the file

file.close()

#Writing a file:
#if file dosennt exist, it will create the new file
#if the file exists it will overwrite all the content

file=open('my_newfile.txt','w')  # file dosent exist, new file create

file.write('Hey, This is the new file')
file.close()

#Appending to the file:

file=open('my_newfile.txt','a')
file.write('\nThis is the 2nd line in the new file created.')
file.close()

#using 'with' :
with open("my_newfile.txt", "r") as file:
    content = file.read()


# The file is automatically closed when exiting the 'with' block

#ContextManager in Python:
# Python program creating a
# context manager

class ContextManager():
    def __init__(self):
        print('init method called')

    def __enter__(self):
        print('enter method called')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')


with ContextManager() as manager:
    print('with statement block')

print('')

# Python program showing
# file management using
# context manager

class FileManager():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


# loading a file
with FileManager('test.txt', 'w') as f:
    f.write('Test')

print(f.closed)
