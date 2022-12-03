x, y, n = map(int, input().split())

triplets = n // 3
one_a_time = n * x
three_plus_one = triplets * y + (n - triplets * 3) * x

if n < 3:
    print(one_a_time)
else:
    minimum = min(one_a_time, three_plus_one)
    print(minimum)
    
