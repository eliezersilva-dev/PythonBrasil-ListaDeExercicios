"""
Eliezer Silva
Exercício 18
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

tamanho_arquivo = int(input('Digite o tamnho do arquivo (Mb): '))
print(f'Tamanho do arquivo {tamanho_arquivo} Mb.')

velocidade_link = int(input('Informe a velocidade da internet (Mbps): '))
print(f'Velocidade da internet {velocidade_link} Mbps.')

tempo_total = float(tamanho_arquivo / velocidade_link)
print(f'Tempo total de download: {tempo_total} segundos')

tempo_minutos = 0
tempo_minutos_segundos = 0
tempo_horas = 0
tempo_horas_minutos = 0

if tempo_total > 60:
    tempo_minutos = int(tempo_total / 60)
    tempo_minutos_segundos = tempo_minutos % 60
    print(f'Tempo de download: {tempo_minutos} minutos e {tempo_minutos_segundos} segundos')
    if tempo_minutos > 60:
        tempo_horas = int(tempo_minutos / 60)
        tempo_horas_minutos = tempo_horas % 60
        print(f'Tempo de download: {tempo_horas} horas e {tempo_horas_minutos} minutos')
