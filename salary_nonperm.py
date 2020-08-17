n = int(input())
l = [int(i) for i in input().split()]

n = len(str(max(l)))+1

l2 = list(map(int,[(str(i)*64)[:n+1] for i in l]))
d = list(zip(l,l2))
d.sort(reverse = True, key = lambda x: x[1])

print("".join([str(i[0]) for i in d]))
