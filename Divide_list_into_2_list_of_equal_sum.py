'''
Program to divide a list into 2 parts such that both parts have equal sum assuming the sum is even and if it is odd, the nearest 
possible division of list.
'''
list1_str=input('Enter the list of numbers to be divided into 2 (comma separated):')
list1=list1_str.split(',')
list1=map(int,list1)
list2=sorted(list1)
list_sum=sum(list2)
sum2=list_sum//2
list2=list2[::-1]
list3=list(list2)
sum3=[]
counter=0
for i in range(len(list2)):
	sum3.append(list2[i])
	list3.remove(list2[i])
	s=sum(sum3)
	if(s==sum2):
		print(sorted(sum3))
		print(sorted(list3))
		counter=1
		break
	if(s>sum2):
		sum3.remove(list2[i])
		list3.append(list2[i])
if(counter==0):
	print('No such division possible')
