import tkinter as tk
from tkinter import *
from tkinter import filedialog

class Editor:

	def __inti__(self):
		super().__init__(self)

	def tela(self):

		self.windown = tk.Tk()
		self.windown.geometry("500x500+200+200")
		self.windown.title("Pytext")
		self.menu()
		self.text()
		print("hello")
		self.windown.mainloop()

	def menu(self):
		self.menu = tk.Menu(self.windown,tearoff=0)
		self.arquivo1 = tk.Menu(self.menu,tearoff=0)
		self.arquivo1.add_command(label="novo",command=self.new)
		self.arquivo1.add_command(label="abrir")
		self.arquivo1.add_command(label="salvar",command=self.salvar)
		self.menu.add_cascade(label="arquivo",menu=self.arquivo1)
		self.windown.configure(menu=self.menu)


	def text(self):
		self.text = tk.Text(self.windown)
		self.text.configure(width=500,height=500)
		self.text.configure(font=("helvetica",14,"bold"))
		self.text.focus()
		self.text.pack()

	def salvar(self):
            
            self.texto = self.text.get(1.0,END)
	    arq = tk.filedialog.asksaveasfilename(initialdir ="/home/jelinux/Documentos",title="Arquivos",filetype=(("todos","*.py"),("arquivos","*")))
            with open(arq, mode = 'w')as f:
        	f.write(self.texto)
        	f.close()
        return False



	def new(self):
		self.new = True
		self.windown.title("undefine")
		self.windown.geometry("500x500+500+200")
		novo = Editor()
		novo.tela()

app = Editor()
app.tela()
