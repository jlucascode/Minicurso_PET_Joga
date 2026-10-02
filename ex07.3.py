nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
vida = 100
moedas = 30
espada = False
inventario = []
local_atual = ""


def limitar_vida(valor):
    if valor > 100:
        return 100
    if valor < 0:
        return 0
    return valor


def validar_escolha(mensagem):
    while True:
        escolha = input(mensagem)
        if escolha == "1" or escolha == "2":
            return int(escolha)
        print("Opção inválida. Digite 1 ou 2.")


def mostrar_status():
    itens = ", ".join(inventario) if inventario else "vazio"
    print("\n--- STATUS ---")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Vida: {vida}")
    print(f"Ouro: {moedas}")
    print(f"Espada: {'Sim' if espada else 'Não'}")
    print(f"Inventário: {itens}")


def combater_caminhante(vida_atual, possui_espada):
    print("\nUm Caminhante Branco apareceu!")
    escolha = validar_escolha("1 - Lutar contra o Caminhante Branco | 2 - Fugir: ")

    if escolha == 1:
        if possui_espada:
            dano = 25
            print("Você lutou com a espada contra o Caminhante Branco.")
        else:
            dano = 80
            print("Você lutou sem espada contra o Caminhante Branco.")
    else:
        dano = 20
        print("Você fugiu do Caminhante Branco.")

    return limitar_vida(vida_atual - dano)


def usar_pocao():
    global vida

    escolha = validar_escolha("1 - Usar a poção | 2 - Não usar: ")
    if escolha == 1:
        vida = limitar_vida(vida + 20)
        inventario.remove("poção")
        print(f"Você usou a poção. Vida atual: {vida}")
    else:
        print("Você decidiu não usar a poção.")


locais = ["Winterfell", "Estrada Real", "Floresta", "Porto Real"]
resultado = ""

for local_atual in locais:
    print(f"\nVocê chegou a {local_atual}.")

    if local_atual == "Winterfell":
        print("Um mercador oferece uma espada por 20 moedas.")
        escolha = validar_escolha("1 - Comprar a espada | 2 - Guardar o ouro: ")

        if escolha == 1:
            moedas -= 20
            espada = True
            inventario.append("espada")
            print("Você comprou a espada.")
        else:
            print("Você decidiu guardar o ouro.")

    elif local_atual == "Estrada Real":
        print("Um bandido bloqueou o caminho.")
        escolha = validar_escolha("1 - Lutar | 2 - Fugir: ")

        if escolha == 1:
            if espada:
                vida = limitar_vida(vida - 10)
                moedas += 10
                print("Você derrotou o bandido com a espada.")
            else:
                vida = limitar_vida(vida - 50)
                moedas += 15
                print("Você derrotou o bandido, mas ficou gravemente ferido.")
        else:
            vida = limitar_vida(vida - 10)
            moedas = max(0, moedas - 5)
            print("Você fugiu do bandido e perdeu 5 moedas.")

    elif local_atual == "Floresta":
        print("Você encontrou uma poção.")
        inventario.append("poção")
        escolha = validar_escolha("1 - Usar a poção agora | 2 - Guardar: ")

        if escolha == 1:
            vida = limitar_vida(vida + 20)
            inventario.remove("poção")
            print(f"Você usou a poção. Vida atual: {vida}")
        else:
            print("Você guardou a poção para depois.")

        vida = combater_caminhante(vida, espada)
        if vida == 0:
            resultado = "DERROTA"
            print("Você morreu na Floresta.")
            break

    elif local_atual == "Porto Real":
        if "poção" in inventario:
            print("Você ainda tem uma poção no inventário.")
            usar_pocao()

        print("\nO Trono de Ferro está diante de você.")
        escolha = validar_escolha("1 - Disputar o trono | 2 - Abandonar: ")

        if escolha == 2:
            resultado = "SOBREVIVEU, MAS NÃO VENCEU"
            print("Você abandonou a batalha e decidiu viver em paz.")
        elif espada and vida >= 40:
            resultado = "VITÓRIA"
            print("Você conquistou o Trono de Ferro!")
        else:
            vida = 0
            resultado = "DERROTA"
            print("Você entrou na batalha sem estar preparado e foi derrotado.")

        break


mostrar_status()
print(f"\nRESULTADO FINAL: {resultado}")
