import random
class Forca:
    def __init__(self):
        self.palavra = self.gerador()
        self.digitadas = []
        self.certas = []
        self.erro = 0
    def gerador(self):
        with open("/home/jelinux/Documentos/teste.txt",mode="r")as f:
            x = f.read().split()
            return(random.choice(x).upper())  
    def draw_erro(self):
        if self.erro == 1:
            print()
            print('###( )###')
        elif self.erro == 2:
            print('###( )###')
            print('    |    ')
        elif self.erro == 3:
            print('###( )###')
            print('    |    ')
            print('  \ | /  ')
        elif self.erro == 4:
            print('###( )###')
            print('    |    ')
            print('  \ | /  ')
            print('   \ /   ')
        elif self.erro == 5:
            print('###( )###')
            print('    |    ')
            print('  \ | /  ')
            print('   \ /   ')
            print('   / \   ')
            print('  /   \  ')
            print(self.palavra)
            return print('Enforcado')
    

    def jogar(self):
        while True:
            print("JOGO DA FORCA 0.1")
        
            if self.erro == 5:
                print(self.digitadas)
                break
                return False
            
            self.key = ""
            
            for letra in self.palavra:
                self.key+= letra if letra in self.certas else '.'
                
            print(self.key,'\n')
            
            if self.key == self.palavra:
                return print('Ganhou')
                
            self.chute = input('digite uma letra\n').upper().strip()
            
            if self.chute in self.digitadas:
                print('Voce ja digitou essa\n')
                continue   
            else:
                self.digitadas+=self.chute
                
                if self.chute in self.palavra:
                    self.certas += self.chute
                    
                else:
                    self.erro +=1
                    self.draw_erro()

x = Forca()
x.jogar()
