 # codigo em python para existir as tabuadas de 7, 8 e 9
numero= int(input("digite a base da tabuada"))
def tabuada(numero):
  print (f"tabuada do {numero}:")
  for i in range (1, 11):
      print (f"{numero} x {i} = { numero * i}")

tabuada(numero)




