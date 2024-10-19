import xml.etree.ElementTree as ET
import os


def consultar_empleado_xml(nombre, xml_path):
    if os.path.exists(xml_path):
        tree = ET.parse(xml_path)
        root = tree.getroot()


        for empleado in root.findall("empleado"):
            nombre_elem = empleado.find("nombre")
            if nombre_elem is not None and nombre_elem.text == nombre:
                # Extraer la información del empleado
                edad_elem = empleado.find("edad")
                depto_elem = empleado.find("departamento")
                salario_elem = empleado.find("salario")
                

                print(f"Información del empleado '{nombre}':")
                print(f"Edad: {edad_elem.text}")
                print(f"Departamento: {depto_elem.text}")
                print(f"Salario: {salario_elem.text}")
                return
        print(f"Empleado '{nombre}' no encontrado en el archivo XML.")
    else:
        print(f"El archivo {xml_path} no existe.")


xml_path = r"C:\Users\jjuan\OneDrive\Escritorio\Universidad Juanjo\Base de datos 2\Parcial2\Punto1\a\XML\empleados.xml"
consultar_empleado_xml("Juan Perez", xml_path)
