#KEY VALUE PAIRS WHERE KEY IS UNIQUE IDENTIFER FOR EACH VALUE.
student ={'name':'Vikrant','Age':25, 'courses': ['Math','CompSci']}
print(student['name'])
print(student['courses'])

student['phone'] ='9423778822'

#Keys can be any mutable datatypes
print(student.get('phone','Not found')) #Get method to give None instead of an error.#Adding Not found custom message.

#Update Multiple values.
student.update({'name:':'Jane','age': '26','phone': '992929292'})
print(student)

#Delete
#del student['age']
#age = student.pop('age')  #pop removes and returns the value specified.
#print(age)

#Length
print(len(student))
print(student.values())
print(student.items())

#Lopping through dictionary
for key in student:          #Only Keys are accesed in the loop.
    print(key)

#Using two variables and items method.
for key, value in student.items():
    print(key,value)

#F-string Formatting

person ={'name':'Vikrant','age': 24}
#sentence ='My name is {} and I am {} years old'.format(person['name']),person['age'])
sentence = f"My name is {person['name']} and i am {person['age']} years old"
print(sentence)

#Calucations can be performed in F Strings.
calcuion =f'4 times 11 is equal to {4 * 11}'
print(calcuion)

#For loop

for n in range(0,10):          #Zero padding values.Sometimes used for databases.
    sentence =f'Value is {n:02}'    #:02 0 for zero padding for 2 digits = 01
    print(sentence)

pi= 3.14158265

sentence= f'pi equal to {pi:.4f}'  #.4 for 4 digits and f for floating point value.
print(sentence)


#----------------------------------------------------------------
from datetime import datetime
birthday= datetime(1996,10,30)
sentence = f'Vikrant has a birthday on {birthday:%B %d,%Y}'
print(sentence)


fav_numbers ={'Eric':17,"Marks":45}
for name,number in fav_numbers.items():
    print('Eric loves {}'.format(name,number))