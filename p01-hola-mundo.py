# Lee datos del usuario y envia un saludo la pantalla

print("Leyendo datos y enviando un mensaje a pantalla \n")

nombre = input("Dame tu nombre ? ")
edad   = int(input("Dame la edad   ? "))
peso   = float(input("Dame el peso ? "))

print(f"\nTu nombre es {nombre} tu edad es {edad} tu peso es {peso} \n")

print(type(nombre))
print(type(edad))
print(type(peso))