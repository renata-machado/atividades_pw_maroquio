nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    print("Aprovado!")
else:
    print("Reprovado!")
if nota1 == 10 or nota2 == 10 or nota3 == 10:
    print("Parabéns!")