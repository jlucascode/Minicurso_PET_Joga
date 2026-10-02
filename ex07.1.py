
nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
vida = 100
moeda = 30
espada = False
lista_inventario = []
#função para mostrar as informações do personagem
def mostrar_informacoes():
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Vida: {vida}")
    print(f"Moedas: {moeda}")
    print(f"Espada: {'Sim' if espada else 'Não'}")
    print(f"Inventário: {', '.join(lista_inventario) if lista_inventario else 'Vazio'}")

lista_locais = ['Winterfell', 'Estrada Real', 'Floresta', 'Porto Real']
while True:
    print("\n=== MENU ===")
    print("1 - Mostrar informações do personagem")
    print("2 - Escolher local para ir")
    print("3 - Sair do jogo")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        mostrar_informacoes()
    elif opcao == 2:
        print("\nLocais disponíveis:")
        for i, local in enumerate(lista_locais):
            print(f"{i + 1} - {local}")
        escolha_local = int(input("Escolha um local para ir: "))
        if 1 <= escolha_local <= len(lista_locais):
            local_escolhido = lista_locais[escolha_local - 1]
            print(f"Você foi para {local_escolhido}.")
            # Aqui é para adicionar eventos ou desafios específicos para cada local
            #WINTERFELL - O MERCADOR : Em Winterfell, o personagem encontra um mercador oferecendo uma espada por 20 moedas. Ojogadore deverá escolher: 1 - Comprar a espada 2 - Guardar o ouro
            #Se comprar: retire 20 moedas; altere a informação da espada para True; adicione a espada ao inventário. Se guardar o ouro, não altere nada.
            if local_escolhido == 'Winterfell':
                print("Você encontrou um mercador oferecendo uma espada por 20 moedas.")
                escolha_mercador = int(input("Escolha: 1 - Comprar a espada, 2 - Guardar o ouro: "))
                if escolha_mercador == 1:
                    if moeda >= 20:
                        moeda -= 20
                        espada = True
                        lista_inventario.append('Espada')
                        print("Você comprou a espada!")
                    else:
                        print("Você não tem moedas suficientes para comprar a espada.")
                elif escolha_mercador == 2:
                    print("Você decidiu guardar o ouro.")
            #ESTRADA REAL - O BANDIDO : Na Estrada Real, um bandido bloqueia o caminho. O jogador deverá escolher: 1 - Lutar com o bandido 2 - Fugir
            #Se lutar com espada O personagem vence sem perder vida e recebe: +10 moedas. 
            # Se lutar sem espada, o personagem vence mas sofre ferimentos: vida -30 ouro +10 se fugir o personagem escapa, mas perde: vida -10
            if local_escolhido == 'Estrada Real':
                print("Você encontrou um bandido bloqueando o caminho.")
                escolha_bandido = int(input("Escolha: 1 - Lutar com o bandido, 2 - Fugir: "))
                if escolha_bandido == 1:
                    if espada:
                        print("Você venceu o bandido sem perder vida!")
                        moeda += 10
                    else:
                        print("Você venceu o bandido, mas sofreu ferimentos.")
                        vida -= 30
                        moeda += 10
                elif escolha_bandido == 2:
                    print("Você fugiu do bandido, mas perdeu um pouco de vida.")
                    vida -= 10
            #Depois dos acontecimentos, perigosos verifique se a vida chegou a 0 ou menos. Caso isso aconteça, a jornada deverá terminar.
            if vida <= 0:
                print("Você perdeu toda a sua vida. A jornada terminou.")
                break
            #FLORESTA - Encontrando uma poção : Na Floresta, o personagem encontra uma poção.
            # Adicione "poção" ao inventário. A poção recupera 20 pontos de vida. O jogador deverá escolher: 1 - Beber a poção 2 - Guardar a poção
            if local_escolhido == 'Floresta':
                print("Você encontrou uma poção na floresta.")
                escolha_pocao = int(input("Escolha: 1 - Beber a poção, 2 - Guardar a poção: "))
                if escolha_pocao == 1:
                    vida += 20
                    print("Você bebeu a poção e recuperou 20 pontos de vida!")
                elif escolha_pocao == 2:
                    lista_inventario.append('Poção')
                    print("Você guardou a poção no inventário.") 
            #FLORESTA - O CAMINHANTE BRANCO : Depois de encontrar a poção, surge um Caminhante Branco. O jogador deverá escolher: 1 - Lutar 2 - Fugir
            if local_escolhido == 'Floresta':
                print("Um Caminhante Branco apareceu!")
                escolha_caminhante = int(input("Escolha: 1 - Lutar com o Caminhante Branco, 2 - Fugir: "))
                if escolha_caminhante == 1:
                    if espada:
                        print("Você derrotou o Caminhante Branco sem perder vida!")
                        vida -= 25
                    else:
                        print("Você derrotou o Caminhante Branco, mas sofreu ferimentos.")
                        vida -= 80
                elif escolha_caminhante == 2:
                    print("Você fugiu do Caminhante Branco, mas perdeu um pouco de vida.")
                    vida -= 15
            if vida <= 0:
                print("Você perdeu toda a sua vida. A jornada terminou.")
                break
            #Se tiver guardado a poção anterior, será permitido usar ela.
            if 'Poção' in lista_inventario:
                print("Você tem uma poção no inventário.")
                escolha_usar_pocao = int(input("Deseja usar a poção? 1 - Sim, 2 - Não: "))
                if escolha_usar_pocao == 1:
                    vida += 20
                    lista_inventario.remove('Poção')
                    print("Você usou a poção e recuperou 20 pontos de vida!")
                elif escolha_usar_pocao == 2:
                    print("Você decidiu não usar a poção.")
            else:
                print("Você não tem poções no inventário.")
            #A decisão final. Ao chegar a Porto Real, o jogador deverá decidir se deseja disputar o trono. 1-Entrar na batalha pelo trono 2-abandonar a batalha
            if local_escolhido == 'Porto Real':
                print("Você chegou a Porto Real. Deseja disputar o trono?")
                escolha_trono = int(input("Escolha: 1 - Entrar na batalha pelo trono, 2 - Abandonar a batalha: "))
                if escolha_trono == 1:
                    if espada:
                        print("Você entrou na batalha pelo trono e venceu sem perder vida!")
                        moeda += 50
                    else:
                        print("Você entrou na batalha pelo trono, mas sofreu ferimentos.")
                        vida -= 50
                        moeda += 50
                elif escolha_trono == 2:
                    print("Você decidiu abandonar a batalha pelo trono.")
        else:
            print("Opção inválida. Tente novamente.")
    elif opcao == 3:
        print("Obrigado por jogar!")
        break
    else:
        print("Opção inválida. Tente novamente.")