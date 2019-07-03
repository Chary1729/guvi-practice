myinput=int(input())
temp=myinput
if(myinput==2):
  print('yes')
elif(myinput % 1 ==0 and myinput % temp==0 and myinput%2!=0 and myinput%3!=0 and myinput%4!=0):
  print('yes')
else:
  print('no')
