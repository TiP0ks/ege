f = open("26-56.txt")
v, k, n = map(int, f.readline().split())
a = [v]*k
data = [int(x) for x in f]
data.sort(reverse=True)
print(data)
c=0
local_finder=[]
for i in range(n):
    f=0
    for j in range(f,k):
        if data[i] <= a[j]:
            a[j]-=data[i]
            break
            f+=1
        else:
            continue
    else:
        local_finder.append(data[i])
print(sum(local_finder),len(local_finder))
print(local_finder)