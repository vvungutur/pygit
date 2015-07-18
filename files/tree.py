



class binaryNode():
	def __init__(self, value = None):
		self.value = value
		self.left = None
		self.right = None

	def add(self, value):
		if value <= self.value:
			if self.left:
				self.left.add(value)
			else:
				self.left = binaryNode(value)
			
		else:
			if self.right:
				self.right.add(value)
			else:
				self.right = binaryNode(value)






class binaryTree():

	def __init__(self):
		self.root = None


	def add(self, value):
		if self.root is None:
			self.root = binaryNode(value)
		else:
			self.root.add(value)

	def contains(self, target):
		node = self.root
		while node:
			if target == node.value:
				return True
			elif target < node.value:
				node = node.left
			else:
				node = node.right
		return False

