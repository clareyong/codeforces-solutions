y = int(input())
y_offset = y-2
rounded_down = (y_offset//4)*4
latest_world_cup = rounded_down + 2
if y == latest_world_cup:
    print(y)
else:
    print(latest_world_cup+4)