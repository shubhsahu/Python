'''
Checking if we will reach at the end of the list by assuming each number in the list will be number of steps to move forward.
example:
a=[2,4,1,1,4] -> True
b=[3,2,1,0,4,3,2,1,0,2] -> False
c=[3,3,1,0,4,0,1,0,1] -> True
'''

a=[2,4,1,1,4]
b=[3,2,1,0,4,3,2,1,0,2]
c=[3,3,1,0,4,0,1,0,1]

def shubh(k):
	count=0
	if 0 not in k:
		return True
	else:
		pos=[i for i, value in enumerate(k) if value == 0]
		print(pos)
		for i in pos:
			j=i
			for l in range(i):
				s=(j-1)+k[j-1]
				if s<=i:
					j-=1
					continue
				else:
					count+=1
					break
		if count==len(pos):
			return True
		else:
			return False

print(shubh(a))
print(shubh(b))
print(shubh(c))