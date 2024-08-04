# 5. Desenvolva um programa que solicite ao usuário os comprimentos dos três
# lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
# equilátero: todos os lados com o mesmo valor
# isósceles: dois lados com o mesmo valor
# escaleno: todos os lados com medidas distintas.

def classificar_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return "Equilátero"
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        return "Isósceles"
    else:
        return "Escaleno"

def main():
    try:
        lado1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
        lado2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
        lado3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))

        if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
            tipo_triangulo = classificar_triangulo(lado1, lado2, lado3)
            print(f"O triângulo é {tipo_triangulo}.")
        else:
            print("Os comprimentos fornecidos não formam um triângulo válido.")
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
    main()