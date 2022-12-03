contest = int(input())
scores = list(map(int, input().split()))

min_score = scores[0]
max_score = scores[0]
counter = 0
for score in scores:
    if score < min_score:
        min_score = score
        counter += 1
    if score > max_score:
        max_score = score
        counter += 1
print(counter)