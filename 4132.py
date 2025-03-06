f = open("26-56.txt")
v, k, n = map(int, f.readline().split())
a = [v]*k
data = [int(x) for x in f]
data.sort(reverse=True)
c=0
local_finder=[]
f=0
for i in range(n):
    if f>7:
        f-=k
    for j in range(f,k):
        if data[i] <= a[j]:
            a[j]-=data[i]
            f += 1
            break
        else:
            continue
    else:
        local_finder.append(data[i])
print(sum(local_finder),len(local_finder))
