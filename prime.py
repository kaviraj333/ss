n=int(input(""))
c=0
for i in range(2,n-1):
    if(n%i==0):
        c=c+1
if(c==0):
    print("yes")
else:
    print("no")
