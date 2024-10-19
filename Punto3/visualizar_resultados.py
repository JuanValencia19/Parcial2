
def visualizar_resumen_xml(xml_output_path):
    tree = ET.parse(xml_output_path)
    root = tree.getroot()

    print("Resumen de encuestas de transporte público:\n")
    
    for ciudad in root.findall("ciudad"):
        nombre = ciudad.find("nombre").text
        personas = ciudad.find("personas_encuestadas").text
        transporte = ciudad.find("transporte_mas_utilizado").text
        
        print(f"Ciudad: {nombre}")
        print(f"Personas encuestadas: {personas}")
        print(f"Transporte más utilizado: {transporte}\n")


visualizar_resumen_xml(xml_output_path)
