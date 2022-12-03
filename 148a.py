import sys

dragons_list = []
dragons = sys.stdin.read().split('\n')
for dragon in dragons:
    if not dragon:
        continue
    dragons_list.append(int(dragon))

dragon_damages = dragons_list[:-1]
dragon_count = dragons_list[-1]

counter = set()
for dragon in range(1, dragon_count+1):
    for dragon_damage in dragon_damages:
        if dragon % dragon_damage == 0:
            counter.add(dragon)
print(len(counter))
