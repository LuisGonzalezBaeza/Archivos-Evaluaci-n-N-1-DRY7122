import json

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
datos = {"nombre": nombre, "apellido": apellido}
json_datos = json.dumps(datos)
print("nombre y apellido en json")
print(json_datos)

