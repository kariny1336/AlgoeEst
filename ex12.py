# um banco deseja diminuir contas sem saldos do sistema, solicitar ao responsavel o saldo da sua conta, caso for =0 alterara o status da conta
status_conta = True

valor_saldo= int(input("digite seu saldo no banco"))
if valor_saldo >=0.01:
    print("sua conta ainda esta ativa")
elif valor_saldo <0:
    print ("renegociar a divida")
else:
    status_conta = False
    print("conta inativada")