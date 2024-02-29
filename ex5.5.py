alunos = dict()
while True:
    nome_aluno = input("Digite o nome do aluno (ENTER para concluir): ")
    if (nome_aluno): 
        nota_aluno = float(input(f"Digite a nota de {nome_aluno} (0 a 10): "))
        alunos[nome_aluno] = nota_aluno
    else:
        break

alunos_aprovados = {aluno: nota for aluno, nota in alunos.items() if nota>= 7}
print(alunos_aprovados)

  