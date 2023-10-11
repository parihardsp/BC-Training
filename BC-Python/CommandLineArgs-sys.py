"""
Open the file
import sys module- These arguments are stored in a list called 'argv' inside sys module
write the code , as here print(len(sys.argv)).
In terminal, write py <filename.py> agr1 arg2, eg.  py commandLineArgs.py 10 trees
This give 3 (including the pythonfile name you are working on.)

"""

import sys

print(len(sys.argv))
print(sys.argv)   #saves all arguments in a list in form of strings.
#
# n=len(sys.argv) #skippinng the python file name.
#
# for x in range(1,n):
#     print(sys.argv[x])

#we can get these argumnet by indexing the list 'sys.argv'

# arg=sys.argv[1]
#
# if arg =="test":
#     print("This is a test")
# elif arg=="full-fleged":
#     print("This is a full-fledged")
# else:
#     print("Invalid Argument")