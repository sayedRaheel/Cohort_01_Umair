# regular_string = "C:\new_folder\file.txt"
# print("Regular String:", regular_string)

# raw_string = r"C:\ew_folder\**file.txt"
# print("Raw String:", raw_string)

name = "The"

print(name[0]) # first character
print(name[-1]) # last character
length = len(name) # length of string
print("Length of the string:", length) 

print("The \ntechnology") # new line
print("The \t technology") # tab space
print("The \\ technology") # backslash
print("The \' technology") # single quotes
print("The \" technology") # double quotes
print("The ddd \r technology") # remove everthing before \r
print("The d d\b technology") # backspace untill first d
print("The d\ftechnology") # form feed and new line
print("The \v technology") # vertical tab and new line

print(name.find("e"))

print(name.find("ff"))


'''
# Output:
T
e
Length of the string: 3
The 
technology
The      technology
The \ technology
The ' technology
The " technology
 technology
The d  technology
The d
     technology
The 
     technology
2
-1
'''