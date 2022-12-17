
valor = 100
dias = 10

prestacao_acrescimo = valor + ((valor * 3) / 100)
multa = ((valor * 3) / 100) * dias
prestacao = prestacao_acrescimo + multa

print(prestacao_acrescimo)
print(multa)
print(prestacao)