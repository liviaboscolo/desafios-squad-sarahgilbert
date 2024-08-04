'''
Jéssica Caroline Lizar

9. Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício.
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
  horas_exercicio_semana = check_input("Qual o número de horas de exercício físico realizado por semana? ")
  calorias = (horas_exercicio_semana * 5 * 60) * 4 # mês -> 4 semanas, 1 hora = 60 minutos
  calorias = str(round(calorias,2)).replace('.',',')
  print(f'Total de calorias queimadas em um mês: {calorias} cal')
  