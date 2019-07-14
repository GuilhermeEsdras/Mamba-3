N = int(input())
for casos in range(0, N):
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    soma = 0

    if X % 2 == 0:
        X += 1

    for num in range(0, Y):
        soma += X + 2*num

    print(soma)
