t, sx, sy, ex, ey = map(int, input().split())
directions = input()
x_diff = abs(ex - sx)
y_diff = abs(ey - sy)
index = -1
for i, direction in enumerate(directions, start=1):
    if sy != ey:
        if direction == 'N' and abs(ey - (sy + 1)) < y_diff:
            sy += 1
            index = i
        if direction == 'S' and abs(ey - (sy - 1)) < y_diff:
            sy -= 1
            index = i
    if sx != ex:
        if direction == 'E' and abs(ex - (sx + 1)) < x_diff:
            sx += 1
            index = i
        if direction == 'W' and abs(ex - (sx - 1)) < x_diff:
            sx -= 1
            index = i
    else:
        continue

if sx == ex and sy == ey:
    print(index)
else:
    print(-1)
