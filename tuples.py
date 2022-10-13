#tuples 
#they are immutable
#we can write lists in the tuple

t=(1,2,3,4,5,[6,7])
print(t)
print(type(t))
# to access 7
print(t[5][1])

#empty tuple
t=()
print(t)
print(type(t))

t1=(10)
print(type(t1))
t1=(10,)
print(type(t1))


#tyepcatsing using tuple()
l=[1,2,3]
t=tuple(l)
print(t)

#taking input from user for tuple
# t = tuple(input("Enter the elements "))
# print(t)
#to overcome this we have a function called eval() is used
#t=eval(input("Enter the elements "))  #give input in tuple format
#print(t)

t=[1,2,3,4,5]
#to find length
print(len(t))

#sorted(tuple)
t=(1,6,2,4)
print(sorted(t))

#adding cant be done in tuples as they are immmutable
#t[2]=30

#traversing of tuple
t=(1,2,3,4,5,6)
for i in t:
    print(i)

#in and not in the tuple -membership operators
t=(1,2,3,4,5,6)
if 1 in t:
    print("true")
else :
    print("false")

#comparing of tuples : >,<.<=,>=,==,!=
t1=(1,2,3,4,5)
t2=(1,2,3,4,5)
t3=(4,5,6,7,8)
print(t1==t2)
print(t1==t3)

#min(tuple) and max(tuple)
t1=(1,2,3,4,5)
print(min(t1))
print(max(t1))

#to find occurrence using count
t=(1,2,3,4,5,5,6,5,5,7)
print(t.count(5))

#we can delete usinf del statement
t=(1,2,3,4,5,5,6,5,5,7)
del t
#print(t)


#concatenation and replication
t2=(1,2,3,4,5)
t3=(6,7,8)
#concate
print(t2+t3)
#replicate
print(t2*3)