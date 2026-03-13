import math

class GameNode:
    def __init__(self, name, value=None, children=None):
        self.name = name
        self.value = value  # Leaf nodes have values
        self.children = children or []  # Internal nodes have children
        self.best_child = None
        self.final_value = None


def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player, path=""):
    """
    Alpha-Beta pruning that returns optimal value and path
    """
    current_path = path + " -> " + node.name if path else node.name
    
    # Leaf node or terminal state
    if depth == 0 or not node.children:
        print(f"{current_path} = {node.value}")
        return node.value, [node.name]
    
    if maximizing_player:
        best_value = -math.inf
        best_path = []
        
        print(f"\n{current_path} (MAX, α={alpha}, β={beta})")
        
        for child in node.children:
            value, child_path = alpha_beta_pruning(child, depth-1, alpha, beta, False, current_path)
            
            if value > best_value:
                best_value = value
                best_path = [node.name] + child_path
                node.best_child = child
            
            alpha = max(alpha, value)
            
            # Prune
            if beta <= alpha:
                print(f"  ✂️ PRUNE at {child.name} (β={beta} ≤ α={alpha})")
                break
        
        node.final_value = best_value
        print(f"  → Best at {node.name}: {best_value}")
        return best_value, best_path
    
    else:  # Minimizing player
        best_value = math.inf
        best_path = []
        
        print(f"\n{current_path} (MIN, α={alpha}, β={beta})")
        
        for child in node.children:
            value, child_path = alpha_beta_pruning(child, depth-1, alpha, beta, True, current_path)
            
            if value < best_value:
                best_value = value
                best_path = [node.name] + child_path
                node.best_child = child
            
            beta = min(beta, value)
            
            # Prune
            if beta <= alpha:
                print(f"  ✂️ PRUNE at {child.name} (β={beta} ≤ α={alpha})")
                break
        
        node.final_value = best_value
        print(f"  → Best at {node.name}: {best_value}")
        return best_value, best_path


def create_sample_tree():
    """Create a sample game tree for demonstration"""
    
    # Leaf nodes (terminal positions)
    l1 = GameNode("L1", value=3)
    l2 = GameNode("L2", value=5)
    l3 = GameNode("L3", value=2)
    l4 = GameNode("L4", value=9)
    l5 = GameNode("L5", value=0)
    l6 = GameNode("L6", value=7)
    l7 = GameNode("L7", value=4)
    l8 = GameNode("L8", value=1)
    l9 = GameNode("L9", value=8)
    l10 = GameNode("L10", value=6)
    
    # Level 2 nodes (MIN nodes)
    d1 = GameNode("D1", children=[l1, l2, l3])
    d2 = GameNode("D2", children=[l4, l5, l6])
    d3 = GameNode("D3", children=[l7, l8])
    d4 = GameNode("D4", children=[l9, l10])
    
    # Level 1 nodes (MAX nodes)
    c1 = GameNode("C1", children=[d1, d2])
    c2 = GameNode("C2", children=[d3, d4])
    
    # Root node (MAX)
    root = GameNode("ROOT", children=[c1, c2])
    
    return root


def create_tic_tac_toe_tree():
    """Create a simplified Tic-Tac-Toe like tree"""
    
    # Leaf nodes (terminal values from perspective of root player X)
    # Higher values are good for X, lower values are good for O
    l1 = GameNode("Leaf1", value=10)   # X wins
    l2 = GameNode("Leaf2", value=-10)  # O wins
    l3 = GameNode("Leaf3", value=0)    # Draw
    l4 = GameNode("Leaf4", value=10)   # X wins
    l5 = GameNode("Leaf5", value=-10)  # O wins
    l6 = GameNode("Leaf6", value=0)    # Draw
    l7 = GameNode("Leaf7", value=10)   # X wins
    l8 = GameNode("Leaf8", value=-10)  # O wins
    l9 = GameNode("Leaf9", value=5)    # Advantage X
    l10 = GameNode("Leaf10", value=-5) # Advantage O
    l11 = GameNode("Leaf11", value=2)  # Slight X
    l12 = GameNode("Leaf12", value=-2) # Slight O
    
    # Level 3 (O's moves)
    o1 = GameNode("O1", children=[l1, l2, l3])
    o2 = GameNode("O2", children=[l4, l5, l6])
    o3 = GameNode("O3", children=[l7, l8])
    o4 = GameNode("O4", children=[l9, l10])
    o5 = GameNode("O5", children=[l11, l12])
    
    # Level 2 (X's moves)
    x1 = GameNode("X1", children=[o1, o2])
    x2 = GameNode("X2", children=[o3, o4, o5])
    
    # Root (X's turn)
    root = GameNode("ROOT", children=[x1, x2])
    
    return root


def print_tree(node, level=0, prefix="Root: "):
    """Print the game tree structure"""
    indent = "  " * level
    if node.children:
        print(f"{indent}{prefix}{node.name} (value: {node.final_value if node.final_value is not None else '?'})")
        for i, child in enumerate(node.children):
            is_last = i == len(node.children) - 1
            new_prefix = "└─ " if is_last else "├─ "
            print_tree(child, level + 1, new_prefix)
    else:
        print(f"{indent}{prefix}{node.name} = {node.value}")


def show_optimal_path(root, optimal_value, optimal_path):
    """Display the optimal path"""
    print("\n" + "="*60)
    print("📊 RESULTS")
    print("="*60)
    print(f"\n🎯 OPTIMAL VALUE: {optimal_value}")
    print(f"\n🛣️  OPTIMAL PATH:")
    
    for i, node_name in enumerate(optimal_path):
        if i == 0:
            print(f"    Start: {node_name}")
        elif i == len(optimal_path) - 1:
            print(f"    Leaf: {node_name}")
        else:
            print(f"    → {node_name}")
    
    print("\n" + "="*60)


def demonstrate_tree(tree_type="sample"):
    """Demonstrate alpha-beta pruning on a tree"""
    
    print("\n" + "="*60)
    print("🌳 ALPHA-BETA PRUNING TREE SEARCH")
    print("="*60)
    
    if tree_type == "sample":
        print("\n📋 Sample Game Tree Structure:")
        root = create_sample_tree()
    else:
        print("\n📋 Tic-Tac-Toe Simplified Tree:")
        root = create_tic_tac_toe_tree()
    
    print_tree(root)
    
    print("\n" + "="*60)
    print("🔍 SEARCH PROCESS")
    print("="*60)
    
    # Run alpha-beta pruning
    optimal_value, optimal_path = alpha_beta_pruning(
        root, 
        depth=4, 
        alpha=-math.inf, 
        beta=math.inf, 
        maximizing_player=True
    )
    
    # Show results
    show_optimal_path(root, optimal_value, optimal_path)
    
    # Show final tree with computed values
    print("\n📊 Tree with computed values:")
    print_tree(root)
    
    return optimal_value, optimal_path


def simple_example():
    """A very simple tree example"""
    
    print("\n" + "="*60)
    print("🔰 SIMPLE TREE EXAMPLE")
    print("="*60)
    
    # Create a simple tree
    #        MAX
    #       /   \
    #     MIN    MIN
    #    /  \   /  \
    #   3   5  2   9
    
    leaf1 = GameNode("A", value=3)
    leaf2 = GameNode("B", value=5)
    leaf3 = GameNode("C", value=2)
    leaf4 = GameNode("D", value=9)
    
    min1 = GameNode("MIN1", children=[leaf1, leaf2])
    min2 = GameNode("MIN2", children=[leaf3, leaf4])
    
    root = GameNode("MAX", children=[min1, min2])
    
    print("\nTree structure:")
    print_tree(root)
    
    print("\n" + "="*60)
    print("🔍 SEARCH PROCESS")
    print("="*60)
    
    value, path = alpha_beta_pruning(root, 2, -math.inf, math.inf, True)
    
    show_optimal_path(root, value, path)


if __name__ == "__main__":
    while True:
        print("\n" + "="*60)
        print("🎯 OPTIMAL VALUE & PATH FINDER")
        print("="*60)
        print("\nChoose an option:")
        print("  1. Simple tree example")
        print("  2. Sample game tree")
        print("  3. Tic-Tac-Toe simplified tree")
        print("  4. Exit")
        
        choice = input("\nEnter choice (1-4): ")
        
        if choice == '1':
            simple_example()
        elif choice == '2':
            demonstrate_tree("sample")
        elif choice == '3':
            demonstrate_tree("tictactoe")
        elif choice == '4':
            print("\n👋 Goodbye!")
            break
        else:
            print("\n❌ Invalid choice!")
        
        input("\nPress Enter to continue...")