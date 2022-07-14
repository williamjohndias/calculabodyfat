#calculadora de BF (método utilizado pela marinha dos EUA)
import math
def calculaBF():
    print('Você é homem ou mulher? (h / m)\nPara sair digite "q"')
    sexo = str(input('responda: '))
    while True:
        if sexo == 'h':
            homem()
        elif sexo == 'm':
            mulher()
        elif sexo == 'q':
            print('fechando o programa...')
            break
def homem():
    try:
        altura = int(input('Qual sua altura em cm? '))
        cintura = int(input('Circunferência da cintura: '))
        pescoco = int(input('Circunferência do pescoço: '))
    except ValueError:
        print("Digite um número...")
        homem()
    BF = 495 / (1.0324 - 0.19077 * math.log10(cintura - pescoco) + 0.15456 * math.log10(altura)) - 450
    print(BF,'%')
    calculaBF()

def mulher():
    try:
        altura = int(input('Qual sua altura em cm? '))
        cintura = int(input('Circunferência da cintura: '))
        pescoco = int(input('Circunferência do pescoço: '))
        quadril = int(input('Circunferência do quadril'))
    except ValueError:
        print("Digite um número...")
        mulher()
    BF = 495 / (1.29579 - 0.35004 * math.log10(cintura + quadril - pescoco) + 0.22100 * math.log10(altura)) - 450
    print(BF,'%')
    calculaBF()

calculaBF()
