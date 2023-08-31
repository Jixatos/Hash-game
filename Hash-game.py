
#Inicializa o processo, imprime direto o Menu principal que deve receber um input para entrada da próxima ação.
def inicializarTabuleiro():
    while True:
        print("Jogar jogo da velha? Digite sim ou não")
        start = input("R:").lower()
        match start:
            case 's'| 'sim':
                tabuleiro = [[], [], []]
                imprimeMenuPrincipal()
                return tabuleiro
            case 'n' | 'nao' | 'não':
                print("Tudo bem, tchau!")
                break

#Valores devem ser o "O", para o círculo, e "X", para o xis.
def imprimirTabuleiro(tabuleiro):
    print(f'  {tabuleiro[0][0]}  |  {tabuleiro[0][1]}  |  {tabuleiro[0][2]}')
    print("---------------")
    print(f'  {tabuleiro[1][0]}  |  {tabuleiro[1][1]}  |  {tabuleiro[1][2]}')
    print("---------------")
    print(f'  {tabuleiro[2][0]}  |  {tabuleiro[2][1]}  |  {tabuleiro[2][2]}')

def imprimeMenuPrincipal():
    print("Selecione o modo de jogo")
    print("PvP - modoJogador")
    print("PvE - modoFacil")


def leiaCoordenadaLinha()
    linha = input("Digite a linha que deseja saber as coordenadas.")
    print("Digite no seguinte formato: linha X \nCom \"X\" sendo o número da linha")
    match linha:
        case "linha 1" | "Linha 1" | "LINHA 1":
            print("A linha 1 tem como coordenada: 1")
        case "linha 2" | "Linha 2" | "LINHA 2":
            print("A linha 2 tem como coordenada: 2")
        case "linha 3" | "Linha 3" | "LINHA 3":
            print("A linha 3 tem como coordenada: 3")
        case _:
            print("Por favor digite no formato descrito anteriormente \nFormato: linha X")


def leiaCoordenadaColuna(tabuleiro, posicao):
    coluna = input("Digite a coluna que deseja saber as coordenadas.")
    print("Digite no seguinte formato: Coluna X \nCom \"X\" sendo o número da Coluna")
    match coluna:
        case "Coluna 1" | "coluna 1" | "COLUNA 1":
            print("A Coluna 1 tem como coordenada: 1")
        case "Coluna 2" | "coluna 2" | "COLUNA 2":
            print("A Coluna 2 tem como coordenada: 2")
        case "Coluna 3" | "coluna 3" | "COLUNA 3":
            print("A Coluna 3 tem como coordenada: 3")
        case _:
            print("Por favor digite no formato descrito anteriormente \nFormato: Coluna X")

def imprimePontuacao():
    player1 = 0
    player2 = 0
    maquinaF = 0
    print(f'A pontuação do Jogar 1 é de: {player1}')
    print(f'A pontuação do Jogar 2 é de: {player2}')
    print(f'A pontuação da maquina é de: {maquinaF}')

def posicaoValida(tabuleiro, linha, coluna):
    if tabuleiro[linha-1][coluna-1] == "":
        return True
    else:
        return False
