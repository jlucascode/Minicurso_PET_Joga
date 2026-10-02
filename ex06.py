#Atividade Prática: Missão de Patrulha
#lista de inimigos

lista = ["zumbi", "esqueleto", "aranha", "creeper", "boss"]
total_creepers = 0
patrulha_encerrada_por_boss = False

for inimigo in lista:
    if inimigo == "zumbi":
        continue

    print(f"Encontrou com o {inimigo}!")
   
    if inimigo == "creeper":
        print("Cuidado creeper!")
        total_creepers += 1
  
    if inimigo == "boss":
        print("Cuidado! Um inimigo muito forte apareceu!")
        patrulha_encerrada_por_boss = True
        break

print(f"Total de creepers encontrados: {total_creepers}")
if patrulha_encerrada_por_boss:
    print("A patrulha foi encerrada devido à presença do boss.")
else:
    print("A patrulha foi concluída com sucesso sem interrupções de boss.")