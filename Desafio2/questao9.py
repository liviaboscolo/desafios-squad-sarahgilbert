# Jéssica Caroline Lizar
'''
9. O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos.
'''

def par_impar(num):
  par = 0
  if num%2 == 0:
    par = 1
  return par

def check_input():
  controle = 0
  while controle == 0:
    try:
      print("\nDigite 0 para sair")
      numero = int(input(f' - Digite um número inteiro: '))
      if numero >= 0:
        controle = 1
      else:
        print('   - Não é um número inteiro postivo!')
    except:
      print('   - Não é um número inteiro!')
  return numero

if __name__ == "__main__":
  pare = 0
  numeros = []

  while pare == 0:
    numero = check_input()
    numeros.append(numero)
    if numero == 0:
      numeros.pop()
      pare = 1

  pares = []
  impares = []
  for num in numeros:
    if par_impar(num) == 1:
      pares.append(num)
    else:
      impares.append(num)

  print(f"\nTotal número pares: {len(pares)} -> {pares}")
  print(f"Total número ímpares: {len(impares)} -> {impares}")