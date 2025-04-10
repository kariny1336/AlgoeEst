# temos um site de venda, qeueremos filtar nosssos usuarios para receberem os anuncios corretos, conforme a tabela= 
#menor de 15 anos= oferecer artigos infantis
#entre 15 e 21 feminino= oferecer maquiagem e moda
#entre 15 e 32 e atleta masculino= oferecer artigos esportivos
#entre 15 e 21 nao atleta masculino= oferecer videogames
#entre 21 e 32 masculino e nao atleta= oferecer livros, jardinagem e eletrodomesticow
# entre 22 e 35 feminino= oferecer artigos esportivos e intens de casa

idade=int(input("insira sua idade"))
genero= input("insira seu genero")
atleta= input("pratica algum esporte?")

if idade<= 15:
    print(" artigos infantis")
elif idade >=15 and  idade <= 21 and genero == "feminino":
    print(" artigos esportivos")
elif idade >= 15 and idade<= 32 and atleta== "sim" and genero=="masculino":
    print(" artigos esportivos")
elif idade >= 15 and idade <= 21 and atleta== "nao" and  genero== "masculino":
    print("  video games")
elif idade >= 21 and idade <= 32 and genero== "masculino" and atleta== "nao" :
    print("  livros, jardinagens e eletrodomesticos")
elif idade >= 22 and idade <= 35 and genero == "feminino":
    print(" itens de casa")
else:
    (" sua idade nao tem itens ")