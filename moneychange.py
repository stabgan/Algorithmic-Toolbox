c = 0
n = int(input())
while(n!=0) :
	if n<5 :
		c += n
		break
	if n<10 :
		c += n//5
		n = n%5
	else :
		c += n//10
		n = n%10

print(c)