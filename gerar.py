import random
import string
nome = input('ficheiro(com extensão)') 
f = open(nome)                      #ficheiro de texto com informação necessária para gerar sopa de letras
linha = int(f.read(1))
coluna = int(f.read(3))
palavras = list()
line = f.readline()
while line != '':
    palavras.append(line.rstrip())
    line = f.readline()
sopa = []
s = ''
for linha in range(linha):
    for icoluna in range(coluna):
        s+=random.choice(string.ascii_lowercase)
    sopa.append(s)
    s = ''
##############################################################################################################
#write- Esta função vai de linha em linha tentar meter na sopa as palvras que se pretende que estejam na sopa
#
#Argumentos:
#palavras- Lista com as palavras que se deseja meter na sopa de letras
#lista-Lista com a sopa de letras
#Valor de retorno:
#lista da sopa de letras já com as palavras que se quer que lá estejam
##############################################################################################################
def write(palavras,lista):
    i = 0
    for palavra in palavras:
        Achou = False
        while not Achou:
            where = random.choice(range(len(lista[i])))
            if len(palavra) > len(lista[i][where::]):
                continue
            else:
                s = lista[i]
                n = lista[i][:where] + palavra + lista[i][(where+len(palavra))::]
                lista[i]=n
                Achou = True
                i+=1
write(palavras,sopa)
nome2 = input('ficheiro(com extensão)') 
w = open(nome2,'w')         #cria um ficheiro de texto vazio
w.write(str(len(palavras)))
w.write('\n')
for palavra in palavras:
    w.write(palavra+'\n')
for each in sopa:
    w.write(each.upper()+'\n')
w.close()
