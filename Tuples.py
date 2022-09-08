N=int(input())
li=[]
n=input().split()
for i in range(N):
    li.append(int(n[i]))
t=tuple(li)
print(t)
print(hash(t))
