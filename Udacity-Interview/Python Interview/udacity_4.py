"""
Find the least common ancestor between two nodes on a binary search tree.
The least common ancestor is the farthest node from the root that is an ancestor
of both nodes. For example, the root is a common ancestor of all nodes on the
tree, but if both nodes are descendents of the root's left child, then that left
child might be the lowest common ancestor. You can assume that both nodes are in
the tree, and the tree itself adheres to all BST properties. The function
definition should look like question4(T, r, n1, n2), where Tis the tree
represented as a matrix, where the index of the list is equal to the integer
stored in that node and a 1 represents a child node, r is a non-negative integer
representing the root, and n1 and n2 are non-negative integers representing the
two nodes in no particular order. For example, one test case might be ...

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
"""
head = None

class Node(object):
  def __init__(self, data):
    self.data = data
    self.right = None
    self.left = None

# Function to insert a new node at the beginning
def push_right(node, new_data):
    new_node = Node(new_data)
    node.right = new_node
    return new_node

# Function to insert a new node at the beginning
def push_left(node, new_data):
    new_node = Node(new_data)
    node.left = new_node
    return new_node

# Function to find LCA of n1 and n2. The function assumes
# that both n1 and n2 are present in BST
def lca(head, n1, n2):
    # Base Case
    if head is None:
        return None

    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if(head.data > n1 and head.data > n2):
        return lca(head.left, n1, n2)

    # If both n1 and n2 are greater than root, then LCA
    # lies in right
    if(head.data < n1 and head.data < n2):
        return lca(head.right, n1, n2)

    return head.data


def question4(mat, root, n1, n2):
    global head
    # Make BST
    head = Node(root)
    head.left, head.right = None, None
    node_value = 0
    tmp_right, tmp_left = None, None
    node_list = []
    for elem in mat[root]:
        if elem:
            if(node_value>root):
                node_list.append(push_right(head, node_value))
            else:
                node_list.append(push_left(head, node_value))
        node_value += 1

    tmp_node = node_list.pop(0)
    while tmp_node != None:
        node_value = 0
        for elem in mat[tmp_node.data]:
            if elem:
                if(node_value>tmp_node.data):
                    node_list.append(push_right(tmp_node, node_value))
                else:
                    node_list.append(push_left(tmp_node, node_value))
            node_value += 1
        if node_list == []:
            break
        else:
            tmp_node = node_list.pop(0)

    return lca(head, n1, n2)

# Main program
def main():
    global head

    print question4([[0, 0, 0, 0, 0],
                     [1, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 1, 0, 0, 1],
                     [0, 0, 0, 0, 0]],
                     3, 1, 2)

if __name__ == '__main__':
    main()
