count=0
x,y=input().split()
x=int(x)
y=int(y)
ar=[int(i) for i in input().split()]
for j in ar:
  if(j==y):
    count=count+1
print(count)
