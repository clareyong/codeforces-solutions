a, b, c = map(int, input().split())

# Given a, b and c, find x, y and z
z = (a - b + c) / 2
y = c - z
x = a - z
if x >= 0 and x == int(x) and y >= 0 and y == int(y) and z >= 0 and z == int(z):
    print(int(x), int(y), int(z))
else:
    print('Impossible')