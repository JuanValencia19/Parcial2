import json
import os
def actualizar_salario_json(nombre, nuevo_salario, json_path):
    if os.path.exists(json_path):
        with open(json_path, 'r') as json_file:
            data = json.load(json_file)


        for empleado in data["empleados"]:
            if empleado["nombre"] == nombre:
                empleado["salario"] = nuevo_salario
                with open(json_path, 'w') as json_file:
                    json.dump(data, json_file, indent=4)
                print(f"Salario de {nombre} actualizado a {nuevo_salario} en el archivo JSON.")
                return
        print(f"Empleado {nombre} no encontrado en el archivo JSON.")
    else:
        print(f"El archivo {json_path} no existe.")

json_path= r"C:\Users\jjuan\OneDrive\Escritorio\Universidad Juanjo\Base de datos 2\Parcial2\Punto1\a\JSON\empleados.json"

actualizar_salario_json("Juan Perez", 3500, json_path)
