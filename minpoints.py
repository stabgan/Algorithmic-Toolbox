n = int(input())
l = []
for i in range(n) :
	l.append([int(i) for i in input().split()])

l.sort(key = lambda x: x[1])
index = 0
coordinates = []

while index < n:
    curr = l[index]
    while index < n-1 and l[index+1][0] <= curr[1] :
        index += 1
    coordinates.append(curr[1])
    index += 1
print(len(coordinates))
print(' '.join([str(i) for i in coordinates]))