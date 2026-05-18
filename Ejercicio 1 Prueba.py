# Programa para calcular descuento en medicamentos y despacho

# Valores base
valor_medicamentos = 60000
valor_despacho = 8000

# Validación de edad
while True:
    edad = int(input("Ingrese su edad: "))

    if 0 <= edad <= 100:
        break
    else:
        print("Edad inválida. Debe ingresar una edad entre 0 y 100.")

# Validación de tramo
while True:
    tramo = input("Ingrese su tramo (A, B, C o D): ").upper()

    if tramo in ["A", "B", "C", "D"]:
        break
    else:
        print("Tramo inválido. Debe ingresar A, B, C o D.")

# Cálculo descuento medicamentos
descuento_medicamentos = 0

if edad <= 30:
    if tramo == "A" or tramo == "B":
        descuento_medicamentos = 0.18
    elif tramo == "C" or tramo == "D":
        descuento_medicamentos = 0.12

elif 31 <= edad <= 60:
    if tramo == "A" or tramo == "B":
        descuento_medicamentos = 0.12
    elif tramo == "C" or tramo == "D":
        descuento_medicamentos = 0.08

# Si edad > 60, descuento queda en 0%

# Valor final medicamentos
valor_final_medicamentos = valor_medicamentos - (valor_medicamentos * descuento_medicamentos)

# Cálculo descuento despacho
descuento_despacho = 0

# Descuento por tramo
if tramo == "A" or tramo == "B":
    descuento_despacho += 0.10

# Descuento adicional por edad
if edad >= 55:
    descuento_despacho += 0.05

# Valor final despacho
valor_final_despacho = valor_despacho - (valor_despacho * descuento_despacho)

# Total a pagar
total = valor_final_medicamentos + valor_final_despacho

# Mostrar resultados
print("El valor de medicamentos es:", int(valor_final_medicamentos))
print("El valor del despacho es:", int(valor_final_despacho))
print("El total a pagar es:", int(total))