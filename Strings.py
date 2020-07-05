#Print welcome message
print('Hello Vikrant!')
print('This is a Print Function!')

message = 'Orignal message'
print(message)

#Variables should be underscore or should start with _ and should be descriptive.

message1 = 'Vikrant\'s World'
print(message1)

message2 = "Vikrant's World"
#Use single quote if string contains double quote and vice versa.
message3= """Vikrant is a programmer
from Mumbai"""
print(message3)

#Print lenght of string
print(len(message3))

#Access character indivually
print(message3[0])
#Access in range
print(message3[0:5])
print(message3[:5])
print(message3[6:])

print(message.lower())
print(message.upper())

print(message.count('O'))
print(message.find('Orignal'))

person_name = "Vikrant Deshmukh"
#Instead of making new message varibale set the same varibale = to the replacement
person_name = person_name.replace('Vikrant','King')
print(person_name)

#Concatenate 
greeting = 'Hello'
name ='Vikrant'
#Formated String example
welcome = greeting + '.' + name + '.!'
welcome = f'{greeting.lower()} ,{name.upper()}. welcome!'
#Fstrings in Python 3.6 and greater
print(welcome)

#Learn somethig new in python
#DIR Function - If we pass an variable it will show all the methods and attributes
#print(dir(name))
#Help for detailed overview of each methods
#print(help(str.lower))

#F Strings in detail. in 3.6 and above

first_name = 'Vikrant'
last_name = 'Deshmukh'
#sentence = 'My Name is {} {}' .format(first_name, last_name) #using .format method
#print(sentence)

sentence = f'My Name is {first_name.upper()} {last_name.upper()}' #can run functions and methods
print(sentence)