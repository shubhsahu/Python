"""
Given a string str and an array of strings strArr[], the task is to sort the array according to the alphabetical order defined by str.
Note: str and every string in strArr[] consists of only lower case alphabets.
"""

s1 = 'fguecbdavwyxzhijklmnopqrst'
strArr1 = ['game', 'is', 'the', 'best', 'place', 'for', 'learning']
s2 = 'avdfghiwyxzjkecbmnopqrstul'
strArr2 = ['rainbow', 'consists', 'of', 'colours', 'ashu', 'bablu']

def shubh(p,y):
	sortstr=sorted(y, key= lambda x:p.find(x[0]))
	print(sortstr)

print(s1)
shubh(s1,strArr1)

print(s2)
shubh(s2,strArr2)