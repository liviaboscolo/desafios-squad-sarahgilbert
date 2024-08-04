#michelle
#3. Escreva um script que pergunta ao usuário se ele deseja converter
#uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
#cada opção, crie uma função.
def temperatura_cel_tp_fah(celsius):
     fahrenheit = (celsius * 9/5) + 32
     return fahrenheit
temperatura_cel= float(input("Temperatura em celsius"))
temperatura_fah= temperatura_cel_tp_fah(temperatura_cel)
temperatura_cel_tp_fah(temperatura_cel)

def temperatura(fahrenheit):
    celsius =(fahrenheit - 32) * 5/9
    return celsius
temperatura_fahei= float(input("Temperatura em fahrenheit"))
temperatura_cel= temperatura(temperatura_fahei)
temperatura(temperatura_fahei)


#Extra: Crie uma terceira, que é um menu para o usuário escolher a
#opção desejada, onde esse menu chama a função de conversão
#correta
def menu () :
    print("-",*20)
def opcao_temperatura():
    menu()
escolha=str(input("Digite C para celsius e F para  fahrenheit ").upper()) 
if escolha == "C":
    def temperatura(fahrenheit):
     celsius =(fahrenheit - 32) * 5/9
     return celsius
    temperatura_fahei= float(input("Temperatura em fahrenheit"))
    temperatura_cel= temperatura(temperatura_fahei)
    print(f"A temperatura em celsius e ", temperatura(temperatura_fahei))
   
elif escolha == "F"  :
    
    def temperatura_cel_tp_fah(celsius):
         fahrenheit = (celsius * 9/5) + 32
         return fahrenheit
    temperatura_cel= float(input("Temperatura em celsius"))
    temperatura_fah= temperatura_cel_tp_fah(temperatura_cel)
    print(f"A temperatura em fahrenheit e " ,temperatura_cel_tp_fah(temperatura_cel))
else :
    print("Opcao Incalida")    
