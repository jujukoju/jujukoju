class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def copy_tree(node):
    if node is None:
        return None

    new_node = TreeNode(node.value)

    new_node.left = copy_tree(node.left)
    new_node.right = copy_tree(node.right)

    return new_node

def print_tree(node):
    if node is not None:
        print_tree(node.left)
        print(node.value, end=' ')
        print_tree(node.right)

if __name__ == "__main__":
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("Original tree (in-order traversal):")
    print_tree(root)
    print()

    copied_tree_root = copy_tree(root)

    print("Copied tree (in-order traversal):")
    print_tree(copied_tree_root)
    print()
