x=int(input())
for i in range(x):
    n=int(input())
    m=list(map(int,input().split()))
    k=sorted(m)
    if m==k:
        print("0")
    else:
        print(k[-1]-k[0])
