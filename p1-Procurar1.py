nome = (input('nome do ficheiro(com extensão)'))    #pergunta o nome do ficheiro e guarda em nome
s = open(nome)              # abre o ficheiro para poder ler
linhas = int(s.readline())     # lê o numero de linhas e transforma em inteiro
palavras = list()           #cria nova lista vazia
sopal = list()               #cria nova lista vazia
for i in range(linhas):         #percorre as x linhas seguintes e coloca na lista
    palavras.append((s.readline().rstrip().upper()))
line = s.readline()
while line!='':     #percorre o ficheiro até ao fim e adiciona á matriz sopa
    sopal.append((line.rstrip()))
    line = s.readline()
####################################################################################################
#este- Esta função percorre cada linha da sopa de letras da esquerda para a direita
#
#Argumentos:
#palavra- Lista com cada palavra a procurar na sopa de letras
#inicial- Tuplo onde foi encontrada a primeira letra da palavra
#sopa-Lista com cada linha da sopa de letras
#Valor de retorno:
#coordenada da primeira e última letra da palavra, direção em que a palavra está na sopa de letras
####################################################################################################
def este(palavra,inicial,sopa):
    index = 1
    while index < len(palavra) and index + inicial[1] < len(sopa[inicial[0]]):
        if palavra[index]!=sopa[inicial[0]][index + inicial[1]]:
            break
        if index == (len(palavra)-1):
            if palavra[index]==sopa[inicial[0]][index + inicial[1]]:
                print('%s : %d%s-%d%s, este' % (palavra.lower(),inicial[0]+1,chr(97+inicial[1]),inicial[0]+1,chr(97+inicial[1]+index)))
                return True
        index += 1
####################################################################################################
#oeste- Esta função percorre cada linha da sopa de letras da direita para a esquerda
#
#Argumentos:
#palavra- Lista com cada palavra a procurar na sopa de letras
#inicial- Tuplo onde foi encontrada a primeira letra da palavra
#sopa-Lista com cada linha da sopa de letras
#Valor de retorno:
#coordenada da primeira e última letra da palavra, direção em que a palavra está na sopa de letras
####################################################################################################
def oeste(palavra,inicial,sopa):
    index = 1
    while (inicial[1]-index >= 0 and index<len(palavra)):
        if(palavra[index]!=sopa[inicial[0]][inicial[1]-index]):
            break
        if index == (len(palavra)-1):
            if palavra[index]==sopa[inicial[0]][-index + inicial[1]]:
                print('%s : %d%s-%d%s, oeste' % (palavra.lower(),inicial[0]+1,chr(97+inicial[1]),inicial[0]+1,chr(97+inicial[1]-index)))
                return True
        index+=1
####################################################################################################
#sul- Esta função percorre cada linha da sopa de letras de cima para baixo
#
#Argumentos:
#palvra- Lista com cada palavra a procurar na sopa de letras
#inicial- Tuplo onde foi encontrado a primeira letra da palavra
#sopa-Lista com cada linha da sopa de letras
#Valor de retorno:
#coordenada da primeira e última letra da palavra, direção em que a palavra está na sopa de letras
####################################################################################################
def sul(palavra,inicial,sopa):
    index = 1
    while (index + inicial[0] < len (sopa) and index<len(palavra)):
        if(palavra[index]!=sopa[inicial[0]+index][inicial[1]]):
            break
        if index == (len(palavra)-1):
            if palavra[index]==sopa[inicial[0]+index][inicial[1]]:
                print('%s : %d%s-%d%s, sul' % (palavra.lower(),inicial[0]+1,chr(97+inicial[1]),inicial[0]+index+1,chr(97+inicial[1])))
                return True
        index+=1
####################################################################################################
#norte- Esta função percorre cada linha da sopa de letras de baixo para cima
#
#Argumentos:
#palvra- Lista com cada palavra a procurar na sopa de letras
#inicial- Tuplo onde foi encontrado a primeira letra da palavra
#sopa-Lista com cada linha da sopa de letras
#Valor de retorno:
#coordenada da primeira e última letra da palavra, direção em que a palavra está na sopa de letras
####################################################################################################
def norte(palavra,inicial,sopa):
    index = 1
    while (inicial[0]-index >= 0 and index<len(palavra)):
        if(palavra[index]!=sopa[inicial[0]-index][inicial[1]]):
            break
        if index == (len(palavra)-1):
            if palavra[index]==sopa[inicial[0]-index][inicial[1]]:
                print('%s : %d%s-%d%s, norte' % (palavra.lower(),inicial[0]+1,chr(97+inicial[1]),inicial[0]-index+1,chr(97+inicial[1])))
                return True
        index+=1
############################################################################################################
#sudeste- Esta função percorre cada linha da sopa de letras da esquerda para a direita e de cima para baixo
#
#Argumentos:
#palvra- Lista com cada palavra a procurar na sopa de letras
#inicial- Tuplo onde foi encontrado a primeira letra da palavra
#sopa-Lista com cada linha da sopa de letras
#Valor de retorno:
#coordenada da primeira e última letra da palavra, direção em que a palavra está na sopa de letras
############################################################################################################
def sudeste(palavra,inicial,sopa):
    index = 1
    while ((index + inicial[0] < len (sopa))and (index + inicial[1] < len(sopa[inicial[0]])) and (index<len(palavra))):
        if(palavra[index]!=sopa[inicial[0]+index][inicial[1]+index]):
            break
        if index == (len(palavra)-1):
            if palavra[index]==sopa[inicial[0]+index][inicial[1]+index]:
                print('%s : %d%s-%d%s, sudeste' % (palavra.lower(),inicial[0]+1,chr(97+inicial[1]),inicial[0]+index+1,chr(97+inicial[1]+index)))
                return True
        index+=1
############################################################################################################
#sudoeste- Esta função percorre cada linha da sopa de letras da direita para a esquerda e de cima para baixo
#
#Argumentos:
#palvra- Lista com cada palavra a procurar na sopa de letras
#inicial- Tuplo onde foi encontrado a primeira letra da palavra
#sopa-Lista com cada linha da sopa de letras
#Valor de retorno:
#coordenada da primeira e última letra da palavra, direção em que a palavra está na sopa de letras
############################################################################################################
def sudoeste(palavra,inicial,sopa):
    index = 1
    while ((index + inicial[0] < len (sopa)) and (inicial[1]-index >= 0) and (index<len(palavra))):
        if(palavra[index]!=sopa[inicial[0]+index][inicial[1]-index]):
            break
        if index == (len(palavra)-1):
            if palavra[index]==sopa[inicial[0]+index][inicial[1]-index]:
                print('%s : %d%s-%d%s, sudoeste' % (palavra.lower(),inicial[0]+1,chr(97+inicial[1]),inicial[0]+index+1,chr(97+inicial[1]-index)))
                return True
        index+=1
############################################################################################################
#noroeste- Esta função percorre cada linha da sopa de letras da esquerda para a direita e de baixo para cima
#
#Argumentos:
#palvra- Lista com cada palavra a procurar na sopa de letras
#inicial- Tuplo onde foi encontrado a primeira letra da palavra
#sopa-Lista com cada linha da sopa de letras
#Valor de retorno:
#coordenada da primeira e última letra da palavra, direção em que a palavra está na sopa de letras
############################################################################################################
def noroeste(palavra,inicial,sopa):
    index = 1
    while ((inicial[1]-index >= 0) and (index < len(palavra)) and ((inicial[0]-index >= 0))):
        if(palavra[index]!=sopa[inicial[0]-index][inicial[1]-index]):
            break
        index+=1
    print('%s : %d%s-%d%s, noroeste' % (palavra.lower(),inicial[0]+1,chr(97+inicial[1]),inicial[0]-len(palavra)+1,chr(97+inicial[1]-index)))
    return True
############################################################################################################
#nordeste- Esta função percorre cada linha da sopa de letras da direita para a esquerda e de baixo para cima
#
#Argumentos:
#palvra- Lista com cada palavra a procurar na sopa de letras
#inicial- Tuplo onde foi encontrado a primeira letra da palavra
#sopa-Lista com cada linha da sopa de letras
#Valor de retorno:
#coordenada da primeira e última letra da palavra, direção em que a palavra está na sopa de letras
############################################################################################################
def nordeste(palavra,inicial,sopa):
    index = 1
    while ((index + inicial[1] < len(sopa[inicial[0]])) and (index < len(palavra)) and ((inicial[0]-index >= 0))):
        if(palavra[index]!=sopa[inicial[0]-index][inicial[1]+index]):
            break
        if index == (len(palavra)-1):
            if palavra[index]==sopa[inicial[0]-index][inicial[1]+index]:
                print('%s : %d%s-%d%s, nordeste' % (palavra.lower(),inicial[0]+1,chr(97+inicial[1]),inicial[0]-index+1,chr(97+inicial[1]+index)))
                return True
        index+=1
##########################################################################################################################
#localizar-Esta função imprime no ecrã o valor de retorno das funções anteriores
#
#Argumentos:
#palvra- Lista com cada palavra a procurar na sopa de letras
#sopa-Lista com cada linha da sopa de letras
#Valor de retorno:
#coordenada da primeira e última letra da palavra e direção em que a palavra está na sopa de letras de todas as palavras
##########################################################################################################################
def localizar(palavras,sopa):
    for palavra in palavras:
        ini = palavra[0]
        for linha in range(len(sopa)):
            for letra in range(len(sopa[linha])):
                if sopa[linha][letra] == ini:
                    inicial = (linha,letra)
                    if este(palavra,inicial,sopa):
                        break
                    elif oeste(palavra,inicial,sopa):
                        break
                    elif sul(palavra,inicial,sopa):
                        break
                    elif norte(palavra,inicial,sopa):
                        break
                    elif sudeste(palavra,inicial,sopa):
                        break
                    elif sudoeste(palavra,inicial,sopa):
                        break
                    elif noroeste(palavra,inicial,sopa):
                        break
                    elif nordeste(palavra,inicial,sopa):
                        break
localizar(palavras,sopal)
s.close()
