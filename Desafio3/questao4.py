"""
Nadi - questao 4, desafio 3
Crie um dicionário representando contatos (nome, telefone).
Permita ao usuário procurar por um contato pelo nome.
"""
contatos = {
    "Leticia": "11 1234586789",
    "Livia": "22 1234586789",
    "Michelle": "33 1234586789",
    "Nadi": "44 1234586789",
    "Nicola":"55 1234586789",
    "Raquel":"66 1234586789",
    "Rosana": "77 1234586789"
}
nome = input("Digite o nome do contato: ")
if nome in contatos:
    print(f"Telefone de {nome} é {contatos[nome]}")
else:
    print("Contato não encontrado no registro.")
