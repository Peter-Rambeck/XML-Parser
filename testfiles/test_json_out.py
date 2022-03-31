import lxml.etree as ET
from pprint import pprint
import os
import json

def recursive_trees(root, final_json, prefix=''):
    roottag = root.tag.split('}')[1]
    if len(prefix) > 0:
        roottag = prefix + '_' + roottag
    if len(root.getchildren()) == 0:
        #print(root.text)
        #print(roottag)
        if root.text is not None or root.attrib is not None:
            #print('text: ', root.text)
            final_json[roottag] = None
        
    for child in root.getchildren():
        recursive_trees(child, final_json, roottag)

def main():
    final_json = {}
    xml_docs = os.listdir('/home/energy_extract/out')
    for index, doc in enumerate(xml_docs):
        print('index: ', index, ' out of: ', len(xml_docs))
        tree = ET.parse("/home/energy_extract/out/"+doc)
        recursive_trees(tree.getroot(), final_json)
        #pprint(final_json)
        print('len: ', len(final_json))
    with open('/home/energy_extract/test_mape/testfiles/all_tags.json', 'w') as o:
        json.dump(final_json, o)

if __name__ == "__main__":
    main()
