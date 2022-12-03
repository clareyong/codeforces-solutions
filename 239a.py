y, k, n = map(int, input().split())
flag = 'none'
for total in range(0, n+1, k):
    x = total - y
    if x > 0:
        print(x, end=' ')
        flag = 'found'
if flag == 'none':
    print(-1)

    