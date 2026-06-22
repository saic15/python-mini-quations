a=3
b=4
c=2
big=max([a,b,c])
step=big 
while True:
    if big%a==0 and big%b==0 and big%c==0:
        break
    else:
        big=big+step
print(big)