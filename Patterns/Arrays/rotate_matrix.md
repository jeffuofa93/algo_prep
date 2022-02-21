# Rotating a Matrix

```python
def rotate(matrix: List[List[int]]) -> None:
    l,r = 0,len(matrix)-1
    while l < r:
        # each outer square is r-l size 
        for i in range(r-l):
            top,bottom = l,r

            # moves right each iteration
            topLeft = matrix[top][l+i]
            # moves down each iteration
            topRight = matrix[top+i][r]
            # moves left each iteration
            bottomRight = matrix[bottom][r-i]
            # moves up each iteration
            bottomLeft = matrix[bottom-i][l]

            # top right becomes topleft
            matrix[top+i][r] = topLeft
            # bottom right becomes top right
            matrix[bottom][r-i] = topRight
            # bottom left becomes bottom right
            matrix[bottom-i][l] = bottomRight
            # top left becomes bottom left
            matrix[top][l+i] = bottomLeft

        # decrement right and increment left 
        r-=1
        l+=1
```

- Big idea here is that rotating a square matrix we can think it as nested sub matrixes hence the while loop 
- To do the rotation topLeft -> bottomLeft, topRight -> topLeft, bottomRight -> topRight, bottomLeft -> bottomRight 
- Each iteration of the for loop topLeft moves right, topRight moves down, bottomRight moves left and bottomLeft moves up 
- Each while loop we move decrement right and increment left to reach the next sub matrix 

- Fun one liner
```python

class Solution:
    def rotate(self, A):
        A[:] = zip(*A[::-1])
```
