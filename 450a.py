number_of_children, candies_given = map(int, input().split())
candies = list(map(int, input().split()))

idx = list()
for i, candy in enumerate(candies, start=1):
    idx.append([i, candy])
print(idx)
idxs = list(range(1, len(idx)+1))
flag = True

remaining = []
while len(remaining) != 1: 
    for child in idx:
        while len(remaining) != 1: 
            if child[1] > 0:
                child[1] -= candies_given
                print(idx)
                if child[1] <= 0:
                    remaining.append(child[0])
                    if len(remaining) > 0:
                        remaining = list()
print(remaining)

    
    