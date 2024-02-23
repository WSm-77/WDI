import functions as fun

def print_tree_rek(ptr: fun.Node) -> None:
	if ptr == None:
		print("tree is empty")
		return
	
	def rek(ptr: fun.Node) -> None:
		if ptr == None:
			return
		
		rek(ptr.left)
		print(ptr.val, end=" ")
		rek(ptr.right)
	#end def
	
	print("tree: ", end="")
	rek(ptr)
	print()

####################################################
# 8. Funkcja, która usunie wszystkie węzły drzewa. #
####################################################

###########	recursively	###########

def remove_all_nodes_rek(ptr: fun.Node) -> fun.Node:
	def rek(ptr: fun.Node) -> None:
		if ptr == None:
			return None
		
		rek(ptr.left)
		rek(ptr.right)
		ptr.left = None
		ptr.right = None
	#end def
	rek(ptr)
	return None

if __name__ == "__main__":
	list_of_lists = [[j for j in range(1, 2*i + 1)] for i in range(1, 4 + 1)]
	
	for i in range(len(list_of_lists)):
		my_list = list_of_lists[i]
		root = fun.list_to_BST(my_list)
		print_tree_rek(root)
		root = remove_all_nodes_rek(root)
		print_tree_rek(root)
