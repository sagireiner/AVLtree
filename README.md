# AVL Tree

This repository contains an implementation of an AVL tree in Python. The AVL tree is a self-balancing binary search tree that maintains its balance factor, ensuring efficient operations such as insertion, deletion, and search.

## Contents

- [About the AVL Tree](#about-the-avl-tree)
- [License](#license)

## About the AVL Tree

The AVL tree is a binary search tree that maintains the height balance property. It ensures that the heights of the left and right subtrees of any node differ by at most one. This balancing property guarantees efficient operations with a worst-case time complexity of O(log n) for search, insert, and delete operations.

The implementation provided in this repository includes the following features:

- Insertion: Insert a new key-value pair into the AVL tree while maintaining balanc ensuring the structure remains in a valid state.
- Deletion: Remove a key-value pair from the AVL tree while maintaining balance, adjusting the structure as necessary to maintain integrity.
- Search: Find the value associated with a given key in the AVL tree.
- Join: Joining two data structures combines their contents to create a new structure that encompasses all the elements from both sources.
- Split: Splitting a data structure divides it into two separate structures based on the keys' values.
- Rebalance: Self-balancing the AVLtree tree in orderto ensures that the tree remains balanced to achieve efficient operations.
- AVL to Array: Converting the AVL tree keys into a sorted array maintaining the order of the original structure.
- Rank: Determining the position of an element within the data structure.
- Select: Selecting an element retrieves the value at a specific position or order within a data structure.

The AVL tree data structure provides efficient operations with a logarithmic time complexity for most operations, thanks to its self-balancing property. All of the operations above have a logarithmic time complexity of O(log n) since the AVL tree maintains balance during these operations. However, the AVL to array conversion operation, performed using an in-order traversal, has a linear time complexity of O(n) since it requires visiting all nodes in the tree.

## License

This AVL tree implementation is licensed under the MIT License. See the LICENSE file for more details.

