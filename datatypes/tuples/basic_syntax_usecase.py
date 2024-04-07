 
#limited version of list
#unmodifable list is tuples
#Tuples are another kind of seqence that funcation much like a list
#they have elements which are indexed starting at 0 

#syntax 
x = list()
x = ('mahesh','shrishti','mahesh')
#print complete tuple
print('tuple list', x) 
#length of the tuple 
print('length of the tuple',len(x))
#access particular item of the tuple
print('access the second tuple',x[1])
#print max number 
print('max',max(x))

#defination of tuple in the for loop
for name in x: 
    print(name)

#find the position of the object in the tuple 
print(x.index('shrishti'))


#find the count of particular item in the list 
print(x.count('mahesh'))



#tuples are "imm"


#tuples are more effeicient, since python does not have to build tuple structures to be 
#modifiable, they are simpler and more efficient in terms of memory use and performance
#than lists. so in our program when we are making "temporary" variables 
#we prefer tuples over list


#tuples and assignment 


(x,y) = (4,'mahesh')
print(y)
(a,b) = (1,2)
print(a)

x,y = 'a','b'
print(y)

#tuples and dictionaries

#the items() method in dictionaries returns a list of (key, values) tuples

a = {'India':1, 'USA':2}
print(a.items())


#tuples are comparable


(0,2,2) < (4,5,6)



