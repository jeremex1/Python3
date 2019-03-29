
from os import *
from sys import *
import tkinter  as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import Cores as cor
import Menu as menu


class Cores(tk.Frame, cor.Cores, menu.Menu):
    
    def __init__(self, master):
        super().__init__(master)
        self.master.title("TEXTO")
        self.master.geometry("500x500+100+100")
        self.master.configure(bd="2",relief='raised')#tiposs de bd (groove,suken,raised,solid,raidge)
        self.label=tk.Label(self.master,text='Undefild')
        self.label.pack()
        self.texto()
        self.menus()
        
    def texto(self):
        self.text = tk.Text(self.master)
        self.text.configure(width=490, height=490)
        self.text.configure(font=("serief", 14),bg=self.cores()[5][5],fg=self.cores()[18][5])
        self.scroll_y = Scrollbar(self.master, command=self.text.yview)
        self.text.configure(yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

    def salvar(self):
        self.texto = self.text.get(1.0, END)
        arq = tk.filedialog.asksaveasfilename(initialdir="/home/jeremias", title="Arquivos",
                                              filetypes=(("Arquivos de texto", "*txt"), ("Todos", "*.*")))
        with open(arq, mode='w')as f:
            f.write(self.texto)
            f.close()
        return True

    def abrir(self):
        arq = tk.filedialog.askopenfilename(initialdir="/home/jeremias", title="all",
                                            filetypes=(('Arquivos de texto', '*.txt'), ("ALL", "*.*")))
        with open(arq, mode='r') as f:
            texto = f.read()
            f.close()
            self.text.delete(1.0, END)
            self.text.insert(END, texto)

    def layout(self):
        self.tela = tk.Tk()
        self.tela.title("BACKGROUND")
        self.tela.geometry("380x200+150+280")
        self.listbox = tk.Listbox(self.tela)
        self.listbox.configure(justify="center")
        self.listbox.bind("<<ListboxSelect>>",self.copy)
        self.listbox.pack()
        for n in range(len(self.key)):
            for hexa in self.valor[n]:
                self.listbox.insert(END,hexa)#self.key[n])
                """if (hexa == "#000000"):
                    self.listbox.itemconfigure(tk.END, background=hexa, foreground=hexa)"""
                self.listbox.itemconfigure(END, background=hexa)


    def copy(self,x):
        self.posision_cur=self.listbox.curselection()
        self.clipboard_clear()
        self.clipboard_append(self.listbox.get(self.posision_cur))
        self.corente_cor =(self.listbox.get(self.posision_cur))
        print(self.corente_cor)
        #self.background_text()
        self.tela.destroy()
        return 

    def novo(self):
        self.wc = tk.messagebox.askyesno("NEW","O Arquivo nao foi salvo deseja salvar")
        if(self.wc==True):
            self.salvar()
        else:
            self.text.delete(1.0, END)

    def background_text(self):
        self.layout()
        self.tela.title("BACKGROUND COLOR")
        self.message = tk.messagebox.askyesno("Color Background","deseja altera a cor de fundo")
        if (self.message==True):
            self.text.configure(bg = self.corente_cor)
    def foreground_text(self):
        self.layout()
        self.tela.title("FOREGROUND COLOR")
        self.message2 = tk.messagebox.askyesno("Color foreground","Deseja mudar a cor da fonte")
        if (self.message2 == True):
            self.text.configure(fg=self.corente_cor)




root = tk.Tk()
app = Cores(master=root)
app.mainloop()
