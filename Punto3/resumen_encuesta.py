import xml.etree.ElementTree as ET

def generar_resumen_xml(json_path, xml_output_path):

    with open(json_path, 'r') as json_file:
        encuestas = json.load(json_file)

    # Crear el elemento raíz para el XML
    root = ET.Element("resumen_encuestas")

    # Recorrer las encuestas y agregar la información a XML
    for encuesta in encuestas["encuestas"]:
        ciudad_elem = ET.Element("ciudad")
        
        nombre_ciudad = ET.SubElement(ciudad_elem, "nombre")
        nombre_ciudad.text = encuesta["ciudad"]
        
        personas_elem = ET.SubElement(ciudad_elem, "personas_encuestadas")
        personas_elem.text = str(encuesta["personas_encuestadas"])
        
        transporte_elem = ET.SubElement(ciudad_elem, "transporte_mas_utilizado")
        transporte_elem.text = encuesta["transporte_mas_utilizado"]
        

        root.append(ciudad_elem)

    # Crear el árbol de XML y guardarlo en el archivo
    tree = ET.ElementTree(root)
    tree.write(xml_output_path, encoding="utf-8", xml_declaration=True)

    print(f"Resumen exportado a {xml_output_path}")


xml_output_path = "resumen_encuestas.xml"
generar_resumen_xml(json_path, xml_output_path)
