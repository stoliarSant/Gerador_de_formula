from tkinter import *
import random
import string, random
















def movendo_digitos ():
    while True:
        BAGAGEM = [0,0,0]

            
            
        campo = ["PARTIDA",int(32),int(66),int(99),"CHEGADA"]
        
        regras_do_jogo = [int(14),int(8),int(9),int(5),int(17),int(16),int(24),int(16),int(33),int(34),int(33),int(334),int(133),int(343),int(733),int(933),int(3333)]
        
        personagem = float(0.1)
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




movendo_digitos ()








def rede_neural():
    while True:
        
        salario = float(input("DIGITE O SALARIO"))
        pensao = float(input("DIGITE O PREÇO DA PENSÃO"))
        despeza = float(input("DIGITE O PREÇO DA DESPEZA COM COMIDA"))
        guardar = float(input("DIGITE O QUANTO QUER GUARDAR"))
        carro = float(45000)
        casa = float(10000)
        bike = float(5000)
        meses_para_prazos = float(30)

        lista = [salario,pensao,despeza,guardar,carro,casa,bike]#TUNEO 1 ENTRADA
        lista_0 = [(lista[0]-lista[1]),(lista[0]-lista[2]),(lista[0]-lista[3]),
                   lista[4],(lista[5]),(lista[6])]#TUNEO 1 PRIMEIRO PROCESSO /"ARMAZENAMENTO"/
        lista_1 = [(lista_0[0]-lista[2])]#TUNEO 1 SEGUNDO PROCESSO SALARIO - DESPEZA
        lista_2 = [(lista_1[0]-lista[3])]#TUNEO 1 TERCEIRO PROCESSO SALARIO - GUARDAR
        lista_3 = [lista_2[0]/30]#TUNEO 1 QUARTO PROCESSO SALARIO / POR 30 DIAS
        lista_4 = [carro/meses_para_prazos,]# PREÇO TOTAL DO CARRO DIVIDIDO PELO TOTAL DE MESES =  PREÇO MENSAL # ESSE É O RESULTADO FINAL
        lista_5 = [casa/meses_para_prazos,]# PREÇO TOTAL DA CASA DIVIDIDO PELO TOTAL DE MESES =  PREÇO MENSAL # ESSE É O RESULTADO FINAL
        lista_6 = [bike/meses_para_prazos,]# PREÇO TOTAL DA BIKE DIVIDIDO PELO TOTAL DE MESES =  PREÇO MENSAL # ESSE É O RESULTADO FINAL

        #AQUI NOS GERAREMOS AS HERANÇAS DE CAUCULOS E INFORMAÇÕES


        print(lista_0,'\n',lista_4,lista_5,'\n',lista_6)

        print('Sobrou = ',lista_2[0],'\n','Dividido por 30 dias = ',lista_3[0])

        #print(lista,'\n',lista_0)

        #tentativa_1(lista_3)


def tentativa_1(lista_3):
    janela_1 = Tk()
    janela_1.geometry('500x690')
    canvas_1 = Canvas(janela_1,width=20,height=20,bg='blue')
    canvas_1.place(x=lista_3[0],y=10)
    
    
    def fechar():
        canvas_1.after(1000,canvas_1.destroy)
        rede_neural ()
        
    acionar=Button(janela_1,text="ACIONAR",command=fechar)
    acionar.place(x=0,y=200)

    janela_1.mainloop()
#rede_neural()
