#verificaçao de maiores de idade. desenvolva um programa que: solicite o ano de nascimento de uma pessoa, e exiba uma mensagem se ela é maior de idade <=18 anos ou nao
ano_nascimento= int(input("insira o ano de nascimento"))
idade= 2025 - ano_nascimento

if idade>= 18:
    print ("maior de idade")
else:
    print("menor de idade")
