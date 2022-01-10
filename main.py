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
import pprint
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
#from PyQt5.QtWidgets import QApplication, QLabel
cl = {"clBlack":(0,0,0),"clMaroon":(128, 0, 0),"clGreen":(0, 128, 0),"clOlive":(128,128,0),"clNavy":(0,0,128),"clPurple":(128,0,128),"clTeal":(128,128,0),"clGray":(128,128,128),"clSilver":(192,192,192),"clRed":(255, 0, 0),"clLime":(0,255,0),"clYellow":(255,255,0),"clBlue":(0,0,255),"clFuchsia":(255,0,255),"clAqua":(0,255,255),"clLtGray":(192,192,192),"clDkGray":(128,128,128),"clWhite":(255,255,255),"clCream":(255, 251, 240),"clMedGray":(160, 160, 164),"clMoneyGreen":(192, 220, 192),"clSkyBlue":(166, 202, 240)}
semana = {1:'Domingo', 2:'Segunda-Feira', 3:'Terça-Feira', 4:'Quarta-Feira', 5:'Quinta-Feira', 6:'Sexta-Feira', 7:'Sábado'}
itens = {}
geral = {}
tempitens = {}
item = ""
tamanhofonte = 16

def tcolor(cor):
    if cor[0] == "$":
        r = int(cor[7]+cor[8], 16)
        g = int(cor[5]+cor[6], 16)
        b = int(cor[3]+cor[4], 16)
        return((r,g,b))
    else:
        return(cl[cor])

def trataArquivo(diretorio):
    splitado = diretorio.split('\\')
    exten = splitado.pop()
    tratado = exten#[:30]
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
                item = nomeitem.rstrip('\n')    #apagar "\n"
            elif item[0] == "G":
                if line[0] != "A":
                    temp = line.split('=')
                    temp[1] = temp[1].rstrip(';\n')
                    geral[temp[0]] = temp[1].split(';')
            else:
                temp = line.split('=')
                tempitens[temp[0]] = temp[1].rstrip('\n')
    itens[item] = tempitens


for i in geral:
    tamanho = 0
    offset = 0
    if geral[str(i)] == ['']:   #Se for um dia vazio
        print("Dia vazio")
        continue
    
    for x in geral[str(i)]:
        #print(x)
        #print(itens[x])
        if itens[x]["tipo"] == "itensagendados":
            tamanho += tamanhofonte
        elif itens[x]["tipo"] == "anotacao" and itens[x]["subitem"] == "":
            tamanho += tamanhofonte
        else:
            tamanho += tamanhofonte * 2
    tamanho += tamanhofonte
    
    img = Image.new('RGB', (600, tamanho), color = (0,0,0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("cour.ttf", tamanhofonte)
    font2 = ImageFont.truetype("courbd.ttf", tamanhofonte)
    font3 = ImageFont.truetype("courbi.ttf", tamanhofonte)
    font4 = ImageFont.truetype("couri.ttf", tamanhofonte)
    # draw.text((x, y),"Sample Text",(r,g,b))
    #draw.text((0, 0),"Sample Text",(255,255,255),font=font)
    
    #tcolor(itens[x]["cor"])
    
    
    
    
    print(offset+tamanhofonte)
    print(tamanhofonte)
    for x in geral[str(i)]:
        print(itens[x]["item"])
        print(tcolor(itens[x]["cor"]))
        if itens[x]["tipo"] == "categoria":         #Categoria
            offset += tamanhofonte * 2
            draw.rectangle(((0, offset), (400, offset +tamanhofonte)), fill=tcolor(itens[x]["cor"]))
            draw.text((16, offset),itens[x]["item"].upper(),(255,255,255),font=font2)
        else:
            offset += tamanhofonte
            draw.rectangle(((0, offset), (10, offset +tamanhofonte)), fill=tcolor(itens[x]["cor"]))
            draw.text((16, offset),itens[x]["item"],(255,255,255),font=font)
            if itens[x]["tipo"] == "musica":        #Música
                if itens[x]["subitem"] == "Clique para escolher a música":
                    offset += tamanhofonte
                    draw.text((16, offset),"  Música não selecionada",(255,5,5),font=font3)
                else:
                    offset += tamanhofonte
                    draw.text((16, offset),"  " + itens[x]["subitem"],(255,255,255),font=font4)
            elif itens[x]["tipo"] == "anotacao":    #Anotação
                if itens[x]["subitem"] != "":
                    offset += tamanhofonte
                    draw.text((16, offset),"  " + itens[x]["subitem"],(255,255,255),font=font4)
            elif itens[x]["tipo"] == "arquivo":     #Arquivo
                if itens[x]["dir"] != "":
                    offset += tamanhofonte
                    draw.text((16, offset),"  Arquivo " + trataArquivo(itens[x]["dir"]),(255,255,255),font=font4)
                else:
                    offset += tamanhofonte
                    draw.text((16, offset),"  Arquivo não selecionado",(255,5,5),font=font3)
                    
    img.save(str(i) +'.jpg')
    print(itens)
    



'''
pprint.pprint(itens)
pprint.pprint(geral)

for i in geral:
    print("\nDia da semana: "+semana[int(i)])
    if geral[str(i)] == ['']:   #Se for um dia vazio
        print("Dia vazio")
        continue
    for x in geral[str(i)]:
        #print(itens[x]["item"])
        if itens[x]["tipo"] == "categoria":         #Categoria
            print("\n*" + itens[x]["item"].upper() + "*\n")
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
'''
'''
app = QApplication([])
label = QLabel('Hello World!')
label.show()
app.exec()
'''
