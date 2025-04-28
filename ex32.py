base, inicio, fim= int(input("digite um numero")), int(input("digite o inicio de 1 a 10")), int(input("digite o fim"))
def tabuada_personalizada (base, inicio, fim):
 print (f"tabuada do {base} de {inicio} a {fim}:")
 for j in range (inicio, fim +1):
       print (f"{base} x {j} = {base * j}")

# uso
tabuada_personalizada (base, inicio, fim) 
