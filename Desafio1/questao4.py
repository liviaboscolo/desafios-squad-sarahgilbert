"""
Nadi - questao 4, desafio 1
Receba do usuário a quantidade de litros de combustível consumidos e
a distância percorrida. Calcule e imprima o consumo médio em km/l..
"""
qtd_litros = float(input("Insira a quantide de litros de combustíves consumidos: "))
distancia = float(input("Insira a distância percorrida: "))
consumo_medio= distancia/qtd_litros
print(f"O consumo médio do veículo foi de {consumo_medio:.2f} km/l.")
