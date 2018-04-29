# Intersecting Disks
Solution v2 depends on the inputs, but even in the worst case it's better than bruteforce.

# Analysis Summary

This algorithm is different, instead of looking at each circle we look outside it's borders, it's trivial that the circle will intersect with everycircle which its center is inside the domain.
The time complexity here depends on the value of the current element which we can't predict, but we can define the best and worst cases.
O(n2) , Ω(n)

Although the avg. case is close to (n)
