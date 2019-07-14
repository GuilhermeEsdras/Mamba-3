cont = 1

while cont == 1:

    Inicio = int(input())
    t1 = 0
    t2 = 1
    termo = 0

    if (Inicio > 0 and Inicio <= 47):

        if (Inicio == 1):
            print(t1)
        elif (Inicio == 2):
            print(t1, end=" ")
            print(t2)
        else:
            print(t1, end=" ")
            print(t2, end=" ")

        i = 1
        fim = 1

        for Fibbonacci in range(i, Inicio-1, ++i):
            termo = t1 + t2
            t1 = t2
            t2 = termo

            fim += 1

            if (fim != Inicio-1):
                print(termo, end=" ")
            else:
                print(termo)

    else:
        cont = 0