import functions as fun

####################################################
# 5. Funkcja, która zwróci liczbę liści w drzewie. #
####################################################

###########	recursively	###########

def number_of_leaves_rek(root: fun.Node) -> int:
	if root == None: 
		return 0
	
	if root.left == None and root.right == None:
		return 1

	def rek(ptr: fun.Node) -> int:
		if ptr == None:
			return 0
		
		if ptr.left == ptr.right == None:			# this node is a leaf
			return 1
		
		return rek(ptr.left) + rek(ptr.right)
	#end def

	leaves = rek(root)

	return leaves if root.right != None and root.left != None else leaves + 1

###########	iteratively	###########

def number_of_leaves_it(root: fun.Node) -> int:
	if root == None:
		return 0
	
	if root.left == root.right == None:
		return 1
	
	stack = fun.deque()
	stack.append(root)
	leaves = 0 if root.left != None and root.right != None else 1

	while stack:
		current_node = stack.pop()
		if current_node.left == current_node.right == None:
			leaves += 1
		else:
			if current_node.left != None:
				stack.append(current_node.left)
			#end if
			if current_node.right != None:
				stack.append(current_node.right)
			#end if
		#end if
	#end while
	return leaves

if __name__ == "__main__":
	list_of_lists = [[5,2,1,4,3,6,7],
					 [1,2,3,4,5,6,7],
					 [1],
					 [4,2,1,3,6,5,7]]
	
	# number of leaves
	leaves_list = [3, 2, 1, 4]
	
	for i in range(len(list_of_lists)):
		my_list = list_of_lists[i]
		print(f"list of nodes: {my_list}")
		root = fun.list_to_BST(my_list)

		# correct number of leaves
		print(f"correct number of leaves: {leaves_list[i]}")
		# number of leaves recursively
		print(f"number of leaves: {number_of_leaves_rek(root)}\t(rek)")
			
		# number of leaves iteratively
		print(f"number of leaves: {number_of_leaves_it(root)}\t(it)")
		print()
		
		

