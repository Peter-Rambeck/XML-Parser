import os
#from run_energy import get_root
from utils import get_logger
import sys
from etree_helper import generic_extracting, generate_sql_insert
from pprint import pprint

from utils import get_connection

def parse_building_address(etree, content, building_id_ref, logging, esi, cur, conn, id_func):
    print("Address - id_func: ", id_func)
    for id_ref in id_func:
        print("Address - id_ref: ", id_ref)
        building_address_dict={}
        building_address_dict["Name"]= None
        building_address_dict["StreetName"]= None
        building_address_dict["HouseNumber"]= None
        building_address_dict["Floor"]= None
        building_address_dict["SideOrDoor"]= None
        building_address_dict["PostalCode"]= None
        building_address_dict["PostalCity"]= None
        building_address_dict["StreetCode"]= None
        building_address_dict["building_id_ref"] = id_ref
        
        dict_local = generic_extracting(etree, building_address_dict)
        generate_sql_insert("building_address", dict_local, content, logging, esi, cur, conn, 'null')

    