class Treenode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left_child = left
        self.right_child = right
    
    def __str__(self):
        return f"Node{self.value}"
    
    def view_child(self):
        return f"Left child: {self.left_child}, {self}, Right child: {self.right_child}"
t1 = Treenode(30)
t2 = Treenode(20)
root = Treenode(25, t2, t1)

print(root)
print(root.view_child())



#SEARCHING IN BINARY SEARCH TREE using Loop. We pass the root_node as node.
def search(value, node):
    while True:
        if node is None:
            return f"Value not found."
        elif node.value == value:
            return f"Value is in node: {node}"
        elif value < node.value:
                node = node.left_child
        else:
            node = node.righ_child

#SEARCHING IN BINARY TREE using Recursion.
    def search2(value, node):
    #First base case: if node is None
        if node is None:
            return None
    #Second base case: if we found the value
        elif node.value == value:
            return node
        elif value < node.value:
                search2(value, node.left_child)
        else:
            search2(value, node.right_child)




#INSERTION: Insertion of node using loop.
def insert(value, node):
    while True:
        if value < node.value:
            if node.left_child is None:
                new_node = Treenode(value)
                node.left_child = new_node
                return f"Inserted as left child in node: {node}"
            else:
                node = node.left_child
        elif value > node.value:
            if node.right_child is None:
                new_node = Treenode(value)
                node.right_child = new_node
                return f"Inserted as right child in node: {node}"
            else: node = node.right_child
        else:
            return f"Value already exist at the node: {node}"

#INSERTION: Insertion of node using recursion.
def insert2(value, node):
    if value < node.value:
    #In recursion, base case is the case after which occurs then we don't need to make any more recursive call.
    #Here it's one of the base case.
        if node.left_child is None:
            new_node = Treenode(value)
            node.left_child = new_node
            return node
        else:
            insert2(value, node.left_child)
    elif value > node.value:
        if node.right_child is None:
            new_node = Treenode(value)
            node.right_child = new_node
            return node
        else:
            insert2(value, node.right_child)
    else:
        return node




#TRAVERSAL: Inorder traversal.
def traverse(node):
    if node is None:
        return
    traverse(node.left_child)
    print(node)
    traverse(node.right_child)

print("TRAVERSING....")
traverse(root)

#DELETION. using recursion.

'''
def delete(value, node):
    if node is None:
        return None
    elif value < node.value:
        node.left_child = delete(value, node.left_child)
    elif value > node.value:
        node = node.right_child
    elif value == node.value:
        if node.left_child == None and node.right_child == None:
            node.value = None
        elif node.left_child or node.right_child:
            try:
                node = node.left_child
                node.left_child = None
            except:
                node = node.right_child
                node.right_child = None
        elif node.left_child and node.right_child:
            suc_node = node.righ_child.left_child while
            
            '''
