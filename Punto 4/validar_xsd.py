from lxml import etree

def validar_xml_con_xsd(xml_path, xsd_path):
    try:
        # Cargar el archivo XSD
        with open(xsd_path, 'r') as xsd_file:
            esquema_xsd = etree.XMLSchema(etree.parse(xsd_file))

        # Cargar el archivo XML
        with open(xml_path, 'r') as xml_file:
            xml_doc = etree.parse(xml_file)

        # Validar el XML contra el XSD
        esquema_xsd.assertValid(xml_doc)
        print("El archivo XML es válido según el esquema XSD.")
        
    except etree.XMLSchemaError as e:
        print(f"El archivo XML no es válido: {e}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Rutas de los archivos XML y XSD
xml_path = r"C:\Users\jjuan\OneDrive\Escritorio\Universidad Juanjo\Base de datos 2\Parcial2\Punto 4\empleados_xsd.xml"
xsd_path = r"C:\Users\jjuan\OneDrive\Escritorio\Universidad Juanjo\Base de datos 2\Parcial2\Punto 4\empleados.xsd"

# Validar XML
validar_xml_con_xsd(xml_path, xsd_path)
