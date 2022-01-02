#--------------------------------------------
#scrypt criado com o objetivo de facilitar uma ativade, o tempo gasto na construcao deste, poderia ser o tempo que levaria pra responder
#a atividade, mas eu sou otario mesmo
#----------------------------------------
#bruno santos
import math,sys
from random import randint


def bubble_sort(lista):# funcao recebe a lista passada pelo usuario e gera uma nova lista ordenada

    tm = len(lista)
    menor = 0
    menor_lista = [0] * tm # a nova lista er criada com o mesmo tamanho da recebida, aqui ela er preenchida com zeros
    cont = 0
    while len(lista) > 0:
    
        menor = min(lista) # pega o menor elemento da lista recebida
        ind = lista.index(menor) # pega o index do menor elemento
        retirado = lista.pop(ind) # remove o menor elemento passado pelo index
        menor_lista[cont] = retirado # adiciona o elemento retirado
        cont = cont +1
        
    return menor_lista # ao final retorna a lista ordenada

def strurger(lista):# usa a formula de sturgers
    n = len(lista)
    k = 1 + (3.32 *(math.log(n,10)))
    return k # retorna o valor obtido 

def Anselmo(Lista):
    n = len(Lista)
    K = 1 + (3.32 *(math.log(n,e)/2))
    return K
def intervalor_classe(ranger,k): # calcula o h

    h = (ranger / k)
    
    return h # retorna o valor obtido


def fi(lista,h): # calcula a frequencia acumulada

    
    mx = min(lista) # menor da lista
    menor = float(mx) # converter em float

    menor = round(menor,1)
    proximo = round(menor + h,1)

    _ocorre = 0 # variavel que iria receber a ocorrencia entre o intervalo menor => _ocorre < proximo
    cont = 0.0
    y = max(lista) # pega o maior valor da lista
    maior = float(y)
    fr =  0
    fac = 0
    total = len(lista) # para a fr

    while cont < (maior+h):

        for x in lista:

            if float(x) >= menor and float(x) < proximo:
                _ocorre = _ocorre + 1
                fac  = fac + 1
            elif float(x) == proximo:
                break
        fr = (_ocorre/total)*100
        
        print ("|",round(menor,1)," ->", round(proximo,1),"| ",_ocorre,"  | ", round(fac,0),"   |",round(fr,0),"%")
        print ("|-------------|------|-------|--------|")
        fr = 0
        menor = proximo 
        proximo = menor + h

        _ocorre = 0
        cont = proximo


def Aleatorio(quantidade,tipo):
	Lista = [0] * quantidade
	contador = 0
	incremental = 0.5
	if tipo == 'i':
	
		
		
		while contador < quantidade:
			Lista[contador] = randint(0,100)
			contador +=1
			
	elif tipo == 'd':
		
		while contador < quantidade:
			Lista[contador] = randint(0,100)+incremental
			
			if randint(0,1) == 1:
				incremental += 0.1
			elif randint(0,1) == 0:
				incremental += 0.2
			else:
				pass
			contador +=1
	else:
		print ("O tipo informado nao existe nesse escorpo!")
	
	return Lista

def _Log(arg,valor):
	log = ""
	ax = ''
	
	if valor == 1: # primeira entrada
		if arg == 1: 
			log += "[+] ENTRADA DE DADOS -> MANUAL!\n"
		elif arg == 2:
			log += "[+] ENTRADA DE DADOS -> AUTOMATICA!\n"
		else:
			log += "[?] ENTRADA DESCONHECIDA!\n"
			
	elif valor == 2:
		ax = str(arg)
		
		if ax == 'i':
			log += "[+] TIPO DE DADOS -> INTEIROS!\n"
		elif ax == 'd':
			log += "[+] TIPO DE DADOS -> DECIMAIS!\n"
		else:
			log += "[+] TIPO DE DADOS -> DESCONHECIDO!\n"
	if valor == 3:
		log += "[+] QUANTIDADE DADOS -> "+str(arg)
	else:
		pass
	return log
	
def main():

    _log = ""
    Formula = None
    print ("\t\t[---* MENU *---]")
    print ("============================================================")
    print ("[!] ESCOLHA ABAIXO O NUMERO CORRESPONDENTE A OPCAO DESEJADA!")
    print ("[ 1 ] -> INSERIR DADOS MANUALMENTE!")
    print ("[ 2 ] -> GERAR DADOS AUTOMATICOS E ALEATORIOS!")
    print ("[ 0 ] -> SAIR!")
    _esc = int(input("INSIRA AQUI SUA ESCOLHA :>"))
    _log = _Log(_esc,1)
    if _esc == 0:
    	print ("[+] STATUS -> SAINDO...")
    	sys.exit(0)
    
    print("============================================================")
    print ("[ ESCOLHA ENTRE INTEIRO OU DECIMAL ABAIXO ]")
    print ("[ i ] INTEIRO!")
    print ("[ d ] DECIMAL!")
    _tipo = input("INSIRA AQUI SUA ESCOLA :>")
    _log += _Log(_tipo,2)
    print ("============================================================")   
    _quant = int(input("_quant DE DADOS DESEJADA :>"))
    _log += _Log(_quant,3)
    print ("============================================================")
    print ("[ 1 ] Sturges!")
    print ("[ 2 ] Anselmo!")
    Formula = int(input(":>"))
    print ("============================================================")
    print ("DADOS")
    print (_log)
    print ("============================================================")   
    string = [0]  * _quant
    _contador = 0
    
    if _esc == 1 and _tipo == 'i':
    	
    	
    	while _contador < _quant:
    		
    		print ("INSIRA O VALOR",_contador + 1, "ABAIXO!")
    		string[_contador] = int(input("DIGITE AQUI :>"))
    		_contador +=1
    if _esc == 1 and _tipo == 'd':
    
     	while _contador < _quant:
    	  print ("INSIRA O VALOR",_contador + 1, "ABAIXO!")
    	  string[_contador] = float(input("DIGITE AQUI :>"))
    	  _contador +=1
    
    
    if _esc == 2 and _tipo == 'i':
    	string = Aleatorio(_quant,"i")
    elif _esc == 2 and _tipo == 'd':
    	string = Aleatorio(_quant,"d")
    else:
    	print ("Combinacao de entrada e tipo nao definida!")
    	sys.exit(0)
    
   #daqui para baixo ocorre os momentos finais
    lista_ordenada = bubble_sort(string) # ordena em ordem crescente

    if Formula == 1:	
    	st = strurger(lista_ordenada) #chama a formula de Sturges e guarda o valor retornado em st
    elif Formula == 2:
    	st = Anselmo(lista_ordenada) #chama a formula de Anselmo
    else:
    	print ("Formula nao existe no escorpo!")
    	sys.exit(0)
    	
    m_1 = min(lista_ordenada) # pega o menor valor da lista
    m_2 = max(lista_ordenada) # pega o maior valor da lista

    menor = float(m_1) # convert o menor valor que esta em str para decimal
    maior = float(m_2) # convert o maior valor que esta em str para decimal

    ranger = maior - menor # calcula o ranger
    ranger = round(ranger,1) # pega apenas duas casas decimais apos a virgula
    H = intervalor_classe(ranger,st) # onde st er o k
    H = round(H,1)

    #----- limpar o console -----
    
    print("|--------------|")
    print("|lista ordena  |")
    print("|--------------|")
    print (lista_ordenada)
    print("--------------------------------------")
    print ("formula de strurger   : ",round(st,1))
    st = round(st,1) #pega apenas duas casas decimais e guarda em st

    print ("ranger                : ",ranger)
    print ("intervalo de classe   : ",H)
    print ("--------------------------------------")

    print ("--------------------------------------")
    print ("\t\tClasses")
    print ("--------------------------------------")
    print ("|Notas        |  Fi  |  Fac  | Fr     |")
    print ("|-------------|------|-------|--------|")
    fi(lista_ordenada,H)
    
    e = None
    while e != 'e':

        e = None
        e = input("digite 'e' para sair:")

        
        if e == 'e' or e == 'E':
            sys.system("exit")
        elif e != 'e' or e != 'E':
            print ("Digite e para sair")
        else:
            pass

if __name__ == "__main__":
    main()
