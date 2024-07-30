import random
def jogar_forca():
    print("Descubra a linguagem de Programação...🦖")
    
    lista = ["Python", "JavaScript", "C#", "Java", "C++", "C"]
    
    palavra_secreta = random.choice(lista).lower() #faz o sorteio da palavra da lista

    mascara_palavra = ['_' for _ in palavra_secreta] #mascara a palavra da lista

    tentativas = 6
    

    while True:
        print(' '.join(mascara_palavra))
        
        # Verifica se a palavra foi completamente descoberta
        if '_' not in mascara_palavra:
            print("Parabéns! Você ganhou!")
            return
        
        letra = input("Digite uma letra: ").lower()
        
        # Verifica se a letra está na palavra secreta
        if letra in palavra_secreta:
            # Revela todas as ocorrências da letra na palavra
            for i, l in enumerate(palavra_secreta):
                if l == letra:
                    mascara_palavra[i] = letra
        else:
            # Decrementa o número de tentativas se a letra estiver errada
            tentativas -= 1
            print(f"Erro! Letra não está na palavra. Tentativas restantes: {tentativas}")
            
            # Verifica se o jogador perdeu
            if tentativas <= 0:
                print("Game Over! Você perdeu.")
                return

jogar_forca()
