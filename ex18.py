#calcule o salario com horas extras e crie u m programa que peça o salario base,  numero de horas extras trabalhadas e o valor pago por hora extra, calcule o salario total (base+hora extra) e exiba o valor total do salario

salario_base= int(input("insira o valor do salario base"))
horas_extras= int(input("insira as horas extras"))
valor_hora_extra= int(input("insira o valor pago por horas extras"))

 
salario_total = salario_base + (horas_extras * valor_hora_extra)
print(f"o salario total é {salario_total}")