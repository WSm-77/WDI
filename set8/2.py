import functions as fun

################################################################
# 2. Funkcja, która sprawdza czy dana liczba należy do drzewa. #
################################################################

###########	recursively	###########

def tree_member_rek(ptr: fun.Node, val: int) -> bool:
	if ptr == None:
		return False
	
	if ptr.val == val:
		return True
	
	return tree_member_rek(ptr.left, val) or tree_member_rek(ptr.right, val)

###########	iteratively	###########

def tree_member_it(ptr: fun.Node, val: int) -> bool:
	stack = fun.deque()

	if ptr == None:
		return False
	
	stack.append(ptr)

	while stack:
		current_node = stack.pop()
		if current_node.val == val:
			return True
		
		if current_node.left != None:
			stack.append(current_node.left)

		if current_node.right != None:
			stack.append(current_node.right)
	#end while
	return False

if __name__ == "__main__":
	my_list = [fun.randint(1,20) for _ in range(fun.randint(8, 15))]
	print("list:")
	print(*my_list, sep=" ", end="\n\n")
	root = fun.list_to_BST(my_list)
	member = fun.randint(1, 20)

	# member recursively
	print(f"is {member} a member? {tree_member_rek(root, member)}\t(rek)")
		
	# # member iteratively
	print(f"is {member} a member? {tree_member_it(root, member)}\t(it)")
