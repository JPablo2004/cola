# cola
cola = ["Salas", "Sebas", "Santi", "Brand"]

# Se agregan los elementos al final de la cola 
cola.append("Jhonatan")
cola.append("Feiber")

print("Cola inicial:", cola)

# lista para almacenar los nombres atendidos
atendidos = []

# sacando elemetos por el principio
while cola:
    n = cola.pop(0)
    atendidos.append(n)
    print(f"Atendiendo a {n}")

print("Cola final:", cola)
print("Nombres atendidos:", atendidos)