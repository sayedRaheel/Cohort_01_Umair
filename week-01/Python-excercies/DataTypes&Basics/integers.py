a = 2
b = 4
c = a + b
print(c)

print("The sum of", a, "and", b, "is", c)
# print(f"The sum of {a} and {b} is {c}")
print("The sum of {} and {} is {}".format(a, b, c))
print("The sum of %d and %d is %d" % (a, b, c))
print(type(c))
print(id(c))
print(isinstance(c, int))
d = -10
print(type(d))
print(id(d))
print(isinstance(d, int))

'''
Output:
6
The sum of 2 and 4 is 6
The sum of 2 and 4 is 6
The sum of 2 and 4 is 6
<class 'int'>
126252296962448
True
<class 'int'>
126252297998480
True
'''