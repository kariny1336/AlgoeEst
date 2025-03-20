#isso e um comentario
# print ("mensagem")
# idade=6
# altura=0.50
# peso=5.950
# nome="Franscisco"
# print(idade,altura,peso,nome)
# nome=input ("insira seu nome")
# idade=int(input("insira sua idade"))  #int= inteiro para numeros
# peso=float(input("insira seu peso"))
# print(f"{nome} {idade} anos {peso}kg")

#com a funcao type
# pedaco_pizza=5
# cliente="John"
# print(type(pedaco_pizza))
# print(type(cliente))

# pedaco_pizza=input("informe quantos pedacos comeu")
# print(type(pedaco_pizza))

# a=4
# A="sally"
# print(a)
# print(A)


# a=4
# a="sally"
# print(a)
# print(a)

# fruta1, fruta2, fruta3= "laranja", "banana", "maça"
# print(fruta1,fruta2,fruta3)

# primeiro_numero=5
# segundo_numero=10
# print(primeiro_numero + segundo_numero)

# nome=input("qual o vingador mais forte?")
# print(f"olá, {nome}!")
# if nome == "hulk":   # 2 == um para comparar outro para atribuir
#     print("bem vindo vingador mais forte!")
# else:
#     print ("acesso negado")

# # and (e logico) retorna true se ambas cndições forem verdadeiras
# x=5
# if x > 2 and x< 10: # ambas as condicoes devem ser verdadeiras
#     print (" o numero esta entre 2 e 10")
# else:
#     print(" nao esta entre 2 e 10")


# x=5
# if x<2 or x>4: #apenas uma condicao precisa ser verdadeira
#     print(" o numero é menor que 2 ou maior que 4")

# x=3
# if x <2 or x> 4:
#         print (" o numero é menor que 2 ou maior que 4")

# x= 5
# if not x> 10: #inverte a condição ( x nao é maior que 10)
#     print (" o numero nao é maior que 10")

x=5
y=8

if x > 2 and (y >10 or not x==5):
    print(" condição complexa atendida")
else:
    print (" condição não atendida")   

    #1. not 2. and 3. or