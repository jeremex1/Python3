from tkinter import Label, Frame, Button, Entry,Menu
import tkinter as tk
class Calc_juros(tk.Frame):
	"""docstring for calc_juros"""
	def __init__(self,master):
		super().__init__(master)
		self.master.title("Calculo de juros compostos")
		self.master.geometry("400x400+350+150")
		self.master['bg']="#00afaf"
		self.menu()
		self.Screen()

	def menu(self):
		self.menu = tk.Menu(self.master,bg="#ACACAC",tearoff=0)
		self.menu.add_command(label="about",command= self.about)
		self.master.configure(menu = self.menu)

	def Screen(self):
		self.label_value = tk.Label(self.master,fg="#121212",bg="#00afaf",text="VALOR INICIAL",font=("sanserif",12, "italic"))
		self.label_value.place(x = 10, y = 50)
		self.text_value = tk.Entry(self.master,width=10,bd=2,relief="flat",bg="#cccccc")
		self.text_value.place(x=10,y=85)
		self.text_value.focus()

		self.label_taxa = tk.Label(self.master,fg="#121212",bg="#00afaf",text="TAXA DE JUROS",font=("sanserif",12, "italic"))
		self.label_taxa.place(x = 10, y = 130)
		self.text_taxa = tk.Entry(self.master,width=10,bd=2,relief="flat",bg="#cccccc",text="%")
		self.text_taxa.place(x=10,y=165)


		self.label_parcelas = tk.Label(self.master,fg="#121212",bg="#00afaf",text="NUEMRO DE PARCELAS",font=("sanserif",12, "italic"))
		self.label_parcelas.place(x = 10, y = 210)
		self.text_parcelas = tk.Entry(self.master,width=10,bd=2,relief="flat",bg="#cccccc")
		self.text_parcelas.place(x=10,y=245)


		self.label_Total = tk.Label(self.master,fg="#121212",bg="#00afaf",text="TOTAL COM JUROS",font=("sanserif",12, "bold"))
		self.label_Total.place(x = 10, y = 290)
		self.text_Total = tk.Entry(self.master,width=10,bd=2,relief="flat",bg="#cccccc",text="valor")
		self.text_Total.place(x=10,y=325)

		self.bt_teste= tk.Button(self.master,text="aplicar",command=self.get_valor,relief="flat",bg="#00ac55")
		self.bt_teste.place(x=250,y=325)

	def get_taxa(self):
		 self.taxa = float(self.text_taxa.get())
		 return (self.taxa/100)	
	def get_value(self):
		self.value = float(self.text_value.get())
		return self.value
	def get_parcela(self):
		self.parcela = float(self.text_parcelas.get())
		return self.parcela
	def get_valor(self):
		self.text_Total.delete(0,tk.END)
		self.valor = self.get_value()*((self.get_taxa()+1)**self.get_parcela())
		self.text_Total.insert(0,"{0:.2f}" .format(self.valor))

		self.text_value.delete(0,tk.END)
		self.text_taxa.delete(0,tk.END)
		self.text_parcelas.delete(0,tk.END)

	def about(self):
		self.show_about=tk.Tk()
		self.show_about.title("ABOUT")
		self.show_about.geometry("450x400+250+150")
		self.info=tk.Label(self.show_about,text='''
PROGRAMA SIMPLES PARA CALCULO DE JUROS COMPOSTOS COM \n
TAXA FIXA VALOR TOTAL EM FUNCAO DO NUMERO DE PARCELAS\n
ESSE CALCULO FOI FEITO UTILIZANDO A FORMULA\n
FV(n) = (PV.(1+i)**n)\n
V = VALOR FUTURO\n
PV = VALOR INICIAL\n
i = TAXA\n
n = TEMPO\n
\n\n
CREDITOS
PROFESSORA: Mônica Gaiotto			''',justify="left")
		self.info.place(x=2,y=10)

root = tk.Tk()

if __name__=="__main__":
	app = Calc_juros(master=root)
	app.mainloop()