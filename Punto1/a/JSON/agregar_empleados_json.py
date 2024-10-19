import json
import os

# Función para agregar empleados al archivo JSON
def agregar_empleado_json(nombre, edad, departamento, salario, json_path):

    if os.path.exists(json_path):
        with open(json_path, 'r') as json_file:
            data = json.load(json_file)
    else:
        data = {"empleados": []}

    # Crear un nuevo empleado en el JSON
    nuevo_empleado = {
        "nombre": nombre,
        "edad": edad,
        "departamento": departamento,
        "salario": salario
    }

    # Añadir el empleado al array de empleados
    data["empleados"].append(nuevo_empleado)

    # Guardar los cambios en el archivo JSON
    with open(json_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Empleado {nombre} agregado al archivo JSON.")


json_path = r"C:\Users\jjuan\OneDrive\Escritorio\Universidad Juanjo\Base de datos 2\Parcial2\Punto1\a\JSON\empleados.json"
agregar_empleado_json("Juan Perez", 30, "Recursos Humanos", 3000, json_path)
