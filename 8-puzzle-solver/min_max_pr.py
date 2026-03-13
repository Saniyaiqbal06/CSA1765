class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.children = []

def create_tree():
    # Creating the exact tree from the image
    root = TreeNode(0)
    root.left = TreeNode(3)
    root.right = TreeNode(0)
    
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(0)
    
    root.right.left.left = TreeNode(-3)
    root.right.right.right = TreeNode(4)
    
    # Also populate children list for easier traversal
    root.children = [root.left, root.right]
    root.right.children = [root.right.left, root.right.right]
    root.right.left.children = [root.right.left.left]
    root.right.right.children = [root.right.right.right]
    
    return root

def print_tree_visual(node, prefix="", is_last=True, is_root=True):
    """
    Print the tree in a visual format showing the structure
    """
    if node is None:
        return
    
    # Print the current node
    if is_root:
        print(f"root = TreeNode({node.value})")
    else:
        connector = "└── " if is_last else "├── "
        print(prefix + connector + f"TreeNode({node.value})")
    
    # Prepare the prefix for children
    if is_root:
        child_prefix = ""
    else:
        child_prefix = prefix + ("    " if is_last else "│   ")
    
    # Print children
    children = []
    if node.left:
        children.append(("left", node.left))
    if node.right:
        children.append(("right", node.right))
    
    for i, (child_name, child_node) in enumerate(children):
        is_last_child = (i == len(children) - 1)
        if is_root:
            print(f"{child_prefix}{child_name} = TreeNode({child_node.value})")
        else:
            print(child_prefix + ("└── " if is_last_child else "├── ") + 
                  f"{child_name}: TreeNode({child_node.value})")
        
        # Recursively print grandchildren
        print_subtree(child_node, child_prefix + ("    " if is_last_child else "│   "))

def print_subtree(node, prefix):
    """
    Helper function to print subtrees
    """
    children = []
    if node.left:
        children.append(("left", node.left))
    if node.right:
        children.append(("right", node.right))
    
    for i, (child_name, child_node) in enumerate(children):
        is_last_child = (i == len(children) - 1)
        print(prefix + ("└── " if is_last_child else "├── ") + 
              f"{child_name}: TreeNode({child_node.value})")
        
        # Recursively print deeper levels
        print_subtree(child_node, prefix + ("    " if is_last_child else "│   "))

def print_tree_compact(node, level=0, position="root"):
    """
    Print the tree in a compact format showing values only
    """
    if node is None:
        return
    
    indent = "    " * level
    if level == 0:
        print(f"{indent}root: {node.value}")
    else:
        print(f"{indent}{position}: {node.value}")
    
    if node.left or node.right:
        if node.left:
            print_tree_compact(node.left, level + 1, "left")
        else:
            print(f"{indent}    left: None")
        
        if node.right:
            print_tree_compact(node.right, level + 1, "right")
        else:
            print(f"{indent}    right: None")

def print_tree_ascii(node, prefix="", is_left=True):
    """
    Print the tree in ASCII format showing the structure
    """
    if node is None:
        return
    
    print(prefix + ("├── " if not is_left else "└── ") + str(node.value))
    
    children = []
    if node.left:
        children.append(("L", node.left))
    if node.right:
        children.append(("R", node.right))
    
    for i, (marker, child) in enumerate(children):
        if i == len(children) - 1:
            print_tree_ascii(child, prefix + ("    " if is_left else "│   "), True)
        else:
            print_tree_ascii(child, prefix + ("    " if is_left else "│   "), False)

def print_tree_structure():
    """
    Print the exact tree structure as Python code
    """
    print("# Tree structure from the image")
    print("root = TreeNode(0)")
    print("root.left = TreeNode(3)")
    print("root.right = TreeNode(0)")
    print("root.right.left = TreeNode(0)")
    print("root.right.right = TreeNode(0)")
    print("root.right.left.left = TreeNode(-3)")
    print("root.right.right.right = TreeNode(4)")
    print()
    
    print("# Complete tree with all connections:")
    root = create_tree()
    
    print("\n1. Visual Tree Structure:")
    print("=" * 40)
    print_tree_visual(root)
    
    print("\n2. Compact Tree Format:")
    print("=" * 40)
    print_tree_compact(root)
    
    print("\n3. ASCII Tree Representation:")
    print("=" * 40)
    print_tree_ascii(root)

def verify_tree_structure(root):
    """
    Verify that the tree matches the given structure
    """
    print("\n4. Tree Structure Verification:")
    print("=" * 40)
    
    # Check root
    assert root.value == 0, f"Root should be 0, got {root.value}"
    print("✓ Root is 0")
    
    # Check level 1
    assert root.left.value == 3, f"Left child should be 3, got {root.left.value}"
    assert root.right.value == 0, f"Right child should be 0, got {root.right.value}"
    print("✓ Level 1: left=3, right=0")
    
    # Check level 2
    assert root.right.left.value == 0, f"Right-left should be 0, got {root.right.left.value}"
    assert root.right.right.value == 0, f"Right-right should be 0, got {root.right.right.value}"
    print("✓ Level 2: right.left=0, right.right=0")
    
    # Check level 3
    assert root.right.left.left.value == -3, f"Right-left-left should be -3, got {root.right.left.left.value}"
    assert root.right.right.right.value == 4, f"Right-right-right should be 4, got {root.right.right.right.value}"
    print("✓ Level 3: right.left.left=-3, right.right.right=4")
    
    # Check None values
    assert root.left.left is None, "Left-left should be None"
    assert root.left.right is None, "Left-right should be None"
    assert root.right.left.right is None, "Right-left-right should be None"
    assert root.right.right.left is None, "Right-right-left should be None"
    print("✓ All unspecified children are None")
    
    print("\n✓ Tree structure verified successfully!")

def print_tree_paths(node, path=""):
    """
    Print all paths from root to leaves
    """
    if node is None:
        return
    
    current_path = path + " -> " + str(node.value) if path else str(node.value)
    
    if node.left is None and node.right is None:
        print(f"Leaf path: {current_path}")
    else:
        if node.left:
            print_tree_paths(node.left, current_path)
        if node.right:
            print_tree_paths(node.right, current_path)

def main():
    print("TREE STRUCTURE FROM IMAGE")
    print("=" * 50)
    
    # Print the exact code that creates the tree
    print_tree_structure()
    
    # Create the tree
    root = create_tree()
    
    # Verify the structure
    verify_tree_structure(root)
    
    print("\n5. All Paths from Root to Leaves:")
    print("=" * 40)
    print_tree_paths(root)
    
    print("\n6. Tree Height and Statistics:")
    print("=" * 40)
    
    def get_height(node):
        if node is None:
            return 0
        return 1 + max(get_height(node.left), get_height(node.right))
    
    def count_nodes(node):
        if node is None:
            return 0
        return 1 + count_nodes(node.left) + count_nodes(node.right)
    
    def count_leaves(node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return count_leaves(node.left) + count_leaves(node.right)
    
    height = get_height(root)
    nodes = count_nodes(root)
    leaves = count_leaves(root)
    
    print(f"Tree Height: {height}")
    print(f"Total Nodes: {nodes}")
    print(f"Leaf Nodes: {leaves}")
    print(f"Internal Nodes: {nodes - leaves}")

if __name__ == "__main__":
    main()