
import xml.etree.ElementTree as ET
def modificar_stock(xml_path, id_producto, nuevo_stock):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Buscar el producto por su identificador
    for producto in root.findall("producto"):
        if producto.get("id") == id_producto:
            stock_elem = producto.find("stock")
            if stock_elem is not None:
                stock_elem.text = str(nuevo_stock)
                tree.write(xml_path, encoding="utf-8", xml_declaration=True)
                print(f"Stock de {id_producto} actualizado a {nuevo_stock}.")
                return
    print(f"Producto con ID {id_producto} no encontrado.")

xml_path= r"C:\Users\jjuan\OneDrive\Escritorio\Universidad Juanjo\Base de datos 2\Parcial2\Punto2\catalogo.xml"
modificar_stock(xml_path, "P001", 20)
