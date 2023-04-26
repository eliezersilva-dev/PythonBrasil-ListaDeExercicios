"""
Eliezer Silva
Exercício 01
-------------
Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um
relatório dos endereços IP válidos e inválidos. O arquivo de entrada possui o seguinte formato:

200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256

O arquivo de saída possui o seguinte formato:

[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256
"""
import re

with open('arquivo_entrada.txt', 'r', encoding='utf8') as arquivo:
    arquivo = arquivo.readlines()
    lista_ip = []

for i in arquivo:
    lista_ip.append(i.replace('\n', ''))

padrao = re.compile(r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.)"
                    r"{3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$")

ip_valido = []
ip_invalido = []

for ip in lista_ip:
    if padrao.findall(ip):
        ip_valido.append(ip)
    else:
        ip_invalido.append(ip)

ip_valido = ';'.join(ip_valido)
ip_valido = ip_valido.replace(';', '\n')
ip_invalido = ';'.join(ip_invalido)
ip_invalido = ip_invalido.replace(';', '\n')

print(ip_invalido)
print(ip_valido)

with open('arquivo_saida.txt', 'w', encoding='utf8') as arquivo_saida:
    arquivo_saida.write(f'[Endereços válidos:]\n'
                        f'{ip_valido}\n'
                        f'\n'
                        f'[Endereços inválidos:]\n'
                        f'{ip_invalido}')
