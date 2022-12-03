number_of_people, seconds = map(int, input().split())
q = list(input())

for _ in range(seconds):
    positions = []
    for i in range(len(q)-1):
        if q[i] == 'B' and q[i+1] == 'G':
            positions.append(i)
    for position in positions:
        q[position] = 'G' 
        q[position+1] = 'B'

queue = ''.join(q)
print(queue)