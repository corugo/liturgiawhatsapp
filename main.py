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

itens = {}
geral = {}
tempitens = {}
item = "a"
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
print(geral)

for i in range(1,8):
    print("\nDia da semana: "+str(i))
    try:
        for x in geral[str(i)]:
            #print(itens[x]["item"])
            if itens[x]["tipo"] == "categoria":
                print("\n*" + itens[x]["item"].upper() + "*")
            else:
                print("- " + itens[x]["item"])
                if itens[x]["tipo"] == "musica":
                    print("  _"+ itens[x]["subitem"]+ "_")
            
    except:
        pass
