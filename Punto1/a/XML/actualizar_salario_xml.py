import os
import xml.etree.ElementTree as ET

def actualizar_salario_xml(nombre, nuevo_salario, xml_path):
    if os.path.exists(xml_path):
        tree = ET.parse(xml_path)
        root = tree.getroot()

        # Buscar el empleado por nombre y actualizar el salario
        for empleado in root.findall("empleado"):
            nombre_elem = empleado.find("nombre")
            if nombre_elem is not None and nombre_elem.text == nombre:
                salario_elem = empleado.find("salario")
                if salario_elem is not None:
                    salario_elem.text = str(nuevo_salario)
                    tree.write(xml_path, encoding="utf-8", xml_declaration=True)
                    print(f"Salario de {nombre} actualizado a {nuevo_salario} en el archivo XML.")
                    return
        print(f"Empleado {nombre} no encontrado en el archivo XML.")
    else:
        print(f"El archivo {xml_path} no existe.")

xml_path = r"C:\Users\jjuan\OneDrive\Escritorio\Universidad Juanjo\Base de datos 2\Parcial2\Punto1\a\XML\empleados.xml"

actualizar_salario_xml("Juan Perez", 3500, xml_path)
