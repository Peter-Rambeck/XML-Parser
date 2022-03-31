from itertools import count
import os
#from run_energy import get_root
from utils import get_logger
import sys
from etree_helper import generic_extracting, generate_sql_insert
from pprint import pprint
from lxml import etree as ET
from utils import get_connection
      
#Still needs to get inputdata_label_id_ref

def proposal_group_extracting_test(etree, content, logging, esi, cur, conn):

    #print(etree.tag)

    proposal_groups_dict = {}
    proposal_groups_dict["attribute_id"] = None
    proposal_groups_dict["inputdata_label_id_ref"] = None
    proposal_groups_dict["ShortText"] = None
    proposal_groups_dict["LongText"] = None
    proposal_groups_dict["Investment"] = None
    proposal_groups_dict["IsInvestmentOverridden"] = None
    proposal_groups_dict["SEEBClassification"] = None 
    
    proposal_groups_dict["IsRecommended"] = None
    proposal_groups_dict["BIClassification"] = None
    proposal_groups_dict["ImplementationReferenceText"] = None
    proposal_groups_dict["ImplementationReferenceLink"] = None
    proposal_groups_dict["RenovationTime"] = None
    proposal_groups_dict["AlternativeImplementationText"] = None

    proposal_ref_dict = {}
    proposal_ref_dict["ProposalReferences"] = {"ProposalReference": [{"attribute_proposalid": None}]}
    
    dict_local = generic_extracting(etree, proposal_groups_dict)
    tablename1 = "inputdata_proposalgroups"
    tablename2 = "inputdata_proposalreferences"    
    proposal_group_id = generate_sql_insert(tablename1, dict_local, content, logging, esi, cur, conn, "id", 'test2')
    #Use the method call below when switching to the schema intended for the real deal
    #proposal_group_id = generate_sql_insert(tablename1, dict_local, content, logging, esi, cur, conn, "id")

    # cont. in etree helper: parse attribute of ProposalReference 
    del dict_local
    dict_local = generic_extracting(etree, proposal_ref_dict)
    #count = 10
    for s in proposal_ref_dict["ProposalReferences"]["ProposalReference"]:
        s["inputdata_proposalgroups_serial_id_ref"] = proposal_group_id

        #The proposal id is the only thing we really want in the proposalreference
        # dictionary, so don't insert null values into the DB table.
        if s["attribute_proposalid"] is not None:
            pprint("Found proposal ID!")
            generate_sql_insert(tablename2, s, content, logging, esi, cur, conn, 'id', 'test2')
            #Use the method call below when switching to the schema intended for the real deal
            #generate_sql_insert(tablename2, s, content, logging, esi, cur, conn, 'id')
        
        #Below is part of test code
        #pprint(s)
        # count -= 1
        # if count <= 1:
        #     conn.commit()
        #     sys.exit(1)
    #import sys
    #sys.exit(1)

def get_root(doc, etree_content):
    try:
        tree = ET.parse(doc)
        if etree_content == 'EnergyLabel': return tree.getroot()
        etree = tree.findall('.//{*}' + etree_content)
    except ET.XMLSyntaxError:
        return None
    return etree

def handle_dicts(pretty_doc, content, esi, serial_id, logging, cur, conn, etree_param = None):
    for key, vals in content.items():
        if etree_param is not None:
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
                        pass
                        # her hvis dict er lige nested (2,4,6,8,osv.)
                        # if key1 == 'Building':
                        #     #pass
                        #     #pprint('Building Even: Do something here in handle_dicts!')
                        #     parse_inputdata_for_autolabels_buildings_bbr_and_address_extracting_test(et, key, serial_id, logging, esi, cur, conn)
                        #     #count -= 1
            else:
                # her hvis dict er ulige nested (1,3,5,7,osv.)
                #pass
                if key == 'ProposalGroup':
                    proposal_group_extracting_test(et, content, logging, esi, cur, conn)
                

def old_handle_dicts(pretty_doc, content, esi, serial_id, logging, cur, conn, etree_param = None):
    for key, vals in content.items():
    
        if etree_param is not None:
            etree = etree_param.findall('.//{*}' + key)
        else:
            etree = get_root(pretty_doc, key)
        for et in etree:
            if isinstance(vals, dict):
                for key1 in vals.keys():
                    et_keys = et.findall('.//{*}' + key1)
                    for et_key in et_keys:
                        handle_dicts(pretty_doc, vals[key1], esi, serial_id, logging, cur, conn, et_key)
            else:
                if key == 'ProposalGroup':
                    proposal_group_extracting_test(et, key, logging, esi, cur, conn)

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
            logging.info('test logging succesfull', extra={'energylabel_serial_identifier': esi})
            return esi, serial_id
    except IndexError:
        pass

def main():
    debug = None
    if len(sys.argv) > 1:
        debug = True
    logging = get_logger(debug)
    #(FB says): It seemed like making Label under InputData into a dictionary was a good idea
    # because it had to go a few levels down and ProposalGroups will appear in another tag's hierarchy.
    content_types = ['EnergyLabel','EnergyLabelSerialIdentifier', {"Label": {"ProposalGroups": {"ProposalGroup": None}}}] # {'ResultData': ["LabelResults", "BuildingResult"]}, 'Building']
    #doc = "/home/energy_extract/test_mape/XML_docs/copy_pretty_100115068.xml"
    esi = None
    serial_id = None
    with get_connection() as conn:
        with conn.cursor() as cur:
            file_path = "/home/energy_extract/out"
            for pretty_doc in os.listdir(file_path):
                pretty_doc = file_path + "/" + pretty_doc
                for content in content_types:
                    if isinstance(content, dict):
                        handle_dicts(pretty_doc, content, esi, serial_id, logging, cur, conn)
                        #sys.exit(1)
                    #print("pretty_doc: " , pretty_doc)
                    if content == "EnergyLabelSerialIdentifier":
                        #print("here")
                        etree = get_root(pretty_doc, content)
                        esi, serial_id = insert_energylabel_serial_identifier(etree, pretty_doc, cur, logging)
                    
if __name__ == "__main__":
    main()
