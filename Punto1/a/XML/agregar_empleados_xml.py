import xml.etree.ElementTree as ET
import os


def agregar_empleado_xml(nombre, edad, departamento, salario, xml_path):
    # Verifica si el archivo existe y carga el árbol
    if os.path.exists(xml_path):
        tree = ET.parse(xml_path)
        root = tree.getroot()
    else:
        root = ET.Element("empleados")
        tree = ET.ElementTree(root)
    

    empleado = ET.Element("empleado")
    
    nombre_elem = ET.SubElement(empleado, "nombre")
    nombre_elem.text = nombre

    edad_elem = ET.SubElement(empleado, "edad")
    edad_elem.text = str(edad)

    depto_elem = ET.SubElement(empleado, "departamento")
    depto_elem.text = departamento

    salario_elem = ET.SubElement(empleado, "salario")
    salario_elem.text = str(salario)


    root.append(empleado)

    # Guardar los cambios en el archivo
    tree.write(xml_path, encoding="utf-8", xml_declaration=True)
    print(f"Empleado {nombre} agregado al archivo XML.")


xml_path = r"C:\Users\jjuan\OneDrive\Escritorio\Universidad Juanjo\Base de datos 2\Parcial2\Punto1\a\XML\empleados.xml"
agregar_empleado_xml("Juan Perez", 30, "Recursos Humanos", 3000, xml_path)
