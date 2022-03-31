import os
#from run_energy import get_root
from utils import get_logger
import sys
from etree_helper import generic_extracting, generate_sql_insert
from pprint import pprint

from utils import get_connection

def parse_building_bbr(etree, content, serial_id, logging, esi, cur, conn, id_func):
    for id_ref in id_func:
        bbr_dict={}
        bbr_dict["BuildingNumber"]= None
        bbr_dict["UseCode"]= None
        bbr_dict["YearOfConstruction"]= None
        bbr_dict["DwellingArea"]= None
        bbr_dict["CommercialArea"]= None
        bbr_dict["YearOfRenovation"]= None
        bbr_dict["building_id_ref"]= id_ref
        #print('bbr - got building_id_ref: ', id_ref)
        dict_local = generic_extracting(etree, bbr_dict)
        generate_sql_insert("bbr", dict_local, content, logging, esi, cur, conn, 'null')

        
