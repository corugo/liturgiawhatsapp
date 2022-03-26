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
entrelinhas = round(tamanhofonte * 0.2) + tamanhofonte
espacamento = 2

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
        if itens[x]["tipo"] == "itensagendados" or itens[x]["item"].lower() == "lista":
            tamanho += entrelinhas
        elif itens[x]["tipo"] == "anotacao" and (itens[x]["subitem"] == "" or itens[x]["subitem"] == "  "):
            tamanho += entrelinhas
        else:
            tamanho += entrelinhas * 2
        tamanho += espacamento
    tamanho += entrelinhas
    
    img = Image.new('RGB', (600, tamanho), color = (202,187,170))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", tamanhofonte)
    font2 = ImageFont.truetype("arialbd.ttf", tamanhofonte)
    font3 = ImageFont.truetype("arialbi.ttf", tamanhofonte)
    font4 = ImageFont.truetype("ariali.ttf", tamanhofonte)
    corFonteItens = (0,0,0)
    corFonteCategorias = (255,255,255)
    # draw.text((x, y),"Sample Text",(r,g,b))
    #draw.text((0, 0),"Sample Text",(255,255,255),font=font)
    
    #tcolor(itens[x]["cor"])
    
    
    draw.text((230, 0),semana[int(i)],(255,255,255),font=font2)
    
    for x in geral[str(i)]:
        if itens[x]["tipo"] == "categoria":         #Categoria
            offset += entrelinhas * 2
            draw.rectangle(((0, offset), (600, offset +entrelinhas-1)), fill=tcolor(itens[x]["cor"]))
            draw.text((16, offset),itens[x]["item"].upper(),corFonteCategorias,font=font2)
            draw.rectangle(((0, offset +entrelinhas-2), (600, offset +entrelinhas-1)), fill=(187,168,147)) #Linha inferior
        
        elif itens[x]["tipo"] == "musica":        #Música
            if itens[x]["item"].lower() != "lista":
                offset += entrelinhas
                draw.rectangle(((4, offset + (entrelinhas * 0.3)), (12, offset + (entrelinhas * 0.7))), fill=tcolor(itens[x]["cor"]))
                draw.text((16, offset),itens[x]["item"],corFonteItens,font=font)
            if itens[x]["subitem"] == "Clique para escolher a música":
                offset += entrelinhas
                draw.text((16, offset),"  Música não selecionada",(219,49,49),font=font3)

            else:
                offset += entrelinhas
                draw.text((16, offset),"  " + itens[x]["subitem"],corFonteItens,font=font4)
            draw.rectangle(((0, offset +entrelinhas), (600, offset +entrelinhas + espacamento -1)), fill=(187,168,147)) #Linha inferior

        else:
            offset += entrelinhas
            draw.rectangle(((4, offset + (entrelinhas * 0.3)), (12, offset + (entrelinhas * 0.7))), fill=tcolor(itens[x]["cor"]))
            draw.text((16, offset),itens[x]["item"],corFonteItens,font=font)

            if itens[x]["tipo"] == "anotacao":    #Anotação
                if itens[x]["subitem"] != "" and itens[x]["subitem"] != "  ":
                    offset += entrelinhas
                    draw.text((16, offset),"  " + itens[x]["subitem"],corFonteItens,font=font4)

            elif itens[x]["tipo"] == "arquivo":     #Arquivo
                if itens[x]["dir"] != "":
                    offset += entrelinhas
                    draw.text((16, offset),"  Arquivo " + trataArquivo(itens[x]["dir"]),corFonteItens,font=font4)
                
                else:
                    offset += entrelinhas
                    draw.text((16, offset),"  Arquivo não selecionado",(219,49,49),font=font3)
            draw.rectangle(((0, offset +entrelinhas), (600, offset +entrelinhas + espacamento -1)), fill=(187,168,147)) #Linha inferior
        offset += espacamento
    draw.rectangle(((0, 0), (599, tamanho-1)), width=2, outline=(0,0,0)) #contorno
    img.save(str(i) +'.png')
    #print(itens)
    



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
