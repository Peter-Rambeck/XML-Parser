import os
#from run_energy import get_root
from utils import get_logger
import sys
from etree_helper import generic_extracting, generate_sql_insert
from pprint import pprint

from utils import get_connection

def parse_zone_result(etree, content, serial_id, logging, esi, cur, conn, id_func):

    print("Zone_result")
    
    zone_result_dict = {}
    zone_result_dict["EnergyLabelClassification"] = None
    #zone_result_dict["attribute_zoneid"] = None
    zone_result_dict["xml_id_ref"] = serial_id
        
    dict_local = generic_extracting(etree, zone_result_dict)
    generate_sql_insert("zone_result", dict_local, content, logging, esi, cur, conn, 'id')
      
