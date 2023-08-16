import xmlschema
from xml.etree import ElementTree as ET

# Load the XML Schema from a file
schema = xmlschema.XMLSchema('employee_schema.xsd')  # Replace with the actual path to your XSD file

# Load and parse the XML document
xml_file = 'employee.xml'  # Replace with the actual path to your XML file
try:
    tree = ET.parse(xml_file)
    root = tree.getroot()
except ET.ParseError as e:
    print("Error parsing XML:", e)
    exit()

# Validate the XML document against the schema
is_valid = schema.is_valid(tree)

if is_valid:
    print("XML document is valid.")
else:
    print("XML document is not valid. Validation errors:")

    # Get and display validation errors with line and column numbers
    validation_errors = schema.validate(tree, namespaces=root.nsmap)
    for error in validation_errors:
        print(f"Error: {error.message}")
        if error.elem is not None:
            print(f"  Line: {error.elem.sourceline}, Column: {error.elem.sourcecolumn}")
