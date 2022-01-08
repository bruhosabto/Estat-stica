#!/usr/bin env python3

# concluido dia 8 de janeiro de 2022
#---------------------
#autor - bruno da silva santos
#---------------------
# script para o cálculo de valores de tabela de frequencia
# todos os calculos aqui utilizados foram dados em aula de estatistica da universidade estadual do maranhão - UEMA
#----------------------------------------------------------------------------------------------------------------
#Voce pode modificar este codigo de acordo com as suas necessidades, mantendo é claro, os créditos do criador original

import sys
import math
from typing import List
from random import randint
from colorama import Fore, Back, Style


Lista1 = [0] * 4
ListaG = [0] * 5
ListaH = [0] * 5
ListaI = [0] * 5



def Q3(h):
    li = ListaI[3]
    qi = ListaI[0]
    fiqi = ListaI[4]
    fantQ = ListaI[1]

    qi = li +((qi - fantQ)/fiqi)*h
    qi = round(qi,1)
    return qi

def Qii(h):
    li = ListaH[3]
    qi = ListaH[0]
    fiqi = ListaH[4]
    fantQ =ListaH[1]
    qi = li +((qi - fantQ)/fiqi)*h
    qi = round(qi,1)
    return qi
def Qi(h):
    li = ListaG[3]
    qi = ListaG[0]
    fiqi = ListaG[4]
    fantQ = ListaG[1]
    qi = li +((qi -fantQ)/fiqi)*h
    qi = round(qi,1)
    return qi

def Variancia(dv):
    S = math.sqrt(dv)
    return round(S,1)
def DesvioPadrao(SXi2Fi,SXiFi,total):

    step1 = 1/(total-1)
    step2 = SXi2Fi - ((math.pow(SXiFi,2)/total))
    Dv = math.sqrt(step1*step2)
    Dv = round(Dv,1)
    return Dv
def Media(SXiFi,total):
    media = round((SXiFi/total),1)
    return media
def SomatorioXi2Fi(Xi2Fi):
    Somatorio = 0
    contador = 0
    total = len(Xi2Fi)
    
    while contador < total:
        Somatorio +=Xi2Fi[contador]
        contador +=1
    return round(Somatorio,1)

def SomatorioXiFi(XiFi):

    Somatorio = 0
    contador = 0
    total = len(XiFi)
    
    while contador < total:
        Somatorio +=XiFi[contador]
        contador +=1
    return round(Somatorio,1)

def XI2FI(xi2,fi):

    contador = 0
    total = len(xi2)
    ListaRetorno = [0] * total

    while contador < total:
        ListaRetorno[contador] = round(xi2[contador]*fi[contador],1)
        contador +=1
    return ListaRetorno

def XIxFI(ListaFi,ListaXi):

    contador  = 0
    total = len(ListaXi)
    ListaRetorno = [0]*total
    while contador < total:
        ListaRetorno[contador] = round(ListaFi[contador] * ListaXi[contador],1)
        contador +=1
    return ListaRetorno

def Xi_2(Lista):#xi ao quadrado

    ListaXi2 = [0] * len(Lista)
    contador = 0
    valor = None

    while contador < len(Lista):
        Valor = Lista[contador]
        ListaXi2[contador] = round(math.pow(Valor,2),1)
        contador +=1

    return ListaXi2

def Xi(Lista,h,k):

    Menor = min(Lista)
    Maior = max(Lista)
    Proximo = (h + Menor)
    xi = None
    contador = 0
    ListaXi = [0] * (int(k)+1)

    while contador < (int(k)+1):

        xi = (Menor+Proximo)/2
        Menor = Proximo
        Proximo = Menor +h
        ListaXi[contador] = round(xi,1)
        contador +=1
    
    return ListaXi

    
def Classes(h,Lista,K):
    
    H = h
    
    Menor = min(Lista)
    Maior = max(Lista)
    Proximo = Menor+H
    Tamanho = len(Lista)
    Fac = 0
    Fr  = 0
    Fi = 0
    ListaFi = [0] *round((int(K)+2))
    contador = 0
    contadorFi = 0
    xi = (Menor+Maior)/2
    xi_fi = 0
    xi2_fi = 0
    x_tmp = 0
    #para quartil 1
    Qi = (Tamanho/4)
    CQi = 0
    contador_Qi = 0
    Li = 0
    FantQ = 0
    FiQi = 0
    ListaQi = [0]*5
    ListaQi[0] = Qi
    #para quartil 2
    Qii = (Tamanho/2)
    CQii = 0
    FantQii = 0
    ListaQii = [0] * 5
    ListaQii[0] = Qii
    contador_Qii = 0
    Lii = 0
    FiQii = 0
    #para quartil 3
    Q3 = (Tamanho*3)/4
    _CQii = 0
    FantQ3 = 0
    ListaQ3 = [0] * 5
    ListaQ3[0] = Q3
    contador_Q3 = 0
    FiQ3 = 0
    L3 = 0

    while contador < (Maior + H):
	
        for x in Lista:
            
            if float(x) >= Menor and float(x) < Proximo:
                Fi  = Fi + 1
                Fac = Fac + 1
            elif float(x) == Proximo:
                break
        Fr = (Fi/Tamanho) * 100
        Fr = round(Fr,1)
        xi = round((Menor+Proximo)/2,1)
        x_tmp = math.pow(xi,2)
        xi2_fi = round(x_tmp*Fi,1)
        xi_fi = round(xi*Fi,1)
        Menor = float(Menor)
        
        

        print (round(Menor,1),"->",round(Proximo,1),Back.WHITE+"        "+Style.RESET_ALL,Fi,Back.WHITE+ "        "+Style.RESET_ALL,Fac,Back.WHITE+"        "+Style.RESET_ALL,Fr,"%",Back.WHITE+"        "+Style.RESET_ALL,xi,Back.WHITE+"        "+Style.RESET_ALL,xi_fi,Back.WHITE+"        "+Style.RESET_ALL,xi2_fi)
        print (Back.RED+"-----------------------------------------------------------------------------------------------------------"+Style.RESET_ALL)
        Fr = 0
        xi_fi = 0.0
        xi = 0.0
        if Fac == Qi:
            CQi = Fac
        elif Fac < Qi:
            FantQ = Fac
            ListaQi[1] = FantQ
        if Fac > Qi and contador_Qi == 0:
            CQi = Fac
            FiQi = Fi
            ListaQi[2] = CQi
            contador_Qi +=1
            Li = Menor
            ListaQi[3] = Li
            ListaQi[4] = FiQi
        if Fac == Qii:
            CQii = Fac
        elif Fac < Qii:
            FantQii = Fac
            ListaQii[1] = FantQii
        if Fac > Qii and contador_Qii == 0:
            CQii = Fac
            FiQii = Fi
            ListaQii[2] = CQii
            contador_Qii +=1
            Lii = Menor
            ListaQii[3] = Lii
            ListaQii[4] = FiQii
        if Fac == Q3:
            _CQii = Fac
        elif Fac < Q3:
            FantQ3 = Fac
            ListaQ3[1] = FantQ3
        if Fac > Q3 and contador_Q3 == 0:
            _CQii = Fac
            FiQ3 =  Fi
            ListaQ3[2] = _CQii
            contador_Q3 +=1
            L3 = Menor
            ListaQ3[3] = L3
            ListaQ3[4] = FiQ3
        
        ListaFi[contadorFi] = Fi
        contadorFi +=1
        Menor = Proximo
        Proximo = Menor + H
        Fi = 0
        contador = Proximo
    #transerindo valores dos quartis para as listas globais
    xcontador = 0
    for x in ListaQi:
        ListaG[xcontador] = x
        xcontador +=1
    ycontador = 0
    for y in ListaQii:
        ListaH[ycontador] = y
        ycontador +=1
    zcontador = 0
    for z in ListaQ3:
        ListaI[zcontador] = z
        zcontador +=1
    #fim da transferencia
    
    return ListaFi

def Intervalor(r,k): # calculando o valor de H
    h = r / k
    return round(h,1)

def Anselmo(n): # FORMULA DE ANSELMO
    K = ((1 + (3.32*(math.log10(n))))/2)*math.log(n)
    return K

def Sturges(n):# Formula de Sturges
    K = 1 + (3.32*(math.log10(n)))
    return K

def ControleF(n,x):# controleF ira gerenciar a entrada da formula
    K = None

    if x == 's':
        K = Sturges(n)
    elif x == 'a':
       K = Anselmo(n)
    else:
        pass
    return round(K,1)

def Ranger(Lista):# calcula o ranger
    menor = min(Lista)
    maior = max(Lista)
    ranger = maior - menor
    return round(ranger,1)

def Sort(Lista):#ordena a lista

    menor = None
    contador = 0
    Lista_x = [0]*len(Lista)

    while len(Lista) > 0:
        menor = min(Lista)
        indez = Lista.index(menor)
        retirado = Lista.pop(indez)
        Lista_x[contador] = retirado
        contador +=1
    return Lista_x
def LerArquivo(Lista):# ler um arquivo passado pelo usuario

    print ("Digite abaixo o caminho do e o nome")
    print ("Exemplo: /home/fulano/Documentos/lista.txt")
    nome = input(":>")
    abrir = open(nome,"r")
    
    #percorrendo arquivo para saber o tamanho
    Tamanho = 0
    Tipo = Lista[1]
    
    for x in abrir:
        Tamanho +=1
        
    
    abrir.close()
    abrir = open(nome,"r")
    
    ListaRetorno = [0]*Tamanho
    contador = 0

    if Tipo == 'i':
        print (Fore.GREEN+"[+] Coletando valores inteiros"+Style.RESET_ALL)
        for x in abrir:
            ListaRetorno[contador] = int(x)
            contador +=1
        print (Fore.GREEN+"[+] Valores coletados com sucesso!"+Style.RESET_ALL)
    elif Tipo == 'd':
        print (Fore.GREEN+"[+] Coletando valores decimais"+Style.RESET_ALL)
        for x in abrir:
            ListaRetorno[contador] = float(x)
            contador +=1
        print (Fore.GREEN+"[+] Valcores coletados com sucesso!"+Style.RESET_ALL)
    else:
        print (Fore.YELLOW+"[!] O valores do arquivo nao sao inteiros nem decimais, tente informar um arquivo valido!"+Style.RESET_ALL)
        sys.exit(0)
    abrir.close()
    Lista[3] = str(Tamanho)
    Lista1 = Lista 
    
    return ListaRetorno


def Entrada_a_Decimal(q):# entrada automatica de valores decimais
    print("Iniciando a entrada automatica de valores aleatorios decimais")
    _q = int(q)
    Lista = [0]* _q
    contador = 0
    tmp = 0.5
    valor = 0
    while contador < _q:
        valor= randint(0,10)
        Lista[contador] = round(valor + tmp,1)
        
        if randint(0,1) == 1 and tmp < 0.5:
            tmp +=0.5
        else:
            tmp -=0.1
        contador +=1
    return Lista

def Entrada_a_Inteiro(q):# entrada automatica de valores inteiros
    print ("Iniciando a entrada automatica de valroes aletorios inteiros")
    _q = int(q)
    Lista = [0] * _q
    contador = 0
    while contador < _q:
        Lista[contador] = randint(1,100)
        contador +=1
    return Lista

def Entrada_m_Decimal(q):# entrada manual de valores decimais
    
    _q = int(q)
    Lista = [0] * _q
    contador = 0
    valor = None
    print ("Iniciando a entrada manual com valores decimais")
    try:
        while contador < _q:
            print("Insira o valor ",contador+1)
            Valor = input(":>")
            Lista[contador] = float(Valor)
            contador +=1
    except:
        print (Fore.YELLOW+"Nesta parte er permitido apenas valores inteiros!"+Style.RESET_ALL)
        sys.exit(0)
    return Lista

def Entrada_m_Inteiro(q):# entrada manual de valores inteiros
    _q = int(q)
    Lista = [0] * _q
    contador = 0
    print("Iniciando entrada manual com valores inteiros")
    try:
        while contador < _q:
            print("Insira o valor ",contador+1)
            Lista[contador] = int(input(":>"))
            contador +=1
    except:
        print (Fore.YELLOW+"[!] Nesta parte er permitido apenas valores inteiros"+Style.RESET_ALL)
        sys.exit(0)
    return Lista

def Controle(Lista):# gerencia a escolha de entrada de valores
    
    ListaRetorno = [0]*int(Lista[3])
    if Lista[0] =='m'  and Lista[1] == 'i':
        ListaRetorno = Entrada_m_Inteiro(Lista[3])
    elif Lista[0] == 'm'  and Lista[1] == 'd':
       ListaRetorno = Entrada_m_Decimal(Lista[3])
    if Lista[0] =='a'  and Lista[1] == 'i':
        ListaRetorno = Entrada_a_Inteiro(Lista[3])
    elif Lista[0] == 'a'  and Lista[1] == 'd':
        ListaRetorno = Entrada_a_Decimal(Lista[3])
    if Lista[0] == 'l':
        ListaRetorno = LerArquivo(Lista)
        
    
    return ListaRetorno

def Status(Lista): # printa a escolha do usuario
    
    print (Back.GREEN+"[+] Tipo de entrada -> ",Lista[0]+Style.RESET_ALL)
    print (Back.GREEN+"[+] Tipo de dados   -> ",Lista[1]+Style.RESET_ALL)
    print (Back.GREEN+"[+] Formula         -> ",Lista[2]+Style.RESET_ALL)
    print (Back.GREEN+"[+] Quantidade      -> ",Lista[3]+Style.RESET_ALL)
    

def Erro_entrada(Lista): # verifica a ocorrencia de erros

    if Lista[0] != 'm' and Lista[0] !='a' and Lista[0] !='l':
        return  Fore.RED+"[!] Um erro encontrado no tipo de entrada escolhido por voce!"+Style.RESET_ALL
    if Lista[1] != 'i' and Lista[1] !='d':
        return Fore.RED+"[!] Um erro encontrado no tipo de dados escolhido por voce!"+Style.RESET_ALL
    if Lista[2] !='s' and Lista[2] !='a':
        return Fore.RED+"[!] Um erro encontrado na formula escolhida!"+Style.RESET_ALL
    if int(Lista[3]) <= 0 and Lista[0] =='l':
    	pass
    elif int(Lista[3]) <=0 and Lista[0] != 'l':
        return Fore.RED+"[!] A quantidade escolhida nao er valida!"+Style.RESET_ALL
    return "[+] Nenhum erro encontrado!"

def Menu():# primeira entrada de dados

    quantidade = None
    retorno = None
    formula = None
    tipo    = None
    entrada = None

    print ("MENU")
    try:
        print ("escolha abaixo o tipo de entrada que deseja!")
        print ("[m] MANUAL")
        print ("[a] automatica aleatória")
        print ("[l] ler arquivo .txt")
        entrada = input(":>")

        print ("escolha abaixo o tipo de dado que deseja inserir")
        print ("[i] inteiros")
        print ("[d] decimal")
        tipo = input(":>")

        print ("escolha abaixo a formula para calcular o valor de k")
        print ("[s] STURGES")
        print ("[a] ANSELMO")
        formula = input(":>")
        if entrada != 'l' and entrada != 'L':
            print("digite abaixo a quantidade de dados que deseja inserir")
            quantidade = int(input(":>"))
        else:
            quantidade = 0
    except:
        print (FORE.RED+"Voce digitou alguma coisa erra, execute novamente e tente nao errar!"+Style.RESET_ALL)
        sys.exit(0)
    
    
    if entrada.isupper():
        entrada = entrada.lower()
    if tipo.isupper():
        tipo = tipo.lower()
    if formula.isupper():
        formula = formula.lower()
    
    retorno = [0]*4
    retorno [0] = entrada
    retorno [1] = tipo
    retorno [2] = formula
    retorno [3] = str(quantidade)
    
    return retorno

def main():
    Lista = Menu()
    print ("------------------------------------")
    if "[+] Nenhum erro encontrado!" != Erro_entrada(Lista):
    	print (Fore.RED+ "Status Erro -> ",Erro_entrada(Lista))
    	sys.exit(0)
    else:
    	Status(Lista)
    

    Lista_ = Controle(Lista)

    print ("[+]Lista inserida")
    
    print(Back.GREEN+str(Lista_)+Style.RESET_ALL)
    
    Lista_Ordenada = Sort(Lista_)
    print ("---------------------------")
    print ("[+]Lista ordenada abaixo")
    print (Back.GREEN+str(Lista_Ordenada)+Style.RESET_ALL)
    print ("---------------------------")
    ranger = Ranger(Lista_Ordenada)
    print (Back.GREEN+"[+] Ranger    -> ",str(ranger)+Style.RESET_ALL)
    K = ControleF(int(Lista[3]),Lista[2])
    print (Back.GREEN+"[+] K         -> ",str(K)+Style.RESET_ALL)
    H = Intervalor(ranger,K)
    print (Back.GREEN+"[+] Intervalo -> ",str(H)+Style.RESET_ALL)
    print ("   Classe           FI           FAC           FR           XI           XI*FI           XI²*FI")
    
    print (Back.YELLOW+"-----------------------------------------------------------------------------------------------------------"+Style.RESET_ALL)
    ListaFi = Classes(H,Lista_Ordenada,K)
    print (Back.YELLOW+"-----------------------------------------------------------------------------------------------------------"+Style.RESET_ALL)
    
    ListaXi=Xi(Lista_Ordenada,H,K)
    ListaXI2=Xi_2(ListaXi)
    ListaXiFi  = XIxFI(ListaFi,ListaXi)
    ListaXi2Fi =XI2FI(ListaXI2,ListaFi)
    somatorioXiFi = SomatorioXiFi(ListaXiFi)
    somatorioXi2Fi = SomatorioXi2Fi(ListaXi2Fi)
    desvioPadrao = DesvioPadrao(somatorioXi2Fi,somatorioXiFi,int(Lista[3]))
    variancia = Variancia(desvioPadrao)
    media = Media(somatorioXiFi,int(Lista[3]))
    cv = round((desvioPadrao/media)*100,1)
    
   
    print (Back.GREEN+"Somatorio XixFi -> ",str(somatorioXiFi)+Style.RESET_ALL)
    print (Back.YELLOW+"----------------------------#"+Style.RESET_ALL)

    print (Back.GREEN+"Somatario Xi2Fi -> ",str(somatorioXi2Fi)+Style.RESET_ALL)
    print (Back.YELLOW+"----------------------------#"+Style.RESET_ALL)

    print (Back.GREEN+"Media                   -> ",str(media)+Style.RESET_ALL)
    print (Back.YELLOW+"----------------------------#"+Style.RESET_ALL)

    print (Back.GREEN+"Desvio Padrao           -> ",str(desvioPadrao)+Style.RESET_ALL)
    print (Back.YELLOW+"----------------------------#"+Style.RESET_ALL)

    print (Back.GREEN+"Variancia               -> ",str(variancia)+Style.RESET_ALL)
    print (Back.YELLOW+"----------------------------#"+Style.RESET_ALL)
    print (Back.GREEN+"Coeficiente de variação -> ",str(cv),"%"+Style.RESET_ALL)
    print (Back.GREEN+"Quartil 1       -> ",str(Qi(H))+Style.RESET_ALL)
    print (Back.GREEN+"Quartil 2       -> ",str(Qii(H))+Style.RESET_ALL)
    print (Back.GREEN+"Quartil 3       -> ",str(Q3(H))+Style.RESET_ALL)
    
    
if __name__ == "__main__":
    main()
