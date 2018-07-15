#############################################
# SCRIPT para resolver equações quadráticas #
#      (ou equações do segundo grau)        #
#                                           #
# 14/07/2018 (15/07/2018)        por: KRNS  #
#############################################

# MODULOS
import baskhara as bsk                                      #-- modulo criado por KRNS
import matplotlib.pyplot as mplot                           #-- modulo do SciPy.org (https://scipy.org/)
import numpy as np                                          #-- modulo do SciPy.org (https://scipy.org/)

# INICIANDO PROGRAMA
print()
print('### PROGRAMA PARA EQUAÇÕES DE SEGUNDO GRAU ###')
print()


# VALIDADORES
a = 0
b = 0
c = 0
valida_a = False
valida_b = False
valida_c = False

# OBTENDO A
while valida_a == False:
    a = input('Entre com o valor de \'a\': ')
    try:
        a = float(a)
        valida_a = True
    except:
        print('[!] Número inválido. O valor de \'a\' deve ser um número real, positivo ou negativo. [!]\n')

# OBTENDO B
while valida_b == False:
    b = input('Entre com o valor de \'b\': ')
    try:
        b = float(b)
        valida_b = True
    except:
        print('[!] Número inválido. O valor de \'b\' deve ser um número real, positivo ou negativo. [!]\n')

# OBTENDO C
while valida_c == False:
    c = input('Entre com o valor de \'c\': ')
    try:
        c = float(c)
        valida_c = True
    except:
        print('[!] Número inválido. O valor de \'c\' deve ser um número real, positivo ou negativo. [!]\n')


# EXIBINDO EQUAÇÃO
print()
txtEquacao = '(' + str(a) + ')x^2 + (' + str(b) + ')x + (' + str(c) + ') = 0'
print( 'Equação: ' + txtEquacao )
print()

delta = bsk.calculaDelta(a,b,c)                             #-- calcula delta da equação
print('Delta = ' + str(delta) + '.')                        #-- exibe o valor de delta
print('Delta:', bsk.validaDelta(delta))                     #-- valida valor obtido para delta
print('A:'    , bsk.validaA(a))                             #-- valida valor obtido para a
print('C:'    , bsk.validaC(c))                             #-- valida valor obtido para c

if delta >= 0:
    
    # CALCULO DAS RAÍZES
    x1 = bsk.calculaX1(a,b,c,delta)                         #-- calcula raíz 1 da equação
    x2 = bsk.calculaX2(a,b,c,delta)                         #-- calcula raíz 2 da equação
    print('Raízes: x1 = ' + str(x1) + ' e x2 = ' + str(x2) + '.')

    # VÉRTICE DA PARÁBOLA
    xv = bsk.verticeX(a,b)                                  #-- calcula ponto X do vértice da parábola
    yv = bsk.verticeY(a,delta)                              #-- calcula ponto Y do vértice da parábola
    print('Vértice da parábola em (' + str(xv) + ',' + str(yv) + ').')
    print()

    # PONTOS BÁSICOS PARA GRÁFICO
    pontosBasicos  = [                                      #-- X, Y, Legenda, Cor, Marcador
        [0,  c,  'Encontra Y (0,c)', 'orange', 'o'],        #-- ponto onde a parábola cruza o eixo y
        [xv, yv, 'Vértice (xv,yv)',  'black',  'x'],        #-- ponto do vértice da parábola (max ou min)
        [x1, 0,  'Raíz 1 (x1,0)',    'red',    '^'],        #-- ponto da raíz 1 de x para y = 0
        [x2, 0,  'Raíz 2 (x2,0)',    'green',  '^']         #-- ponto da raíz 2 de x para y = 0
    ]

    # DEFININDO INTEVALO xInicio e xFim PARA GRÁFICO
    raizesX = [x1, x2]                                      #-- cria lista com valores das raízes de x
    raizesX.sort()                                          #-- ordena lista do menor valor para o maior
    xInicio = int(raizesX[0]) - 2                           #-- define valor inicial de X para gráfico
    xFim    = int(raizesX[1]) + 2                           #-- define valor final de X para gráfico

    # GERANDO VALORES INTERMEDIÁRIOS PARA GRÁFICO
    xValores = []                                           #-- valores de x para criar gráfico
    yValores = []                                           #-- valores de y para criar gráfico
    for xValor in np.linspace(xInicio, xFim, 1000):         #-- loop for para gerar os valores de x e y
        yValor = ( a * xValor**2 ) + ( b*xValor ) + c       #-- f(x) = ax^2 + bx + c
        xValores.append(xValor)                             #-- guarda valores de x na lista
        yValores.append(yValor)                             #-- guarda valores de y na lista

    # INICIANDO GRÁFICO
    plot    = mplot.figure(                                 #-- cria figura principal do gráfico (plot)
        num='ESG -' + txtEquacao        #-- insere título na janela do gráfico
    )                 
    subplot = plot.add_subplot(111)                         #-- cria figura secundária do gráfico (subplot)

    # GERANDO O GRÁFICO    
    mplot.plot(                                             #-- exibe valores f(x) e x gerados para gráfico
        xValores,                                           #-- valores x para desenhar parábola
        yValores,                                           #-- valores y para desenhar parábola
        zorder=1                                            #-- ordem de exibição no gráfico: maior = topo
    )

    # INSERE PONTOS BÁSICOS NO GRÁFICO
    print('Os pontos de referência, são:')
    pontosBasicosGrafico = []                               #-- lista para pontos básicos após inserção com SCATTER()
    pontosBasicosLegenda = []                               #-- lista para legenda dos pontos básicos
    for ponto in pontosBasicos:
        pontosBasicosGrafico.append(
            subplot.scatter(                                #-- insere pontos individuais no gráfico
                ponto[0],                                   #-- ponto[0] = x
                ponto[1],                                   #-- ponto[1] = y
                marker=ponto[4],                            #-- ponto[4] = marcador
                color=ponto[3],                             #-- ponto[3] = cor
                zorder=2                                    #-- ordem de exibição no gráfico: maior = topo
            )
        )
        pontosBasicosLegenda.append(ponto[2])               #-- ponto[2] = legenda
        print(
            ' '+str(ponto[2])+': ('+str(ponto[0])+','+str(ponto[1])+')'
        )                                                   #-- imprime no console pontos de referência

    # INSERE LEGENDA DOS PONTOS BÁSICOS
    mplot.legend(
        pontosBasicosGrafico,                               #-- lista dos pontos básicos inseridos individualmente no gráfico com SCATTER()
        pontosBasicosLegenda,                               #-- lista das legendas dos pontos básicos
        loc='lower left',                                   #-- posição da legenda no gráfico
        ncol=2,                                             #-- número de colunas da legenda
        fontsize=6                                          #-- tamanho do texto dentro da legenda
    )

    # CONFIGURA OPÇÕES DO GRÁFICO
    subplot.set_xlabel('x')                                #-- insere o nome do eixo x
    subplot.set_ylabel('y = f(x)')                         #-- insere o nome do eixo y
    subplot.set_title('EQUAÇÃO DO SEGUNDO GRAU')           #-- insere o título do gráfico
    mplot.grid()                                           #-- exibe a grade de referência no gráfico
    mplot.show()                                           #-- exibe o gráfico criado
    print()

elif delta < 0:
    
    print('Delta = ' + str(delta) + '. Este script ainda não está preparado para cálculos complexos.')
    print()

    # CALCULO DAS RAÍZES
    x1 = bsk.calculaX1(a,b,c,delta)                        #-- calcula raíz 1 da equação
    x2 = bsk.calculaX2(a,b,c,delta)                        #-- calcula raíz 2 da equação
    print('Raízes: x1 = ' + str(x1) + ' e x2 = ' + str(x2) + '.')
    print()

else:
    
    print('Delta = ' + str(delta) + '. OMG! Pitágoras ficou encanado agora...')
    print()

# FINALIZANDO PROGRAMA
print('### FIM ###')
print()