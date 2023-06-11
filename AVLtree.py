"""A class representing a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type key: int or None
    @param key: key of your node
    @type value: any
    @param value: data of your node
    """

    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1
        self.size = 0

    """returns the key

    @rtype: int or None
    @returns: the key of self, None if the node is virtual
    """

    def get_key(self):
        return self.key

    """returns the value

    @rtype: any
    @returns: the value of self, None if the node is virtual
    """

    def get_value(self):
        return self.value

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child (if self is virtual)
    """

    def get_left(self):
        return self.left

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child (if self is virtual)
    """

    def get_right(self):
        return self.right

    # def get_blance_factor(self):
    #     return self.left.height - self.right.height

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    def get_parent(self):
        return self.parent

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    def get_height(self):
        return self.height

    """returns the size of the subtree

    @rtype: int
    @returns: the size of the subtree of self, 0 if the node is virtual
    """

    def get_size(self):
        return self.size

    """sets key

    @type key: int or None
    @param key: key
    """

    def set_key(self, key):
        self.key = key
        return None

    """sets value

    @type value: any
    @param value: data
    """

    def set_value(self, value):
        self.value = value
        return None

    """sets left child

    @type node: AVLNode
    @param node: a node
    """

    def set_left(self, node):
        self.left = node
        return None

    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    def set_right(self, node):
        self.right = node
        return None

    """sets parent

    @type node: AVLNode
    @param node: a node
    """

    def set_parent(self, node):
        self.parent = node
        return None

    """sets the height of the node

    @type h: int
    @param h: the height
    """

    def set_height(self, h):
        self.height = h
        return None

    def balance_height(self):
        tmp = self.height
        self.height = max(self.left.height, self.right.height) + 1
        if tmp == self.height:
            return False
        return True

    """sets the size of node

    @type s: int
    @param s: the size
    """

    def set_size(self, s):
        self.size = s
        return None

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def is_real_node(self):
        return self.key is not None


"""
A class implementing an AVL tree.
"""


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.root = AVLNode(None, None)

    # add your fields here

    def print_tree(self):
        for i in (printree(self.root)):
            print(i)

    """searches for a value in the dictionary corresponding to the key

    @type key: int
    @param key: a key to be searched
    @rtype: any
    @returns: the value corresponding to key.
    """

    def search(self, key):
        node = self.root

        # Traverse the tree until a leaf node is reached
        while node.is_real_node():
            if node.key == key:  # If the current node has the desired key
                return node
            elif node.key < key:  # If the key is greater, move to the right subtree
                node = node.get_right()
            else:  # If the key is smaller, move to the left subtree
                node = node.get_left()

        # If the key is not found, return None
        return None

    """inserts val at position i in the dictionary

    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: any
    @param val: the value of the item
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def insert(self, key, val):
        node = self.root

        # Check if the tree is empty
        if node.key is None:
            # Create a new root node with the given key and value
            self.root = AVLNode(key, val)
            node = self.root
            node.size = 1
            node.height = 0
        else:
            # Traverse the tree to find the appropriate position for insertion
            while node.key is not None:
                node.size += 1
                if node.key < key:
                    node = node.right
                else:
                    node = node.left
            # Update the size and height of the new node
            node.size += 1
            node.height = 0
            node.key, node.value = key, val

        # Create empty left and right child nodes for the new node
        node.left = AVLNode(None, None)
        node.right = AVLNode(None, None)
        node.right.parent = node.left.parent = node

        # Rebalance the tree starting from the parent of the new node
        number_of_balances = self.rebalance_tree(node.parent, True)

        # Return the number of balance operations performed
        return number_of_balances

    """adjusts the height of the node
    @type node: AVLNode
    @param node: a node
    @rtype: int
    """

    def set_heights(self, node):
        while node is not None:
            node.height = max(node.right.height, node.left.height) + 1
            node = node.parent

    """adjusts the size of the node
    @type node: AVLNode
    @param node: a node
    @rtype: int
    """

    def set_sizes(self, node):
        while node is not None:
            node.size = node.left.size + node.right.size + 1
            node = node.parent

    """deletes node from the dictionary

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, node):
        parent = node.parent

        # Check if the node is a leaf node
        if node.size == 1:
            self.delete_leaf(node)
            return self.rebalance_tree(parent, False)
        # Check if the node has one child
        elif node.size == 2:
            self.delete_node_with_one_child(node)
            return self.rebalance_tree(parent, False)
        else:
            # Find the successor of the node
            successor = self.find_successor(node)

            # Check if the successor has a right child
            if successor.right.key is not None:
                self.delete_node_with_one_child(successor)
                # Replace the node's key and value with the successor's key and value
                node.key, node.value = successor.key, successor.value
                return self.rebalance_tree(successor.parent, False)
            else:
                self.delete_leaf(successor)
                # Replace the node's key and value with the successor's key and value
                node.key, node.value = successor.key, successor.value
                return self.rebalance_tree(successor.parent, False)

    """findes the successor of the node
        @type node: AVLNode
        @param node: a node
        @rtype: AVLNode
        @returns: the successor of the node
        """

    def find_successor(self, node):
        # Check if the node has a right child
        if node.right.key is not None:
            node = node.right
            # Find the leftmost node in the right subtree
            while node.left.key is not None:
                node = node.left
            return node
        else:
            # Traverse up the tree until finding a node with a greater key
            while node.key > node.parent.key:
                node = node.parent
            return node.parent

    """delete a node that has one child from the tree
    @type node: AVLNode
    @param node: a node
    """

    def delete_node_with_one_child(self, node):
        # Determine which child (left or right) exists
        if node.left.key is not None:
            child = node.left
        else:
            child = node.right
        child.parent = node.parent
        # Update the parent reference to the child
        if child.parent is None:
            # If the node is the root, update the root reference
            self.root = child
        else:
            if node.key > node.parent.key:
                # If the node is the right child of its parent, update the right child reference
                node.parent.right = child
            else:
                # If the node is the left child of its parent, update the left child reference
                node.parent.left = child
            # Update the sizes of the parent and its ancestors
            self.set_sizes(node.parent)

    """delete a leaf from the tree
    @type node: AVLNode
    @param node: a node
    """

    def delete_leaf(self, node):
        parent = node.parent
        if parent is None:
            # If the node is the root, set the root to a new empty node
            self.root = AVLNode(None, None)
        else:
            if node.key < parent.key:
                # If the node is the left child of its parent, set the left child to a new empty node
                parent.left = AVLNode(None, None)
                parent.left.parent = parent
            else:
                # If the node is the right child of its parent, set the right child to a new empty node
                parent.right = AVLNode(None, None)
                parent.right.parent = parent
            # Update the sizes of the parent and its ancestors
            self.set_sizes(parent)

    """calculates the balance factor of the node
    @type node: AVLNode
    @param node: a node
    @rtype: int
    @returns: the balance factor of the node
    """

    def calc_balance_factor(self, node):
        return node.left.height - node.right.height

    """performs a rebalance of the tree
    @type node: AVLNode
    @param node: a node
    @type is_insert: bool
    @param is_insert: True if the rebalance is due to an insert, False otherwise
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def rebalance_tree(self, node, is_insert):
        counter = 0
        while node is not None:
            tmp_height = node.height
            node.height = max(node.left.height, node.right.height) + 1
            balance_factor = self.calc_balance_factor(node)

            if abs(balance_factor) < 2:
                if tmp_height == node.height:
                    # If the height of the node did not change, the tree is balanced up to this point
                    break
                else:
                    counter += 1
                    node = node.parent

            elif balance_factor == 2:
                if self.calc_balance_factor(node.left) == 1 or (
                        not is_insert and self.calc_balance_factor(node.left) == 0):
                    # Left-Left case or Left-Left/Right case after deletion
                    self.right_rotation(node.left)
                    node = node.parent.parent
                    counter += 1
                else:
                    # Left-Right case after insertion
                    self.left_rotation(node.left.right)
                    self.right_rotation(node.left)
                    node = node.parent.parent
                    counter += 2

            else:
                if self.calc_balance_factor(node.right) == -1 or (
                        not is_insert and self.calc_balance_factor(node.right) == 0):
                    # Right-Right case or Right-Right/Left case after deletion
                    self.left_rotation(node.right)
                    node = node.parent.parent
                    counter += 1
                else:
                    # Right-Left case after insertion
                    self.right_rotation(node.right.left)
                    self.left_rotation(node.right)
                    node = node.parent.parent
                    counter += 2

        return counter

    """preforms AVL right rotation on the node
    @type node: AVLNode
    @param node: a node
    """

    def right_rotation(self, node):
        node_parent = node.parent

        # Perform the right rotation
        node_parent.left = node.right
        node_parent.left.parent = node_parent
        node.right = node_parent
        node.parent = node_parent.parent

        # Update the parent of the rotated nodes
        if node_parent.parent is not None:
            if node.key > node.parent.key:
                node.parent.right = node
            else:
                node.parent.left = node
        else:
            # If the node's parent is None, it means the rotated node becomes the new root
            self.root = node

        # Update the parent and size of the rotated nodes
        node_parent.parent = node
        node_parent.size = node_parent.left.size + node_parent.right.size + 1
        node.size = node.left.size + node.right.size + 1

        # Recalculate the heights and balance factors of the rotated nodes
        node.right.balance_height()
        node.balance_height()

    """preforms AVL left rotation on the node
    @type node: AVLNode
    @param node: a node
    """

    def left_rotation(self, node):
        node_parent = node.parent

        # Perform the left rotation
        node_parent.right = node.left
        node_parent.right.parent = node_parent
        node.left = node_parent
        node.parent = node_parent.parent

        # Update the parent of the rotated nodes
        if node_parent.parent is not None:
            if node.key > node.parent.key:
                node.parent.right = node
            else:
                node.parent.left = node
        else:
            # If the node's parent is None, it means the rotated node becomes the new root
            self.root = node

        # Update the parent and size of the rotated nodes
        node_parent.parent = node
        node_parent.size = node_parent.left.size + node_parent.right.size + 1
        node.size = node.left.size + node.right.size + 1

        # Recalculate the heights and balance factors of the rotated nodes
        node.left.balance_height()
        node.balance_height()

    """returns an array representing dictionary sorted by key
    @rtype: list
    @returns: a sorted list according to key of tuples (key, value) representing the data structure
    """

    def avl_to_array(self):
        lst = self.avl_to_array_rec(self.root, [])
        return lst

    def avl_to_array_rec(self, node, lst):
        # Recursive function to convert the AVL tree to a list

        # Base case: If the current node is None, return the list
        if node.key is None:
            return lst
        else:
            # Recursively convert the left subtree and append the node's key-value pair to the list
            lst = self.avl_to_array_rec(node.left, lst)
            lst.append((node.key, node.value))
            # Recursively convert the right subtree
            lst = self.avl_to_array_rec(node.right, lst)
        return lst

    """returns the number of items in dictionary 

    @rtype: int
    @returns: the number of items in dictionary 
    """

    def size(self):
        return self.get_root().get_size()

    """splits the dictionary at a given node

    @type node: AVLNode
    @pre: node is in self
    @param node: The intended node in the dictionary according to whom we split
    @rtype: list
    @returns: a list [left, right], where left is an AVLTree representing the keys in the 
    dictionary smaller than node.key, right is an AVLTree representing the keys in the 
    dictionary larger than node.key.
    """

    def split(self, node):
        # Create two new AVL trees to store the smaller and bigger parts
        small_tree = AVLTree()
        big_tree = AVLTree()
        small_tree.root = node.left
        big_tree.root = node.right

        # Traverse up the tree from the given node's parent and split the remaining nodes
        while node.parent is not None:
            add_tree = AVLTree()
            if node.key < node.parent.key:
                # If the current node is on the left side of its parent, add the right subtree of the parent to the bigger tree
                add_tree.root = node.parent.right
                add_tree.root.parent = None
                big_tree.join(add_tree, node.parent.key, node.parent.value)
            else:
                # If the current node is on the right side of its parent, add the left subtree of the parent to the smaller tree
                add_tree.root = node.parent.left
                add_tree.root.parent = None
                small_tree.join(add_tree, node.parent.key, node.parent.value)

            # Move up to the parent node
            node = node.parent

        # Set the parent pointers of the roots of the smaller and bigger trees to None
        big_tree.root.parent = None
        small_tree.root.parent = None

        # Reset the current tree by creating a new empty root node
        self.root = AVLNode(None, None)

        return small_tree, big_tree

    """joins self with key and another AVLTree

    @type tree: AVLTree 
    @param tree: a dictionary to be joined with self
    @type key: int 
    @param key: The key separating self with tree
    @type val: any 
    @param val: The value attached to key
    @pre: all keys in self are smaller than key and all keys in tree are larger than key,
    or the other way around.
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def join(self, tree, key, val):
        # Create a new node with the given key and value
        new_node = AVLNode(key, val)
        new_node.size += 1
        new_node.height += 1
        new_node.left = AVLNode(None, None)
        new_node.right = AVLNode(None, None)
        new_node.right.parent = new_node.left.parent = new_node

        if self.root.key is None:
            # If self is empty, set self.root to tree.root and insert the new node
            self.root = tree.root
            self.insert(key, val)
            gap = tree.root.height + 1
        elif tree.root.key is None:
            # If tree is empty, insert the new node into self
            gap = self.root.height + 1
            self.insert(key, val)
        else:
            if self.root.key < key:
                # If self.root is smaller than key, self is the smaller tree and tree is the larger tree
                big_tree = tree
                small_tree = self
            else:
                # If self.root is greater than key, tree is the smaller tree and self is the larger tree
                big_tree = self
                small_tree = tree

            gap = big_tree.root.height - small_tree.root.height

            if gap == 0:
                # If the height difference is 0, make the new node the root and attach the trees
                small_tree.root.parent = big_tree.root.parent = new_node
                new_node.left, new_node.right = small_tree.root, big_tree.root
                self.root = new_node
            elif gap > 0:
                # If the height difference is positive, find the appropriate node in big_tree and attach the trees
                node = big_tree.root
                while node.height > small_tree.root.height:
                    node = node.left
                new_node.parent, node.parent.left = node.parent, new_node
                small_tree.root.parent, new_node.left = new_node, small_tree.root
                new_node.right, node.parent = node, new_node
                small_tree.root = big_tree.root
            else:
                # If the height difference is negative, find the appropriate node in small_tree and attach the trees
                node = small_tree.root
                while node.height > big_tree.root.height:
                    node = node.right
                new_node.parent, node.parent.right = node.parent, new_node
                big_tree.root.parent, new_node.right = new_node, big_tree.root
                new_node.left, node.parent = node, new_node
                big_tree.root = small_tree.root

            # Update the sizes of the nodes and rebalance the tree
            self.set_sizes(new_node)
            self.rebalance_tree(new_node, False)

        # Clear the tree to be joined
        tree.root = AVLNode(None, None)

        # Return the absolute value of the height difference
        return abs(gap)

    """compute the rank of node in the self
    @type node: AVLNode
    @pre: node is in self
    @param node: a node in the dictionary which we want to compute its rank
    @rtype: int
    @returns: the rank of node in self
    """

    def rank(self, node):
        # Initialize the rank with the size of the left subtree plus 1
        rank = node.left.size + 1

        # Traverse up the tree from the given node's parent and update the rank
        parent = node.parent
        while parent is not None:
            if parent.key < node.key:
                # If the parent's key is less than the current node's key, add the size of the left subtree of the parent plus 1 to the rank
                rank += parent.left.size + 1
            parent = parent.parent
        return rank

    """finds the i'th smallest item (according to keys) in self

    @type i: int
    @pre: 1 <= i <= self.size()
    @param i: the rank to be selected in self
    @rtype: int
    @returns: the item of rank i in self
    """

    def select(self, k):
        return self.select_rec(k, self.root)

    def select_rec(self, k, node):
        # Recursive helper function to find the node with the k-th smallest key
        rank = node.left.size + 1

        if k == rank:
            # If k is equal to the rank of the current node, return the node
            return node
        elif k < rank:
            # If k is smaller than the rank, search in the left subtree
            return self.select_rec(k, node.left)
        else:
            # If k is greater than the rank, search in the right subtree and adjust k
            return self.select_rec(k - rank, node.right)

    """returns the root of the tree representing the dictionary

    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    """

    def get_root(self):
        return self.root

    """returns the height of dictionary 

    @rtype: int
    @returns: the height of the dictionary 
    """

    def get_height(self):
        return self.get_root().get_height()

    """inserts a list of items to the dictionary
    @pre lst[i] is a tuple (key, value) where key is an int and value can be any type
    @type lst: list
    @param lst: a list of items to be inserted to the dictionary
    @rtype: None
    @returns: None
    @post: self contains all items in lst  
    """

    def insert_lst_to_tree(self, lst):
        for p in lst:
            self.insert(p[0], p[1])
        return None


"""Print tree, by levels with indentation"""


def printree(t):
    """Print a textual representation of t
    bykey=True: show keys instead of values"""
    return trepr(t)


def trepr(t):
    """Return a list of textual representations of the levels in t
    bykey=True: show keys instead of values"""
    if t.key is None:
        return ["#"]

    thistr = "key:" + str(t.key) + ", value:" + str(t.value) + " height:" + str(t.height) + ", bf:" + str(
        t.left.height - t.right.height)  # + ", p:" + str(t.parent)

    return conc(trepr(t.left), thistr, trepr(t.right))


def conc(left, root, right):
    """Return a concatenation of textual represantations of
    a root node, its left node, and its right node
    root is a string, and left and right are lists of strings"""

    lwid = len(left[-1])
    rwid = len(right[-1])
    rootwid = len(root)

    result = [(lwid + 1) * " " + root + (rwid + 1) * " "]

    ls = leftspace(left[0])
    rs = rightspace(right[0])
    result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid * " " + "\\" + rs * "_" + (rwid - rs) * " ")

    for i in range(max(len(left), len(right))):
        row = ""
        if i < len(left):
            row += left[i]
        else:
            row += lwid * " "

        row += (rootwid + 2) * " "

        if i < len(right):
            row += right[i]
        else:
            row += rwid * " "

        result.append(row)

    return result


def leftspace(row):
    """helper for conc"""
    # row is the first row of a left node
    # returns the index of where the second whitespace starts
    i = len(row) - 1
    while row[i] == " ":
        i -= 1
    return i + 1


def rightspace(row):
    """helper for conc"""
    # row is the first row of a right node
    # returns the index of where the first whitespace ends
    i = 0
    while row[i] == " ":
        i += 1
    return i