# Spiral Matrix Template 

- The idea is that to traverse a spiral matrix we create a max and min for the left and right col 
and the top and bottom row 

- When move right we go from min_col to max_col at the min_row and increment the min_row at the end
- When move down we go from min_row to max_row at the max_row and increment the max_row 
- In between we need to check if we are done searching to prevent duplicates by checking if
min_row > max_row or min_col > max_col 
- Move left max_col to min_col at max_row end decrement max_row
- Move up from max_row to min_row at min_col end increment  min_col

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix or len(matrix[0]) < 1: 
            return result
        m = len(matrix)
        n = len(matrix[0])
        row_min = col_min = 0
        row_max = m-1
        col_max = n-1
        
        while (row_min <= row_max and col_min <= col_max):
            for i in range(col_min,col_max+1):
                result.append(matrix[row_min][i])
            row_min+=1
            
            for i in range(row_min,row_max+1):
                result.append(matrix[i][col_max])
            col_max-=1
            
            if row_min > row_max or col_min > col_max:
                break
            
            for i in range(col_max,col_min-1,-1):
                result.append(matrix[row_max][i])
            row_max-=1
            
            for i in range(row_max,row_min-1,-1):
                result.append(matrix[i][col_min])
            col_min+=1
        return result

```
