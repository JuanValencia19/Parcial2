import json
import os


def consultar_empleado_json(nombre, json_path):
    if os.path.exists(json_path):
        with open(json_path, 'r') as json_file:
            data = json.load(json_file)

        # Buscar el empleado por nombre
        for empleado in data["empleados"]:
            if empleado["nombre"] == nombre:

                print(f"Información del empleado '{nombre}':")
                print(f"Edad: {empleado['edad']}")
                print(f"Departamento: {empleado['departamento']}")
                print(f"Salario: {empleado['salario']}")
                return
        print(f"Empleado '{nombre}' no encontrado en el archivo JSON.")
    else:
        print(f"El archivo {json_path} no existe.")


json_path = r"C:\Users\jjuan\OneDrive\Escritorio\Universidad Juanjo\Base de datos 2\Parcial2\Punto1\a\JSON\empleados.json"
consultar_empleado_json("Juan Perez", json_path)
