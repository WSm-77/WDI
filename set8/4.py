import functions as fun

##############################################################
# 4. Funkcja, która zwróci wysokość drzewa (ilość poziomów). #
##############################################################

###########	recursively	###########

def height_rek(ptr: fun.Node) -> int:
	if ptr == None:
		return 0

	return 1 + max(height_rek(ptr.left), height_rek(ptr.right))

###########	iteratively	###########

def height_it(ptr: fun.Node) -> int:
	if ptr == None:
		return 0

	height = 0	
	stack = fun.deque()			# this stack will contain tuple of nodes and these nodes' level
	stack.append((ptr, 1))
	
	while stack:
		current_node, level = stack.pop()
		height = max(height, level)

		if current_node.left != None:
			stack.append((current_node.left, level + 1))
		#end if
		if current_node.right != None:
			stack.append((current_node.right, level + 1))
		#end if
	#end while
	
	return height

if __name__ == "__main__":
	root = fun.Node(0)
	ptr = root
	left_size = fun.randint(1, 10)
	for i in range(1, left_size + 1):
		ptr.left = fun.Node(i)
		ptr = ptr.left
	#end for
	ptr = root
	right_size = fun.randint(1, 10)
	for j in range(1, right_size + 1):
		ptr.right = fun.Node(j*10)
		ptr = ptr.right
	#end for
		
	# size of subtrees
	print(f"size of left subtree:\t{left_size}")
	print(f"size of right subtree:\t{right_size}")

	# size recursively
	print(f"tree size: {height_rek(root)}\t(rek)")
		
	# size iteratively
	print(f"tree size: {height_it(root)}\t(it)")