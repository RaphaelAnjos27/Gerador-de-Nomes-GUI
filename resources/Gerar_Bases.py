from resources.node import Gerar_bases
import csv, os

class Gerar_Bases():
    def Gerar(self):
        caminho_abs = (os.path.dirname(os.path.abspath(__file__)))
        caminho = os.path.join(caminho_abs,'assets','Base_nomes.csv')

        listas = []

        with open(caminho, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            titulo = True
            
            for linha in spamreader:
                if titulo == True:
                    for titulo in linha:
                        listas.append({"titulo":titulo, "data":''}) 
                    titulo = False
                else:
                    ct = 0
                    for content in linha:
                        if content != '':
                            listas[ct]['data'] += f'{content},'
                        ct +=1

        for item in listas:
            base = Gerar_bases()
            base.Criar_lista(item['data'],2)
            base.Criar_base(item['titulo'].replace(' ','').replace('/','-'))



'''with open("Assets/Viking.txt", 'r',encoding='utf-8') as data:
    lista = data.read()'''
