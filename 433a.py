number = int(input())
apples = list(map(int, input().split()))

sum = 0
two_hundred = 0
one_hundred = 0

for apple in apples:
    sum += apple
    if apple == 100:
        one_hundred += 1
    else:
        two_hundred += 1

flag = False
if sum % 200 != 0:
    print("NO")
else:
    if len(apples) == 1:
        print("NO")
    else:
        for a in range(101):
            for b in range(101):
                for c in range(101):
                    for d in range(101):
                        if (100 * (a+c) + 200 * (b+d) == sum and 
                            a+c == one_hundred and 
                            b+d == two_hundred and 
                            (100*a + 200*b == sum/2) and 
                            (100*c + 200*d == sum/2)):
                            flag = True
        if flag == True:
            print("YES")
        else:
            print("NO")


 
