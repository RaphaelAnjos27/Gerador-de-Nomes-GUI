import json,random,os
from resources.Gerar_Bases import Gerar_Bases

class Gerar_nome(Gerar_Bases):
    nodes = ''
    Geravel = False
    cat = None

    def __init__(self,categoria = None) -> None:
        caminho_abs = (os.path.dirname(os.path.abspath(__file__)))
        caminho = os.path.join(caminho_abs, 'bases', f'{categoria}.json')
        try:
            with open(caminho, 'r',encoding='utf-8') as data:
                self.nodes = json.loads(data.read())
            self.Geravel = True
            self.cat = categoria
        except:
            ...
    
    def get_geravel(self):
        return self.Geravel

    def Setar_categoria(self,categoria):
        caminho_abs = (os.path.dirname(os.path.abspath(__file__)))
        caminho = os.path.join(caminho_abs, 'bases', f'{categoria}.json')
        try:
            with open(caminho, 'r',encoding='utf-8') as data:
                self.nodes = json.loads(data.read())
            self.Geravel = True
            self.cat = categoria

            categorias = self.Retornar_categorias()
            '''if categoria in categorias:
                self.cat = categoria
            else:
                self.cat = None'''
        except:
            ...


    def Retornar_categorias(self):
        
        caminho_abs = (os.path.dirname(os.path.abspath(__file__)))
        caminho = os.path.join(caminho_abs, 'bases')
        categorias = []
        for i in os.listdir(caminho):
            nome = i.split('.')
            categorias.append(nome[0])
        return categorias
        

    def Gerar_nome(self,tamanho="curto"):
        if self.Geravel:
            nome = ''
            valor = 0

            if tamanho == 'curto':
                valor = random.randint(4, 6)-1
            elif tamanho == 'medio':
                valor = random.randint(7, 9)-1
            elif tamanho == 'grande':
                valor = random.randint(8, 13)-1

            chaves = self.nodes.keys()

            primeira_letra = random.choice(list(chaves))
            nome += primeira_letra
            prox_letra = primeira_letra

            for i in range(valor):
                chaves = list(self.nodes[prox_letra].keys())
                valores = list(self.nodes[prox_letra].values())
                
                sorteado = random.choices(chaves, valores, k = 1)

                nome +=sorteado[0]
                prox_letra = sorteado[0]

            return nome.capitalize()
        else:
            return False

if __name__ == '__main__':
    
    nome = Gerar_nome()
    #nome.Setar_categoria('Anões')
    
    print(nome.get_geravel()) # Retorna False se não conseguirmos gerar o nome (devido nao termos categorias pré criadas)
    
    print(nome.Gerar_nome('medio')) # retorna false se nao conseguirmos gerar o nome devido ao mesmo problema descrito acima

    print(nome.Retornar_categorias()) # Retorna as categorias que existem (false se nao existirem categorias)

    nome.Gerar() # Gera as categorias caso nao existam


    #for i in range(100):
    #    print(nome.Gerar_nome('grande'))