numbers = list(map(int, input().split()))

people = numbers[0]
bottles = numbers[1]
volume = numbers[2]
limes = numbers[3]
slices = numbers[4]
salt = numbers[5]
volume_needed = numbers[6]
salt_needed = numbers[7]

by_volume = ((bottles * volume) // volume_needed) // people
by_lime = (limes * slices) // people
by_salt = (salt // salt_needed) // people

minimum = min(by_volume, by_lime, by_salt)

print(minimum)
