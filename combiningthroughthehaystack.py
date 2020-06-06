s=input()
t=input()
for i in range(len(s)):
	if(s[i:i+len(t)]==t):
		print(i+1,end=" ")
print("\n")
