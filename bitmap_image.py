# in a bitmap image containing empty and filled pixels,
# we call lonely a filled pixels which is the only one in its row and column and filled a pixel which is not alone

image = [[None for x in range(6)],
         [None, 'x', None, None, None, None],
         [None, None, 'x', None, None, None],
         [None, None, None, 'x', None, None],
         [None, 'x', None, 'x', None, 'x']]


def find_lonelies(bitmap):
    all_pixels = set() # Space: O (rows * columns)
    filled = set() # Space: O (rows * columns)
    rows = {}  # Space: O (rows * 2) #  I optimized it  :-)
    columns = {} # Space: O (columns * 2)
    for i in range(len(image)):
        for j in range(len(image[i])):  # O ( rows * columns)
            if bitmap[i][j]:
                all_pixels.add((i, j))  # O (1)
                if i in rows:  # O (1)
                    if len(rows[i]) is 1:
                        filled.add(rows[i][0])  # O (1)
                        filled.add((i,j))  # O (1)
                        rows[i].append((i, j))  # O (1)
                    else:
                        filled.add((i, j))  # O (1)
                else:
                    rows[i]=[(i, j)]  # O (1)
                if j in columns:  # O (1)
                    if len(columns[j]) is 1:  # O (1)
                        filled.add(columns[j][0])  # O (1)
                        filled.add((i,j))  # O (1)
                        columns[j].append((i, j))  # O (1)
                    else:
                        filled.add((i,j))  # O (1)
                else:
                    columns[j] = [(i, j)]  # O (1)
    print(f'Here are your lonelies: \n {all_pixels - filled}') # O (rows * columns)
    print(f'Here are your filled: \n {filled}')

# I optimized it to have a time complexity of O(rows * columns)
# and a space complexity of O ((2 * rows) + (2 * columns) + 2(rows * columns))
find_lonelies(image)