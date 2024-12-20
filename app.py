print('Sabor Express\n')

print ('1.Cadastrar Restaurante')
print ('2.Listar Restaurante')
print ('3.Ativar Restaurante')
print ('4.Logoff\n')


opcao_escolhida = input('Escolha uma opção: ')

if opcao_escolhida == 1:
    print('Cadastrar restaurante')
elif opcao_escolhida == 2:
    print('Listar restaurantes')
elif opcao_escolhida == 3:
    print('Ativar restaurantes')
else:
    print('Encerrando o programa')