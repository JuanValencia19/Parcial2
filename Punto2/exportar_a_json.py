import json
import xml.etree.ElementTree as ET

# Función para exportar productos del XML a un archivo JSON
def exportar_a_json(xml_path, json_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    productos = []
    # Recorrer los productos y crear la estructura para el JSON
    for producto in root.findall("producto"):
        prod_info = {
            "id": producto.get("id"),
            "nombre": producto.find("nombre").text,
            "descripcion": producto.find("descripcion").text,
            "precio": float(producto.find("precio").text),
            "stock": int(producto.find("stock").text)
        }
        productos.append(prod_info)


    with open(json_path, 'w') as json_file:
        json.dump({"productos": productos}, json_file, indent=4)

    print(f"Catálogo exportado a {json_path}")


json_path = r"C:\Users\jjuan\OneDrive\Escritorio\Universidad Juanjo\Base de datos 2\Parcial2\Punto2\catalogo.json"
xml_path= r"C:\Users\jjuan\OneDrive\Escritorio\Universidad Juanjo\Base de datos 2\Parcial2\Punto2\catalogo.xml"
exportar_a_json(xml_path, json_path)


def buscar_producto_por_id(json_path, id_producto):

    with open(json_path, 'r') as json_file:
        catalogo = json.load(json_file)

    # Buscar el producto por su identificador
    for producto in catalogo["productos"]:
        if producto["id"] == id_producto:
            print(f"Producto encontrado: {producto}")
            return producto
    print(f"Producto con ID {id_producto} no encontrado.")
    return None


buscar_producto_por_id(json_path, "P001")

