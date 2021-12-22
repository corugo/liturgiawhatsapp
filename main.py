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
itens = {}
geral = {}
tempitens = {}
item = "a"
#dicionario = {"teste":{"testedici":"testecerto"}}
#print(dicionario["teste"]["testedici"])
with open('liturgia.ja') as input_file:
    for line in input_file:
        if line != "\n":
            if line[0] == "[":
                itens[item] = tempitens
                tempitens = {}
                nomeitem = line
                nomeitem = nomeitem.replace("[","")
                nomeitem = nomeitem.replace("]","")
                item = nomeitem.rstrip('\n')
                #print("primeira linha")
            elif item[0] == "G":
                temp = line.split('=')
                #print(temp)
                geral[temp[0]] = temp[1].split(';')
                #print(geral)
            else:
                #print(line)
                temp = line.split('=')
                #temp = {temp[0]:temp[1]}
                print(temp)
                tempitens[temp[0]] = temp[1].rstrip('\n')
print(itens)
print(itens["item_anot"]["tipo"])
print(len(geral["1"]))

for i in range(1,7):
    for x in range(len(geral["1"])):
        print(itens[geral["1"]])
            