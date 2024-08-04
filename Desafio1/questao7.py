def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC).

    Args:
        peso (float): O peso da pessoa em quilogramas.
        altura (float): A altura da pessoa em metros.

    Returns:
        float: O valor do IMC calculado.
    """
    return peso / (altura * altura)

def categoria_imc(imc):
    """
    Determina a categoria do IMC.

    Args:
        imc (float): O valor do IMC.

    Returns:
        str: A categoria correspondente ao IMC.
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

try:
    # Solicita ao usuário que insira o peso em quilogramas
    peso = float(input("Digite o seu peso (kg): "))
    
    # Solicita ao usuário que insira a altura em metros
    altura = float(input("Digite a sua altura (m): "))

    # Verifica se os valores de peso e altura são positivos
    if peso <= 0 or altura <= 0:
        print("Peso e altura devem ser valores positivos.")
    else:
        # Calcula o IMC usando a função calcular_imc
        imc = calcular_imc(peso, altura)
        
        # Imprime o valor do IMC formatado com duas casas decimais
        print("Seu Índice de Massa Corporal (IMC) é: {:.2f}".format(imc))
        
        # Determina e imprime a categoria do IMC
        print("Categoria: {}".format(categoria_imc(imc)))

except ValueError:
    # Captura exceções de valor inválido e imprime uma mensagem de erro
    print("Por favor, insira valores numéricos válidos.")