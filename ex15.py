#solicite ao usuario o nome de um produto, a quantidade comprada e o preço unitario, calcule e exiba o total da compra, aplique um desconto de 5% se o valor total for maior que r$100
produto= input(" digite o nome do produto")
quant_compra=int(input (" insira a quantidade de produto"))
preço_unit= float(input(" insira o preço por unidade"))
total_compra= quant_compra * preço_unit

if total_compra>=100:
    desconto= total_compra* 0.05
    print(f" sem o desconto a compra de {total_compra} passou a ser {total_compra-desconto} ")
else:
    print (f"não terá desconto, valor da compra {total_compra}")
