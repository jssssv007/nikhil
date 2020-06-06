s=input()
t=""
def rev(s):
	return s[len(s)-1::-1]
for i in range(len(s)):
	if(s[i]=='A'):
		t=t+'T'
	elif(s[i]=='T'):
		t=t+'A'
	elif(s[i]=='C'):
		t=t+'G'
	elif(s[i]=='G'):
		t=t+'C'
print(rev(t))
