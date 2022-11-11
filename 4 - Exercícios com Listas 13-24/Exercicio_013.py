"""
Eliezer Silva
Exercicio 13
-------------
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""
print()
print('-'*10+' Dados '+10*'-')
print()

# montando e organizando os dados
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
dados = {}
for mes in meses:
    dados.update({mes: float(input(f'Temperatura mês {mes}: '))})

# calculando a média anual
media_temperatura = sum(dados.values()) / len(dados)

# selecionando meses acima da média
acima_media = {}
for mes, temperatura in dados.items():
    if temperatura > media_temperatura:
        acima_media.update({mes: temperatura})

# retornando resultados
print()
print('-'*10+' Resultado '+10*'-')
print()

dados = str(dados)
dados = dados.replace('{', ' ')
dados = dados.replace('}', '')
dados = dados.replace("'", "")
dados = dados.replace(',', ' graus\n')
print(dados)
print()

print(f'Média anual de Temperatura: {media_temperatura:.2f} graus')
print()

acima_media = str(acima_media)
acima_media = acima_media.replace('{', '')
acima_media = acima_media.replace('}', '')
acima_media = acima_media.replace("'", "")
acima_media = acima_media.replace(',', ' graus\n')
print(f'Mês(es) acima da média:\n'
      f' {acima_media}', end=' graus')
