nums = list()
N = int(input())

for n in range(0, N):
    elementos = int(input())
    nums.append(elementos)
    
deslocamento = int(input())

lista_1 = nums[deslocamento:]
for i, v in enumerate(lista_1):
    print(lista_1[i])
    
lista_2 = nums[:deslocamento]
for i, v in enumerate(lista_2):
    print(lista_2[i])