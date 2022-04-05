a = int(input("Digite a primeira nota: "))
b = int(input("Digite a segunda nota: "))
c = int(input("Digite a terceira nota: "))
d = int(input("Digite a quarta nota: "))

media = (a + b + c + d) /4

if media >= 7:
    print("Parabéns você foi aprovado: {}".format(media))
elif media == 10.0:
    print("Parabéns você foi aprovado com Distinção: {}".format(media))
elif media < 7:
    print("Infelizmente você foi reprovado: {}".format(media))




