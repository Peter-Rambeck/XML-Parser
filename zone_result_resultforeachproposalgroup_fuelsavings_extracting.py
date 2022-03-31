from itertools import count
import os
#from run_energy import get_root
from utils import get_logger
import sys
from etree_helper import generic_extracting, generate_sql_insert
from pprint import pprint

from utils import get_connection
      

def parse_zone_result_resultforeachproposalgroup_fuelsavings(etree, logging, serial_id, content, esi, cur, conn):
    
    result_resultforeachproposalgroup_fuelsavings_dict = {}
    result_resultforeachproposalgroup_fuelsavings_dict['FuelSaving'] = {'Fuel': {'Material': None, 'Unit': None, 'EnergyPerUnit' : None, 'CO2PerUnit': None},
    'FuelPrice': {'CostPerUnit': None, 'FixedCostPerYear': None, 'SupplierCompanyName': None }}

    result_resultforeachproposalgroup_fuelsavings_dict['FuelSaving'] = {'FuelSaved': None }
    result_resultforeachproposalgroup_fuelsavings_dict['zone_result_resultsforeachproposalgroup_id_ref'] = serial_id

    dict_local = generic_extracting(etree, result_resultforeachproposalgroup_fuelsavings_dict)
    generate_sql_insert("resultforeachproposalgroup_fuelsavings", dict_local, content, logging, esi, cur, conn, 'id')

