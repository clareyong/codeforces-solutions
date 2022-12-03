number_of_passengers, number_of_planes = map(int, input().split())
seat = list(map(int, input().split()))
seat_min = list()
for each_seat in seat:
    seat_min.append(each_seat)

counter = 0
maximum = 0
while counter != number_of_passengers:
    for i in range(number_of_planes):
        if counter != number_of_passengers:
            maximum += max(seat)
            seat[seat.index(max(seat))] -= 1
            counter += 1
        else:
            break

minimum = 0
counter_min = 0
while counter_min != number_of_passengers:
    for i in range(number_of_planes):
        if counter_min != number_of_passengers:
            if 0 in seat_min:
                seat_min.remove(0)
                continue
            if min(seat_min) != 0:
                minimum += min(seat_min)
                seat_min[seat_min.index(min(seat_min))] -= 1
                counter_min += 1

print(maximum, minimum)
