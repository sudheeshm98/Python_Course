"""
File Handling
-------------
File handling is an important part of any web application
Python has several functions for creating, reading, updating, and deleting files
The key function for working with files in Python is the open() function
The open() function takes two parameters; filename, and mode

There are four different methods (modes) for opening a file:
------------------------------------------------------------
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)

"""

file1 = open("samplefile.txt","w")
file1.write("Hi Dears!!!")

file1 = open("samplefile.txt","r")
print(file1.read())

file1 = open("samplefile.txt","a")
print(file1.write(" Welcome to python World ,\n""Python is a popular programming language ,\n"
                  "It was created by Guido van Rossum, and released in 1991"))

file1 = open("samplefile.txt","r")
lines = file1.readlines()
print(type(lines))
print(lines[0])





