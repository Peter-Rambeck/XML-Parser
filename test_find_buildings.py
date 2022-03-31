
from lxml import etree as ET
import sys
import os
from pprint import pprint


doc = "/home/energy_extract/out/pretty_310027022.xml"
etree_content = "Building"

def get_root(doc, etree_content):
    try:
        tree = ET.parse(doc)
        if etree_content == 'EnergyLabel': return tree.getroot()
        etree = tree.findall('.//{*}' + etree_content)
        print(etree)
    except ET.XMLSyntaxError:
        return None
    return etree