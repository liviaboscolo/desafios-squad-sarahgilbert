#michelle
#3.Crie um dicionário representando um carrinho de compras.
#Adicione produtos (chaves) e quantidades (valores) ao carrinho.
#Calcule o total do carrinho de compra.
carrinho = {}

while True:
    produto = input("Digite o produto: ")
    valor = float(input("Digite o valor: ").replace(",", "."))

    if produto in carrinho:
        carrinho[produto] += valor
    else:
       carrinho[produto] = valor

    add_produtos = input("Mais Peodutos? (S/N): ").upper()
    if add_produtos == 'N':
        break

print("\nCarrinho de compras:")
for produto, valor in carrinho.items():
    print(f"- {produto}: R$ {valor:.2f}")

print(f"\nValor total: R$ {sum(carrinho.values()):.2f}")    
