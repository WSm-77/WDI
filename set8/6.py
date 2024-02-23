import functions as fun

#############################################################
# 6. Funkcja, która zwróci liczbę węzłów na n-tym poziomie. #
#############################################################

###########	recursively	###########

def number_of_nodes_on_nth_level_rek(ptr: fun.Node, level: int, current_level: int = 1) -> int:
	if ptr == None or current_level > level:
		return 0

	if current_level == level:
		return 1

	return number_of_nodes_on_nth_level_rek(ptr.left, level, current_level + 1) + \
		   number_of_nodes_on_nth_level_rek(ptr.right, level, current_level + 1)

###########	iteratively	###########

def number_of_nodes_on_nth_level_it(ptr: fun.Node, level: int) -> int:
	if ptr == None: 
		return 0

	cnt  = 0	
	stack = fun.deque()
	stack.append((ptr, 1))				# this stack contains tuple of node and it's level

	while stack:
		current_node, current_level = stack.pop()
		if current_level == level:
			cnt += 1
		elif current_level < level:
			if current_node.left != None:
				stack.append((current_node.left, current_level + 1))
			#end if
			if current_node.right != None:
				stack.append((current_node.right, current_level + 1))
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
	list_of_correct_answers = [[1,2,3],
							   [1,1,1],
							   [1,0,0],
							   [1,2,4]]
	
	for i in range(len(list_of_lists)):
		my_list = list_of_lists[i]
		print(f"list of nodes: {my_list}")
		root = fun.list_to_BST(my_list)
		for level in range(len(list_of_correct_answers[i])):
			correct_answer = list_of_correct_answers[i][level]
			number_of_nodes_function_rek = number_of_nodes_on_nth_level_rek(root, level + 1)			
			number_of_nodes_function_it = number_of_nodes_on_nth_level_it(root, level + 1)
			check = '\u2714' if number_of_nodes_function_rek == number_of_nodes_function_it == correct_answer else '\u2718'
			print(f"number of nodes at level {level}: {number_of_nodes_function_rek} (rek), {number_of_nodes_function_it} (it) {check}\ncorrect: {correct_answer}")
		#end for
		print()
	#end for
