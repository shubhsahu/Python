'''
Given an array of positive integers, find maximum possible value K such that array has at-least K elements that are greater than or equal to K. 
The array is unsorted and may contain duplicate values.
'''

i=[7,6,5,4,3,2]
j=[11,12,13,14,15,16,17,18,19,20,21,20,14,15,30,16]
t=[11,12,13,14,15,16,17,18,19,20,21,20,14,15,11,12,13,14,15,16,17,18,19,20,21,20,14,15]

def shubh1(k):
	sorted_list=sorted(k)
	length=len(k)
	p=length
	for x in range(length):
		p-=1
		if x+1>=sorted_list[p]:
			return sorted_list[p]

def shubh2(k):
	sorted_list=sorted(k)
	length=len(k)
	m=length//2
	valid_number=[]
	lower,upper=m,length
	repeat_num=0
	for x in range(m):
		p=sorted_list[m]
		l=len([i for i in sorted_list if i >= p])
		if l>=p:
			if(repeat_num==sorted_list[m]):
				break
			valid_number.append(sorted_list[m])
			lower=((lower+upper)//2)
			repeat_num=sorted_list[m]
		else:
			upper=lower
			m=lower=m//2
	return(max(valid_number))
			
def shubh3(k):
	if(len(k)<=15):
		print(shubh1(k))
	else:
		print(shubh2(k))

shubh3(i)
shubh3(j)
shubh3(t)