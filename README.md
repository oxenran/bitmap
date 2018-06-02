# Lonely and Not lonely Pixels
Find the pixels in a bitmap that are located in the same row or column as other pixels and find the ones that aren't.

## Method
Using Python 3, I defined a function that takes an argument: one bitmap.
The bitmap will be a matrix with empty and not empty pixels. 

Example:
```python
bitmap = [
          [None, None, 'x'],
          ['x', None, None],
          ['x', None, None],
         ]
```
In this case the lonely pixel will be the one at location: (0,2)
and the two that are not lonely are: (0,1), (2,1)
