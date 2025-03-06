f = open("26-j9.txt")
v, n = map(int,f.readline().split())
data = [int(x) for x in f]
data.sort(reverse=True)
b=[]
print(data)
for i in range(n):
    if sum(b)+data[i]<v:
        b.append(data[i])
    if sum(b)+data[-i-1]<v:
        b.append(data[-i-1])
print(len(b),b[-1])
