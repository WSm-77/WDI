import functions as fun

###########################################
# 1. Funkcja wypisującą zawartość drzewa. #
###########################################
        
###########	recursively	###########

def print_tree_rek(ptr: fun.Node) -> None:
	def rek(ptr: fun.Node) -> None:
		if ptr == None:
			return
		
		rek(ptr.left)
		print(ptr.val, end=" ")
		rek(ptr.right)
	#end def
	
	rek(ptr)
	print("\n")

###########	iteratively	###########
    
def print_tree_it(ptr: fun.Node) -> None:
	stack = fun.deque()

	if ptr == None:
		return
	
	stack.append(ptr)

	while stack: 						# checking if stack is not empty
		current_node = stack.pop()
		print(current_node.val, end=" ")
		if current_node.left != None:
			stack.append(current_node.left)
		#end if
		if current_node.right != None:
			stack.append(current_node.right)
		#end if
	#end while
	print()
     
########### 	main 	###########

if __name__ == "__main__":
	my_list = [fun.randint(1,10) for _ in range(fun.randint(8, 15))]
	print("list:")
	print(*my_list, sep=" ", end="\n\n")
	root = fun.list_to_BST(my_list)
     
	# print recursively
	print("tree recursively:")
	print_tree_rek(root)
     
	# print iteratively
	print("tree iteratively:")
	print_tree_it(root)