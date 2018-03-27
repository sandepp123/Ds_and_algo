### Reversing a String Using Stack
import Stack 
import sys
string = sys.argv[1]
c= Stack.Stack()
for i in string:
	c.push(i)

t = ""
while not c.isEmpty():
	t+=c.pop()
print(t)
	

