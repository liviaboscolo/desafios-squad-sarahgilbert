# Escreva um programa que calcule o salário líquido. Lembrando de
# declarar o salário bruto e o percentual de desconto do Imposto de
# Renda.
# ● Renda até R$ 1.903,98: isento de imposto de renda;
# ● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
# ● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
# ● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
# ● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.


def calcular_salario_liquido(salario_bruto):
    # Definindo as faixas e alíquotas do imposto de renda
    faixas = [
        (0, 1903.98, 0),
        (1903.99, 2826.65, 7.5),
        (2826.66, 3751.05, 15),
        (3751.06, 4664.68, 22.5),
        (4664.69, None, 27.5) 
    ]

    imposto_renda = 0
    for faixa in faixas:
        limite_inferior, limite_superior, aliquota = faixa
        if salario_bruto > limite_inferior:
            if limite_superior is None or salario_bruto <= limite_superior:
                imposto_renda += (salario_bruto - limite_inferior) * (aliquota / 100)
                break
            else:
                imposto_renda += (limite_superior - limite_inferior) * (aliquota / 100)

    salario_liquido = salario_bruto - imposto_renda

    return salario_liquido, imposto_renda

salario_bruto = float(input("Digite o salário bruto: R$ "))
salario_liquido, imposto_renda = calcular_salario_liquido(salario_bruto)

print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Imposto de Renda: R$ {imposto_renda:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")