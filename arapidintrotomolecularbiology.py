s=input()
a=0
c=0
g=0
t=0
for i in range(len(s)):
	if(s[i]=='A'):
		a=a+1
	elif(s[i]=='C'):
		c=c+1
	elif(s[i]=='G'):
		g=g+1
	elif(s[i]=='T'):
		t=t+1
print(a,end=" ")
print(c,end=" ")
print(g,end=" ")
print(t)
