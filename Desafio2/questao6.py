def solicitar_e_validar(input_prompt, valid_value, erro):
    while True:
        user_input = input(input_prompt)
        if user_input == valid_value:
            print(f"{input_prompt.split(' ')[2][:-1]} válido.")
            break
        else:
            print(f"🚨 {erro}.")

solicitar_e_validar("Adicione seu usuário: ", "admin", "Por favor, adicione um usuário correto")
solicitar_e_validar("Adicione sua senha: ", "admin123", "Por favor, adicione a senha correta")

print("Acesso liberado🎈")