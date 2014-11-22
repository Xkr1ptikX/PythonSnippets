# in this file I'll be practicing strings and a few basic ways to use or
# manipulate strings.

# string variable for our name, you can enclose the string with single quotes or
# double quotes, I'll use singles so I don't have to use the shift key
name = 'Jason'

# string variable for a number as a string, using double quotes here
stringNum = "1"

# printing a string, in this case the word Hello with
print ("Hello")

# printing string variable name and "\n" is for adding an extra space between
# this print statement and the next print statement
print (name + "\n")

#print ("\n")

# printing the same string and concatenating (fancy word for appending) the
# variable name to it
print ('Hello' + name)

# notice the previous line printed "Hello" and name with no space between them
# let's fix that by simply adding an extra space after "Hello" so "Hello "
print ("Hello" + " " + name)

# An alternate way of doing this and in my opinion a simpler way, less typing ;)
print ("Hello " + name)

# anotther way of printing an extra line 
print()

# printing a number as a string
print ("num: " + stringNum)

# print (stringNum + 2) would produce an error you would either have to convert
# the string variable stringNum to a int variable or the number 2 to a string

# first we'll convert the number 2 to a string, we'll use the str() command
print ("first num: " + stringNum + "; second num: " + str(2))

# about tired of retyping this let's throw it in a variable
greet = 'Hello '

print()

# putting it all together
print (greet + name + ' your number is: ' + stringNum) 

