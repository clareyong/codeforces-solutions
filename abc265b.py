n, m, t = map(int, input().split())
time_limit = list(map(int, input().split()))
time_limits = list()
for i, c in enumerate(time_limit, start=1):
    time_limits.append((i, c))
from collections import defaultdict
bonus = defaultdict(int)
for i in range(m):
    key, value = map(int, input().split())
    bonus[key] = value

flag = True
for i in range(n-1):
    if t - time_limit[i] > 0:
        t -= time_limit[i]
        if (i+2) in bonus.keys():
            t += bonus[i+2]
    else:
        flag = False
        break

if flag == True:
    print('Yes')
else:
    print('No')
