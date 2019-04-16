'''
Requirement -> To develop a kiosk system for a hotel which will display a configurable menu, ask for order, check for correct entries, 
suggest various combination of food items, ask for quantity and finally print the order summary and bill.
Note: If this code is downloaded from Git, please reconfigure the menu.py path on line 9 accordingly.
'''

import configparser
config=configparser.ConfigParser()
config.read_file(open(r'E:\Python\menu.py'))
i=0
item={}
item_list=[]
for each_section in config.sections():
	print(each_section)
	for (each_key, each_val) in config.items(each_section):
		i+=1
		print('%2s. %-15s->%s'%(i,each_key.capitalize(),each_val))
		item_list.append(each_key.capitalize())
		item[each_key.capitalize()]={'Food_Type':each_section, 'Price':each_val}
print('\n Press "e" to exit\n')
while True:
	total=0
	z=0
	food_set=set({})
	k=0
	order=input('Please Enter the number of item you wish to order together (comma separated): ')
	if(order=='e'):
		break
	order=order.split(',')
	try:
		order=list(map(int,order))
	except ValueError:
		print('\nYou have entered an incorrect order entry. Please try again! :-)\n')
		continue
	for i in order:
		try:
			j=item_list[i-1]
		except IndexError:
			print('\nYou have entered an incorrect order entry. Please try again! :-)\n')
			z=1
			break
		food_set.add(item[j]['Food_Type'])
	if(z==1):
		continue
#print(food_set)
	if('Breads' in food_set or 'Curry' in food_set or 'Rice' in food_set or 'Daal' in food_set):
		if('Breads' in food_set and 'Curry' not in food_set and 'Daal' not in food_set and 'Rice' in food_set):
			print('You have not chosen any Curry or Daal. How will you eat the bread and rice ;-b\n')
			k=input('Do you wanna re enter the order: Y or N?')
		elif('Breads' not in food_set and 'Curry' in food_set and 'Rice' not in food_set):
			print('You have not chosen any Bread or Rice. How will you eat the Curry ;-b\n')
			k=input('Do you wanna re enter the order: Y or N?')
		elif('Breads' not in food_set and 'Daal' in food_set and 'Rice' not in food_set):
			print('You have not chosen any Bread or Rice. How will you eat the Daal ;-b\n')
			k=input('Do you wanna re enter the order: Y or N?')
		elif('Rice' in food_set and 'Curry' not in food_set and 'Daal' not in food_set):
			print('You have not chosen any Curry or Daal. How will you eat the Rice ;-b\n')
			k=input('Do you wanna re enter the order: Y or N?')
		elif('Breads' in food_set and 'Curry' not in food_set and 'Daal' not in food_set):
			print('You have not chosen any Curry or Daal. How will you eat the bread ;-b\n')
			k=input('Do you wanna re enter the order: Y or N?')
	if(k=='Y'):
		continue
	print('\nPlease enter the quantity of each item:')
	bill=dict()
	for i in order:
		n=item_list[i-1]
		m=int(input('%s : '%(n)))
		total+=m*int(item[n]['Price'])
		bill[n]={'quantity':m,'price':item[n]['Price']}
	print('\nYour Order summary is as below:')
	print('Sr.No. Order Item       Quantity  Price per item  Amount')
	p=1
	for order_item in bill.keys():
		a=int(bill[order_item]['quantity'])
		b=int(bill[order_item]['price'])
		print('  %-5s%-17s   %-6s       %-9s   %s'%(p,order_item,a,b,a*b))
		p+=1
	#print(bill)
	print('\nYour total payable amount is : %s'%(total))
	print('\nBon Appetite!:-)')
	break

