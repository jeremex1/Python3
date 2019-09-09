import tkinter as tk
#from cadastrar_produtos import Cadastro_produtos
from  conexao_bd import Conexao
from tkinter import Button,Frame,Label,Entry,messagebox,Menu

class Systema_cadastro():
    def __init__(self):  
        self.con = Conexao()
        if(self.con.tela()==True):
            self.con.login.destroy()
            self.systema()
       
    def systema(self):
        self.master = tk.Tk()
        self.master.geometry("900x250+200+350")
        self.master.title("Gerenciamento de Stoque de Produtos")
        self.frames()
        self.master.mainloop()

    def frames(self):
        self.frame_insert = tk.Frame(self.master,width=900,height=250)
        self.frame_insert.pack()

        self.frame_listar = tk.Frame(self.master,width=800,height=600)
        self.frame_listar.pack()

        self.menu = tk.Menu(self.master)
        self.menu.add_command(label="Inserir Produtos",command=self.layout_inserir)
        self.menu.add_command(label="Listar Estoque",command=self.layout_listar)
        self.master.configure(menu=self.menu)

    def layout_inserir(self):
        self.frame_listar.pack_forget()
        self.master.geometry("900x250+200+250")
        self.frame_insert.pack()

        self.titulo_janela = tk.Label(self.frame_insert,text='Cadastrar Produtos',fg='blue',font=('arial',16,'bold'))
        self.titulo_janela.place(x=350,y=0)

        self.label_codigo = tk.Label(self.frame_insert,text='Codigo Produto : ',bd=2)
        self.label_codigo.place(x = 10 ,y = 50)

        self.entry_codigo = tk.Entry(self.frame_insert,width=15)
        self.entry_codigo.place(x = 150 ,y = 50)

        self.label_nome = tk.Label(self.frame_insert,text='Nome :',bd=2)
        self.label_nome.place(x = 10, y = 80)

        self.entry_nome = tk.Entry(self.frame_insert,width=30)
        self.entry_nome.place(x = 150 ,y = 80)
        
        self.label_quantidade = tk.Label(self.frame_insert,text='Quantidade : ',bd=2)
        self.label_quantidade.place(x = 10 , y = 110)

        self.entry_quantidade = tk.Entry(self.frame_insert,width=5)
        self.entry_quantidade.place(x = 150 , y = 110)

        self.label_preco = tk.Label(self.frame_insert,text='Preco : ',bd=2)
        self.label_preco.place(x = 10, y = 140)

        self.entry_preco = tk.Entry(self.frame_insert,width=10)
        self.entry_preco.place(x = 150 , y = 140)

        self.label_descricao = tk.Label(self.frame_insert,text='descricao :',bd=2)
        self.label_descricao.place(x = 10 ,y = 170)

        self.entry_descricao = tk.Entry(self.frame_insert,width=30)
        self.entry_descricao.place(x = 150 , y = 170)

        self.bt_cadastra_produto = tk.Button(self.frame_insert,text='cadastrar',
        relief='ridge',cursor='pirate',bg='grey',command=self.get_nome)
        self.bt_cadastra_produto.place(x = 10 ,y = 210)

    def layout_listar(self):
        self.frame_insert.pack_forget()
        self.frame_listar.pack()
        self.master.geometry('900x700+200+150')
        self.texto = tk.Text(self.frame_listar,width=110,height=43)
        self.texto.pack()

    def get_codigo_produto(self):
        return self.entry_codigo.get()

    def get_nome(self):
        return self.entry_nome.get()

    def get_quantidade(self):
        return self.entry_quantidade.get()
    
    def get_preco(self):
        return self.entry_preco.get()

    def get_descricao(self):
        return self.entry_descricao.get()

    def bt_aplicar(self):

        self.bt_inserir= tk.Button(self.frame_insert,bd=2,text='salvar',command=self.get_nome)
        self.bt_inserir.place(x = 50 ,y = 400)

    def testes(self):
        s= self.get_nome()
        print(s)

Systema_cadastro()