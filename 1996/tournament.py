# a[i] число игоков с номерами > i,
# которых обогнал i-й игрок
a = [int(i) for i in input().split(" ")]

# b[i] номер игрока, занявшего i- e место
b = []

# список всех возможных номеров
c = list(range(len(a)))

for loser_members in a:
    # print(b, c)
    b.append(c.pop(-loser_members - 1) + 1)

print(b)