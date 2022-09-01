import random
menu = 0
while menu != 4:
    print("==================="
          "\n      JOKENPO      " 
          "\n==================="
          "\n   MODOS DE JOGO   "
          "\n|[1] HumanoxHumano|"
          "\n|[2] HumanoxPC    |"
          "\n|[3] PCxPC        |"
          "\n|[4] SAIR         |"
          "\n===================")
    menu = int(input("Digite um número para escolher o modo de jogo: "))
    S = "S"
    S1 = "S"
    S2 = "S"
# HumanoxHumano
    if menu == 1:
        placar_1 = 0
        placar_2 = 0
        while S == "S":
            print("=============="
                  "\n[1] Pedra"
                  "\n[2] Papel"
                  "\n[3] Tesoura"
                  "\n============== ")
            n = int(input("Escolha jogador 1: "))
            n1 = int(input("Escolha jogador 2: "))
            print('=' * 16)
            if n == n1:
                print("Empatou!")
                S = str(input("Quer Jogar de novo?[S/N] ")).upper()
            elif n == 1 and n1 == 2:
                print("Pedra perde contra Papel. JOGADOR 2 GANHOU!")
                S = str(input("Quer Jogar de novo?[S/N] ")).upper()
                placar_2 = placar_2 + 1
            elif n == 2 and n1 == 3:
                print("Papel perde contra Tesoura. JOGDADOR 2 GANHOU!")
                S = str(input("Quer Jogar de novo?[S/N] ")).upper()
                placar_2 = placar_2 + 1
            elif n == 3 and n1 == 1:
                print("Tesoura perde contra Pedra. JOGDADOR 2 GANHOU!")
                S = str(input("Quer Jogar de novo?[S/N] ")).upper()
                placar_2 = placar_2 + 1
            elif n == 2 and n1 == 1:
                print("Pedra perde contra Papel. JOGDADOR 1 GANHOU!")
                S = str(input("Quer Jogar de novo?[S/N] ")).upper()
                placar_1 = placar_1 + 1
            elif n == 3 and n1 == 2:
                print("Papel perde contra Tesoura. JOGDADOR 1 GANHOU!")
                S = str(input("Quer Jogar de novo?[S/N] ")).upper()
                placar_1 = placar_1 + 1
            elif n == 1 and n1 == 3:
                print("Tesoura perde contra Pedra. JOGDADOR 1 GANHOU!")
                S = str(input("Quer Jogar de novo?[S/N] ")).upper()
                placar_1 = placar_1 + 1
            else:
                print("JOGADA INVALIDA!")
        print(f"Jogador_1: {placar_1} Vitórias")
        print(f"Jogador_2: {placar_2} Vitórias")
# HumanoxPC
    elif menu == 2:
        placar_1 = 0
        placar_2 = 0
        while S1 == "S":
            print("=============="
                  "\n[1] Pedra"
                  "\n[2] Papel"
                  "\n[3] Tesoura"
                  "\n============== ")
            n = int(input("Escolha o que você vai jogar: "))
            r = random.randint(1, 3)
            if r == n:
                print("Empatou!")
                S1 = str(input("Quer Jogar de novo?[S/N] ")).upper()
            elif r == 1 and n == 2:
                print("Você Ganhou! Eu Escolhi Pedra, Parabéns.")
                S1 = str(input("Quer Jogar de novo?[S/N] ")).upper()
                placar_1 = placar_1 + 1
            elif r == 2 and n == 3:
                print("Você Ganhou! Eu Escolhi Papel, Parabéns.")
                S1 = str(input("Quer Jogar de novo?[S/N] ")).upper()
                placar_1 = placar_1 + 1
            elif r == 3 and n == 1:
                print("Você Ganhou! Eu Escolhi Tesoura, Parabéns.")
                S1 = str(input("Quer Jogar de novo?[S/N] ")).upper()
                placar_1 = placar_1 + 1
            elif r == 1 and n == 3:
                print("Você Perdeu! Eu Escolhi Pedra.")
                S1 = str(input("Quer Jogar de novo?[S/N] ")).upper()
                placar_2 = placar_2 + 1
            elif r == 2 and n == 1:
                print("Você Perdeu! Eu Escolhi Papel.")
                S1 = str(input("Quer Jogar de novo?[S/N] ")).upper()
                placar_2 = placar_2 + 1
            elif r == 3 and n == 2:
                print("Você Perdeu! Eu Escolhi Tesoura.")
                S1 = str(input("Quer Jogar de novo?[S/N] ")).upper()
                placar_2 = placar_2 + 1
            else:
                print("JOGADA INVALIDA!")
        print(f"Jogador: {placar_1} Vitórias")
        print(f"Computador: {placar_2} Vitórias")
# PCxPC
    elif menu == 3:
        placar_1 = 0
        placar_2 = 0
        while S2 == "S":
            print("=============="
                  "\n    PCxPC      "
                  "\n============== ")
            r = random.randint(1, 3)
            r1 = random.randint(1, 3)
            if r == r1:
                print("Empatou!")
                S2 = str(input("Quer Jogar de novo?[S/N] ")).upper()
            elif r == 1 and r1 == 2:
                print("Pedra x Papel PC_2 Ganhou!")
                S2 = str(input("Quer Jogar de novo?[S/N] ")).upper()
                placar_2 = placar_2 + 1
            elif r == 2 and r1 == 3:
                print("Papel x Tesoura PC_2 Ganhou!")
                S2 = str(input("Quer Jogar de novo?[S/N] ")).upper()
                placar_2 = placar_2 + 1
            elif r == 3 and r1 == 1:
                print("Tesoura x Pedra PC_2 Ganhou!")
                S2 = str(input("Quer Jogar de novo?[S/N] ")).upper()
                placar_2 = placar_2 + 1
            elif r == 2 and r1 == 1:
                print("Papel x Pedra PC_1 Ganhou!")
                S2 = str(input("Quer Jogar de novo?[S/N] ")).upper()
                placar_1 = placar_1 + 1
            elif r == 3 and r1 == 2:
                print("Tesoura x Papel PC_1 Ganhou!")
                S2 = str(input("Quer Jogar de novo?[S/N] ")).upper()
                placar_1 = placar_1 + 1
            elif r == 1 and r1 == 3:
                print("Pedra x Tesoura PC_1 Ganhou!")
                S2 = str(input("Quer Jogar de novo?[S/N] ")).upper()
                placar_1 = placar_1 + 1
        print(f"Computador_1: {placar_1} Vitórias")
        print(f"Computador_2: {placar_2} Vitórias")
#Fim
print("Fim de Jogo! feito por Vinicius Guilherme. Obrigado por jogar.")