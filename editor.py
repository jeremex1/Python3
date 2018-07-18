
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import sys
import time


        
class Janela(tk.Frame):

    def __init__(self,master):

        super().__init__(master)

        self.master.title("SISTEMA")
        self.master.geometry("500x500+200+100")
        #self.master['bg'] = "grey"
        
        self.menus()
        self.texto()

       
    def menus(self):

        self.menu = tk.Menu(self.master)
        self.arq = tk.Menu(self.menu, tearoff=0)#tearoff define se o menu bode ser movido como uma janela do menu principal
        self.arq.add_command(label = 'novo')
        self.arq.add_command(label = 'abrir',command=self.abrir)
        self.arq.add_command(label = 'salvar',command=self.salvar)
        self.menu.add_cascade(label = 'arquivo',menu=self.arq)

        self.editar = tk.Menu(self.menu,tearoff=0)
        self.editar.add_command(label = 'copiar')
        self.editar.add_command(label = 'colar')
        self.editar.add_command(label = 'recortar')
        self.menu.add_cascade(label = 'editar',menu=self.editar)

        self.formatar = tk.Menu(self.menu,tearoff=0)
        self.formatar1 = tk.Menu(self.formatar,tearoff=0)
        self.formatar2 = tk.Menu(self.formatar)
        self.colors = tk.Menu(self.formatar)
        self.colors.add_command(label='blue',command=self.color1)
        self.colors.add_command(label='purple',command=self.color2)
        self.colors.add_command(label='red',command=self.color3)
        self.colors.add_command(label='white',command=self.color4)
        self.colors.add_command(label='black',command=self.color5)
        self.color_font = tk.Menu(self.formatar)
        self.color_font.add_command(label='green',command=self.font1)
        self.color_font.add_command(label='red',command=self.font2)
        self.color_font.add_command(label='blue',command=self.font3)
        self.color_font.add_command(label='purple',command=self.font4)
        self.color_font.add_command(label='black',command=self.font5)
        self.color_font.add_command(label='white',command=self.font6)
        
        self.formatar.add_cascade(label = 'font',menu=self.box)
        self.formatar1.add_cascade(label = 'cor-font',menu=self.color_font)
        self.formatar1.add_cascade(label = 'cor-fundo',menu=self.colors)
        self.menu.add_cascade(label = 'formatar',menu=self.formatar)
        self.master.configure(menu=self.menu)

    def texto(self):

        self.text = tk.Text(self.master)
        self.text.configure(width = 500,height = 500)
        self.text.configure(font=('serief',14,'italic'))
        self.text.pack()

    def box(self):
        
        lista = Listbox(self.master, width=15)
        lista.pack()
        for item in range(1,10):
            lista.insert(END, item)
            if lista.index(0):
                self.text.configure(font=("helvetica",20))

       
    def salvar(self):
        
        self.texto = self.text.get(1.0,END)
        arq = tk.filedialog.asksaveasfilename(initialdir ="/home/jeremias/Documentos",title="Arquivos",
                                              filetypes=(('Arquivo de texto','*.py'),('Todos os arquivos','*.*')))
        with open(arq, mode = 'w')as f:
            f.write(self.texto)
            f.close()
        return False
            
    def abrir(self):
        arq = tk.filedialog.askopenfilename(initialdir='~/',title='Arquivos',filetypes=(('Arquivos de texto ','*.txt'),
                                                                                        ('Todos','*.*')))
        with open(arq,mode='r') as f :
            texto = f.read()
            f.close()
            self.text.delete(1.0,END)
            self.text.insert(END,texto)

    def color1(self):
        self.text.configure(bg = 'blue')
    def color2(self):
        self.text.configure(bg = 'purple')
    def color3(self):
        self.text.configure(bg = 'red')
    def color4(self):
        self.text.configure(bg = 'white')
    def color5(self):
        self.text.configure(bg = 'black')
        
    def font1(self):
        self.text.configure(font =('calibre',16,'italic'),fg='green')
    def font2(self):
        self.text.configure(font =('arial',16),fg='red')
    def font3(self):
        self.text.configure(font =('arial',16),fg='blue')
    def font4(self):
        self.text.configure(font =('arial',16),fg='purple')
    def font5(self):
        self.text.configure(font =('arial',16),fg='black')

    def font6(self):
        self.text.configure(font =('arial',16),fg='white')

        
root = tk.Tk()
app = Janela(master=root)
app.mainloop()

if __name__ == '__main__':
    pass

    
