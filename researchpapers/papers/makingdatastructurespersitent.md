<h3 align="center">Making Data Structures Persistent</h3>

> Data structure is peristent if it supports access to multiple versions; only partially persistent if it all the versions can be accessed but only the newest version can be modified, and fully persitent if every version can be accessed and modified.

> Ordinary data structures are *ephemeral* in the sesne that making a change to the structure would destroys the old version, leaving only the new one.

Author defines a *linked data structure* to be a finite collection of *nodes* and each of these *nodes* contain "*data*" field and a pointer field. 

> If a *node* `x` contains a pointer to a *node* `y`, we call `y` a *sucessor* of `x` and `x` a *predecessor* of `y`.

> In a general linked data structure we allow two kinds of operations
>- *access operations* : An *access* operation consists of a sequence of *access* steps, which compute a set of *accessed nodes* by beginning with the empty set and adding nodes. The **time** of an **access operation** would be number of **access steps** performed. Example for *access operation* would be *search for an item in a binary tree*.
> - *update operations*:  Intermixed sequence of *access* steps and *update* steps. The *update* step changes the structure. The **total time** of an *update* operation is **total number** of **access** and **update steps**; the **update time** is the number of **update steps**.Example for *update operation* would be *insertion of a new item in a binary search tree*.

### Partial Persistence

> In Overmars research, he studied three simple techniques to obtain partial persistence.

> 1. Explicitly store every version by copying the entire *ephemeral* structure after each update. This cost ![](https://latex.codecogs.com/png.image?\inline&space;\dpi{110}\Omega(n)) time and space per update
> 2. Store the entire update sequence, rebuilding the current version from scratch each time an *access operation* is performed. Storing an update takes `O(m)` space but accessing the version `i` takes ![](https://latex.codecogs.com/png.image?\inline&space;\dpi{110}\Omega(i))  
> A hybrid method to store entire update sequence every `k`th version. *suitable value for `k` should be chosen*. The accessing version `i` requires rebuilding it from version `k[i/k]`. 
> 3. Dynamization technique of `Bentley and Saxe`.

Author's first idea is to record all updates to node fields in the node themselves without changing the older values of the fields; This would increase the `size` of the node. 
> When an *empheral* update step creates a new node, we create a corresponding `fat node`. When an *empheral* update step changes a field value in a node, we add the new value to the corresponding `fat node`, along with the name of the field whose value has changed and a *version stamp* that is number of update operations being performed.

> When an *emphemeral* access step applied to version `i` follow the pointer in field `f` of a node; we follow the pointer in the corresponding fat node whose field name is `f`; if there are several such pointers, we select one with maximum version stamp **no greater than** `i`. 

Author suggest to use an auxiliary data structure to store the access pointer of the various version. I think it would be interesting use *linked* `fatnode` instead of using an *helper*.
for an *array* updating any version takes `O(1)` time. My problem is that if we are using an array to store the `fatnode` it is going to limit the *amount of* `fatnode` we can use.

<p align="center"> <a href=""> Implementation On Fat Node </a></p>

```c
// maybe something like this?
typedef struct fatnode_{
    int versionstamp; // current update version
    float nodeval; // latest value of the node
    fatnode* prevnode; // pointer to the previous node value
} fatnode;

typedef struct node_ {
    float nodeval; // stores the newest node value
    fatnode* m_fatnode;// fatnode of the node
    node* nextnode;
} node;
```

> The method has two related drawbacks; `fatnode` must be represented by linked collection of fixed-size nodes. This poses no fundamental difficulty but complicates the implementation. Second, choosing which pointer in a `fatnode` to follow when simulating an access step takes more than constant time.

Author suggest the idea of using a binary search with the `fatnodes` being ordered by the version stamp and each access step would be around `O(log m)` time.

Author's second idea is **node copying**. Instead of holding all the `fatnodes` we will only allow a fixed number of `fatnodes` to be stored in it. 
> When we run of space in a node for new pointers, we create a new copy of the node, containing only the current field values. The old pointers should contain a pointer to the new copy.

Single **update step** can cause large number of node to be copied;

```C
// ephemeral node
typedef struct ephnode {
    int version;
    float data;
} ephemeralnode;

// ephemeral structure
typedef struct ephstruct {
    int version;
    ephemeralnode* next;
    ephemeralnode* prev;
} ephemeralstruct;

// persistent node
typedef struct pernode {
    int version;
    float data;
} persistentnode;

// persistent structure
typedef struct perstruct {
    int version;
    persistentnode* next;
    persistentnode* prev;
}persistentstruct;
```

`x` is an ephemeral node occuring in version `i` of the ephemeral structure. 

```C
ephemeralnode* x = createEphemeralNode(5.00);
ephmeralstruct.add(x);
```
> let `d` be the number of pointer in an ephemeral node and let `p` be the maximum number of predecessors of an ephemeral node in any single version; Assume that `p` is constant.

> Each ephemeral node `x` corresponds to a set `F(x)` of persistent nodes, called a **family**. The members of `F(x)` form a singly-linked list, linked by the copy pointers.

Navigation through the persistent structure is the same as in the `fat node` method. We will have an *access array* with access for `entry nodes` for access of data in `O(1)` time.

<p align="center"> <a href=""> Implementation On Node Copying </a></p>

I can't grasp the idea of `node copying`; like the author mentioned; So the above implementation is bit incomplete.

---

### Full Persistence

> The lack of linear ordering on versions makes navigation through the resulting persistent structure problematic. 

In the lecture, [Persistent Data Structures By MIT](https://www.youtube.com/watch?v=T0yzrZL1py0), **Order-Maintenance Data Structure** which is a *magical linked list* is used to avoid the above problem. The Data Structure is capable of finding relative order of `2` *items/nodes* in `O(1)` time. Author uses **version list** to avoid the above mentioned problem.

> using `fat nodes` to make a linked structure fully persistent.

```c
int arbitrarily_large_number = 5;

// ephemeral node
typedef struct ephnode {
    int version;
    float data;
} ephemeralnode;

typedef struct versionrec {
    int versionstamp;
    // other fields in the 
    // in an ephemeralnode
    float data;
    // ...
} versionrecords;

typedef struct fatnode_{
    versionrecords* vr[arbitrarily_large_number];
    struct fatnode* nextnode;
} fatnode;
```

> The efficiency of the fat node method is the same for full persistence as its for partial persistence. The space cost per update step is `O(1)` and time cost per access step is `O(log m)`, if a fat node is represented as a search tree of version records, ordered by version stamp.

> For full persistence instead of using `Node Copying` you can use `Node Splitting`.  Persistent node will hold version records. `d` will be the number of pointers in an ephemeral node and `p` will be constant upper bound on the in-degree of an ephemeral node. Ephemeral node contain a set of `p inverse pointers`, inverse pointers point to a valid node with valid versions from the ephemeral node.

---

### References

```bibtex
@inproceedings{10.1145/12130.12142,
author = {Driscoll, J R and Sarnak, N and Sleator, D D and Tarjan, R E},
title = {Making Data Structures Persistent},
year = {1986},
isbn = {0897911938},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/12130.12142},
doi = {10.1145/12130.12142},
booktitle = {Proceedings of the Eighteenth Annual ACM Symposium on Theory of Computing},
pages = {109–121},
numpages = {13},
location = {Berkeley, California, USA},
series = {STOC '86}
}
```
- [MIT 68.851 Advanced Data Structures Persistent Data Structure](https://www.youtube.com/watch?v=T0yzrZL1py0) | [Notes]()
