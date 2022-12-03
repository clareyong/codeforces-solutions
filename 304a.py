from tqdm import tqdm
# import math

# number = int(input())
# counter = 0
# squares = set()
# for i in range(1, number+1):
#     squares.add(i ** 2)

# for a in tqdm(range(3, number+1)):
#     for b in range(a, number+1):
#         counter += (a ** 2 + b ** 2) in squares

# print(counter)
import math
number = int(input())
counter = 0
    
for a in tqdm(range(1, number+1)):
    for b in range(a+1, number+1):
        operation = math.sqrt(a * a + b * b)
        counter += operation <= number and int(operation) == operation
    
print(counter)