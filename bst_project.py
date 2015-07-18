from tree import binaryTree


def balancedTree(ordered):
	
	bt = binaryTree()


	addRange(bt, ordered, 0, len(ordered) - 1)

	return bt

def addRange(bt, ordered, low, high):


	if low <= high:
		mid = (low + high)/2

		bt.add(ordered[mid])
		addRange(bt, ordered, low, mid - 1)
		addRange(bt, ordered, mid + 1, high)
