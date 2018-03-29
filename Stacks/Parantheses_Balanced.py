from Stack import  Stack
### program for checking balanced parantheses ##

container = Stack()

string = input()

x=True
def is_i_equal_to_peek(first,second):
	t="[{("
	x = "]})"
	if x.index(first) == t.index(second):
		return True
	else:
		return False 
for i in string:
	if x ==True:
		if not (i in '{}[]()'):
			
			

			pass
		else:
			if i in "[{(":				
				container.push(i)
				
			else:
				if container.isEmpty():
					print(container.item)
					x=False
					# break
				else:
					if is_i_equal_to_peek(i,container.peek()):

						print("sad")
						container.pop()
					else:
						x=False
						break



		

		

# print(container.item,s,t)			# container.pop()
if container.isEmpty() and x:
	print(x)
	print("parantheses balanced")

else:
	print("parantheses not balanced")

