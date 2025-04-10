#verificaçao de acesso ao clube. crie um programa em py que determine se uma pessoa pode entrar em um clube com as seguintes condições: precisa ter mais de 18 anos, se nao for membro, deve pagar um ingresso e se estiver acompanhado por um membro, paga meia entrada
idade= int(input("insira sua idade"))
membro= input("você é membro?")
acompanhado= input("você esta acompanhado")

if idade>= 18:
    if membro== "sim":
        print(" bem vindo")
    else:
        if acompanhado== "sim":
            print(" pagar meia entrada")
        else:
            print(" pagar meia entrada")
            if acompanhado =="nao":
                print("pagar ingresso")