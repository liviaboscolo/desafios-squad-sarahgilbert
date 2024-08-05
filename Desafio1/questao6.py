"""
Raquel - questao 6, desafio 1
 Escreva um programa que calcule o tempo de uma viagem. Faça um
comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h
"""
def time_travel():
    
    distancia = float(input('Digite a distância da viagem em KM: '))
    #removendo espaços
    velocidade_aviao = 600
    velocidade_carro = 100
    velocidade_onibus = 80

    tempo_aviao = distancia / velocidade_aviao
    tempo_carro = distancia / velocidade_carro
    tempo_onibus = distancia / velocidade_onibus #variaveis
    

    print(f"O tempo do percurso de avião é de {tempo_aviao:.2f} horas.")
    print(f"O tempo do percurso de carro é de {tempo_carro:.2f} horas.")
    print(f"O tempo do percurso de ônibus é de {tempo_onibus:.2f} horas.")

time_travel() #chamando a função