n, s, t = map(int, input().split())
mapping = list(map(int, input().split()))
marble_loc = s
count = 0
while marble_loc != t:
    count += 1
    marble_loc = mapping[marble_loc-1]
    if count > n-1:
        count = -1
        break
print(count)