#DICTIONARY


#empty dict
d={}
print(d)
print(type(d))

#creating  a dict
d={'usn':'01','name':'qwer','branch':'ise'}
print(d)
#to access qwer as name only
print(d['name'])

#to traverse a dict
for i in d:
    print(d[i])

for i in d:
    print(i,":",d[i])

#adding elements in dict
d={1:10,2:20,3:30}
d[4]=40
print(d)

#to find length
print(len(d))

#updating alements in dict
d={'usn':'01','name':'qwer','branch':'ise'}
#let us change the name from qwer to xyz
d['name']='xyz'
print(d)

#old_dic.update(new_dict)
d1={1:10,2:20,3:30}
d2={4:40,5:50}
print(d1)
d1.update(d2)
print(d1)

#deleting the elements from dictionary
'''
there are two ways
1.pop(key)
2.del statement
'''
#pop(key) here key nothing but index
d1={1:10,2:20,3:30}
print(d1.pop(2))
print(d1)

#del statement
d1={1:10,2:20,3:30}
del d1
#print(d1)


#to find items using items()
d1={1:10,2:20,3:30}
print(d1.items())

#keys() to print list of keys in the given dict
d1={1:10,2:20,3:30}
print(d1.keys())

#values()
d1={1:10,2:20,3:30}
print(d1.values())


