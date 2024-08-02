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
