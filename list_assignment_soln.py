'''
Write a Python program to remove duplicates from a list
Write a Python program to find the length of all words of a list

Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']

Write a Python program to get the difference between the two lists.

Write a Python program to find the index of an item in a specified list

Write a Python program to append a list to the second list. 

Write a Python program to get unique values from a list

Write a Python program to count the number of elements in a list within a specified range

Write a Python program to check whether a list contains a sublist

Write a Python program to remove an empty tuple(s) from a list of tuples.
Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
'''

a=[1,2,3,4,5,4,2,8,7,6,4,2,5,8]
a1=list(set(a))
print(a)
print('After removing duplicate values:')
print(a1)


b=['shubh','sahu','ethans','baner']
print(b)
for i in range(len(b)):
	print('length of word at index '+str(i)+' is: '+str(len(b[i])))

c=['a','b','c','d','e','f','g','h']
print(c)
c.remove(c[0])
c.remove(c[3])
c.remove(c[3])
print('After removing 0th, 4th and 5th elements:')
print(c)

d1=[1,2,3,4,5]
d2=[3,4,5,6,7]
print(d1)
print(d2)
d3=set(d1)
d4=set(d2)
d5=list(d3-d4)
print('Difference between first and second list:')
print(d5)

e=[1,'a',2,'b',3,'c',4,'d',5,'e']
print(e)
e1='c'
print("The character 'c' is at "+str(e.index(e1)))

f1=[1,2,3,4]
f2=[5,6,7,8]
print(f1)
print(f2)
print('After extending list 1 to list 2:')
f1.extend(f2)
print(f1)

g=[1,2,3,2,3,4,5,6,7,6,7,8]
print(g)
g1=[]
for i in g:
	if(g.count(i)==1):
		g1.append(i)
print('Unique values in above list:')
print(g1)

h=[1,2,3,4,5,6,7,8,9,4,6,5,8,6,4,2,9]
lower_range=3
upper_range=7
print(h)
print('lower_range: '+ str(lower_range) + '  upper_range: '+ str(upper_range))
h1=0
for i in h:
	if(i >= lower_range and i <= upper_range):
		h1+=1
print('Number of elements in above range:')
print(h1)

i=set([1,2,3,4,5,6,7,8,9])
print(i)
i1=set([2,3,4])
print(i1)
print('First list has a sublist as second list:')
i2=i|i1
if(i == i2):
	print(True)
else:
	print(False)

j=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print(j)
print('After removing empty tuples:')
k=list(j)
for i in range(len(j)):
	if(type(j[i])==tuple and len(j[i])==0):
		k.remove(j[i])
print(k)