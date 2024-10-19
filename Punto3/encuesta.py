import json

# Datos de encuestas
encuestas = {
    "encuestas": [
        {
            "ciudad": "Bogotá",
            "personas_encuestadas": 150,
            "transporte_mas_utilizado": "TransMilenio"
        },
        {
            "ciudad": "Medellín",
            "personas_encuestadas": 120,
            "transporte_mas_utilizado": "Metro"
        },
        {
            "ciudad": "Cali",
            "personas_encuestadas": 90,
            "transporte_mas_utilizado": "Bus"
        }
    ]
}

# Guardar encuestas en un archivo JSON
json_path = r"C:\Users\jjuan\OneDrive\Escritorio\Universidad Juanjo\Base de datos 2\Parcial2\Punto3\encuesta.json"
with open(json_path, 'w') as json_file:
    json.dump(encuestas, json_file, indent=4)

print("Archivo encuestas.json creado con éxito.")