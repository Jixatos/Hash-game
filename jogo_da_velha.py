
def inicializarTabuleiro():
    while True:
        print("Jogar jogo da velha? Digite sim ou não")
        start = input("R:").lower()
        match start:
            case 's'| 'sim':
                tabuleiro = [[0,0,0], [0,0,0], [0,0,0]]
                return tabuleiro
            case 'n' | 'nao' | 'não':
                print("Tudo bem, tchau!")
                break

def imprimirTabuleiro(t):
    print(f'{t[0][0]} | {t[0][1]} | {t[0][2]}')
    print("----------------")
    print(f'{t[1][0]} | {t[1][1]} | {t[1][2]}')
    print("--------------------------------------------------")
    print(f'{t[2][0]} | {t[2][1]} | {t[2][2]}')

def imprimeMenuPrincipal():
    print("PvP - modoJogador")
    print("PvE - modoFacil")

def leiaCoordenadaLinha(t):
    for i,x in enumerate(t):
        return t[i]

def leiaCoordenadaColuna():

def posicaoValida(tabuleiro):
    for i in tabuleiro:
        for j in i:
            if j == 0:
                return True
            else:
                return False
