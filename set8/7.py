import functions as fun

####################################################################
# 7. Funkcja, która zwróci liczbę węzłów mających jednego potomka. #
####################################################################

###########	recursively	###########

def number_of_nodes_with_one_child_rek(ptr: fun.Node) -> int:
	if ptr == None:
		return 0
	
	if ptr.left == None and ptr.right != None:
		return 1 + number_of_nodes_with_one_child_rek(ptr.right)
	
	if ptr.left != None and ptr.right == None:
		return 1 + number_of_nodes_with_one_child_rek(ptr.left)
	
	return number_of_nodes_with_one_child_rek(ptr.left) + number_of_nodes_with_one_child_rek(ptr.right)

###########	iteratively	###########

def number_of_nodes_with_one_child_it(ptr: fun.Node) -> int:
	if ptr == None:
		return 0
	
	cnt = 0
	stack = fun.deque()
	stack.append(ptr)

	while stack:
		current_node = stack.pop()
		if current_node.left != None:
			stack.append(current_node.left)
			if current_node.right == None:
				cnt += 1
			#end if
		#end if
		if current_node.right != None:
			stack.append(current_node.right)
			if current_node.left == None:
				cnt += 1
			#end if
		#end if
	#end while
				
	return cnt

if __name__ == "__main__":
	list_of_lists = [[5,2,1,4,3,6,7],
					 [1,2,3,4,5,6,7],
					 [1],
					 [4,2,1,3,6,5,7]]
	
	# number of leaves
	list_of_correct_answers = [2,6,0,0]
	
	for i in range(len(list_of_lists)):
		my_list = list_of_lists[i]
		print(f"list of nodes: {my_list}")
		root = fun.list_to_BST(my_list)
		correct_answer = list_of_correct_answers[i]
		number_of_nodes_function_rek = number_of_nodes_with_one_child_rek(root)			
		number_of_nodes_function_it = number_of_nodes_with_one_child_it(root)
		check = '\u2714' if number_of_nodes_function_rek == number_of_nodes_function_it == correct_answer else '\u2718'
		print(f"number of nodes with one child: {number_of_nodes_function_rek} (rek), {number_of_nodes_function_it} (it) {check}\ncorrect: {correct_answer}")
		print()
	#end for
