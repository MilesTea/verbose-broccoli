class Stack:
	def __init__(self):
		self.list = list()

	def isEmpty(self):
		if len(self.list) == 0:
			return True
		else:
			return False

	def push(self, element):
		self.list.append(element)

	def pop(self):
		return self.list.pop()

	def peek(self):
		return self.list[-1]

	def size(self):
		return len(self.list)


brackets = {
	'(': ')',
	'{': '}',
	'[': ']'
}

base_string = input('Введите строку со скобками ')
stack = Stack()
balanced = True
for element in base_string:
	if element in brackets.keys():
		stack.push(element)

	elif element in brackets.values():
		if not stack.isEmpty():
			expected_element = brackets[stack.pop()]
			if expected_element != element:
				balanced = False
				break
		else:
			balanced = False
			break

if balanced:
	print('Сбалансировано')
else:
	print('Несбалансировано')
