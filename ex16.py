#calcule a media das notas e faça um programa que peça ao usuario tres notas, calcule a media aritmética das notas, informe se o aluno esta aprovado(media>=7,) em recuperação (media entre 5 e 7) oy reprovado (media<5)
nota1=int(input("insira a primeira nota"))
nota2=int(input("insira a segunda nota"))
nota3=int(input("insira a terceira nota"))
media= (nota1+nota2+nota3)/3

if media>=7:
    print("você foi aprovado")
elif media>=5 and media <7:
    print("você está de recuperação")
else:
    media<5
    print ("você foi reprovado")