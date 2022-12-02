"""
Eliezer Silva
Exercício 19
-------------
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande
quantidade de organizações: "Qual o melhor Sistema Operacional para uso em servidores?"
As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe
ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0,
que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o
programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor.
Após os dados terem sido completamente informados, o programa deverá calcular a percentual de
cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela
empresa, e é o seguinte:

Sistema Operacional     Votos    %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.

obs: O exercício traz um problema similar ao do exercício 18, porém nesse caso, afim de evitar
repetições, procurei uma solução diferente da anterior, mesmo acreditando que aquela seria uma
melhor abordagem.
"""
import random

print()

windows_Server = 0
unix = 0
linux = 0
netware = 0
mac_os = 0
outro = 0

votacao = 0

while votacao < 8800:
    voto = random.randint(1, 6)

    if voto == 1:
        windows_Server += 1
    elif voto == 2:
        unix += 1
    elif voto == 3:
        linux += 1
    elif voto == 4:
        netware += 1
    elif voto == 5:
        mac_os += 1
    elif voto == 6:
        outro += 1

    votacao += 1

print()
print('Sistema Operacional  Votos   %')
print('-------------------  -----  ---')
print(f'Windows Server       {windows_Server}   {(windows_Server * 100) / votacao:.2f}%\n'
      f'Unix                 {unix}   {(unix * 100) / votacao:.2f}%\n'
      f'Linux                {linux}   {(linux * 100) / votacao:.2f}%\n'
      f'Netware              {netware}   {(netware * 100) / votacao:.2f}%\n'
      f'Mac OS               {mac_os}   {(mac_os * 100) / votacao:.2f}%\n'
      f'Outro                {outro}   {(outro * 100) / votacao:.2f}%')
print('--------------------------\n'
      f'Total                {votacao}')
print()

pontuacao = windows_Server, unix, linux, netware, mac_os, outro
maior_pontuacao = max(pontuacao)
sistema_vencedor = pontuacao.index(max(pontuacao))

if sistema_vencedor == 0:
    sistema_vencedor = 'Windows Server'
elif sistema_vencedor == 1:
    sistema_vencedor = 'Unix'
elif sistema_vencedor == 2:
    sistema_vencedor = 'Linux'
elif sistema_vencedor == 3:
    sistema_vencedor = 'Netware'
elif sistema_vencedor == 4:
    sistema_vencedor = 'Mac OS'
elif sistema_vencedor == 5:
    sistema_vencedor = 'Outro'

print(f'O Sistema Operacional mais votado foi o {sistema_vencedor}\n'
      f'Com {maior_pontuacao} votos, correspondendo a {(maior_pontuacao * 100) / votacao:.2f}% dos votos.')
