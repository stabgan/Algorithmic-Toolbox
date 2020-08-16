n, W = [int(i) for i in input().split()]
l = []
for i in range(n) :
	l.append([int(i) for i in input().split()])

l = [(v/w,w) for v,w in l]
l.sort(key = lambda x: x[0], reverse = True)
value = 0
for i in range(n) :
	if W > 0 :
		a = min(l[i][1],W)
		value += a*l[i][0]
		W -= a
print(value)

	