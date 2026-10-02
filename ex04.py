import math
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7:
    print("Aprovado", media)

elif media <= 6.9 and media >= 4:
    print("Avaliação Final", media)

else:
    print("Reprovado", media)
