'''
To generate numbers that are always between 0 and 6 such that when I add a number to that the result is always between 0 and 6.
For example if we add 4 to 3 (3+4) the result is 0, add 5 to 3 (5+3) the result is 1 and if we subtract 2 to 1 (1-2) the result is 6.
'''

first_num=int(input("Enter first number: "))
second_num=int(input("Enter second number: "))
output=[0,1,2,3,4,5,6]
sum_num=first_num + second_num
remainder=sum_num % 7
print(output[remainder])