'''
1) WAP to take input string from user and print the length of string

2) Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.

3) Write a Python program to get a single string from two given strings by user , separated by a space and swap the first two characters of each string. 
Sample String : 'abc', 'xyz' 
Expected Result : 'xyc abz'

4) Write a Python program to change a given string to a new string where all the even position characters are in starting and all odd position characters are in end.

5) Write a Python program to remove the characters which have odd index values of a given string

6) WAP to insert a string in the middle of a other string.
'''

a=input("Enter the string to print the length: ")
print(len(a))

b=input("Enter the string to make a new string from first and last 2 characters: ")
print(b[0:2]+b[-2:])

c=input("Enter a string separated by a space to swap first 2 character of each word: ")
c1=c.split()
print(c1[1][:2]+c1[0][2:]+' '+c1[0][:2]+c1[1][2:])

d=input("Enter a string to bring even position characters at front and odd position characters at end: ")
print(d[1::2]+d[::2])

e=input("Enter a string to remove all odd indexed values: ")
print(e[::2])

f1=input("Enter a string in which string has to inserted in middle: ")
f2=input("Enter a string which will be inserted in middle: ")
f3=len(f1)//2
print(f1[:f3]+f2+f1[f3:])
