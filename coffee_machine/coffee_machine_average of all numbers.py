a = int(input())
b = int(input())

items = [i for i in list(range(a, b + 1)) if i % 3 == 0]
print(sum(items) / len(items))

n = 0
sum_ = 0
a = int(input())
b = int(input())
for mean in range(a, b + 1):
    if mean % 3 == 0:
        n += 1
        sum_ += mean
print(sum_ / n)
