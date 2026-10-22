capital = float(input("Capital (C): "))
tasa = float(input("Tasa anual (I): "))
anios = int(input("Años (M): "))

while capital < 0 or tasa <= 0 or tasa >= 100 or anios <= 0:
    print("Terna inválida. Ingrese nuevos datos.")
    capital = float(input("Capital (C): "))
    tasa = float(input("Tasa anual (I): "))
    anios = int(input("Años (M): "))

saldo = capital

for anio in range(1, anios + 1):
    interes = saldo * tasa / 100
    saldo = saldo + interes
    print(f"Año {anio}: {saldo:.2f}")

print(f"Saldo final: {saldo:.2f}")