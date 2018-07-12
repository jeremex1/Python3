import tkinter as tk
from tkinter import *

class Editor:

	def windown(self):

		self.master = tk.Tk()
		self.master.geometry("500x500+200+200")
		self.master.title("Pytext")
		self.menu = tk.Menu(self.master,tearoff=0)
		self.menu1 = tk.Menu(self.menu,tearoff=0)
		self.menu1.add_command(label="novo",command=self.new)
		self.menu.add_cascade(label="arquivo",menu=self.menu1)
		self.master.configure(menu = self.menu)
		self.master.mainloop()

	def new(self):
		if self.new == True:
			return False


		

x = Editor()
x.windown()
if x.new == False:
	new = x
else:
	print("errou")
