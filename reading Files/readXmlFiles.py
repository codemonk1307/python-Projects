

import xml.etree.ElementTree as ET 

content = ET.parse("file.xml")
# getting into the main contents of the xml file 
root = content.getroot()

# loop through each of the parameters key, value, values, dependancy or whatever
for child in root:
    print(child.tag, child.text)

