NOME_VENDEDOR = input()
SALARIO_BASE = float(input())
VENDAS = float(input())

TOTAL = SALARIO_BASE + (0.15 * VENDAS)

print("TOTAL = R$ {:.2f}".format(TOTAL))
