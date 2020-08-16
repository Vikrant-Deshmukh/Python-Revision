#Comparsions
#Equal: ==
#Not equal: !=
#Greater than and Less than > <
#Greater or equal: >=
#Less or equal: <=
#Object identity: is 

lang ='Javascript'

if lang == 'Python':
    print('Its true')     #Add elif of more conditions #no switch case in python.
elif lang == 'Java':
    print('Lang is java')

elif lang == 'Javascript':
    print('Lang is javascripy')
else:
    print('no match')

#Boolean #and #or #not

user ='Admin'
logged_in = True

if not logged_in:
    print('Enter Admin page unsuccesfull')
else: 
    print('Logged out')

a =[1,2,3]
b =[1,2,3]
print(a==b)
print(a is b) #Two different objects in memory hence prints False
print(id(a))
print(id(b))

#False values:
#False
#None
#ZERO 0
#Zero of any numeric type
#Any empty sequence.For example, '',().[].
#Any empty mapping.for example,{}.

condition ={}

if condition:
    print('Evaluation is true')
else:
    print('Evaluation is false')
   

#----------------------------------------------------------------

