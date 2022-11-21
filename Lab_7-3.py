# Author: PCL 11/18/22

#creating a function that will print "Hello World"
def greeting ():
    #giving the function a docstring for others who use this code to understand what the function does
    '''this function can only print "Hello World" on one line'''
    #main part of the function - when called the function will simply print "Hello World"
    return("Hello World")

#having the consule return the docstring to explain what the function greeting does - this does not need a print statement to execute
help(greeting)

#calling the greeting fuction to run all of the code within the function
print(greeting())

#Test Cases
print(greeting() == "Hello World")
#should result in true
print(greeting() == "Goodbye World")
#should result in false
print(greeting() == "World")
#should result in false
print(greeting() == "Hello")
#should result in false