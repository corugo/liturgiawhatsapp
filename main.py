'''
tipo [anotacao, arquivo, categoria, itensagendados, musica, site]
item [nome do item]
cor = codigo cor
subitem = ???
checked = se checado, tem data
subtipo = [hasd/cdja]
escolha = escolha na hora == 1
musica = numero musica
subitem = Nome item
url = URL
'''
import os

semana = {1:'Domingo', 2:'Segunda-Feira', 3:'Terça-Feira', 4:'Quarta-Feira', 5:'Quinta-Feira', 6:'Sexta-Feira', 7:'Sábado'}
itens = {}
geral = {}
tempitens = {}
item = "a"

def trataArquivo(diretorio):
    splitado = diretorio.split('\\')
    exten = splitado.pop()
    tratado = exten[:30]# + "..." + exten.pop()
    return(tratado)

#dicionario = {"teste":{"testedici":"testecerto"}}
#print(dicionario["teste"]["testedici"])
with open(os.getenv('APPDATA') + "\LouvorJA\liturgia.ja") as input_file:
    for line in input_file:
        if line != "\n":
            if line[0] == "[":
                itens[item] = tempitens
                tempitens = {}
                nomeitem = line
                nomeitem = nomeitem.replace("[","")
                nomeitem = nomeitem.replace("]","")
                item = nomeitem.rstrip('\n')
            elif item[0] == "G":
                temp = line.split('=')
                geral[temp[0]] = temp[1].split(';')
            else:
                temp = line.split('=')
                tempitens[temp[0]] = temp[1].rstrip('\n')
    itens[item] = tempitens
print(itens)

for i in range(1,8):
    print("\nDia da semana: "+semana[i])
    try:
        for x in geral[str(i)]:
            #print(itens[x]["item"])
            if itens[x]["tipo"] == "categoria":
                print("\n*" + itens[x]["item"].upper() + "*")
            else:
                print("- " + itens[x]["item"])
                if itens[x]["tipo"] == "musica":        #Música
                    if itens[x]["subitem"] == "Clique para escolher a música":
                        print("  *_Música não selecionada_*")
                    else:
                        print("  _"+ itens[x]["subitem"]+ "_")
                elif itens[x]["tipo"] == "anotacao":    #Anotação
                    if itens[x]["subitem"] != "":
                        print("  _"+ itens[x]["subitem"]+ "_")
                elif itens[x]["tipo"] == "arquivo":     #Arquivo
                    if itens[x]["dir"] != "":
                        print("  _Arquivo "+ trataArquivo(itens[x]["dir"]) + "_")
                    else:
                        print("  *_Arquivo não selecionado_*")
            
    except:
        pass
