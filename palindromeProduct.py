def check(int):
	x=str(int)
	l=len(x) - 1
	n=""
	while l >= 0:
		n=n+x[l]
		l=l-1
	if n==x:
		return True
	return False
set=[]
x=999
y=999
while x > 900:
	if(check(x*y)==True):
		set.append(x*y)
		y=999
		x=x-1
	elif y < 900:
		y=999
		x = x - 1
	else:
		y=y-1
set.sort(reverse=True)
print(set[0])
