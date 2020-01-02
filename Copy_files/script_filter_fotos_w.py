#####VERSION FOR WINDOWS####
##copias as Imagens selecionadas para uma pasta que sera criada se nao existir

from tkinter import Frame,Entry,Menu,Button,messagebox,filedialog
import os
import re
import sys
import string
import tkinter as tk

class Filter(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master.title("FILTER")
        self.master.geometry("350x250+300+300")
        self.master.resizable(False,False)
        self.set_label_list()
    def set_label_list(self):

        self.local_dir = tk.Label(self.master,text="localizacao das fotos")
        self.local_dir.place(x=50,y=10)
        
        self.list_localdir = tk.Entry(self.master,width=35)
        self.list_localdir.place(x=5,y=30)
        self.list_localdir.focus()
        
        self.bt_search_dir=tk.Button(self.master,text="....",bg="#0AFF55",bd=0.25,relief="flat",command=self.get_directory_curent)
        self.bt_search_dir.place(x=295,y=28)

        self.label_dir = tk.Label(self.master,text="local onde sera copiado as fotos")
        self.label_dir.place(x=50,y=60)

        self.list_dir = Entry(self.master,width=35)
        self.list_dir.place(x=5,y=90)

        self.bt_search_dir=tk.Button(self.master,text="....",bg="#0AFF55",bd=0.25,relief="flat",command=self.get_directory_distination)
        self.bt_search_dir.place(x=295,y=88)

        self.label_list_file = tk.Label(self.master,text='que fotos você deseja \ntipo no formato "número, número, "\n nome do arquivo padrão IMG+número.CR2 ')
        self.label_list_file.place(x=20,y=115)

        self.list_file = tk.Entry(self.master,width=35)
        self.list_file.place(x=5,y=170)

        self.bt_get_list = tk.Button(self.master,text="filter",bg="#0AFF55",bd=0.25,command=self.get_list)
        self.bt_get_list.place(x=285,y=210)

    def get_list(self):
        directory = self.list_dir.get()
        actual_directory=self.list_localdir.get()
        os.system("mkdir "+str(directory))
        for i in self.list_file.get().split(','):
            x= ("copy "+actual_directory+"\IMG"+str(i)+".CR2 "+str(directory))
            y=str.replace((x),"/","\\")
            os.system(y)

    def get_directory_curent(self):
        
        self.search_local_dir = tk.filedialog.askdirectory()
        self.list_localdir.delete(0,tk.END)
        self.list_localdir.insert(tk.END,self.search_local_dir)
        
    
    def get_directory_distination(self):
        self.dir_destination = tk.filedialog.askdirectory()
        self.list_dir.delete(0,tk.END)
        self.list_dir.insert(tk.END,self.dir_destination)

root=tk.Tk()
app=Filter(master=root)
app.mainloop()
