n=int(input(""))
a=n
s=0
while(n>0):
    r=n%10
    s=s+r*r*r
    n=n//10
if(a==s):
    print("yes")
else:
    print("no")