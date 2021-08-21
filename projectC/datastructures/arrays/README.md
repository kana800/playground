Idea is from [jwasham's](https://github.com/jwasham/coding-interview-university#arrays) coding uni repository.

---
#### Implementation of a list using C & C++

- [x] Implement a vector (mutable array with automatic resizing):

  - [x] size() - number of items

  - [x] capacity() - number of items it can hold

  - [x] is_empty()

  - [x] at(index) - returns item at given index, blows up if index out of bounds

  - [x] push(item)

  - [x] insert(index, item) - inserts item at index, shifts that index's value and trailing elements to the right

  - [x] prepend(item) - can use insert above at index 0

  - [x] pop() - remove from end, return value

  - [x] delete(index) - delete item at index, shifting all trailing elements left

  - [x] remove(item) - looks for value and removes index holding it (even if in multiple places)

  - [x] find(item) - looks for value and returns first index with that value, -1 if not found