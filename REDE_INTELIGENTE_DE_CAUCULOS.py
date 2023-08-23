from tkinter import *
import random
import string, random






# ESTE CODIGO COMBINA DIVERSAS FORMULAS









def movendo_digitos ():
    while True:
        BAGAGEM = [0,0,0]

            
            
        campo = ["PARTIDA",int(32),int(66),int(99),"CHEGADA"] ## TODOS OS NUMEROS DA variavel REGRA_DO_JOGO eles serÃO COMBINADOS ATE FORMAR PRIMEIRAMENTE O int(32) EM SEGUIDA COMBINARÁ O int(32)
        ### COM OUTROS NUMEROS DA REGRA DO JOGO E O MESMO COM O int(99)  ELE VAI GERAR MUITOS DADOS DAS COMBINAÇÕES AS QUAIS PODERÃO SER USADAS
        ### PARA DIVERSOS FINS DE COMBINAÇÕES, "O CODIGO PODE SER MODIFICADO E APERFEIÇOADO É GRATUITO PARA O USO DE TODOS.
        
        regras_do_jogo = [int(14),int(8),int(9),int(5),int(17),int(16),int(24),int(16),int(33),int(34),int(33),int(334),int(133),int(343),int(733),int(933),int(3333)]
        
        personagem = float(0.1)#### FUNÇÃO EM ANDAMENTO
        tiro = random.choice(regras_do_jogo)
        tiro_1 = random.choice(regras_do_jogo)

        conta = int(tiro+tiro_1)
        print(conta)
        if conta==campo[1]:
            BAGAGEM.insert(0,conta)
            print('PRIMEIRA PORTA')
            print(conta)
            #BAGAGEM.insert(0,conta)
        tiro_2 = random.choice(regras_do_jogo)
        if BAGAGEM[0]+tiro_2 == campo[2]:
            print("REGISTRADO = ",BAGAGEM[0]+tiro_2)
            conta_0 = BAGAGEM[0]+tiro_2
            BAGAGEM.insert(1,conta_0)
            print(tiro_2)
            
        tiro_3 = random.choice(regras_do_jogo)
        if BAGAGEM[1]+tiro_3 == campo[3]:
            print("REGISTRADO TERCEIRA PORTA= ",BAGAGEM[1]+tiro_3)
            conta_1 = BAGAGEM[1]+tiro_3
            BAGAGEM.insert(2,conta_1)
            print(tiro_3)
            print(BAGAGEM)
            break

       # input('tr')





