# Intersecting Disks
Solution v1 is optimized brute force

Input is in "n" which is the size of the array
•	the interesting part is  how T(n(n+1)/2) is calculated
•	n + n-1Σi=1 = nΣi=1 = n(n+1)/2) , approximately 1/2(n2), but the algorithm is Θ(n2)
