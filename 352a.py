pedal = int(input())
pedal_stars = list(map(int, input().split()))
rear_wheel = int(input())
rear_wheel_stars = list(map(int, input().split()))

integers = list()
for star in pedal_stars:
    for star_ in rear_wheel_stars:
        if star_ % star == 0:
            integers.append(int(star_ / star))

maximum = max(integers)
counter = 0
for integer in integers:
    if integer == maximum:
        counter += 1

print(counter)