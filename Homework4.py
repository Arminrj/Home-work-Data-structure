def pre_order(tree, node):
    order_list = []
    stack = [node]  # We use a stack to keep track of nodes

    while stack:
        current_node = stack.pop()  # Pop the top node from the stack
        order_list.append(current_node.label)  # Add the label of the current node to the order list
        
        # Add the right sibling to the stack
        if current_node.right_sibling is not None:
            stack.append(current_node.right_sibling)
        
        # Add the left child to the stack
        if current_node.left_child is not None:
            stack.append(current_node.left_child)
    
    return order_list

Tree.pre_order = pre_order
print(tree.pre_order(tree.root))