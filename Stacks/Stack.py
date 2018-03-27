# Implementation of basic Stack
# Sandeep Pathak
# Implementation of Stack Using Python List 

class Stack:

	def __init__(self):
		self.item = []    #initialized and now all the the push and pop will happen on this list.

	def isEmpty(self):
		# print(len(self.item))
		return not bool(len(self.item)) #return length converted as boolean.

	def push(self,value):
		return self.item.append(value) #append the list

	def pop(self):
		return self.item.pop()

	def peek(self):
		return self.item[-1] #return the last element from list

	def size(self):
		return len(self.item) 


# c=Stack()
# print(c.isEmpty())
# c.push("Dog")
# c.push(4)
# c.push(20)
# print(c.peek())
# print(c.size())
# print(c.item)





