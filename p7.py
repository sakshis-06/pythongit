#for loop
'''
syntax: for(start,end,step)
1.starts from start till end-1 for positive
2.starts from start till end+1 for negative
3.default step value is +1
4.range() works only on int
5.if only one value is passed in range then it indicates end value
6.default start value is 0
'''

#example for range
for d in range(7):
    print(d)
    #this prints number from 0 to 6 here
#start =0  end=7  and step=1

for d in range(3,10):
    print(d)
#start =3  end=10 and step=1

for d in range(3,10,2):
    print(d)
#start =3  end=10  and step=2



#While
i=0 #start
while i<5: #end
    print(i)
    i+=1   #step

i=0 #start
while i<5: #end
    print(i,end=" ")
    i+=1   #step

#example of array of strings
s="bat"
i=0
print()
while i < len(s):
    print(s[i],end = " ")
    i+=1


#while loop

i=1
while(i<=10):
     print(i)
     i=i+1
print()

#sum of n natural numbers
sum=0
for i in range(1,11):
    sum=sum+i
print(sum)


#print 1 to 10 except 5 using continue
for i in range(1,11):
    if i==5:
        continue
    print(i)

#print and break
for i in range(1,11):
    if i==5:
        break
    print(i)

