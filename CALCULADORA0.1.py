#variaveis do progama
x = 1# x verifica a operacao digitada pelo usuario
n1 = 0 # n1 armasena o primeiro numero aser usado nos calculos esse numerro e digitado pelo usuario
n2 = 0 # n2 armasena o primeiro numero aser usado nos calculos esse numerro e digitado pelo usuario
result = 0 # armasena o resultado dasoperacoes
while x != 0:
    print ("CALCULADORA BASICA SEM INTERFACE GRAFICA 0.1\n\n")# titulo

# Operacoes suportadas pela calculadora
    print ("(1) para fazer a operacao de soma : +\n")
    print ("(2) para fazer a operacao de subtracao : -\n")
    print ("(3) para fazer a operacao de multiplicacao : *\n")
    print ("(4) para fazer a operacao de divisao : /\n")
    print ("(0) para fazer a operacao de SAIR\n")

    #verifica qual operacao o usuario deseja realizar
    x = int(input("Digite a operacao desejada\n\t\t:"))
    if x > 4 :
        print("Digite uma opearacao valida")
   #verifica se a operacao desejada e valida ou se o usuario deseja encerar a aplicacao se for valida solicita que o usuario digite os valore
    if x >= 1 and x <=4 :
         n1 = int(input("Digite o primerio operando\n\t\t:"))
         n2 = int(input("Digite o segundo operando\n\t\t:"))
         #verifica se  a opcao do usuario e a de soma se for executa o bloca do codigo se nao passa para a proxima condicao
         if x == 1 :
               result = n1 + n2
               print("O resultado da soma entre os valores e :  ",result)
         #verifica se  a opcao do usuario e a de soma se for executa o bloca do codigo se nao passa para a proxima condicao
         elif x == 2 :
               result = n1 - n2
               print("O resultado da subtracao entre os valores e : %d "%result)
         #verifica se  a opcao do usuario e a de soma se for executa o bloca do codigo se nao passa para a proxima condicao
         elif x == 3:
               result = n1 * n2
               print("O resultado da multiplicacao entre o valores e : %d \n" %result)
         #verifica se  a opcao do usuario e a de soma se for executa o bloca do codigo se nao passa para a proxima condicao
         elif x == 4 :
               result = n1 / n2
               print ("O resultado da divisao entre os valores e : %d "%result)
