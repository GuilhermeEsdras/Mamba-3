array_intercalado = []
n = int(input())
p1 = 0
p2 = 1
for x in range(0, n):
    valor = int(input())
    array_intercalado.insert(p1, valor)
    p1 += 2
for y in range(0, n):
    valor = int(input())
    array_intercalado.insert(p2, valor)
    p2 += 2
for i, v in enumerate(array_intercalado):
    print(v)