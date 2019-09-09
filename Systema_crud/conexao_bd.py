from mysql.connector import connect
import tkinter as tk


class Conexao():
    def __init__(self):
        pass
        #self.tela()
    def tela(self):
        self.login = tk.Tk()
        self.login.title('Login')
        self.login.geometry("350x200+200+200")
        self.login.focus()
        self.conectar()
        self.bt_conexao()
        self.login.mainloop()
        return self.connect()
    def conectar(self):
        self.label_user = tk.Label(self.login,text='User: ')
        self.label_user.place(x = 5 ,y = 10)

        self.entry_user = tk.Entry(self.login,width=30)
        self.entry_user.place(x = 80 , y = 10)

        self.label_password = tk.Label(self.login,text='Password : ')
        self.label_password.place(x = 5 , y = 40)

        self.entry_password = tk.Entry(self.login,width=30,show='*')
        self.entry_password.place(x = 80 , y = 40)

        self.label_host = tk.Label(self.login,text='Host : ')
        self.label_host.place(x = 5 , y = 70 )

        self.entry_host = tk .Entry(self.login,width=30)
        self.entry_host.place(x = 80 ,y = 70)

        self.label_port = tk.Label(self.login,text='Port : ')
        self.label_port.place(x = 5 ,y = 100)
        
        self.entry_port = tk.Entry(self.login,width=10)
        self.entry_port.place(x = 80 , y = 100)

        self.label_database = tk.Label(self.login,text='Database : ')
        self.label_database.place(x = 5 ,y = 130)

        self.entry_database = tk.Entry(self.login,width=30)
        self.entry_database.place(x = 80 , y = 130)
        return None

    def bt_conexao(self):
        self.bt_conect = tk.Button(self.login,text='conectar',command=self.connect)
        self.bt_conect.place(x = 150, y = 160)
        self.bt_conect.focus()
        
    def connect(self):

        try:
            self.conn = connect(user=self.entry_user.get(),password=self.entry_password.get(),
            host=self.entry_host.get(),port=self.entry_port.get(),database=self.entry_database.get())

        except Exception as e:
            tk.messagebox.showerror("falha no login",e)
            return False
        else:
            self.cursor = self.conn.cursor()
            self.cursor.execute('SELECT * FROM clientes')
            print(self.cursor.fetchone())
            self.login.quit()
            self.entry_user.delete(0,tk.END)
            return True
    
        
#conection = Conexao()
