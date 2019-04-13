'''
Take 2 words from user and check how many elements have to be removed from both words to make them both anagram of each other
'''
first=input('Please enter the first word: ').upper()
first_split=list(first)
second=input('Please enter the second word: ').upper()
second_split=list(second)
first_len=len(first_split)
second_len=len(second_split)

def shubh(a,b):
	a1=list(a)
	b1=list(b)
	for i in a:
		if(i in b and i in b1):
			a1.remove(i)
			b1.remove(i)
	print('Number of characters to be removed to make both words Anagram is: ' + str(len(a1)+len(b1)))

if(first_len < second_len):
	shubh(first_split,second_split)
else:
	shubh(second_split,first_split)