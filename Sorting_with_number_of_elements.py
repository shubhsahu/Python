"""
Given an integer array, 
sort the array according to the frequency of elements in decreasing order, if frequency of two elements are same then sort in increasing order.
"""

i=[2,3,2,4,5,12,2,3,3,3,12]
l=[4,4,2,2,2,2,3,3,1,1,6,7,5]

def shubh(k):
	print(k)
	mydict={j:k.count(j) for j in k}
	print(mydict)
	p=[]
	for w in sorted(mydict, key=mydict.get, reverse = True):
		for k in range(mydict.get(w)):
			p.append(w)
	print(p)


shubh(i)
shubh(l)