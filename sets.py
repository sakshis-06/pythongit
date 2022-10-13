# SETS

#it doesnot print the duplicates

#empty set
s=set()
print(type(s))

s={10}
print(s)
print(type(s))

#unique set
s={2,2,6,4,5,2,}
print(s)

#set()
l=[1,2,3,3,1]
s=set(l)
print(s)

#traverse the set
s={'a','b','c'}
for i in s:
    print(i,end='   ')
print(" ")

#we cannot access the set members using index but we can traverse it
#print(s[1])

#length
s={'a','b','c'}
print(len(s))

#ading new elements in a set using add(element)
s={1,2,3,4}
s.add(5)
print(s)


#updating elements in set using update(set)
#syntax  :  oldset.update(newset)
s2={1,2,3,4}
s1={5,6,7}
s1.update(s2)
print(s1)


#deleting in 3 ways
'''
1. remove(ele)
2.discard(ele)
3.pop()
'''
#deleting using remove(element)
s1={1,2,3,4}
s1.remove(2)
print(s1)

#pop()
s1={1,2,3,4}
s1.pop()
print(s1)
#print(id(s1))

#discard(element)
s1={1,2,3,4}
s1.discard(2)
print(s1)


#union(var) ot |
s={1,2,3,4}
a={5,6,7}
print(s.union(a))
s={1,2,3,4}
a={5,6,7}
print(s|a)


#intersection or &
s={1,2,3,4}
a={5,6,7,4}
print(s.intersection(a))
s={1,2,3,4}
a={5,6,7,4}
print(s&a)


#difference or -
s={1,2,3,4}
a={5,6,7,4}
print(s.difference(a))
s={1,2,3,4}
a={5,6,7,4}
print(s-a)