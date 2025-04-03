#cadrastar alunos em uma escola, solicitando nome, idade e turma, e exiba uma mensagem "aluno cadastrado com sucesso" e verifique se a idade é maior que 6 anos ou igual para validar a matricula

nome= input ("insira seu nome")
idade= int(input("insira sua idade"))
turma= input("qual turma pertence")
if idade>=6:
    print(f"Aluno Cadastrado com sucesso{nome} {idade}anos, turma {turma}")
else:
    print ("a criança ainda nao possui idade suficienta")

