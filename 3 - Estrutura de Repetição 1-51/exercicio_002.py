"""
Eliezer Silva
Exercício 02
_____________
Faça um programa que leia um nome de usuário e a sua senha e não aceite
a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando
a pedir as informações.
"""

print()
print('-' * 10 + ' Usuário e Senha ' + '-' * 10)
print()


def usuario_senha(usuario, senha):
    usuario = input('Defina um nome de usuário: ')
    senha = input('Defina uma senha: ')
    print()

    if usuario == senha:
        print('Erro: Nome de usuário igual a senha.\n'
              'Redefina a senha.')
        print()
        usuario_senha(usuario, senha)
    else:
        print('Usuário e senha definidos com sucesso.')
        quit()


usuario_senha(usuario=None, senha=None)
