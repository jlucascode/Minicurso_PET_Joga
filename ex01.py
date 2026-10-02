#exemplo = int(idade)
#print("Idade em float: ", exemplo)

print("\n=== ENTRADA ===")
nome = str(input("Digite o nome do personagem: "))
vida = int(input("Digite a vida do personagem: ")) #vida maior ou igual a 50
comida = int(input("Digite a quantidade de comida do personagem: ")) #comida maior ou igual a 10, caso não atenda aos requisitos informar que é insuficiente
#idade = int(input("Digite a idade do personagem: "))
#ouro = int(input("Digite a quantidade de ouro do personagem: "))
sword = str(input("Digite se tem espada o personagem (sim/nao): ")).strip().lower()
armadura = str(input("Digite se tem armadura o personagem (sim/nao): ")).strip().lower()

print("\n=== SAÍDA ===")
if vida >= 50:
    print("A vida do personagem é suficiente")
else:
    print("A vida do personagem é insuficiente")

if comida >= 10:
    print("A quantidade de comida é suficiente")
else:
    print("A quantidade de comida é insuficiente")

if armadura == "sim" and sword == "sim":
    print("O personagem tem armadura e espada\n")
elif armadura == "sim":
    print("O personagem tem armadura, mas não tem espada\n")
elif sword == "sim":
    print("O personagem tem espada, mas não tem armadura\n")
else:
    print("Você precisa de pelo menos uma armadura ou espada, caso não tenha, o personagem não terá defesa contra ataques inimigos")

#ouro = int(ouro) #Acontecimentos da Jornada
#ouro += 20
#ouro -= 15

#idade = int(idade)
#if idade >= 18:
#    print("O personagem é maior de idade")
#else:
#    print("O personagem não é maior de idade")

print("\n=== FINAL ===")
print(f"O nome do personagem é: {nome}\n"
    f"A vida do personagem é: {vida}\n"
    f"A quantidade de comida do personagem é: {comida}\n"
#      f"Possui mais de 30 de ouro? {ouro >= 30}\n"
      f"O personagem tem espada? {sword}\n"
      f"O personagem tem armadura? {armadura}\n")
#print(f"O nome do personagem é: {nome}, A idade do personagem é: {idade}, A quantidade de ouro do personagem é: {ouro}, O personagem tem espada? {sword}")