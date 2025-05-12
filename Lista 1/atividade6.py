#Atividade 6
latas = int(input("Latas (350ml): "))
g600 = int(input("Garrafas 600ml: "))
g2l = int(input("Garrafas 2L: "))
litros = (latas * 350 + g600 * 600 + g2l * 2000) / 1000
print(f"Total: {litros} litros")