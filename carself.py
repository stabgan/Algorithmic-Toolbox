d = int(input())
m = int(input())
n = int(input())
s = [int(i) for i in input().split()]

s.insert(0,0)
s.append(d)
n += 2

def func(d,m,n,s) :
	current = 0
	last = 0
	t = 0
	while(current < n-1) :
		last = current
		while(current < n-1) :
			if s[current+1] - s[last]<= m :
				current += 1
			else :
				break
		if last == current :
			return -1
		if current < n-1 :
			t += 1
	return t

print(func(d,m,n,s))
