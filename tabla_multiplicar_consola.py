import sys



if len(sys.argv) == 2:
    valor = int(sys.argv[1])

    print(f" ---------- Tabla de multiplicar {valor} -----------")

    for i in range(11):
        print(f"{valor} x {i} = {valor * i}")
else:
    print("Uso del script; tabla:multiplicar.py <valor>")

