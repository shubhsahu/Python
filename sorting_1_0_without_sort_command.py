x=[1,0,1,1,0,1,0,1,1,1,0,1,0,1,0]
y=sum(x)
k=len(x)-y
print(y)
p=[]
for i in range(y):
	p.append(1)
for i in range(k):
	p.append(0)
print(p)

