inp=int(input())
if(inp%2==0):
  print(inp)
else:
  for i in range(2,inp):
    if(i%2==0 and inp-i<3):
      print(i)
