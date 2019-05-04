'''
Requirement -> To develop a kiosk system for a hotel which will display a configurable menu, ask for order, check for correct entries, 
suggest various combination of food items, ask for quantity and finally print the order summary and bill.
Note: If this code is downloaded from Git, please reconfigure the menu.py path on line 9 accordingly.
'''
import configparser
config=configparser.ConfigParser()
config.read_file(open(r'E:\Python\menu.py'))

class Hotel:
	def __init__(self):
		self.item={}
		self.item_list=[]

	def print_menu(self):
		i=0
		print('*'*30+'\n'+' '*10+'MENU\n'+'*'*30)
		for each_section in config.sections():
			print(each_section)
			for (each_key, each_val) in config.items(each_section):
				i+=1
				print('%2s. %-15s->%s'%(i,each_key.capitalize(),each_val))
				self.item_list.append(each_key.capitalize())
				self.item[each_key.capitalize()]={'Food_Type':each_section, 'Price':each_val}
		print('\n Press "e" to exit\n')
		print('*'*30+'\n'+'*'*30)
		self.customer_order()

	def customer_order(self):
		while True:
			self.total=0
			z=0
			self.food_set=set({})
			k=0
			self.order=input('Please Enter the number of item you wish to order together (comma separated): ')
			if(self.order=='e'):
				break
			self.order=self.order.split(',')
			try:
				self.order=list(map(int,self.order))
			except ValueError:
				print('\nYou have entered an incorrect order entry. Please try again! :-)\n')
				continue
			for i in self.order:
				try:
					j=self.item_list[i-1]
				except IndexError:
					print('\nYou have entered an incorrect order entry. Please try again! :-)\n')
					z=1
					break
				self.food_set.add(self.item[j]['Food_Type'])
			if(z==1):
				continue
			if('Breads' in self.food_set or 'Curry' in self.food_set or 'Rice' in self.food_set or 'Daal' in self.food_set):
				if('Breads' in self.food_set and 'Curry' not in self.food_set and 'Daal' not in self.food_set and 'Rice' in self.food_set):
					print('You have not chosen any Curry or Daal. How will you eat the bread and rice ;-b\n')
					k=input('Do you wanna re enter the order: Y or N?')
				elif('Breads' not in self.food_set and 'Curry' in self.food_set and 'Rice' not in self.food_set):
					print('You have not chosen any Bread or Rice. How will you eat the Curry ;-b\n')
					k=input('Do you wanna re enter the order: Y or N?')
				elif('Breads' not in self.food_set and 'Daal' in self.food_set and 'Rice' not in self.food_set):
					print('You have not chosen any Bread or Rice. How will you eat the Daal ;-b\n')
					k=input('Do you wanna re enter the order: Y or N?')
				elif('Rice' in self.food_set and 'Curry' not in self.food_set and 'Daal' not in self.food_set):
					print('You have not chosen any Curry or Daal. How will you eat the Rice ;-b\n')
					k=input('Do you wanna re enter the order: Y or N?')
				elif('Breads' in self.food_set and 'Curry' not in self.food_set and 'Daal' not in self.food_set):
					print('You have not chosen any Curry or Daal. How will you eat the bread ;-b\n')
					k=input('Do you wanna re enter the order: Y or N?')
			if(k=='Y'):
				continue
			else:
				break
		self.order_count()

	def order_count(self):
		print('\nPlease enter the quantity of each item:')
		self.bill=dict()
		for i in self.order:
			n=self.item_list[i-1]
			m=int(input('%s : '%(n)))
			self.total+=m*int(self.item[n]['Price'])
			self.bill[n]={'quantity':m,'price':self.item[n]['Price']}
		self.bill_summary()

	def bill_summary(self):
		print('\nYour Order summary is as below:')
		print('Sr.No. Order Item       Quantity  Price per item  Amount')
		p=1
		for order_item in self.bill.keys():
			a=int(self.bill[order_item]['quantity'])
			b=int(self.bill[order_item]['price'])
			print('  %-5s%-17s   %-6s       %-9s   %s'%(p,order_item,a,b,a*b))
			p+=1
		print('\nYour total payable amount is : %s'%(self.total))
		print('\nBon Appetite!:-)')

c1=Hotel()
c1.print_menu()
