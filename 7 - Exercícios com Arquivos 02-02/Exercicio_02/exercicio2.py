"""
Eliezer Silva
Exercício 02
-------------
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e
identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar
o seguinte arquivo, chamado "usuarios.txt":

alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125

Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um
relatório, chamado "relatório.txt", no seguinte formato:

ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma
a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita
através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá
ser feito através de uma função, que será chamada pelo programa principal.
"""

# Abre o arquivo para leitura
arquivo = open('usuarios.txt', 'r')

# Coloca todas as linhas em memoria
linhas = arquivo.readlines()

# Fecha o arquivo
arquivo.close()

usuarios = []
espacos = []
total = 0

for i in linhas:
    linha = i.split()
    usuarios.append(linha[0])
    espacos.append(int(linha[1]))
total = sum(espacos)

# Abre o arquivo para escrita
arquivoRelatorio = open('relatorio.txt', 'w')
arquivoRelatorio.write(
    'ACME Inc.               Uso do espaco em disco pelos usuarios\n')
arquivoRelatorio.write(
    '------------------------------------------------------------------------')
arquivoRelatorio.write('\nNr.  Usuario        Espaco utilizado     % do uso')

for i in range(0, len(usuarios)):
    espacoMB = espacos[i] / (1024.0 * 1024.0)
    percentualUso = espacos[i] / total
    arquivoRelatorio.write('\n%d - %s - %.2f MB - %.2f%%' %
                           (i + 1, usuarios[i], espacoMB, percentualUso * 100.0))

arquivoRelatorio.write('\nEspaco total ocupado: %.2f MB' %
                       (total / (1024.0 * 1024.0)))
arquivoRelatorio.write('\nEspaco medio ocupado: %.2f MB' %
                       (total / len(usuarios) / (1024.0 * 1024.0)))
# Fecha o arquivo
arquivoRelatorio.close()
