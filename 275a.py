row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
row3 = list(map(int, input().split()))

grid = [row1, row2, row3]
print(grid)
print(type(row1))
print(grid[0][1])

affect_list = [(0,0), (0,1), (1,0),(0, -1), (-1, 0)]

def check_status(x, y):
    if x < 0 or x > 2:
        return False
    if y < 0 or y > 2:
        return False
    return True

for i in range(3):
    for j in range(3):
        if grid[i][j] == 1:
            print('m')

a = 1
a ^= 1
print(a)
a ^= 1
print(a)