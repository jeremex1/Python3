
from tkinter import Frame,Label
import tkinter as tk
import material_design_colors as c

class Cores(tk.Frame,c.Hexa):
	def __init__(self):
		self.master= tk.Tk()
		self.master.geometry("850x530+200+200")
		#self.master.resizable(width=False, height=False)
		self.master.title("Cores_Hexadecimal")
		self.frame()
		self.master.mainloop()

	def frame(self):
		self.frame1=tk.Frame(self.master,width=845,height=530,bd=5,relief='raise')
		self.frame1.pack(side="top")
		self.cores1()
		self.label(self.red,0,0)
		self.label(self.pink,0,1)
		self.label(self.purple,0,2)
		self.label(self.deep_purple,0,3)
		self.label(self.indigo,0,4)
		self.label(self.blue,0,5)
		self.label(self.light_blue,0,6)
		self.label(self.cyan,0,7)
		self.label(self.teal,0,8)
		self.label(self.black,0,9)
		self.label(self.green,18,0)
		self.label(self.light_green,18,1)
		self.label(self.lime,18,2)
		self.label(self.yellow,18,3)
		self.label(self.amber,18,4)
		self.label(self.orange,18,5)
		self.label(self.deep_orange,18,6)
		self.label(self.brown,18,7)
		self.label(self.grey,18,8)
		self.label(self.blue_grey,18,9)
		
	def label(self,tons,linha,coluna):
		self.tons =tons
		linha =linha
		coluna = coluna
		cor =[cor for cor in self.tons.values() ]
		for lab in cor:
			self.label2 = tk.Label(self.frame1,width=10,text=lab,bg=lab)
			self.label2.grid(row=linha,column=coluna)
			linha +=1
if __name__=="__main__":
	x = Cores()
