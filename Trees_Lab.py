# Given the following array representation of a binary search tree:
#
#
# Array = [15, 10, 20, 8, 12, 17, 25, 6, 9]
#
# Do the following:
# 1) Write python code to implement this binary search tree.
# Below is a link to an example implementation:

"""
Array Represented as a Tree

         15
       /    \
     10      20
    /  \    /  \
   8   12  17  25
  / \
 6   9

"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class BinaryTree:
    def __init__(self, root_val=None):
        self.root = TreeNode(root_val) if root_val is not None else None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
            print(f"{val} is inserted as the root")
        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
                print(f"{val} is inserted to the left of {node.val}")
            else:
                self._insert(node.left, val)
        elif val > node.val:
            if node.right is None:
                node.right = TreeNode(val)
                print(f"{val} is inserted to the right of {node.val}")
            else:
                self._insert(node.right, val)
        else:
            print(f"{val} already exists in the tree")

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.val)
            self._inorder_traversal(node.right, result)


array = [15, 10, 20, 8, 12, 17, 25, 6, 9]

bst = BinaryTree()
for value in array:
    bst.insert(value)

print("In-order traversal of the BST:", bst.inorder_traversal())


# 2) Write python code to print out the  nodes of the tree using
#         (a) Inorder traversal
#         (b) Preorder traversal
#         (c) Postorder traversal


def pre_order(node):
    """Pre-order traversal: Root -> Left -> Right"""
    if not node:
        return
    print(node.val, end=" ")
    pre_order(node.left)
    pre_order(node.right)

def in_order(node):
    """In-order traversal: Left -> Root -> Right"""
    if not node:
        return
    in_order(node.left)
    print(node.val, end=" ")
    in_order(node.right)

def post_order(node):
    """Post-order traversal: Left -> Right -> Root"""
    if not node:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.val, end=" ")

print("In-order Traversal:")
in_order(bst.root)
print("\nPre-order Traversal:")
pre_order(bst.root)
print("\nPost-order Traversal:")
post_order(bst.root)


# 3)  Write Python code to search and print out the path to the following nodes:
#         (a) 12
#         (b) 25
#         (c) 6

"""
Path to 12: 15 -> 10 -> 12
Path to 25: 15 -> 20 -> 25
Path to 6: 15 -> 10 -> 8 -> 6
"""

class BinaryTreeSearch:
    def __init__(self, root):
        self.root = root

    def search_path(self, target):
        """Find and print the path to the target node."""
        path = []
        found = self._search(self.root, target, path)
        if found:
            print(f"Path to {target}: {' -> '.join(map(str, path))}")
        else:
            print(f"Node {target} not found in the tree.")

    def _search(self, node, target, path):
        """Recursive helper function to find the path."""
        if not node:
            return False

        path.append(node.val)

        if node.val == target:
            return True

        if target < node.val and self._search(node.left, target, path):
            return True

        if target > node.val and self._search(node.right, target, path):
            return True

        path.pop()
        return False

search_tree = BinaryTreeSearch(bst.root)

print()
search_tree.search_path(12)
search_tree.search_path(25)
search_tree.search_path(6)


# 4) Write python code to print out the maximum and minimum values,
# respectively, in the binary search tree.

class BinaryTreeMinMax:
    def __init__(self, root):
        self.root = root

    def find_min(self):
        """Find the minimum value in the binary search tree."""
        if not self.root:
            print("The tree is empty.")
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.val

    def find_max(self):
        """Find the maximum value in the binary search tree."""
        if not self.root:
            print("The tree is empty.")
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.val

min_max_finder = BinaryTreeMinMax(bst.root)

min_value = min_max_finder.find_min()
max_value = min_max_finder.find_max()

print(f"Minimum value in the BST: {min_value}")
print(f"Maximum value in the BST: {max_value}")

