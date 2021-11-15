# Program to convert an xml
# file to json file
 
# import json module and xmltodict
# module provided by python
import json
import xmltodict
from tkinter import Tk
from tkinter.filedialog import askopenfilename
 
# choose XML file to be converted from system
Tk().withdraw()
filename = askopenfilename()
print(filename)
# open the input xml file and read
# data in form of python dictionary
# using xmltodict module

# with open("C:\GIT/testFiles/employee.xml") as xml_file:
with open(filename) as xml_file:
     
    data_dict = xmltodict.parse(xml_file.read())
    xml_file.close()
     
    # generate the object using json.dumps()
    # corresponding to json data
     
    json_data = json.dumps(data_dict)
     
    # Write the json data to output
    # json file
    with open("data.json", "w") as json_file:
        json_file.write(json_data)
        json_file.close()