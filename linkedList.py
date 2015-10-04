class Node:

	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
		self.next_node = new_next

class linkedList(object):

	def __init__(self, head=None):
		self.head = head

	def insertFront(self, data):
		newNode = Node(data)
		newNode.set_next(self.head)
		self.head = newNode

	def insertBack(self, data):
		newNode = Node(data)

		if(self.size() == 0):
			self.head = newNode
			return

		curr = self.head

		while curr.get_next():
			curr = curr.get_next()

		curr.set_next(newNode)

	#Helper function to insert a node into a sorted position
	def insert(self, data):
		curr = self.head
		if curr is None:
			newNode = Node(data)
			self.head = newNode
			return

		elif curr.get_data() > data:
			newNode = Node(data)
			newNode.set_next(curr)
			self.head = newNode
			return

		while curr.get_next() is not None:
			if curr.get_next().data > data:
				break
			curr = curr.get_next()
		newNode = Node(data)
		newNode.set_next(curr.get_next())
		curr.set_next(newNode)


	def size(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.get_next()
		return count

	def printHelp(self, curr):
		if(curr == self.head):
			print "<",

		print curr.get_data(),

		if(curr.get_next() != None):
			return linkedList.printHelp(self, curr.get_next())
		else:
			print ">"

		return

	def printList(self):
		self.printHelp(self.head)

	def __average(self, curr, total):
		if(curr.get_next() is None):
			total += curr.get_data()
			return total/self.size()
		total += curr.get_data()
		return linkedList.__average(self, curr.get_next(), total)

	def average(self):
		return self.__average(self.head, 0)

	def median(self):
		midpoint = self.size()/2 - 1
		curr = self.head

		while midpoint > 0:
			curr = curr.get_next()
			midpoint -= 1

		if self.size() % 2 is 0:
			nextNode = curr.get_next().get_data()
			median = (curr.get_data() + nextNode)/2
		else:
			median = curr.get_next().get_data()

		return median


