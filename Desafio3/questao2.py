medias_alunos = []

for a in range(5):
    print(f"Digite as 4 notas do aluno {a+1}:")
    notas = [float(input(f"Nota {b+1}: ")) for b in range(4)]
    media = sum(notas) / 4
    medias_alunos.append(media)


acima_media = len([media for media in medias_alunos if media >= 7.0])

print(f"{acima_media} alunos apresentaram média maior ou igual a 7")
