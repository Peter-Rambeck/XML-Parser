from typing import Counter
from energy_label_extracting import parse_energy_label, parse_energy_label_apartments
#from resultdata_labelresults import parse_resultdata_label_result 
from resultdata_building_result import parse_resultdata_building_result
from status_extracting import parse_status
from inputdata_proposalgroup_extracting import parse_inputdata_proposalgroup, parse_inputdata_proposalreference
from utils import get_logger, get_connection
import sys
from copy import deepcopy

from zone_result_status_fuelconsumption_extracting import parse_zone_result_status_fuelconsumption
from zone_result_status_extracting import parse_zone_result_status
from zone_result_status_calculatedsbiresults_resultfigures_extracting import parse_zone_result_status_calculatedsbiresult_resultfigures
from zone_result_status_calculatedsbiresults_keyfigures_extracting import parse_zone_result_status_calculatedsbiresult_keyfigures
from zone_result_status_calculatedbe15results_resultfigures_extracting import parse_zone_result_status_calculatedbe15result_resultfigures
from zone_result_status_calculatedbe15results_keyfigures_extracting import parse_zone_result_status_calculatedbe15result_keyfigures
from zone_result_status_calculatedbe18results_resultfigures_extracting import parse_zone_result_status_calculatedbe18result_resultfigures
from zone_result_status_calculatedbe18results_keyfigures_extracting import parse_zone_result_status_calculatedbe18result_keyfigures
from zone_result_status_calculatedbe10results_resultfigures_extracting import parse_zone_result_status_calculatedbe10result_resultfigures
from zone_result_status_calculatedbe10results_keyfigures_extracting import parse_zone_result_status_calculatedbe10result_keyfigures
from zone_result_status_calculatedbe06results_resultfigures_extracting import parse_zone_result_status_calculatedbe06result_resultfigures
from zone_result_status_calculatedbe06results_keyfigures_extracting import parse_zone_result_status_calculatedbe06result_keyfigures

from zone_result_resultforallprofitableproposals_extracting import parse_zone_resultforallprofitableproposals
from zone_result_f_a_p_proposals_calculatedbe06result_resultfigures_extracting import parse_result_f_a_p_proposals_calculatedbe06result_resultfigures
from zone_result_f_a_p_proposals_calculatedbe06result_keyfigures_extracting import parse_result_f_a_p_proposals_calculatedbe06result_keyfigures
from zone_result_f_a_p_proposals_calculatedbe10result_resultfigures_extracting import parse_result_f_a_p_proposals_calculatedbe10result_resultfigures
from zone_result_f_a_p_proposals_calculatedbe10result_keyfigures_extracting import parse_result_f_a_p_proposals_calculatedbe10result_keyfigures
from zone_result_f_a_p_proposals_calculatedbe15result_resultfigures_extracting import parse_result_f_a_p_proposals_calculatedbe15result_resultfigures
from zone_result_f_a_p_proposals_calculatedbe15result_keyfigures_extracting import parse_result_f_a_p_proposals_calculatedbe15result_keyfigures
from zone_result_f_a_p_proposals_calculatedsbiresults_resultfigures_extracting import parse_result_f_a_p_proposals_calculatedsbiresult_resultfigures
from zone_result_f_a_p_proposals_calculatedbe18result_resultfigures_extracting import parse_result_f_a_p_proposals_calculatedbe18result_resultfigures
from zone_result_f_a_p_proposals_calculatedbe18result_keyfigures_extracting import parse_result_f_a_p_proposals_calculatedbe18result_keyfigures
from zone_result_f_a_p_proposals_calculatedsolarcellutilization_extracting import parse_result_f_a_p_proposals_calculatedsolarcellutilization
from zone_result_f_a_p_proposals_calculatedsbiresults_keyfigures_extracting import parse_result_f_a_p_proposals_calculatedsbiresult_keyfigures
from zone_result_f_a_p_proposals_fuelconsumption_extracting import parse_result_f_a_p_proposals_fuelconsumption

from zone_result_resultforallproposals_extracting import parse_zone_result_resultforallproposals
from zone_result_resultforallproposals_fuelconsumption_extracting import parse_zone_result_resultforallproposals_fuelconsumption
from zone_result_resultforallproposals_calculatedsolarcellutilization_extracting import parse_zone_result_resultforallproposals_calculatedsolarcellutilization
from zone_result_resultforallproposals_calculatedbe18result_keyfigures_extracting import parse_result_resultforallproposals_calculatedbe18result_keyfigures
from zone_result_resultforallproposals_calculatedbe18result_resultfigures_extracting import parse_result_resultforallproposals_calculatedbe18result_resultfigures
from zone_result_resultforallproposals_calculatedbe15result_keyfigures_extracting import parse_result_resultforallproposals_calculatedbe15result_keyfigures
from zone_result_resultforallproposals_calculatedbe15result_resultfigures_extracting import parse_result_resultforallproposals_calculatedbe15result_resultfigures
from zone_result_resultforallproposals_calculatedbe10result_keyfigures_extracting import parse_result_resultforallproposals_calculatedbe10result_keyfigures
from zone_result_resultforallproposals_calculatedbe10result_resultfigures_extracting import parse_result_resultforallproposals_calculatedbe10result_resultfigures
from zone_result_resultforallproposals_calculatedbe06result_keyfigures_extracting import parse_result_resultforallproposals_calculatedbe06result_keyfigures
from zone_result_resultforallproposals_calculatedbe06result_resultfigures_extracting import parse_result_resultforallproposals_calculatedbe06result_resultfigures

from zone_result_extracting import parse_zone_result

from zone_result_resultsforeachproposalgroup_extracting import parse_zone_result_resultsforeachproposalgroup
from zone_result_resultforeachproposalgroup_proposalresult_extracting import parse_zone_result_resultforeachproposalgroup_proposalresult
from zone_result_resultforeachproposalgroup_fuelsavings_extracting import parse_zone_result_resultforeachproposalgroup_fuelsavings

from building_extracting import parse_building, parse_building_address
from building_bbr_extracting import parse_building_bbr
from building_zones_zone_extracting import parse_building_zones_zone
#from building_zones_zone_buildingunits_status_extracting import parse_building_zones_zone_buildingunits_status

#import inputdata_for_autolabels_extracting_test2
#Names are too long!
from inputdata_for_autolabels_extracting_test2 import parse_inputdata_for_autolabels_address_extracting_test, parse_inputdata_for_autolabels_bbr_extracting_test
from inputdata_for_autolabels_extracting_test2 import parse_inputdata_for_autolabels_buildings_ref_extracting_test, parse_inputdata_for_autolabels_buildings_address_extracting_test
from inputdata_for_autolabels_extracting_test2 import parse_inputdata_for_autolabels_buildings_bbr_extracting_test

from lxml import etree as ET
import sys
import os
from pprint import pprint

def get_root(doc, etree_content):
    try:
        tree = ET.parse(doc)
        if etree_content == 'EnergyLabel': return tree.getroot()
        etree = tree.findall('.//{*}' + etree_content)
    except ET.XMLSyntaxError:
        return None
    return etree

def insert_energylabel_serial_identifier(etree, doc, cur, logging):
    try:
        tag = etree[0].tag.split("}")[1]
        if tag == "EnergyLabelSerialIdentifier":
            esi = etree[0].text
            sql_statement = """INSERT INTO
                        test1.xmldoc(energylabel_serial_identifier, xml_name)
                        VALUES(%s, %s)
                        RETURNING id"""
            cur.execute(sql_statement, [esi, doc.split("/")[-1]])
            serial_id = cur.fetchone()[0]
            # logging.info('test logging succesfull', extra={'energylabel_serial_identifier': esi})
            return esi, serial_id
    except IndexError:
        pass

def handle_dicts_rewrite(pretty_doc, content, esi, serial_id, logging, cur, conn, etree_param = None,  decision_string = "none", id_func_list=[]):
    # global id_func
    # global id_func_counter
    # global prev

    for key, vals in content.items():
        
        if etree_param is None:
            print('1')
            print("key: ", key)
            print("vals: ", vals)
            etree = get_root(pretty_doc, key)
            print("1: etree: ", etree)
        else:
            print('2')
            etree = etree_param.findall('.//{*}' + key)

        if isinstance(vals, dict):
            print('3')
            for et in etree:
                handle_dicts_rewrite(pretty_doc, content, esi, serial_id, logging, cur, conn, et)
        else:
            id_func = 0
            print('4')
            print('4 id_func: ', id_func)
            print('4 etree: ', etree)

            #get the function call from list in dict, no parameters
            function = vals[1]
            print('4 function: ', function)
            id_func = function(etree, content, serial_id, logging, esi, cur, conn, id_func)
            print('4 id_func: ', id_func)

        for item in etree[0]: 
            for elem in item.iter():
                if 'EnergyLabelClassification' in elem.tag: #310020992
                    key_elem = elem.tag.split("}")[1]
                    value = elem.text
                #    print(key_elem, " ", value )
                #print(elem)
                
                if len(item) == 0:
                    key = item.tag.split("}")[1]
                    #print(key)
                    value = item.text
                    
        if etree_param is None:
            print("1, etree_param none")
            etree = get_root(pretty_doc, key)
        else:
            print("2, etree_param set")
            etree = etree_param.findall('.//{*}' + key)
        if isinstance(vals, dict):
            print("3, vals is dict")
            for et in etree:
                handle_dicts_rewrite(pretty_doc, vals, esi, serial_id, logging, cur, conn, et)
        else:
            print("4, vals not dict")
            function = vals[1]
            print("function: ", function)
            overwrite = vals[-1] #-1 means last item.
            print("overwrite: ", overwrite)
            overwrite_ids = []
            if id_func_counter == -1:
                break
            for et in etree:
                print("5, iterate innermost dict level's etree")
                if overwrite is True:
                    print("6, overwrite the id_func")
                    id_func = function(et, content, serial_id, logging, esi, cur, conn, id_func)
                    print("id_func handle_dict: ", id_func)
                    print('True is overwriting id_func: ', id_func)
                    id_func_counter = -1
                else:
                    print("7, don't overwrite the id_func")
                    prev = id_func_counter
                    print("id_func_counter: ", id_func_counter)
                    #print('id_func: ', id_func)
                    #print('id_func_counter: ', id_func_counter)
                    #print('len etree: ', len(etree))
                    function(et, content, serial_id, logging, esi, cur, conn, id_func[id_func_counter])
    if id_func_counter != -1 and id_func_counter == prev:
        print("8")
        #print('plus 1')
        id_func_counter += 1
        #print("Post2: ", id_func)

def handle_dicts_new(pretty_doc, content, esi, serial_id, logging, cur, conn, etree_param = None, prev_function = None):
    global id_func
    global id_func_counter
    #global prev
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
            #overwrite_ids = []
            
            for et in etree:
                if overwrite is True:
                    print("Overwriting id_func. Previous id_func: ", id_func)
                    print('ETREE BEING CALLED (with overwrite): ', et)
                    id_func = function(et, content, serial_id, logging, esi, cur, conn, id_func)
                    print("Wrote new id_func: ", id_func)
                    # if isinstance(id_func, list):
                    #     del id_func
                    #     id_func[0] = new_id
                    #     print("updated id_func list: ", id_func)
                    # else:
                    #     id_func[0] = new_id
                    #     print("new id_func list", id_func)
                    #id_func_counter = -1
                else:                    
                    if isinstance(id_func, list):
                        if len(id_func) > 0:
                            print("Got id_func list")
                            print('ETREE BEING CALLED: ', et)
                            function(et, content, serial_id, logging, esi, cur, conn, id_func)
                            #id_func.pop(0)
                    else:
                        print("How did you get here? - id_func is not a list")

            print('id_func after et for loop: ', id_func)
            #print('id_func_counter: ', id_func_counter)
            print('len etree after et for loop: ', len(etree))
            print('etree after for loop: ', etree)

def main():
    debug = None
    if len(sys.argv) > 1:
        debug = True
    logging = get_logger(debug)
    content_types_test = [
        'EnergyLabelSerialIdentifier',
        {"InputDataForAutoLabels": {"Label": {"Address": [None, parse_inputdata_for_autolabels_address_extracting_test]}}},
        {"InputDataForAutoLabels": {"Label": {"BBR": [None, parse_inputdata_for_autolabels_bbr_extracting_test]}}},
        {"InputDataForAutoLabels": {"Label": {"Buildings": [None, parse_inputdata_for_autolabels_buildings_ref_extracting_test, True]}}},
        {"InputDataForAutoLabels": {"Label": {"Buildings": {"Building": {"Address": [None, parse_inputdata_for_autolabels_buildings_address_extracting_test]}}}}},
        {"InputDataForAutoLabels": {"Label": {"Buildings": {"Building": {"BBR": [None, parse_inputdata_for_autolabels_buildings_bbr_extracting_test]}}}}}
        #{'InputData': [None, parse_building, True]},
        #{'InputData': {'Building': {'Address': [None, parse_building_address]}}},
        #{'InputData': {'Building': {'BBR': [None, parse_building_bbr]}}},
        #{'InputData': {'Building': {'Zones': [None, parse_building_zones_zone, True]}}},
        #{'InputData': {'Building': {'Zones': {'Zone': {'BuildingUnits': {'Status': [None, parse_building_zones_zone_buildingunits_status]}}}}}}
        #{'InputData': {"Label": {"ProposalGroups": [None, parse_inputdata_proposalgroup, True]}}}, #(FB) Not tested, needs Inputdata_Label_ids
        #{'InputData': {'Label': {'ProposalGroups': {'ProposalGroup': {'ProposalReferences': [None, parse_inputdata_proposalreference]}}}}}
    ]
    esi = None
    serial_id = None
    with get_connection() as conn:
        with conn.cursor() as cur:
            file_path = "/home/energy_extract/out"
            for pretty_doc in os.listdir(file_path):
                if not '310020992' in pretty_doc: #310020992
                     continue
                print(pretty_doc)
                pretty_doc = file_path + "/" + pretty_doc

                global id_func 
                global id_func_counter
                #global prev

                id_func = []
            #    print("id_func main: ", id_func)
                for index, content in enumerate(content_types_test):
                    #print('reached actual content: ', content)
                    id_func_counter = 0
                    index += 1
                    #if index == 6:
                        #sys.exit(1)
                    if isinstance(content, dict):
                        handle_dicts_new(pretty_doc, content, esi, serial_id, logging, cur, conn)
                        continue
                    etree = get_root(pretty_doc, content)
                    if content == "EnergyLabelSerialIdentifier":
                        esi, serial_id = insert_energylabel_serial_identifier(etree, pretty_doc, cur, logging)

if __name__ == "__main__":
    main()



#NOT USED
def handle_dicts(pretty_doc, content, esi, serial_id, logging, cur, conn, etree_param = None):
    global id_func
    for key, vals in content.items():
        if etree_param is not None:
            #print("Key: ", key)
            etree = etree_param.findall('.//{*}' + key)
        else:
            etree = get_root(pretty_doc, key)
        for et in etree:
            if isinstance(vals, dict):
                for key1 in vals.keys():
                    if isinstance(vals[key1], dict):
                        et_keys = et.findall('.//{*}' + key1)
                        for et_key in et_keys:
                            handle_dicts(pretty_doc, vals[key1], esi, serial_id, logging, cur, conn, et_key)
                    else:
                        function = vals[key1][1]
                        id_func = function(et, content, serial_id, logging, esi, cur, conn, id_func)
                        #print("Post: ", id_func)
            else:
                function = vals[1]
                id_func = function(et, content, serial_id, logging, esi, cur, conn, id_func)