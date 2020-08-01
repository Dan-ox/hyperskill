Number = int(input())
count = 0

for i in range(2, (Number // 2 + 1)):
    if Number % i == 0:
        count = count + 1
        break
if count == 0 and Number != 1:
    print('This number is prime')
else:
    print('This number is not prime')
