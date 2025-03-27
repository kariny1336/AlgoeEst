#escrever um programa que receba dois numeros e uma operação
numero1=float (int(input("digite o primeiro numero")))
numero2=float (int(input("digite o segundo numero")))
operação=input("digite uma operação(+, - , *, /)")
 
if operação == "+":
    adição=numero1+numero2
    print("resultado da soma:", adição)
elif operação == "-":
    subtração=numero1-numero2
    print("resultado da subtração:", subtração)
elif operação == "*":
    multiplicação=numero1*numero2
    print("resultado da multiplicaçao:", multiplicação)
elif operação == "/":
    divisão=numero1/numero2
    print("resultado da divisão:", divisão)
else:
    print("operação invalida:")
