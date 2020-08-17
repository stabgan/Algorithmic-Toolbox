from itertools import permutations
n = int(input())
l = [int(i) for i in input().split()]
nums = []
for i in permutations(l,n) :
	nums.append(int(''.join([str(j) for j in i])))
print(max(nums))