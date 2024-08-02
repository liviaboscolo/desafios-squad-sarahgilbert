ano_nascimento = int(input("Informe seu ano de nascimento: "))
ano_atual = int(input("Informe o ano atual: "))
idade = ano_atual - ano_nascimento
if idade == 1:
    print(f"Você tem {idade} ano")
else:
    print(f"Você tem {idade} anos")
