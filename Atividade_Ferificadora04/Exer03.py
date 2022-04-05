#Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

digite = int(input("Digite 1 para M-maculino ou Digite 2 para F-feminio:  "))

M = digite
F = digite

if M == 1 :
    print('Você digitou a letra M :{}'.format(M))
elif F == 2:
    print('Você digitou a letra F : {}'.format(F))
else:
    print('Valor inválido: ')