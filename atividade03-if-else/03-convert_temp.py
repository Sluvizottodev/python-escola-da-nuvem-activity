def celsiusPFahrenheit(c): return c * 9 / 5 + 32
def celsiusPKelvin(c): return c + 273.15

def fahrenheitPCelsius(f): return (f - 32) * 5 / 9
def fahrenheitPKelvin(f): return (f - 32) * 5 / 9 + 273.15

def kelvinPCelsius(k): return k - 273.15
def kelvinPFahrenheit(k): return (k - 273.15) * 9 / 5 + 32

orig = input("Digite a unidade de origem (C, F ou K): ").upper()
dest = input("Digite a unidade de destino (C, F ou K): ").upper()
val = float(input("Digite a temperatura: "))

if orig == dest:
    print(f"Temperatura convertida: {val:.1f}°{dest}")
elif orig == "C" and dest == "F":
    print(f"Temperatura convertida: {celsiusPFahrenheit(val):.1f}°F")
elif orig == "C" and dest == "K":
    print(f"Temperatura convertida: {celsiusPKelvin(val):.1f}K")
elif orig == "F" and dest == "C":
    print(f"Temperatura convertida: {fahrenheitPCelsius(val):.1f}°C")
elif orig == "F" and dest == "K":
    print(f"Temperatura convertida: {fahrenheitPKelvin(val):.1f}K")
elif orig == "K" and dest == "C":
    print(f"Temperatura convertida: {kelvinPCelsius(val):.1f}°C")
elif orig == "K" and dest == "F":
    print(f"Temperatura convertida: {kelvinPFahrenheit(val):.1f}°F")
else:
    print("Conversão inválida. Use apenas C, F ou K.")