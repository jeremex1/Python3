
import tkinter as tk
from tkinter import *
import material_design_colors as c

class Cores(tk.Frame,c.Hexa):
	def __init__(self):
		self.master= tk.Tk()
		self.master.geometry("850x530+200+200")
		#self.master.resizable(width=False, height=False)
		self.master.title("Cores_Hexadecimal")
		self.Frame()
		self.master.mainloop()

	def Frame(self):
		self.frame1=tk.Frame(self.master,width=845,height=530,bd=5,relief='raise')
		self.frame1.pack(side=TOP)
		self.cores1()
		self.Label(self.red,0,0)
		self.Label(self.pink,0,1)
		self.Label(self.purple,0,2)
		self.Label(self.deep_purple,0,3)
		self.Label(self.indigo,0,4)
		self.Label(self.blue,0,5)
		self.Label(self.light_blue,0,6)
		self.Label(self.cyan,0,7)
		self.Label(self.teal,0,8)
		self.Label(self.black,0,9)
		self.Label(self.green,18,0)
		self.Label(self.light_green,18,1)
		self.Label(self.lime,18,2)
		self.Label(self.yellow,18,3)
		self.Label(self.amber,18,4)
		self.Label(self.orange,18,5)
		self.Label(self.deep_orange,18,6)
		self.Label(self.brown,18,7)
		self.Label(self.grey,18,8)
		self.Label(self.blue_grey,18,9)
		
	def Label(self,tons,linha,coluna):
		
		self.tons =tons
		cor = []
		linha =linha
		coluna = coluna
		for c in self.tons.values():
			cor.append(c)
		for lab in cor:
			self.label = tk.Label(self.frame1,width=10,text=lab,bg=lab)
			self.label.grid(row=linha,column=coluna)
			linha +=1

x = Cores()
