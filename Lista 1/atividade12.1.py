soma = 0
n = 3

for i in range (1, n + 1):
    numero = float(input(f"digite o {i}º numero:" ))
    soma += numero

multiplicacao = soma / n 

print("a media dos numeros digitados e:", multiplicacao)