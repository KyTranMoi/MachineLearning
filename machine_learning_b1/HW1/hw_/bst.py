from collections import deque


class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# 1. Thêm một node trên cây BST
def insert(node, key):

    if node == None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)

    return node


#2. Đếm node lá và in ra các node lá

def count_leaves(node, list_leaves):

    if node != None:
        if node.left == None and node.right == None:
            list_leaves.append(node)
        
        count_leaves(node.left, list_leaves)
        count_leaves(node.right, list_leaves)


#3. Đếm node 1 con và in ra các node đó

def count_one_child(node, list_child):

    if node != None:
        if node.left == None and node.right != None:
            
            list_child.append(node)
        elif node.left != None and node.right == None:
            list_child.append(node)

        count_one_child(node.left, list_child)
        count_one_child(node.right, list_child)


#4. Đếm node 2 con và in ra các node đó

def count_two_child(node, list_child):

    if node != None:
        if node.left != None and node.right != None:
            list_child.append(node)

        count_two_child(node.left, list_child)
        count_two_child(node.right, list_child)


#5. Chiều cao của cây
        
def tree_height(node):
    if node is None:
        return 0
    else:
        left_height = tree_height(node.left)
        right_height = tree_height(node.right)

        return max(left_height, right_height) + 1
        

#6. Duyệt cây theo từng tầng

def browse_by_floor(node):
    if node is None:
        return []

    result = []
    q = [node]

    while q:
        current_node = q.pop(-1)
        result.append(current_node.key)

        if current_node.left != None:
            q.append(current_node.left)
        if current_node.right != None:
            q.append(current_node.right)

    return result


# 7.BFT – Duyệt theo chiều rộng
def BFS(node):
    if node is None:
        return []

    result = []
    queue = deque([node])

    while queue:
        current_node = queue.popleft()
        result.append(current_node.key)

        if current_node.left != None:
            queue.append(current_node.left)
        if current_node.right != None:
            queue.append(current_node.right)

    return result

#8.Duyệt cây theo NLR, LRN và LNR dùng đệ quy

def NLR(node):
    if node != None:
        print(node.key, end=' ->')
        NLR(node.left)
        NLR(node.right)

def LRN(node):
    if node is not None:
        LRN(node.left)
        LRN(node.right)
        print(node.key, end=' ->')

def LNR(node):
    if node is not None:
        LNR(node.left)
        print(node.key, end=' ->')
        LNR(node.right)


#9. Khử đệ quy của NLR
def NLR_recursion(node):
    result = []
    stack = [node]

    while stack:

        current_node = stack.pop()
        
        result.append(current_node.key)
        if current_node.right!= None:
            stack.append(current_node.right)
        if current_node.left != None:
            stack.append(current_node.left)

    return result

#10. Khử đệ quy BFT

def iterative_breadth_first_traversal(root):
    result = []
    queue = deque([root])

    while queue:
        current_node = queue.popleft()
        result.append(current_node.key)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return result


#11.leftMostRoot(self): trả về leftmost của Root
def leftMostRoot(node):
    current = node

    while current.left:
        current = current.left

    return current

#12.leftMost(self,el): trả về leftmost của node có giá trị  el
def leftMost(node, el):
    current = node
    ans = None
    if current.key == el: 
        ans = current
    while current.left:
        current = current.left
        if current.key == el: 
            ans = current

    return ans


#13. Xóa bởi Merge
def delete_node(node, key):
    if node is None:
        return node

    # Tìm node cần xóa
    if key < node.key:
        node.left = delete_node(node.left, key)
    elif key > node.key:
        node.right = delete_node(node.right, key)
    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left

        node.key = leftMostRoot(node.right).key
        node.right = delete_node(node.right, node.key)

    return node


#14. xóa bởi copy
def delete_node_copy(node, key):
    if node is None:
        return node

    # Tìm node cần xóa
    if key < node.key:
        node.left = delete_node_copy(node.left, key)
    elif key > node.key:
        node.right = delete_node_copy(node.right, key)
    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left

        
        tmp = leftMostRoot(node.right)
        node.key = tmp.key
        node.right = delete_node_copy(node.right, tmp.key)

    return node


if __name__ == '__main__':
    root = None

    # Thêm các node vào cây BST
    keys_to_insert = [17, 7, 5, 23, 8, 15]
    for key in keys_to_insert:
        root = insert(root, key)

    # In ra cây BST
    print("BST after insertion:")
    NLR(root)

    # Đếm và in ra các node lá
    print("\n======================")
    list_leaves = []
    count_leaves(root, list_leaves)
    print("Number of leaves:", len(list_leaves))
    print("Leaf nodes:", [node.key for node in list_leaves])

    # Đếm và in ra các node có một con
    print("\n======================")
    list_one_child = []
    count_one_child(root, list_one_child)
    print("Number of nodes with one child:", len(list_one_child))
    print("Nodes with one child:", [node.key for node in list_one_child])

    # Đếm và in ra các node có hai con
    print("\n======================")
    list_two_child = []
    count_two_child(root, list_two_child)
    print("Number of nodes with two children:", len(list_two_child))
    print("Nodes with two children:", [node.key for node in list_two_child])

    # In chiều cao của cây
    print("\n======================")
    print("Tree height:", tree_height(root))

    # In ra các node theo từng tầng
    print("\n======================")
    print("Browse by floor:", browse_by_floor(root))

    # In ra các node theo chiều rộng
    print("\n======================")
    print("BFS traversal:", BFS(root))

    # In ra các node theo NLR, LRN và LNR dùng đệ quy
    print("\n======================")
    print("NLR traversal:")
    NLR(root)

    print("\n======================")
    print("LRN traversal:")
    LRN(root)

    print("\n======================")
    print("LNR traversal:")
    LNR(root)

    # In ra kết quả sau khi khử đệ quy
    print("\n======================")
    print("NLR recursion:", NLR_recursion(root))

    # In ra leftmost của Root và của node có giá trị 7
    print("\n======================")
    print("Leftmost root:", leftMostRoot(root).key)

    print("\n======================")
    print("Leftmost node with key 7:", leftMost(root, 7).key)

    # In ra kết quả sau khi xóa node có giá trị 23 và 7
    print("\n======================")
    print("After deleting node with key 23:")
    delete_node(root, 23)
    NLR(root)

    print("\n======================")
    print("After deleting node with key 7:")
    delete_node(root, 7)
    NLR(root)
