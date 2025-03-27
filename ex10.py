# peça o valor da compra e calcule o desconto
valor_compra= int(input("digite o valor da compra:"))
if valor_compra ==200 or valor_compra<=100:
    desconto= valor_compra * 0.02
    print (" desconto de 20%")
elif valor_compra ==500 or 700:
     desconto= valor_compra * 0.04
     print(" o desconto é de 30%")
else:
     desconto= 0
     print ("não foi inserido nenhum valor")
