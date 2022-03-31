from itertools import count
import os
from types import NoneType
#from run_energy import get_root
from utils import get_logger
import sys
from etree_helper import generic_extracting, generate_sql_insert
from pprint import pprint
from lxml import etree as ET
from utils import get_connection

#Using old format because it's only depending on the serial id
def parse_inputdata_for_autolabels_address_extracting_test(etree, content, serial_id, logging, esi, cur, conn, id_func):

    autolabels_address_dict = {}
    autolabels_address_dict["xml_id_ref"] = serial_id
    autolabels_address_dict["Name"] = None
    autolabels_address_dict["StreetName"] = None
    autolabels_address_dict["HouseNumber"] = None
    autolabels_address_dict["Floor"] = None
    autolabels_address_dict["SideOrDoor"] = None
    autolabels_address_dict["PostalCode"] = None
    autolabels_address_dict["PostalCity"] = None
    autolabels_address_dict["StreetCode"] = None

    autolabels_address_tablename = "inputdata_f_autolabels_address"

    dict_local = generic_extracting(etree, autolabels_address_dict)

    if dict_local["Name"] is not None:
        generate_sql_insert(autolabels_address_tablename, dict_local, content, logging, esi, cur, conn, "null", 'test2')
    #Use the method call below when switching to the schema intended for the real deal
    #proposal_group_id = generate_sql_insert(autolabels_address_tablename, dict_local, content, logging, esi, cur, conn, "null")

   
    

def parse_inputdata_for_autolabels_bbr_extracting_test(etree, content, serial_id, logging, esi, cur, conn, id_func):
    autolabels_bbr_dict = {}
    autolabels_bbr_dict["xml_id_ref"] = serial_id
    autolabels_bbr_dict["MunicipalityNumber"] = None
    autolabels_bbr_dict["PropertyNumber"] = None
    autolabels_bbr_dict["BFENumber"] = None

    autolabels_bbr_tablename = "inputdata_f_autolabels_bbr"

    dict_local = generic_extracting(etree, autolabels_bbr_dict)

    if dict_local["MunicipalityNumber"] is not None:
        generate_sql_insert(autolabels_bbr_tablename, dict_local, content, logging, esi, cur, conn, "null", 'test2')
        #generate_sql_insert(autolabels_bbr_tablename, dict_local, content, logging, esi, cur, conn, "null")

def parse_inputdata_for_autolabels_buildings_ref_extracting_test(etree, content, serial_id, logging, esi, cur, conn, id_func):
    #reference table for autolabels_buildings_address_ and autolabels_buildings_bbr_
    building_ids = []
    print("id_func in parse_inputdata_for_autolabels_buildings_ref_extracting_test: ", id_func)

    autolabels_buildings_tablename = "inputdata_f_autolabels_buildings"

    for id_ref in id_func:

        

        autolabels_buildings_dict = {}
        autolabels_buildings_dict["attribute_id"] = None
        autolabels_buildings_dict["xml_id_ref"] = serial_id
        #autolabels_buildings_dict["Building"] = [{"Address": None}, {"BBR": None}]
        
        
        
        dict_local = generic_extracting(etree, autolabels_buildings_dict)

        if dict_local["attribute_id"] is not None:
            pprint("Got Building ID!")

            temp_insert_dict = autolabels_buildings_dict

            autolabels_buildings_id = generate_sql_insert(autolabels_buildings_tablename, temp_insert_dict, content, logging, esi, cur, conn, 'id', 'test2')
            #autolabels_buildings_id = generate_sql_insert(autolabels_buildings_tablename, temp_insert_dict, content, logging, esi, cur, conn, 'id')
            building_ids.append(autolabels_buildings_id)

            # for et in etree:
            #     if et.tag == 'Address':
            #         autolabels_buildings_address_dict = make_auto_autolabels_buildings_address_dict()
            #         autolabels_buildings_address_tablename = "inputdata_f_autolabels_building_address"

            #         del dict_local
            #         dict_local = generic_extracting(et, autolabels_buildings_address_dict)
            #         dict_local["autolabel_building_id_ref"] = autolabels_buildings_id
                    

            #         parse_inputdata_for_autolabels_buildings_address_extracting_test(content, dict_local, autolabels_buildings_address_tablename, logging, esi, cur, conn)
            #     if et.tag == 'BBR':
            #         autolabels_buildings_bbr_dict = make_autolabels_buildings_bbr_dict(et)
            #         autolabels_buildings_bbr_tablename = "inputdata_f_autolabels_building_bbr"

            #         del dict_local
            #         dict_local = generic_extracting(et, autolabels_buildings_bbr_dict)
            #         dict_local["autolabel_building_id_ref"] = autolabels_buildings_id

            #         parse_inputdata_for_autolabels_buildings_bbr_extracting_test(content, dict_local, autolabels_buildings_bbr_tablename, logging, esi, cur, conn)


            # try:
            #     for s in autolabels_buildings_dict["Address"]:
            #         s["Address"]["autolabel_building_id_ref"] = autolabels_buildings_id
            #         parse_inputdata_for_autolabels_buildings_address_extracting_test(etree, content, autolabels_buildings_bbr_dict, logging, esi, cur, conn)
                
            #     for s in autolabels_buildings_dict["BBR"]:
            #         s["BBR"]["autolabel_building_id_ref"] = autolabels_buildings_id
            #         parse_inputdata_for_autolabels_buildings_bbr_extracting_test(etree, content, s["BBR"], logging, esi, cur, conn)
            # except KeyError:
            #     pprint("There was a KeyError!")
        else:
            print("Didn't get Building ID!")
        return building_ids

def parse_inputdata_for_autolabels_buildings_address_extracting_test(etree, content, serial_id, logging, esi, cur, conn, id_func):   

    for id_ref in id_func:
        autolabels_buildings_address_dict = {}
        autolabels_buildings_address_dict["autolabel_building_id_ref"] = id_ref
        autolabels_buildings_address_dict["name"] = None
        autolabels_buildings_address_dict["streetname"] = None
        autolabels_buildings_address_dict["housenumber"] = None
        autolabels_buildings_address_dict["floor"] = None
        autolabels_buildings_address_dict["sideordoor"] = None
        autolabels_buildings_address_dict["postalcode"] = None
        autolabels_buildings_address_dict["postalcity"] = None
        autolabels_buildings_address_dict["streetcity"] = None

        autolabels_buildings_address_tablename = "inputdata_f_autolabels_building_address"

        dict_local = generic_extracting(etree, autolabels_buildings_address_dict)
        #dict_local["autolabel_building_id_ref"] = autolabels_buildings_id

        parse_inputdata_for_autolabels_buildings_address_extracting_test_id = generate_sql_insert(autolabels_buildings_address_tablename, dict_local, content, logging, esi, cur, conn, 'id', 'test2')
        #parse_inputdata_for_autolabels_buildings_address_extracting_test_id = generate_sql_insert(autolabels_buildings_address_tablename, dict_local, content, logging, esi, cur, conn, 'id')
        print("parse_inputdata_for_autolabels_buildings_address_extracting_test_id: ", parse_inputdata_for_autolabels_buildings_address_extracting_test_id)

def parse_inputdata_for_autolabels_buildings_bbr_extracting_test(etree, content, serial_id, logging, esi, cur, conn, id_func):   
    
    for id_ref in id_func:
        autolabels_buildings_bbr_dict = {}
        autolabels_buildings_bbr_dict["autolabel_building_id_ref"] = id_ref
        autolabels_buildings_bbr_dict["buildingnumber"] = None
        autolabels_buildings_bbr_dict["usecode"] = None
        autolabels_buildings_bbr_dict["yearofconstruction"] = None
        autolabels_buildings_bbr_dict["dwellingarea"] = None
        autolabels_buildings_bbr_dict["commercialarea"] = None
        autolabels_buildings_bbr_dict["yearofrenovation"] = None
        
        autolabels_buildings_bbr_tablename = "inputdata_f_autolabels_building_bbr"

        dict_local = generic_extracting(etree, autolabels_buildings_bbr_dict)
        #dict_local["autolabel_building_id_ref"] = autolabels_buildings_id

        parse_inputdata_for_autolabels_buildings_bbr_extracting_test_id = generate_sql_insert(autolabels_buildings_bbr_tablename, dict_local, content, logging, esi, cur, conn, 'id', 'test2')
        #parse_inputdata_for_autolabels_buildings_bbr_extracting_test_id = generate_sql_insert(autolabels_buildings_bbr_tablename, dict_local, content, logging, esi, cur, conn, 'id')
        print("parse_inputdata_for_autolabels_buildings_bbr_extracting_test_id: ", parse_inputdata_for_autolabels_buildings_bbr_extracting_test_id)

def get_root(doc, etree_content):
    try:
        tree = ET.parse(doc)
        if etree_content == 'EnergyLabel': return tree.getroot()
        etree = tree.findall('.//{*}' + etree_content)
    except ET.XMLSyntaxError:
        return None
    return etree

prev = None
def handle_dicts_new(pretty_doc, content, esi, serial_id, logging, cur, conn, etree_param = None):
    global id_func
    print("global id_func: ", id_func)
    global id_func_counter
    global prev
    for key, vals in content.items():
        if etree_param is None:
            etree = get_root(pretty_doc, key)
        else:
            etree = etree_param.findall('.//{*}' + key)
        if isinstance(vals, dict):
            for et in etree:
                handle_dicts_new(pretty_doc, vals, esi, serial_id, logging, cur, conn, et)
        else:
            function = vals[1]
            overwrite = vals[-1]
            overwrite_ids = []
            for et in etree:
                if overwrite is True:
                    id_func = function(et, content, serial_id, logging, esi, cur, conn, id_func)
                    id_func_counter = -1
                else:
                    prev = id_func_counter
                    print('id_func: ', id_func)
                    print('id_func_counter: ', id_func_counter)
                    print('len etree: ', len(etree))
                    function(et, content, serial_id, logging, esi, cur, conn, id_func[id_func_counter])
    if id_func_counter != -1 and id_func_counter == prev:
        print("8")
        #print('plus 1')
        id_func_counter += 1
        #print("Post2: ", id_func)

def handle_dicts(pretty_doc, content, esi, serial_id, logging, cur, conn, etree_param = None):
    for key, vals in content.items():
        if etree_param is not None:
            etree = etree_param.findall('.//{*}' + key)
        else:
            etree = get_root(pretty_doc, key)
        for et in etree:
            if isinstance(vals, dict):
                # index used to access the correct etree element.
                index = 0
                for key1 in vals.keys():
                    if isinstance(vals[key1], dict):
                        et_keys = et.findall('.//{*}' + key1)
                        for et_key in et_keys:
                            handle_dicts(pretty_doc, vals[key1], esi, serial_id, logging, cur, conn, et_key)
                    else:
                        # her hvis dict er lige nested (2,4,6,8,osv.)
                        if key1 == 'Building':
                            #pass
                            parse_inputdata_for_autolabels_buildings_ref_extracting_test(et[index], content, serial_id, logging, esi, cur, conn)
                    index += 1
            else:
                # her hvis dict er ulige nested (1,3,5,7,osv.)
                # if key == 'Address':
                #     #pass
                #     pprint('Label Address Odd: Do something here in handle_dicts!')
                #     parse_inputdata_for_autolabels_address_extracting_test(et, key, serial_id, logging, esi, cur, conn)
                #     #count -= 1
                #     #proposal_group_extracting_test(et, key, logging, esi, cur, conn)
                # if key == 'BBR':
                #     #pass
                #     pprint('BBR Odd: Do something here in handle_dicts!')
                #     parse_inputdata_for_autolabels_bbr_extracting_test(et, key, serial_id, logging, esi, cur, conn)
                #     #count -= 1
                pass
                
                
def insert_energylabel_serial_identifier(etree, doc, cur, logging):
    try:
        tag = etree[0].tag.split("}")[1]
        if tag == "EnergyLabelSerialIdentifier":
            esi = etree[0].text
            sql_statement = """INSERT INTO
                        test2.xmldoc(energylabel_serial_identifier, xml_name)
                        VALUES(%s, %s)
                        RETURNING id"""
            cur.execute(sql_statement, [esi, doc.split("/")[-1]])
            serial_id = cur.fetchone()[0]
            #logging.info('test logging succesfull', extra={'energylabel_serial_identifier': esi})
            return esi, serial_id
    except IndexError:
        pass

def main():
    debug = None
    if len(sys.argv) > 1:
        debug = True
    logging = get_logger(debug)
    content_types = [
        'EnergyLabel',
        'EnergyLabelSerialIdentifier',
    {"InputDataForAutoLabels": {"Label": {"Address": None}}},
    {"InputDataForAutoLabels": {"Label": {"BBR": None}}},
    #{"InputDataForAutoLabels": {"Label": {"Buildings": None}}},
    {"InputDataForAutoLabels": {"Label": {"Buildings": {"Building": None}}}},
    {"InputDataForAutoLabels": {"Label": {"Buildings": {"Building": {"Address": None}}}}},
    {"InputDataForAutoLabels": {"Label": {"Buildings": {"Building": {"BBR": None}}}}}
    ]

    content_types_test = [
        "EnergyLabelSerialIdentifier",
        {"InputDataForAutoLabels": {"Label": {"Address": [None, parse_inputdata_for_autolabels_address_extracting_test]}}},
        {"InputDataForAutoLabels": {"Label": {"BBR": [None, parse_inputdata_for_autolabels_bbr_extracting_test]}}},
        {"InputDataForAutoLabels": {"Label": {"Buildings": [None, parse_inputdata_for_autolabels_buildings_ref_extracting_test, True]}}},
        {"InputDataForAutoLabels": {"Label": {"Buildings": {"Building": {"Address": [None, parse_inputdata_for_autolabels_buildings_address_extracting_test]}}}}},
        {"InputDataForAutoLabels": {"Label": {"Buildings": {"Building": {"BBR": [None, parse_inputdata_for_autolabels_buildings_bbr_extracting_test]}}}}}
    ]
    #doc = "/home/energy_extract/test_mape/XML_docs/copy_pretty_100115068.xml"
    esi = None
    serial_id = None
    with get_connection() as conn:
        with conn.cursor() as cur:
            file_path = "/home/energy_extract/out"
            for pretty_doc in os.listdir(file_path):
                # if not '200052262' in pretty_doc:
                #     continue
                print(pretty_doc)
                pretty_doc = file_path + "/" + pretty_doc
                global id_func 
                global id_func_counter
                id_func = []
                for index, content in enumerate(content_types_test):
                    print('reached actual content: ', content)
                    id_func_counter = 0
                    index += 1
                    #if index > 5:
                        #sys.exit(1)
                    if isinstance(content, dict):
                        handle_dicts_new(pretty_doc, content, esi, serial_id, logging, cur, conn)
                        continue
                    etree = get_root(pretty_doc, content)
                    if content == "EnergyLabelSerialIdentifier":
                        esi, serial_id = insert_energylabel_serial_identifier(etree, pretty_doc, cur, logging)

if __name__ == "__main__":
    main()