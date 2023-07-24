import xml.etree.ElementTree as ET

def read_xml(xml_file):
    try:
        # Parse the XML file
        tree = ET.parse(xml_file)
        root = tree.getroot()
        sample = []

        # Access elements and handle missing keys
        for item in root.findall('item'):
            name = item.find('name').text
            price_element = item.find('price')
            price = float(price_element.text) if price_element is not None else None
            sample.append(name)

            quantity_element = item.find('quantity')
            quantity = int(quantity_element.text) if quantity_element is not None else None

            print(f"Name: {name}")
            if price is not None:
                print(f"Price: {price}")
            if quantity is not None:
                print(f"Quantity: {quantity}")

            print("-" * 20)
        print(sample)

    except ET.ParseError:
        print("Error parsing the XML file.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
xml_file_path = 'python/data.xml'  # Replace with the path to your XML file

read_xml(xml_file_path)
