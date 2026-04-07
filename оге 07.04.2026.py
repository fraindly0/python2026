
total = 0
for i in range(5):
    num = int(input())
    if num % 2 == 0 and num < 30 :
        total += num
print(total)