import xml.etree.ElementTree as ET


def crear_catalogo_xml(xml_path):
    root = ET.Element("catalogo")


    productos = [
        {"id": "P001", "nombre": "Laptop", "descripcion": "Laptop gaming", "precio": 1500, "stock": 10},
        {"id": "P002", "nombre": "Smartphone", "descripcion": "Teléfono inteligente", "precio": 600, "stock": 25},
        {"id": "P003", "nombre": "Teclado", "descripcion": "Teclado mecánico", "precio": 80, "stock": 50},
        {"id": "P004", "nombre": "Monitor", "descripcion": "Monitor 4K", "precio": 300, "stock": 15},
        {"id": "P005", "nombre": "Mouse", "descripcion": "Mouse inalámbrico", "precio": 40, "stock": 100},
    ]

    # Agregar productos al catálogo
    for prod in productos:
        producto = ET.Element("producto", id=prod["id"])

        nombre_elem = ET.SubElement(producto, "nombre")
        nombre_elem.text = prod["nombre"]

        descripcion_elem = ET.SubElement(producto, "descripcion")
        descripcion_elem.text = prod["descripcion"]

        precio_elem = ET.SubElement(producto, "precio")
        precio_elem.text = str(prod["precio"])

        stock_elem = ET.SubElement(producto, "stock")
        stock_elem.text = str(prod["stock"])

        # Añadir el producto a la raíz
        root.append(producto)

    # Crear el árbol y escribirlo en un archivo XML
    tree = ET.ElementTree(root)
    tree.write(xml_path, encoding="utf-8", xml_declaration=True)
    print(f"Catálogo creado en {xml_path}")


xml_path = r"C:\Users\jjuan\OneDrive\Escritorio\Universidad Juanjo\Base de datos 2\Parcial2\Punto2\catalogo.xml"
crear_catalogo_xml(xml_path)
