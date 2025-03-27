#pedir ao usuario um nome de usuario e senha que sejam corretso caso esteja errado escreva "credenciais erradas"
usuario=input("digite um nome de usuario:")
senha= int(input("digite uma senha:"))

if usuario == "kari" and senha == "12345":
    print ("credenciais corretas")
else:
    print ("credenciais erradas")
