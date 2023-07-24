import csv
import xml.etree.ElementTree as ET

# Function to parse XML and save data to CSV
def parse_xml_to_csv(xml_file, csv_file):
    # Create an empty list to store the data
    data_list = []

    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Loop through each 'item' element in the XML
    for item in root.findall('item'):
        name = item.get('name', '')
        price = item.get('price', '')
        quantity = item.get('quantity', '')

        # Append the data to the list
        data_list.append([name, price, quantity])

    # Write the data to a CSV file
    with open(csv_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write the header row
        csv_writer.writerow(['Name', 'Price', 'Quantity'])
        # Write each row of data
        csv_writer.writerows(data_list)

# Replace 'input.xml' with the path to your input XML file
# Replace 'output.csv' with the desired output CSV file path
parse_xml_to_csv('/Volumes/Blockchain/Devops/jfrog/jfrog/python/data_copy.xml', '/Volumes/Blockchain/Devops/jfrog/jfrog/python/output.csv')
