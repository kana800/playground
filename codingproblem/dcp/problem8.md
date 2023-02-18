This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:
```
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
```

A unival tree is tree is a tree where all the nodes under it have the same values and empty nodes are compared as unival subtree
```
  3
 / \
3   3
```

---

we can check the nodes:
	- left and right values are similar
	- number of empty nodes (leaf nodes)
This would take `O(n)` time where `n` is the number of nodes.
```c
// helperfunction: checks if the given tree is a unival tree
// returns 1 if the tree is unival if not 0
int univalTree(struct node * root){
	if (root == NULL){
		return 1;	
	}else if ((root->rightptr != NULL) && (root->rightptr->data != NULL)){
		// checking if the right tree is empty tree
        return 0;
	}else if ((root->leftptr != NULL) && (root->leftptr->data != NULL)){
		return 0;
    }else if (univalTree(root->leftptr) && (univalTree(root->rightptr)){
        // recursion until the end of the nodes
        return 1;
    }else{
        return 0;
    }
}
```

```c
int treeCount; // total number of trees

// counts the number of unival trees
int treeCounter(struct node * root){
    // check if the tree is empty
    if (root == NULL){
        return 0;
    }
    // recursion through the left subtree and the right subtrees
 	treeCount = treeCounter(root.leftptr) + treeCounter(root.rightptr)   ;
	// checking if the tree are unival
    if (univalTree(root) == 1){
        treeCount += 1;
    }
    return treeCount;
}
```

- [References](https://www.youtube.com/watch?v=7HgsS8bRvjo)