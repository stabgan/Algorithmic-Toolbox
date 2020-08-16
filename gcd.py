def gcd(a,b):
	while b!=0 :
		c = b
		b = a%b
		a = c
	return a

n = [int(i) for i in input().split()]
print(gcd(n[0],n[1]))
