from inspect import Traceback
from pprint import pprint
from webbrowser import get
from psycopg2 import sql
import copy
import traceback
import json

def place_on_disk(image):
    pass
    #do base64 encoding here
    #place the image on disk
    #use library from APIclient to upload image on disk
    #add timestamp for uplad to image server

#FB says (25/02): Add any needed attributes to this list to 
# support including them as columns in DB tables.
attrib_list = ['ID', 'ProposalID', 'BuildingID', 'ProposalGroupID', 'ZoneID']
attrib_prefix = 'attribute_'

#FB & PRA says (28/02): Attempted to handle attributes for references such as Building, Zone, Status and Proposal+ProposalReference ID's.
# Still needs to handle instances where the
def generic_extracting(etree, dict_extract):
    for wanted_tags in dict_extract.keys():  
        insert_attribute_if_exists(attrib_prefix, wanted_tags, dict_extract, etree)      
        try:            
            generic_find = etree.find('.//{*}'+ wanted_tags)
            #insert_attribute_if_exists(attrib_prefix, wanted_tags, dict_extract, generic_find) 
        except AttributeError:
            #print(traceback.format_exc())
            continue
        if isinstance(dict_extract[wanted_tags], dict):
            for sub_keys in dict_extract[wanted_tags].keys():
                #insert_attribute_if_exists(attrib_prefix, sub_keys, dict_extract[wanted_tags], etree)
                insert_attribute_if_exists(attrib_prefix, sub_keys, dict_extract[wanted_tags], generic_find)
            generic_extracting(generic_find, dict_extract[wanted_tags])
        elif isinstance(dict_extract[wanted_tags], list):
            generic_findall = etree.findall('.//{*}' + wanted_tags)
            #multiplying the dicts
            dict_extract[wanted_tags] = [dict_extract[wanted_tags][0].copy() for d in range(len(generic_findall))]
            for index, generic in enumerate(generic_findall):
                #print('generic: ', generic.find('.//{*}' + "Name").text)
                generic_extracting(generic, dict_extract[wanted_tags][index])
        else:
            #needs to be able to parse attributes here too (for lowest children, that are references)
            try:                
                for sub_keys in dict_extract[wanted_tags].keys():
                    sub_key_find = generic_find.find('.//{*}'+ sub_keys)
                    
                    #insert_attribute_if_exists(attrib_prefix, wanted_tags, dict_extract, etree)
                    # or
                    #insert_attribute_if_exists(attrib_prefix, sub_keys, dict_extract[wanted_tags][sub_keys], sub_key_find)

                    text = sub_key_find.text
                    dict_extract[wanted_tags][sub_keys] = text
            except AttributeError: 
                if generic_find is not None:
                    
                    text = generic_find.text
                    dict_extract[wanted_tags] = text
    return dict_extract

def flatten_dict(dict_local, f_dict, prev_key=None):
    for key, val in dict_local.items():
        if isinstance(val,dict):
            pkey = key
            if prev_key:
                pkey = prev_key + "_" + pkey
            f_dict = flatten_dict(dict_local[key], f_dict, pkey)
        else:
            if prev_key:
                key = prev_key + "_" + key
            f_dict[key] = val
    return f_dict

#Contructs an SQL insert statement based on table_name and a dictionary where keys = columnnames and values = placeholders 
def generate_sql_insert(table_name, dict_local, content, logging, esi, cursor, conn, returning='null', schemaname='test1'):
    try:
        if schemaname != 'test1':
            sql_statement = """
            insert into test2.{} ({}) values ({}) returning {}
            """
        else:
            sql_statement = """
            insert into test1.{} ({}) values ({}) returning {}
            """
        # validate xml
        f_dict = flatten_dict(dict_local, {})

        column_names = [key.lower() for key in list(f_dict.keys())]
        
        #unexpected_tag = verify_exists(column_names, table_name, content, logging, esi, cursor)
        #if unexpected_tag:
            #import sys
            #sys.exit(1)
            #return None
        column_values = list(f_dict.values())
        qry_str = sql.SQL(sql_statement).format(
            sql.SQL(table_name),
            sql.SQL(",").join(map(sql.Identifier, column_names)),
            sql.SQL(",").join(sql.Placeholder() * len(column_names)),
            sql.SQL(returning)
            )
        #logging.info(f'column_values: {column_values}', extra={'energylabel_serial_identifier': esi})
        #logging.info(qry_str.as_string(conn), extra={'energylabel_serial_identifier': esi})
        #print(qry_str.as_string(conn))
        cursor.execute(qry_str.as_string(conn), list(column_values))
        ## print("SQL exe success")
        #pprint(f_dict)

        return_id = cursor.fetchone()[0]
        return return_id
    except Exception:
        logging.info(f'{qry_str.as_string(conn)}', extra={'energylabel_serial_identifier': esi})
        traceback.print_exc()



def verify_exists(column_names, table_name, content, logging, esi, cur):
    sql_statement = f"SELECT * FROM test1.{table_name} limit 0"
    with open('/home/energy_extract/test_mape/testfiles/all_tags.json', 'r') as d:
        data = json.load(d)
    cur.execute(sql_statement)
    tb_column_names = [desc[0] for desc in cur.description]
    content = content.lower()
    for key in data.keys():
        key = key.lower()

        found = False
        for dict_key in column_names:
            dict_key = dict_key.lower()
            if content in key and dict_key in key:
                found = True
                break

        if not found:
            logging.info(f'UNEXPECTED TAG: {key}. MISSED DICTIONARY KEY. RERUN XML DOCUMENT  ', extra={'energylabel_serial_identifier': esi})

        found1 = False
        for tb_column_name in tb_column_names:
            tb_column_name = tb_column_name.lower()
            if content in key and tb_column_name in key:
                found1 = True
                break

        if not found1:
            logging.info(f'UNEXPECTED TAG: {key}. MISSED TABLE COLUMN. RERUN XML DOCUMENT  ', extra={'energylabel_serial_identifier': esi})

        if found or found1:
            return True

    return False

def get_element_attribute_name_and_value(given_etree, given_attrib_list=attrib_list):
    # Attribute check setup of parent element. Variables need to be in this scope.
    attrib_value = None
    attrib_key_name = None
    attrib_items = given_etree.items()

    parent_et = given_etree.getparent()
    parent_et_items = parent_et.items()
    
    #pprint(attrib_items)
    pprint(given_etree.tag)
    #pprint(parent_et_items)

    # Check if the attributes of the element exist in the attribute list.
    if attrib_items is not None:
        for name, value in sorted(attrib_items):
            print("Value: ", value)
            if name in given_attrib_list:
                attrib_value = value
                # Add the Attrib_ prefix to signify the ID comes from an attribute.
                #attrib_key_name = attrib_prefix + name
                attrib_key_name = attrib_prefix + name.lower()
    elif parent_et_items is not None:
        for name, value in sorted(parent_et_items):
            print("Value: ", value)
            # if name in given_attrib_list:
            #     attrib_value = value
            #     # Add the Attrib_ prefix to signify the ID comes from an attribute.
            #     #attrib_key_name = attrib_prefix + name
            #     attrib_key_name = attrib_prefix + name.lower()

    if attrib_key_name is not None and attrib_value is not None :           
         print("1 ", attrib_key_name)
         print("2 ", attrib_value)
    
    return attrib_key_name, attrib_value

def insert_attribute_if_exists(given_prefix, given_tags, given_dict, given_etree):
    # pprint("The prefix: ")
    # pprint(given_prefix)
    # pprint("The given tags: ")
    # pprint(given_tags)
    # pprint("The given dict: ")
    # pprint(given_dict)

    if given_prefix == given_tags or given_prefix in given_tags:
        #pprint("The given tags include the attrib prefix.")
        attrib_key_name, attrib_value = get_element_attribute_name_and_value(given_etree, attrib_list)
        #print("A key name: ", attrib_key_name, " and value: ", attrib_value)

        # The dictionary key and value pair are inserted.
        
        if attrib_value is not None and attrib_key_name is not None:
            given_dict[attrib_key_name] = attrib_value
