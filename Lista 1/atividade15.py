salario_fixo = float(input("Salário fixo: "))
vendas = float(input("Vendas: "))
comissao = vendas * 0.04
salario_final = salario_fixo + comissao
print(f"Comissão: R${comissao}, Salário final: R${salario_final}")