<h3 align="center">Nearest Neighbor Queries</h3>

Before diving into the research paper, lets try to understand **K-nearest neighbours** algorithm

### K-Nearest Neighbor Algorithm

For a classification usecase, The `K` is going to be how many nearest neighbors
we need to consider in terms of distance. There is two ways to calculate distances
one is **eucledian** and **manhattan** distance.

<p style="text-align: center" align="center">
  <img src=".images\nearestneighbours\samplegraph.png" alt="example points">
</p>

If `K = 3`; We select the `3` nearest neighbours, According the above diagram one **blue** points and **two** green points
are near to the **red** point (new point), The new point should belong to the **green** category.

---

<p style="text-align: center" align="center">
  <img src=".images\nearestneighbours\examplepoints.png" alt="example points">
</p>

**Eucledian Distance** between two points `A` and `B` would be:

<p style="text-align: center" align="center">
  <img src=".images\nearestneighbours\edsamplecalc.png" alt="Eucledian Distance">
</p>

<p style="text-align: center" align="center">
  <img src=".images\nearestneighbours\edeqn.png" alt="Eucledian Distance">
</p>

**Manhattan Distance** between two points `A` and `B` would be:

<p style="text-align: center" align="center">
  <img src=".images\nearestneighbours\manhattan.png" alt="Manhattan Distance">
</p>

---

<p style="text-align: center" align="center">
  <img src=".images\nearestneighbours\regressiongraph.png" alt="Regression Graph">
</p>

For a regression usecase, Just like the **classification** we select `K` nearest neighbours and
then we take the mean value of all those neighbours

<p style="text-align: center" align="center">
  <img src=".images\nearestneighbours\regressiongraph2.png" alt="Regression Graph Mean Value">
</p>

---

Lets jump into the paper,

> This paper present an efficient branch-and-bound R-tree traversal algorithm to find the nearest
neighbor object to a point, and then generalize it to finding the k nearest neighbour.

<p align="center"> <a href="https://github.com/kana800/researchpapers/blob/main/other/rtree.md">Notes on R-Tree</a></p>

### Metrics for NN Search

> Given a query point `P` and an object `O` enclosed in its `MBR` (minimum bounding rectangle), author provides two metrics
for ordering the NN search.
1. Based on the Minimum Distance of the object O from P. (`MINDIST`)
2. Based on the Minimum of the maximum possible distances from P to a face or a vertex of the 
MBR containing `O`. `MINMAXDIST`

> `MINDIST` and `MINMAXDIST` offer a lower and an upper bound on the actual distance of `O` from `P` respectively.

Author uses a variation of the classic Euclidean distance, If the point is inside 
the rectangle the euclidean distance between them is zero if the point is outside the rectangle,
we use the square of the euclidean distance between the point and the nearest edge of the rectangle.
Author also uses the **square** of the euclidean distance.

---

### Nearest Neighbor Algorithm for R-Tree

Author have used a ***branch-and-bound*** R-tree traversal algorithm to find the 
k-NN objects to a given query point.

The algorithm implemented by the author is an ordered depth first traversal. It begins
with the R-tree root node and proceeds down the tree; The Nearest Neighbour is set at **infinity**.
> During the desecnding phase, at each newly visited non-leaf node, the algorithm computes the ordering 
metric bounds for all its MBRs and sorts them into an Active Branch List (ABL).

Pruning strategies listed below are applied to remove the unecessary branches;
> - An MBR `M` with MINDIST(P,M)  greater than the MINMAXDIST(P,M`) is discarded 
because it cannot contain the NN; (look at the definition 1 and 2 in the paper). This
is applied in downward-pruning.
> - An actual distance from point `P` to a given object `O` which is greater than the
MINMAXDIST(P,M) for an MBR M can be discarded (actually replaced by it as an estimate of the NN distance) 
because M contains an object O` which is nearer to `P` (definition 2). This is alsose used in downard pruning.
> - Every MBR M with MINDIST(P,M) greater than the actual distance from P to a given object O is discarded because
it cannot enclose an object nearer than O (definition 1). We use this in upward pruning

The algorithm iterates through the ABL until the list is empty and for each iteration the algorithm selects
the next in the list and applies itself *recursively* to the node corresponding to the MBR of this branch. 

> At a leaf node, the algorithm calls a type specific distance function for each object and selects the 
smaller distance between current value of **Nearest Neighbour** and updates the **Nearest Neigbour** appropriately.
At the return from the recursion, we take this new estimate of the NN and apply upward pruning strategy to removed 
all branches with `MINDIST(P,M) > Nearest Neighbour` for all MBRs M in the ABL.


### References

- [K Nearest Neighbour Explained](https://www.youtube.com/watch?v=wTF6vzS9fy4)

```

inproceedings{10.1145/223784.223794,
author = {Roussopoulos, Nick and Kelley, Stephen and Vincent, Fr\'{e}d\'{e}ric},
title = {Nearest Neighbor Queries},
year = {1995},
isbn = {0897917316},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/223784.223794},
doi = {10.1145/223784.223794},
abstract = {A frequently encountered type of query in Geographic Information Systems is to find the k nearest neighbor objects to a given point in space. Processing such queries requires substantially different search algorithms than those for location or range queries. In this paper we present an efficient branch-and-bound R-tree traversal algorithm to find the nearest neighbor object to a point, and then generalize it to finding the k nearest neighbors. We also discuss metrics for an optimistic and a pessimistic search ordering strategy as well as for pruning. Finally, we present the results of several experiments obtained using the implementation of our algorithm and examine the behavior of the metrics and the scalability of the algorithm.},
booktitle = {Proceedings of the 1995 ACM SIGMOD International Conference on Management of Data},
pages = {71–79},
numpages = {9},
location = {San Jose, California, USA},
series = {SIGMOD '95}
}
```