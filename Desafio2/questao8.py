'''
Jéssica Caroline Lizar

8. Criar um programa em Python que solicite três números ao usuário, utilize
estruturas condicionais para determinar o maior entre eles e apresente o
resultado
'''

def check_input(n):
  controle = 0
  while controle == 0:
    try:
      resp = float(input(f'Digite o {n}º valor numérico: ').replace(',','.'))
      controle = 1
    except:
      print(' - Digite um valor numérico!')
  return resp

if __name__ == "__main__":
  n1 = check_input(1)
  n2 = check_input(2)
  n3 = check_input(3)

  if n1 > n2 and n1 > n3:
    print(f'\nO maior número é: {n1} -> {n1,n2,n3}')
  elif n2 > n3:
    print(f'\nO maior número é: {n2} -> {n1,n2,n3}')
  else:
    print(f'\nO maior número é: {n3} -> {n1,n2,n3}')
    
