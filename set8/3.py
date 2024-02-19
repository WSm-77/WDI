import functions as fun

############################################################
# 3. Funkcja, która zwróci rozmiar drzewa (liczbę węzłów). #
############################################################

###########	recursively	###########

def size_rek(ptr: fun.Node) -> int:
	if ptr == None:
		return 0
	
	return 1 + size_rek(ptr.left) + size_rek(ptr.right)

###########	iteratively	###########

def size_it(ptr: fun.Node) -> int:
	if ptr == None:
		return 0
	
	size = 0
	stack = fun.deque()
	stack.append(ptr)

	while stack:
		current_node = stack.pop()
		size += 1
		if current_node.left != None:
			stack.append(current_node.left)
		#end if
		if current_node.right != None:
			stack.append(current_node.right)
		#end if
	#end while
	
	return size

if __name__ == "__main__":
	my_list = [fun.randint(1,20) for _ in range(fun.randint(8, 15))]
	print("list:")
	print(*my_list, sep=" ", end="\n\n")
	root = fun.list_to_BST(my_list)

	# list length
	list_len = len(my_list)
	print(f"list len: {list_len}")

	# size recursively
	print(f"tree size: {size_rek(root)}\t(rek)")
		
	# size iteratively
	print(f"tree size: {size_it(root)}\t(it)")
