import json, os

class Gerar_bases():
    
    node = {}
    nomes = []
    
    def __init__(self) -> None:
        self.node = {}
        self.nomes = []

    def Criar_lista(self,lista,separador=0):
        
        if separador == 0: #Separador por linhas 
            self.nomes = lista.split('\n')
        elif separador == 1: #Separador por espaço
            self.nomes = lista.split(' ')
        elif separador == 2: #Separador por virgula
            self.nomes = lista.split(',')
        elif separador == 3: #Nomes já separados por lista
            self.nomes = lista
        self.Criar_node(self.nomes)

    def Criar_node(self, nomes):

        for nome in nomes:
            cont = 0
            
            for letra in nome:
                cont += 1
                #Cria o nó
                try:
                    if letra.upper() in self.node:
                        if nome[cont].upper() in self.node[letra.upper()]:
                            self.node[letra.upper()][nome[cont].upper()] +=1
                        else:
                            self.node[letra.upper()][nome[cont].upper()] =1
                    else:
                        self.node[letra.upper()] = {nome[cont].upper():1}
                except:
                    ...

            cont = 0

    def Criar_base(self, categoria):
        caminho_abs = (os.path.dirname(os.path.abspath(__file__)))
        caminho = os.path.join(caminho_abs,'bases', f'{categoria}.json')

        with open(caminho, 'w',encoding='utf-8') as data:
        
            data.write(json.dumps(self.node, indent=4,sort_keys=True))

