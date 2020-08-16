
f = [0]*10000000
def fibo(n) :
	if n == 0 :
		return n
	elif n == 1 or n == 2 :
		f[n] = 1
		return f[n]

	if f[n] :
		return f[n]

	if n&1 :
		k = (n+1)//2
	else :
		k = n//2

	if n&1 :
		f[n] = fibo(k)**2+fibo(k-1)**2
	else :
		f[n] = (fibo(k)+2*fibo(k-1))*fibo(k)

	return f[n]

def pisano(n) :
	prev = 0
	curr = 1
	for i in range(0,n*n) :
		prev, curr = curr, (prev+curr)%n
		if prev == 0 and curr == 1 :
			return i+1

n,m = [int(i) for i in input().split()]

n = n%pisano(m)
a = fibo(n)%m
print(a)