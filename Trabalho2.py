import sys
import math

def calcFunc (x: float, y: float):
    
    a = 2.0*math.exp((-(x-5)**2) /30 )
    b = 1.2*math.exp((-(x-6)**2) /11 )
    c = 0.9*math.exp((-(x-4)**2) /22 )
    d = 1.5*math.exp((-(y-1)**2) /38 )
    e = 1.2*math.exp((-(y-2)**2) /50 )

    return a + b + c + d + e

def FuncaoOtmizacao(estado: dict, inc: float):
    
    xmaior = None
    ymaior = None

    x = estado['x']
    y = estado['y']
    
    print(estado)
    xmaior = x
    ymaior = y
    maior = calcFunc(estado['x'], estado['y'])

    
    atual = calcFunc(x+inc,y)
    if( atual > maior):
        xmaior = x+inc
        ymaior = y
        maior = atual

    atual = calcFunc(x+inc,y+inc)
    if( atual > maior):
        xmaior = x+inc
        ymaior = y+inc
        maior = atual

    atual = calcFunc(x-inc,y+inc)
    if( atual > maior):
        xmaior = x-inc
        ymaior = y+inc
        maior = atual
    
    atual = calcFunc(x-inc,y)
    if( atual > maior):
        xmaior = x-inc
        ymaior = y 
        maior = atual

    atual = calcFunc(x-inc,y-inc)
    if( atual > maior):
        xmaior = x-inc
        ymaior = y-inc
        maior = atual
    
    atual = calcFunc(x,y-inc)
    if( atual > maior):
        xmaior = x
        ymaior = y-inc 
        maior = atual

    atual = calcFunc(x+inc,y-inc)
    if( atual > maior):
        xmaior = x+inc
        ymaior = y-inc 
        maior = atual

    print('direção escolhida: {}'.format(maior))
    return {'x':xmaior,'y':ymaior}


  

def hillClimbing(estadoInicial: dict, inc: float, iteracoes: int):

    estadoAtual = estadoInicial
    maior = None

    i = 0
    while i < iteracoes:
        
        proximoEstado = FuncaoOtmizacao(estadoAtual, inc)
        estadoAtual = proximoEstado
        i+=1


def main():

    # valores padrão

    x = None
    y = None
    inc = -1
    iteracoes = 50

    argumentos = sys.argv[1:]

    if not argumentos or not len(argumentos) == 4:
        raise SystemExit('Numero de Argumentos invalidos!')
   
    if argumentos[0].isalpha() or float(argumentos[0]) < -1 and float(argumentos[0]) > 7:
        raise SystemExit('Coordenada "x": o primeiro paramentro deve ser um numero entre -1 e 7!')
    else:
        x = float(argumentos[0])

    if argumentos[1].isalpha() or float(argumentos[1]) < -1 and float(argumentos[1]) > 7:
        raise SystemExit('Coordenada "y": o segundo paramentro deve ser um numero entre -1 e 7!')
    else:
        y = float(argumentos[1])

    if  argumentos[2].isalpha():
        raise SystemExit('incrmento: o terceiro paramentro deve ser um numero!')
    else:
        inc = float(argumentos[2])
    
    if argumentos[3].isalpha():
        raise SystemExit('nº iteracoes: o quarto paramentro deve ser um numero!')
    else:
        iteracoes = int(argumentos[3])

    print(x, y, inc, iteracoes)

    estadoInicial = {'x': x, 'y':y}

    hillClimbing(estadoInicial, inc, iteracoes)
    

main()