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
	print("\n")

def print_tree_it_sorted(ptr: fun.Node) -> None:
	if ptr == None:
		print("tree is empty")
		return
	
	midStack = fun.deque()
	leftStack = fun.deque()
	rightStack = fun.deque()
	leftStack.append(ptr)

	while True:
		while leftStack:
			currentLeftNode = leftStack.pop()
			if currentLeftNode.left == currentLeftNode.right == None:
				print(currentLeftNode.val, end=" ")
				break
			#end if
			if currentLeftNode.left != None:
				leftStack.append(currentLeftNode.left)
			#end if
			if currentLeftNode.right != None:
				rightStack.append(currentLeftNode.right)
			#end if
			midStack.append(currentLeftNode)
		#end while
		if midStack:
			currenMidNode = midStack.pop()
			print(currenMidNode.val, end=" ")
		if currenMidNode.right != None and rightStack:
			topRight = rightStack.pop()
			leftStack.append(topRight)
		#end if
		if not midStack and not leftStack and not rightStack:
			break
		#end if
	#end while
	print()
     
########### 	main 	###########

if __name__ == "__main__":
	my_list = [fun.randint(1,10) for _ in range(fun.randint(8, 15))]
	# my_list = [5,2,1,4,3,6,7]
	print("list:")
	print(*my_list, sep=" ", end="\n\n")
	root = fun.list_to_BST(my_list)
     
	# print recursively
	print("tree recursively:")
	print_tree_rek(root)
     
	# print iteratively
	print("tree iteratively:")
	print_tree_it(root)
	print("tree iteratively (sorted):")
	print_tree_it_sorted(root)