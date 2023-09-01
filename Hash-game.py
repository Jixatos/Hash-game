# RM551408 | Juan de Godoy
# RM99708  | Gabriel Francisco Lobo

import random

def inicializarTabuleiro():
    while True:
        print("Jogar jogo da velha? Digite sim ou não")
        start = input("R:").lower()
        if start in ['s', 'sim']:
            tabuleiro = [['' for i in range(3)] for i in range(3)]
            return tabuleiro
        elif start in ['n', 'nao', 'não']:
            print("Tudo bem, tchau!")
            exit()

def imprimirTabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(f'  {linha[0]}  |  {linha[1]}  |  {linha[2]}')
        print("---------------")

def imprimeMenuPrincipal():
    while True:
        print("Selecione o modo de jogo")
        print("1 - PvP - modoJogador")
        print("2 - PvE - modoFacil")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            modoJogador()
        elif opcao == '2':
            modoFacil()
        else:
            print("Opção inválida. Escolha novamente.")

def leiaCoordenadaLinha():
    linha = input("Digite a linha que deseja jogar (1, 2 ou 3): ")
    return int(linha) - 1

def leiaCoordenadaColuna():
    coluna = input("Digite a coluna que deseja jogar (1, 2 ou 3): ")
    return int(coluna) - 1

def jogar(tabuleiro, jogador):
    linha = leiaCoordenadaLinha()
    coluna = leiaCoordenadaColuna()

    if tabuleiro[linha][coluna] == '':
        tabuleiro[linha][coluna] = jogador
    else:
        print("Posição inválida. Tente novamente.")
        jogar(tabuleiro, jogador)

def imprimePontuacao(player1, player2, maquinaF):
    print(f'A pontuação do Jogador 1 é de: {player1}')
    print(f'A pontuação do Jogador 2 é de: {player2}')
    print(f'A pontuação da máquina é de: {maquinaF}')

def posicaoValida(tabuleiro, linha, coluna):
    return tabuleiro[linha][coluna] == ''

def verificarVencedor(tabuleiro, jogador):
    for i in range(3):
        if all(linha == jogador for linha in tabuleiro[i]):  # Verifica linhas
            return True
        if all(coluna[i] == jogador for coluna in tabuleiro):  # Verifica colunas
            return True
    if all(tabuleiro[i][i] == jogador for i in range(3)):  # Verifica diagonal principal
        return True
    if all(tabuleiro[i][2 - i] == jogador for i in range(3)):  # Verifica diagonal secundária
        return True
    return False

def verificarVelha(tabuleiro):
    return all(all(linha != '' for linha in coluna) for coluna in tabuleiro)


def modoJogador():
    tabuleiro = inicializarTabuleiro()
    player1 = 0
    player2 = 0
    jogadas = 0
    
    while True:
        jogador = 'X' if jogadas % 2 == 0 else 'O'
        imprimirTabuleiro(tabuleiro)
        jogadaUsuario(tabuleiro, jogador)
        jogadas += 1
        
        if verificarVencedor(tabuleiro, jogador):
            imprimirTabuleiro(tabuleiro)
            print(f"Jogador {jogador} venceu!")
            if jogador == 'X':
                player1 += 1
            else:
                player2 += 1
            imprimePontuacao(player1, player2, 0)
            tabuleiro = inicializarTabuleiro()
            jogadas = 0
        elif verificarVelha(tabuleiro):
            imprimirTabuleiro(tabuleiro)
            print("Empate!")
            tabuleiro = inicializarTabuleiro()
            jogadas = 0

def jogadaUsuario(tabuleiro, jogador):
    print(f"Turno do Jogador {jogador}")
    jogar(tabuleiro, jogador)
    
def modoFacil():
    tabuleiro = inicializarTabuleiro()
    player1 = 0
    maquinaF = 0
    jogadas = 0
    
    while True:
        jogador = 'X' if jogadas % 2 == 0 else 'O'
        
        if jogador == 'X':
            imprimirTabuleiro(tabuleiro)
            print(f"Turno do Jogador {jogador}")
            jogar(tabuleiro, jogador)
        else:
            linha, coluna = jogadaMaquinaFacil(tabuleiro)
            tabuleiro[linha][coluna] = jogador
            print(f"A Máquina jogou na linha {linha + 1}, coluna {coluna + 1}")
            
        jogadas += 1
        
        if verificarVencedor(tabuleiro, jogador):
            imprimirTabuleiro(tabuleiro)
            if jogador == 'X':
                print("Jogador venceu!")
                player1 += 1
            else:
                print("Máquina venceu!")
                maquinaF += 1
            imprimePontuacao(player1, 0, maquinaF)
            tabuleiro = inicializarTabuleiro()
            jogadas = 0
        elif verificarVelha(tabuleiro):
            imprimirTabuleiro(tabuleiro)
            print("Empate!")
            tabuleiro = inicializarTabuleiro()
            jogadas = 0

def jogadaMaquinaFacil(tabuleiro):
    while True:
        linha = random.randint(0, 2)
        coluna = random.randint(0, 2)
        if posicaoValida(tabuleiro, linha, coluna):
            return linha, coluna
        

imprimeMenuPrincipal()