D={5:'a',4:'b',3:'c',2:'d',1:'e'}
# To sort dictionary according to keys
x=sorted(D)
print(x)

# To display key and value sorted according to keys

for key in sorted(D):
    print(key,D[key],end=" ")
print('/r')
# Sorting the Keys and Values in alphabetical using the value

print(sorted(D.items(), key = lambda kv:(kv[1], kv[0]))) 

''' 1.For descending order : Use “reverse = True” in addition to
      the sorted() function.
    2.For sorting w.r.t multiple values: Separate by “comma”
       mentioning the correct order in which sorting has to be performed.'''
# Python code demonstrate the working of
# sorted() with lambda

# Initializing list of dictionaries
lis = [{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]

# using sorted and lambda to print list sorted
# by age
print ("The list printed sorting by age: ")
print (sorted(lis, key = lambda i: i['age']))
print ("\r")

# using sorted and lambda to print list sorted
# by both age and name. Notice that "Manjeet"
# now comes before "Nandini"
print ("The list printed sorting by age and name: ")
print (sorted(lis, key = lambda i: (i['age'], i['name'])))
print ("\r")

# using sorted and lambda to print list sorted
# by age in descending order

print ("The list printed sorting by age in descending order: ")
print (sorted(lis, key = lambda i: i['age'],reverse=True))
