#list
l=[1,6.77,'tt',[7,8,9]]   #nested list
print(l)
print(type(l))

#length of list
print(len(l))

#accessing list members
print(l[3][2])

#concatenation of two lists
a1=[1,2,3]
a2=[5,6,7]
print(a1+a2)

#repeatation in the list
print(a1*3)

#sclicing using static index
#list_variable[startindex:endindex:step]
a3=[1,2,3,4,5,6]
#to print all from 3
print(l[2:])
#tp print from 2 to 5
print(a3[2:5])
#to find index
# variable=index(ele)
print(a3.index(4))


#print last element
print(a3[-1])

#how to reverse list sing sclicing
print(a3[::-1])

#list
l=[10,20,30,[40,50]]
for i in l:
    print(i)

#to count how many times a number is repeated
z=[11,22,33,22,22,44]
print(z.count(22))

#list method used to typecast
#list()
strr="helloe"
l=list(strr)
print(l)
#tupple to list
t=('a',10,20)
print(t)
print(type(t))
l=list(t)
print(l)
print(type(l))
#set to list
s={10,20,3,4,5}
print(s)
l=list(s)
print(l)

#insertion of element in a list
#lists are mutable
'''
1.append(ele)
2.extend(ele)
3.insert(pos,ele)
'''
c=[10,20,30]
#variable.append(ele)   to add element at last position
c.append(100)
print(c)
#variable.extend(ele)
c.extend([200,300])
print(c)
#variable.insert(pos,ele)
c.insert(1,15)
print(c)
print('')

# to delete the eements of list
'''
1.pop(index)
2.remove(ele)
3.clear()
4.del statement
'''
#var.pop(index)
l=[11,22,35,33,44]
print(l.pop(2))

#var.remove(ele)
l=[10,20,25,30,40]
l.remove(25)
print(l)

#var.clear()
l=[1,2,3,4]
l.clear()
print(l) #removes all the elements of list

#var.del
#it completely deleets the list
d=[1,2,3,4]
del d
#print(d)  this gives error saying that d is not defined


#count and reverse()
#reverse in two ways 1. l[::-1] and second way is
l=[1,2,3,4,5]
l.reverse()
print(l)

#sorting list using sort()
w=[3,2,6,4,8,1,9]
w.sort()
print(w)

#sorting using sorted(list)
e=[5,4,7,8,1,3,2,9,6]
k=sorted(e)
print(k)


#add list using sum(list)
u=[1,2,3,4,5,6,7,8,9,10]
s=sum(u)
print("the sum of the  list is",s)


# to find minimum and maximum element of the list using min(list) and max(list)
l=[45,87,99,105,20,15]
max_ele=max(l)
min_ele=min(l)
print("The max ele is ",max_ele)
print("The min ele is ",min_ele)