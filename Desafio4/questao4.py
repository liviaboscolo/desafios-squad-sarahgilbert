"""
Nadi - questao 4, desafio 4
Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
Considere a tabela de conversão abaixo:
Dólar Americano: R$ 4,91
Peso Argentino: R$ 0,02
Dólar Australiano: R$ 3,18
Dólar Canadense: R$ 3,64
Franco Suiço: R$ 0,42
Euro: R$ 5,36
Libra esterlina: R$ 6,21
"""
conversao = {
    "Dólar Americano": 4.91,
    "Peso Argentino": 0.02,
    "Dólar Australiano": 3.18,
    "Dólar Canadense": 3.64,
    "Franco Suiço": 0.42,
    "Euro": 5.36,
    "Libra esterlina": 6.21
}

def converter_moeda(reais, conversao):
  for moeda, taxa in conversao.items():
    quantidade = reais / taxa
    print(f"{quantidade:.2f} {moeda}")

reais = float(input("Digite o valor em reais que você possui: "))
print(f"Com R${reais:.2f}, você pode comprar: ")
converter_moeda(reais, conversao)
