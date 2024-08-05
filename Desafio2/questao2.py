"""
Lívia - questao 2, desafio 2
 Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

turno = input("Digite o turno que você estuda (M-matutino, V-vespertino, N-noturno): ").strip().upper()

inicial = turno[0]

print(f"Entrada recebida: '{turno}'")

if inicial == 'M':
    print("Bom Dia!")
elif inicial == 'V':
    print("Boa Tarde!")
elif inicial == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido!")