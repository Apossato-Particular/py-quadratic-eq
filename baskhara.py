#############################################
# SCRIPT para resolver equações quadráticas #
#      (ou equações do segundo grau)        #
#                                           #
# 14/07/2018                     por: KRNS  #
#############################################

import math                                                     #-- modulo nativo do Python
import cmath                                                    #-- modulo nativo do Python

def calculaDelta(a,b,c):
    delta = b**2 - 4*a*c
    return delta

def calculaX1(a,b,c,delta):
    if delta >= 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)                  #-- cálculo para raízes reais (delta >= 0)
    elif delta < 0:
        x1 = (-b + cmath.sqrt(delta)) / (2 * a)                 #-- cálculo para raízes complexas (delta < 0)
    return x1

def calculaX2(a,b,c,delta):
    if delta >= 0:
        x2 = (-b - math.sqrt(delta)) / (2 * a)                  #-- cálculo para raízes reais (delta >= 0)
    elif delta < 0:
        x2 = (-b - cmath.sqrt(delta)) / (2 * a)                 #-- cálculo para raízes complexas (delta < 0)
    return x2

def verticeX(a,b):
    xv = -b / (2 * a)
    return xv

def verticeY(a,delta):
    yv = -delta / (4 * a)
    return yv

def validaDelta(delta):
    if delta > 0:
        msg = 'Equação possui duas raízes reais e distintas.'
    elif delta == 0:
        msg = 'Equação possui apenas uma raíz real e distinta.'
    elif delta < 0:
        msg = 'Equação não possui raízes reais.'
    else:
        msg = 'OMG! Pitágoras ficou encanado agora...'
    return msg

def validaA(a):
    if a > 0:
        msg = 'Concavidade da parábola para cima.'
    elif a == 0:
        msg = 'Não é uma equação de segundo grau. Não tem parábola, mas uma reta.'
    elif a < 0:
        msg = 'Concavidade da parábola para baixo.'
    else:
        msg = 'OMG! Pitágoras ficou encanado agora...'
    return msg

def validaC(c):
    msg = 'O ponto onde a parábola toca o eixo Y é: (0, ' + str(c) + ')'
    return msg