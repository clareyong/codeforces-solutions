from weakref import ref


number = int(input())
points = list()
for i in range(number):
   point = list(map(int, input().split()))
   points.append(point) 

counter = 0

for point in points:
    ref_point = point
    print(ref_point)
    top = [ref_point[0], ref_point[1] + 1]
    bottom = [ref_point[0], ref_point[1] - 1]
    left = [ref_point[0] + 1, ref_point[1]]
    right = [ref_point[0] - 1, ref_point[1]]
    print(top, bottom, left, right)
    if top in points and bottom in points and left in points and right in points:
        counter += 1

print(number, points, ref_point, counter)