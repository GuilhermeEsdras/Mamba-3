Soma = 0

n1 = int(input())
n2 = int(input())
for x in range(n1, n2+1):
    if x > 0:
        Soma += x
for x in range(n1, n2, -1):
    if x > 0:
        Soma += x
        
print(Soma)