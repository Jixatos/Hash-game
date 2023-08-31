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
    print("Selecione o modo de jogo")
    print("PvP - modoJogador")
    print("PvE - modoFacil")

def leiaCoordenadaLinha():
    linha = input("Digite a linha que deseja jogar (1, 2 ou 3): ")
    return int(linha) - 1

def leiaCoordenadaColuna():
    coluna = input("Digite a coluna que deseja jogar (1, 2 ou 3): ")
    return int(coluna) - 1

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


def jogoDaVelha():
    tabuleiro = inicializarTabuleiro()
    player1 = 0
    player2 = 0
    maquinaF = 0
    jogadas = 0
    

    while True:
        
        jogador = 'X'
        if jogadas % 2 == 0:
            jogador = 'X'
        else:
            jogador = 'O'
            
        imprimirTabuleiro(tabuleiro)
        print(f"Turno do Jogador {jogador}")
        
        linha = leiaCoordenadaLinha()
        coluna = leiaCoordenadaColuna()
        
        if posicaoValida(tabuleiro, linha, coluna):
            tabuleiro[linha][coluna] = jogador
            jogadas += 1
            
            if verificarVencedor(tabuleiro, jogador):
                imprimirTabuleiro(tabuleiro)
                print(f"Jogador {jogador} venceu!")
                if jogador == 'X':
                    player1 += 1
                else:
                    player2 += 1
                imprimePontuacao(player1, player2, maquinaF)
                tabuleiro = inicializarTabuleiro()  # Reinicia o jogo
                jogadas = 0
            elif verificarVelha(tabuleiro):
                imprimirTabuleiro(tabuleiro)
                print("Empate!")
                tabuleiro = inicializarTabuleiro()  # Reinicia o jogo
                jogadas = 0
        else:
            print("Posição inválida. Tente novamente.")

jogoDaVelha()
