import os
#from run_energy import get_root
from utils import get_logger
import sys
from etree_helper import generic_extracting, generate_sql_insert
from pprint import pprint
from utils import get_connection      

def parse_result_f_a_p_proposals_calculatedbe15result_keyfigures(etree, content, serial_id, logging,  esi, cur, conn):

    result_f_a_p_proposals_calculatedbe15result_keyfigures_dict = {}
   
    result_f_a_p_proposals_calculatedbe15result_keyfigures_dict["TransmissionLossThroughEnvelopeExcludingWindowsAndDoors"] = None

    result_f_a_p_proposals_calculatedbe15result_keyfigures_dict["RenovationClass2"] = {"EnergyFrameInBRNoAddition": None, "AdditionToEnergyFrameDueToSpecialConditions": None, 
    "TotalEnergyRequirement": None, "ContributionToEnergyRequirementHeating": None}

    result_f_a_p_proposals_calculatedbe15result_keyfigures_dict["RenovationClass1"] = {"EnergyFrameInBRNoAddition": None, 
    "AdditionToEnergyFrameDueToSpecialConditions": None, 
    "TotalEnergyRequirement": None, "ContributionToEnergyRequirementHeating": None}
   
    result_f_a_p_proposals_calculatedbe15result_keyfigures_dict["EnergyFrame2015"] = {"EnergyFrameInBRNoAddition" : None, "AdditionToEnergyFrameDueToSpecialConditions": None, 
    "TotalEnergyRequirement": None, "ContributionToEnergyRequirementHeating": None, "ContributionToEnergyRequirementElectricity": None, "ContributionToEnergyRequirementExcessTemprature": None }
    
    result_f_a_p_proposals_calculatedbe15result_keyfigures_dict["EnergyFrame2020"] = {"EnergyFrameInBRNoAddition": None, 
    "AdditionToEnergyFrameDueToSpecialConditions": None, "TotalEnergyRequirement": None, "ContributionToEnergyRequirementHeating": None,
     "ContributionToEnergyRequirementElectricity": None, "ContributionToEnergyRequirementExcessTemprature": None}
    
    result_f_a_p_proposals_calculatedbe15result_keyfigures_dict["zone_result_resultforallprofitableproposals_id_ref"] = serial_id

    dict_local = generic_extracting(etree, result_f_a_p_proposals_calculatedbe15result_keyfigures_dict)
    generate_sql_insert("result_f_a_p_proposals_calculatedbe15result_keyfigures", dict_local, content, logging, esi, cur, conn, 'id')

    #import sys
    #sys.exit(1)

# def handle_dicts(pretty_doc, content, esi, serial_id, logging, cur, conn, etree_param = None):
#     for key, vals in content.items():
#         if etree_param is not None:
#             etree = etree_param.findall('.//{*}' + key)
#         else:
#             etree = get_root(pretty_doc, key)
#             print('etree-handle_dicts: ', type(etree))
#         for et in etree:
#             print('Now Im here 1')
    
#             if isinstance(vals, dict):       
#                 print('Now Im here 2')          
#                 for key1 in vals.keys():
#                     print('Now Im here 3')

#                     if isinstance(vals[key1], dict):

#                         print('Now Im here 4')
#                         et_keys = et.findall('.//{*}' + key1)
#                         for et_key in et_keys:
#                             handle_dicts(et_key, vals[key1], esi, serial_id, logging, cur, conn, et_key)
                    
#                     else:
#                       # her hvis dict er lige nested (2,4,6,8,osv.)
#                         if key1 == 'KeyFigures':
#                             print('Now Im here 5')
#                             parse_zone_result_status_calculatedbe15result_keyfigures(et, esi, serial_id, logging, cur, conn)

#             else:
#                 # her hvis dict er ulige nested (1,3,5,7,osv.)
#                 print('Now Im here 6')
#                 if key == '....':
#                     print("do something")
            
#             #import sys
#             #sys.exit(1)                                


# def main():
#     debug = None
#     if len(sys.argv) > 1:
#         debug = True
#     logging = get_logger(debug)
#     #(FB says): It seemed like making Label under InputData into a dictionary was a good idea
#     # because it had to go a few levels down and ProposalGroups will appear in another tag's hierarchy.
#     content_types = [{'ZoneResult': {'Status': {'CalculatedBe15Result': {'KeyFigures': None} }}}]  #[{'InputData':[{"Label": ["ProposalGroups"]}]}, {'ResultData': ["LabelResults", "BuildingResult"]}, 'Building']
#     #doc = "/home/energy_extract/test_mape/XML_docs/copy_pretty_100115068.xml"
    
#     esi = None
#     serial_id = None
#     with get_connection() as conn:
#         with conn.cursor() as cur:
#             file_path = "/home/energy_extract/out"
#             for pretty_doc in os.listdir(file_path):
#                 pretty_doc = file_path + "/" + pretty_doc
#                 for content in content_types:
#                     if isinstance(content, dict):
#                         handle_dicts(pretty_doc, content, esi, serial_id, logging, cur, conn)
#                         continue
#                     print("pretty_doc: " , pretty_doc)
#                     etree = get_root(pretty_doc, content)
#                     print('main: ', type(etree))             
#                     if content == "ZoneResult":
#                         parse_zone_result_status_calculatedbe15result_keyfigures(etree, content, logging, esi, cur, conn)
   
                    
# if __name__ == "__main__":
#     main()

