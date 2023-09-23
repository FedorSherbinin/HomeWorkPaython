n = int(input("Введите кол-во монет: "))
countA = 0
countB = 0
min_count = 0
for i in range(n):
    x = int(input("Введите orel(1) reshka(0): "))
    if x == 1:
        countA += 1
    if x == 0:
        countB += 1
if countA < countB:
    print(countA)
else:
    print(countB)


S = int(input('Введите сумму X и Y (X,Y<=1000): '))
P = int(input('Введите произведение X и Y (X,Y<=1000): '))
for x in range(S):
    for y in range(P):
        if S == x + y and P == x * y:
            print(x, y)

N = int(input("Введите число N: "))
k = 0
while 2 ** k <= N:
    res = 2 ** k
    print(res)
    k += 1

