from energy_label_extracting import parse_energy_label, parse_energy_label_apartments
from resultdata_building_result import parse_resultdata_building_result
from status_extracting import parse_status
from inputdata_proposalgroup_extracting import parse_inputdata_proposalgroup
from utils import get_logger, get_connection
import sys
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
from building_zones_zone_buildingunits_status_extracting import parse_building_zones_zone_buildingunits_status
from lxml import etree as ET
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

def handle_dicts_new(pretty_doc, content, esi, serial_id, logging, cur, conn, etree_param = None):
    global id_func
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
                    function(et, content, serial_id, logging, esi, cur, conn, id_func[id_func_counter])
            print('id_func: ', id_func)
            print('id_func_counter: ', id_func_counter)
            print('len etree: ', len(etree))

    if id_func_counter != -1 and id_func_counter == prev:
        #print('plus 1')
        id_func_counter += 1

def trim_unwanted(str1):                                                                                                                                                           
    str2 = str1.split('}')[1]                                                                                                                                                      
    return str2.split('{')[0] 

def fix_str_path(str_element_path):
    str_element_path = str_element_path[2:].replace('/', '_').lower()


def etree_iter_path(node, tag=None, path='.'):
    if tag == "*":
        tag = None
    if tag is None or node.tag == tag:
        yield node, path
    for child in node:
        _child_path = '%s/%s' % (path, child.tag)
        for child, child_path in etree_iter_path(child, tag, path = _child_path):
            yield child, child_path

def handle_doc(pretty_doc):
    tree = ET.parse(pretty_doc)
    root = tree.getroot()
    for element, str_element_path in etree_iter_path(root):
        if element.attrib.items():
            str_element_path = fix_str_path(str_element_path)
            print('str_element_path: ', str_element_path)
            for key, value in element.attrib.items():
                pass

      
def main():
    debug = None
    if len(sys.argv) > 1:
        debug = True
    logging = get_logger(debug)
    content_types_test = [
        'EnergyLabelSerialIdentifier',
        {'InputData': [None, parse_building, True]},
        {'InputData': {'Building': {'Address': [None, parse_building_address]}}},
        {'InputData': {'Building': {'BBR': [None, parse_building_bbr]}}},
        {'InputData': {'Building': {'Zones': [None, parse_building_zones_zone, True]}}},
        {'InputData': {'Building': {'Zones': {'Zone': {'BuildingUnits': {'Status': [None, parse_building_zones_zone_buildingunits_status]}}}}}}
        #{'InputData': {"Label": {"ProposalGroups": {"ProposalGroup": [None, parse_inputdata_proposalgroup]}}}}, #(FB) Not tested, but should work
    ]
    content_types = [
        'EnergyLabelSerialIdentifier',
        'EnergyLabel', 
        {'ZoneResult': None},
        {'Building': [None, parse_building, True]},
        {'Building': {'Address': [None, parse_building_address]}},
        {'Building': {'BBR': None}},
        {'Building': {'Zones': {'Zone': None}}},
        {'Building': {'Zones': {'Zone': {'BuildingUnits': {'Status': None}}}}},
        {'ZoneResult': {'Status': None}},
        {'ZoneResult': {'ResultForAllProfitableProposals': None}},
        {'ZoneResult': {'ResultForAllProposals': None}},
        {'ZoneResult': {'ResultForEachProposalGroup': None}}, 
        {'ZoneResult': {'Status': {'CalculatedSBIResult': {'ResultFigures': None} }}},
        {'ZoneResult': {'Status': {'CalculatedSBIResult': {'KeyFigures': None} }}},
        {'ZoneResult': {'Status': {'CalculatedBe15Result': {'ResultFigures': None} }}},
        {'ZoneResult': {'Status': {'CalculatedBe15Result': {'KeyFigures': None} }}},
        {'ZoneResult': {'Status': {'CalculatedBe18Result': {'ResultFigures': None} }}},
        {'ZoneResult': {'Status': {'CalculatedBe18Result': {'KeyFigures': None} }}},
        {'ZoneResult': {'Status': {'CalculatedBe10Result': {'ResultFigures': None} }}},
        {'ZoneResult': {'Status': {'CalculatedBe06Result': {'ResultFigures': None} }}},
        {'ZoneResult': {'Status': {'CalculatedBe06Result': {'ResultFigures': None} }}},
        {'ZoneResult': {'Status': {'CalculatedBe10Result': {'KeyFigures': None} }}},
        {'ZoneResult': {'Status': {'CalculatedBe06Result': {'KeyFigures': None} }}},
        {'InputData': {'Label': None}},
        {'InputData': {"Label": {"ProposalGroups": {"ProposalGroup": None}}}},
        {'ResultData': {'LabelResults': None}},
        {'ZoneResult': {'ResultForAllProfitableProposals': {'CalculatedBe06Result': {'ResultFigures': None} }}},
        {'ZoneResult': {'ResultForAllProfitableProposals': {'CalculatedBe06Result': {'KeyFigures': None} }}},
        {'ZoneResult': {'ResultForAllProfitableProposals': {'CalculatedBe10Result': {'ResultFigures': None} }}},
        {'ZoneResult': {'ResultForAllProfitableProposals': {'CalculatedBe10Result': {'KeyFigures': None} }}},
        {'ZoneResult': {'ResultForAllProfitableProposals': {'CalculatedBe15Result': {'ResultFigures': None} }}},
        {'ZoneResult': {'ResultForAllProfitableProposals': {'CalculatedBe15Result': {'KeyFigures': None} }}},
        {'ZoneResult': {'ResultForAllProfitableProposals': {'CalculatedBe18Result': {'ResultFigures': None} }}},
        {'ZoneResult': {'ResultForAllProfitableProposals': {'CalculatedBe18Result': {'KeyFigures': None} }}},
        {'ZoneResult': {'ResultForAllProfitableProposals': {'CalculatedSBIResult': {'ResultFigures': None} }}},
        {'ZoneResult': {'ResultForAllProfitableProposals': {'CalculatedSBIResult': {'KeyFigures': None} }}},
        {'ZoneResult': {'ResultForAllProposals': {'CalculatedBe18Result': {'ResultFigures': None} }}},
        {'ZoneResult': {'ResultForAllProposals': {'CalculatedBe18Result': {'KeyFigures': None} }}},
        {'ZoneResult': {'ResultForAllProposals': {'CalculatedBe15Result': {'ResultFigures': None} }}},
        {'ZoneResult': {'ResultForAllProposals': {'CalculatedBe15Result': {'KeyFigures': None} }}},
        {'ZoneResult': {'ResultForAllProposals': {'CalculatedBe10Result': {'ResultFigures': None} }}},
        {'ZoneResult': {'ResultForAllProposals': {'CalculatedBe10Result': {'KeyFigures': None} }}},
        {'ZoneResult': {'ResultForAllProposals': {'CalculatedBe06Result': {'ResultFigures': None} }}},
        {'ZoneResult': {'ResultForAllProposals': {'CalculatedBe06Result': {'KeyFigures': None} }}},
        {'ZoneResult': {'ResultForEachProposalGroup': {'ProposalResult':None}}},
        {'ZoneResult': {'ResultForEachProposalGroup': {'FuelSavings': None}}}
        ]
    esi = None
    serial_id = None
    with get_connection() as conn:
        with conn.cursor() as cur:
            file_path = "/home/energy_extract/out"
            for pretty_doc in os.listdir(file_path):
                print(pretty_doc)
                pretty_doc = file_path + "/" + pretty_doc
                handle_doc(pretty_doc)
                continue

                global id_func 
                global id_func_counter
                id_func = []
                for index, content in enumerate(content_types_test):
                    id_func_counter = 0
                    index += 1
                    if isinstance(content, dict):
                        handle_dicts_new(pretty_doc, content, esi, serial_id, logging, cur, conn)
                        continue
                    etree = get_root(pretty_doc, content)
                    if content == "EnergyLabelSerialIdentifier":
                        esi, serial_id = insert_energylabel_serial_identifier(etree, pretty_doc, cur, logging)

if __name__ == "__main__":
    main()
