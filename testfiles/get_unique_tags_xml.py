import lxml.etree as ET
from pprint import pprint
import json
import os
import collections
import traceback
# new

def crawl_xml(root, prefix='', memo={}):
    new_prefix = root.tag
    if len(prefix) > 0:
        new_prefix = prefix + "_" + new_prefix.split('}')[1]
    if len(root.getchildren()) == 0:
        memo[new_prefix.split('}')[1]] = None
    for child in root.getchildren():
        crawl_xml(child, new_prefix, memo)
    return memo

# takes all unique tags for each file 
def run_crawl():
    count = 0
    xml_docs = os.listdir('/home/energy_extract/out')
    for doc in xml_docs:
        try:
            # if count == 100:
            #    import sys
            #    sys.exit()
            count += 1
            print(count)
            tree = ET.parse("/home/energy_extract/out/"+doc)
            xml_dict = get_dict_from_xml_schema()
            nodes = crawl_xml(tree.getroot(), memo=xml_dict)
            with open('/home/energy_extract/ciw_test/xml_schema_val.json', 'w+') as o:
                json.dump(nodes,o)
        except Exception:
            traceback.print_exc()

def get_dict_from_xml_schema():
    try:
        with open(f'/home/energy_extract/ciw_test/xml_schema_val.json') as f:
            dict_ = json.load(f)
        return dict_
    except:
        dict_ = {}
        return dict_

