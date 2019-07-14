# Escreva um programa que calcule a quantidade máxima de dados a ser transmitida por um usuário levando em consideração a taxa de
# transmissão maxima de vídeo, áudio e dados e a capacidade do canal contratado:
# QDmax = (TVideo*5.2 + TAudio*3.4 + TDados*1.5) / Capacidade
# O valor de saída deve ser arredondado usando 2 casas decimais. Em Python 3, se sua variável de saída for QDmax, use round(QDmax, 2)

TVideo = float(input())
TAudio = float(input())
TDados = float(input())
Capacidade = float(input())

QDmax = (TVideo*5.2 + TAudio*3.4 + TDados*1.5) / Capacidade

print(round(QDmax, 2))
