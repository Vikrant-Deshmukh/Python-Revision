#List-Allows to works with a list of values that
courses =['History','Math','physics','Computer']
courses2 =['ART','Education']
print(len(courses))
print(courses[0:2])
print((courses[-1]))

#Add at end of the list.
courses.append('Art')
print(courses)

#Add at particular location in the list.
courses.insert(0,'Art') #Does not override the value.
print(courses)

#Extend method.
courses.extend(courses2)
print(courses)

#Remove items from the list...
courses.remove('Math')
popped = courses.pop()
print(popped)

#Sort the list...
courses.reverse()
print(courses)

nums =[1,3,4,5,7,8]
nums.sort(reverse=True) #Descending order
print(nums)

courses.sort()#Alphabetically order for Strings and ascedning order for numbers
print(courses)

#Sorted functions without altering the orginal list
sorted_list = sorted(courses)
print(sorted_list)

print(min(nums))
print(max(nums))

#Find index

print(courses.index('History'))
print('Art' in courses) # in to check if value is present.

for item in enumerate(courses, start =1 ):  #Enumarate for Index. #start =1 for stating the start from particular index.
    print(item)
    
#String method join
courses_str = ','.join(courses)
new_list = courses_str.split('-')
print(courses_str)
print(new_list)

#Tuples- Are not mutable -cannot be modified
#textbook = ('DMBS','CNS','WNL')
#textbook2 = textbook
#textbook[0] = 'Art'
#print(textbook2) = tuple' object does not support item assignment.

#Sets- Values are unordered and no duplicates.

cs_courses = {'History','Geometry','physics'} 
ds_courses = {'History','Geometry','physics','History','Design'}
#Membership test -whether value is in the Sets. 
print('Math'in cs_courses)
print(cs_courses)

print(cs_courses.intersection(ds_courses)) #Common values #Passing ds_courses into intersection() method.
print(cs_courses.difference(ds_courses)) #difference
print(cs_courses.union(ds_courses))
 

#Create empty list and Tuple.
empty_list =[]
empty_list= list()

#Empty tuples
empty_tuples = ()
empty_tuples = tuple()

#Empty Sets
empty_sets = set()
empty_sets = {} # Wrong- This is a dictionary.