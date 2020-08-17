n = int(input())
A = sorted([int(i) for i in input().split()], reverse = True)
B = sorted([int(i) for i in input().split()], reverse = True)

# d = dict(zip(sorted(A,reverse = True),sorted(B, reverse = True)))
# s = 0
# for a,b in d.items() :
# 	s += a*b
s = 0
for i in range(n) :
	s += A[i]*B[i]

print(s)
