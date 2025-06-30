m=int(input("Enter the number of resources:"))
print("Enter the max instances of each resource:")
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
n=int(input("\nEnter the number of processes:"))
alloc=[]
for i in range(n):
    print(f"for process{i}")
    re_a=int(input())
    re_b=int(input())
    re_c=int(input())
    alloc.append([re_a,re_b,re_c])
print("\nEnter the max matrix")
max=[]
for i in range(n):
    print(f"for process{i}")
    ma_a=int(input())
    ma_b=int(input())
    ma_c=int(input())
    max.append([ma_a,ma_b,ma_c])
avail=[2,3,3]
f=[0]*n
ans=[0]*n
ind=0
for k in range(n):
    f[k]=0
need=[[0 for i in range(m)]for i in range(n)]
for i in range(n):
    for j in range(m):
        need[i][j]=max[i][j]-alloc[i][j]
y=0
for k in range(3):
    for i in range(n):
        if (f[i]==0):
            flag=0
            for j in range(m):
                if(need[i][j]>avail[j]):
                  flag=1
                  break
            if(flag==0):
                 ans[ind]=i
                 ind+=1
                 for y in range(m):
                     avail[y]+=alloc[i][y]
                     f[i]=1
print("\nFollowing is the same sequence")
for i in range(n-1):
    print("P",ans[i],"->",sep="",end="")