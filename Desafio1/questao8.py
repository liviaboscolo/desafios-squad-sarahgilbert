'''
Jéssica Caroline Lizar

8. Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.Calcule e mostre o total do seu
salário no referido mês.
'''

def check_input(msg):
  controle = 0
  while controle == 0:
    try:
      resp = float(input(f'{msg}: ').replace(',','.'))
      controle = 1
    except:
      print('Digite um valor numérico!')
  return resp

if __name__ == "__main__":
  valor_hora = check_input("Quanto você ganha por hora? ")
  horas_mes = check_input("Qual número de horas trabalhadas no mês? ")
  salario = valor_hora * horas_mes
  salario = str(round(salario,2)).replace('.',',')
  print(f'Seu salário é de R${salario}')
  