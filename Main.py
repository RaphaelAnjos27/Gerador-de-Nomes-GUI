import gi
from pynotifier import Notification
from resources.Gerar_nomes import Gerar_nome


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk,Gdk

class MyApp(Gtk.Window):
    tool = Gerar_nome()
    categoria = None
    tamanho = 'medio'
    quantidade = 1
    geracao = []
    

    def __init__(self) -> None:
        super().__init__()
        
        #Configuração Basica de tela
        self.set_default_size(500,400)
        self.set_title('Gerador de Nomes Versão 1.0.0')
        self.set_border_width(5)
        self.set_default_icon_from_file('assets/logo.svg')

        container = Gtk.HBox()

        self.nome_copiado = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

        frame_01 = Gtk.Frame()
        frame_02 = Gtk.Frame()
        frame_01.set_label("Configurações")
        frame_02.set_label("Nomes Gerados")

        container.pack_start(frame_01,1,1,5)
        container.pack_start(frame_02,1,1,5)
        
        # Frame 01 ________________________________________________________________________________
        cont_01 = Gtk.VBox()
        
        lb01 = Gtk.Label()
        lb01.set_text('Categorias')
        cont_01.pack_start(lb01,0,1,5)

        #Configuração do ComboBox
        
        self.liststore = Gtk.ListStore(str)
        self.configurar_lista()
        self.combobox = Gtk.ComboBox()
        self.combobox.set_model(self.liststore)
        self.combobox.set_active(0)
        self.combobox.connect("changed", self.capiturar_categoria)


        cont_01.pack_start(self.combobox,0,1,10)

        cellrenderertext = Gtk.CellRendererText()
        self.combobox.pack_start(cellrenderertext, True)
        self.combobox.add_attribute(cellrenderertext, "text", 0)

        # Configurar Tamanho:
        lb02 = Gtk.Label()
        lb02.set_text('Tamanho')
        cont_01.pack_start(lb02,0,1,5)

        liststore = Gtk.ListStore(str)
        for item in ['curto','medio','grande']:
            liststore.append([item])
        self.combobox2 = Gtk.ComboBox()
        self.combobox2.set_model(liststore)
        self.combobox2.set_active(0)
        self.combobox2.connect("changed", self.capiturar_tamanho)


        cont_01.pack_start(self.combobox2,0,1,10)

        cellrenderertext = Gtk.CellRendererText()
        self.combobox2.pack_start(cellrenderertext, True)
        self.combobox2.add_attribute(cellrenderertext, "text", 0)

        # Quantidade de nomes
        lb02 = Gtk.Label()
        lb02.set_text('Quantidade de Nomes')
        cont_01.pack_start(lb02,0,1,5)

        adjustment = Gtk.Adjustment(value=1,
                                    lower=1,
                                    upper=100,
                                    step_increment=1,
                                    page_increment=1,
                                    page_size=0)
        spinbutton = Gtk.SpinButton(adjustment=adjustment)
        spinbutton.connect("value-changed", self.on_spinbutton_changed)
        cont_01.pack_start(spinbutton,0,1,10)
        
        #Botões

        container_hori = Gtk.HBox()

        btn_gerar = Gtk.Button()
        btn_gerar.set_label('Gerar')
        btn_gerar.connect('clicked', self.Gerar_nome)

        btn_copiar = Gtk.Button()
        btn_copiar.connect('clicked',self.Copiar_nome)
        btn_copiar.set_label('Copiar')

        container_hori.pack_start(btn_gerar,1,1,5)
        container_hori.pack_start(btn_copiar,1,1,5)

        cont_01.pack_start(container_hori,0,1,10)

        frame_01.add(cont_01)

        # Frame 02 ________________________________________________________________________________

        self.cont_02 = Gtk.VBox()
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.add(self.cont_02)



        frame_02.add(scrolledwindow)
        self.add(container)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def configurar_lista(self):
        lista = self.tool.Retornar_categorias()
        for item in lista:
            self.liststore.append([item])


    def capiturar_categoria(self, combobox):
        treeiter = self.combobox.get_active_iter()
        model = self.combobox.get_model()
        self.categoria = model[treeiter][0]

    def capiturar_tamanho(self, combobox):
        treeiter = combobox.get_active_iter()
        model = combobox.get_model()
        self.tamanho = model[treeiter][0]
    
    def on_spinbutton_changed(self, spinbutton):
        self.quantidade = spinbutton.get_value_as_int()

    def Gerar_nome(self, botao):
        filhos = self.cont_02.get_children()
        if len(filhos) != 0:
            for i in filhos:
                self.cont_02.remove(i)

        self.geracao = []

        self.tool.Setar_categoria(self.categoria)
        for i in range(self.quantidade):
            self.geracao.append(self.tool.Gerar_nome(self.tamanho))

        for i in self.geracao:
            lb = Gtk.Label()
            lb.set_text(i)
            lb.set_selectable(True) 
            self.cont_02.pack_start(lb,0,0,5)

        self.cont_02

        self.show_all()

    def Copiar_nome(self,botao):
        nome = ''

        for i in self.geracao:
            nome += f'{i} '
        self.nome_copiado.set_text(nome, -1)

        Notification(title='Copiado',
            description='A lista de nomes foram copiadas com sucesso!',
            icon_path='assets/icone_copia.svg',
            duration=3).send()

        

MyApp()
Gtk.main() 

