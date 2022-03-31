from etree_helper import generic_extracting, generate_sql_insert

#FB (10/03): This script is untested with call from run-energy.py
#Based upon test script proposal_group_extracting_test.py
#It depends on the database structure from 012_drop_tables.sql
#Still needs to get inputdata_label_id_ref

#def parse_proposal_groups(etree):
def parse_inputdata_proposalgroup(etree, content, serial_id, logging, esi, cur, conn, id_func):
    print("parse_inputdata_proposalgroup id_func: ", id_func)
    inputdata_proposalgroup_ids = []

    tablename1 = "inputdata_proposalgroups"
    
    for id_ref in id_func:
        print("parse_inputdata_proposalgroup id_ref in loop: ", id_ref) 

        proposal_groups_dict = {}
        proposal_groups_dict["ProposalGroup"] = [{
            "attribute_id": None,
            "inputdata_label_id_ref": None,
            "ShortText": None,
            "LongText": None,
            "Investment": None,
            "IsInvestmentOverridden": None,
            "SEEBClassification": None,
            "IsRecommended": None,
            "BIClassification": None,
            "ImplementationReferenceText": None,
            "ImplementationReferenceLink": None,
            "RenovationTime": None,
            "AlternativeImplementationText": None
        }]

        # proposal_groups_dict["attribute_id"] = None
        # proposal_groups_dict["inputdata_label_id_ref"] = id_ref
        # proposal_groups_dict["ShortText"] = None
        # proposal_groups_dict["LongText"] = None
        # proposal_groups_dict["Investment"] = None
        # proposal_groups_dict["IsInvestmentOverridden"] = None
        # proposal_groups_dict["SEEBClassification"] = None 
        # proposal_groups_dict["IsRecommended"] = None
        # proposal_groups_dict["BIClassification"] = None
        # proposal_groups_dict["ImplementationReferenceText"] = None
        # proposal_groups_dict["ImplementationReferenceLink"] = None
        # proposal_groups_dict["RenovationTime"] = None
        # proposal_groups_dict["AlternativeImplementationText"] = None

        # proposal_ref_dict = {}
        # proposal_ref_dict["ProposalReferences"] = {"ProposalReference": [{"attribute_proposalid": None}]}

        dict_local = generic_extracting(etree, proposal_groups_dict)

        for s in dict_local["ProposalGroup"]:
            s["inputdata_label_id_ref"] = id_ref
            if s["attribute_proposalid"] is not None:
                print("found attribute id: ", s["attribute_proposalid"])
                inputdata_proposalgroup_id_ref = proposal_group_id = generate_sql_insert(tablename1, s, content, logging, esi, cur, conn, "id")
                inputdata_proposalgroup_ids.append(inputdata_proposalgroup_id_ref)
        print("inputdata_proposalgroup_ids ", inputdata_proposalgroup_ids)
        return inputdata_proposalgroup_ids

        
        tablename2 = "inputdata_proposalreferences"    
        #proposal_group_id = generate_sql_insert(tablename1, dict_local, content, logging, esi, cur, conn, "id", 'test2')
        #Use the method call below when switching to the schema intended for the real deal
        #proposal_group_id = generate_sql_insert(tablename1, dict_local, content, logging, esi, cur, conn, "id")

        # cont. in etree helper: parse attribute of ProposalReference 
        del dict_local
        dict_local = generic_extracting(etree, proposal_ref_dict)
        for s in proposal_ref_dict["ProposalReferences"]["ProposalReference"]:
            s["inputdata_proposalgroups_serial_id_ref"] = proposal_group_id

            #The proposal id is the only thing we really want in the proposalreference
            # dictionary, so don't insert null values into the DB table.
            if s["attribute_proposalid"] is not None:
                #generate_sql_insert(tablename2, s, content, logging, esi, cur, conn, 'id', 'test2')
                #Use the method call below when switching to the schema intended for the real deal
                generate_sql_insert(tablename2, s, content, logging, esi, cur, conn, 'id')


# Use if needed, otherwise leave alone.
def parse_inputdata_proposalreference(etree, content, serial_id, logging, esi, cur, conn, id_func):
    print("parse_inputdata_proposalreference id_func: ", id_func)
    tablename2 = "inputdata_proposalreferences"
    
    for id_ref in id_func:
        print("parse_inputdata_proposalreference id_func: ", id_func)

        proposal_ref_dict = {}
        proposal_ref_dict["ProposalReference"] = [{
            "attribute_proposalid": None,
            "inputdata_proposalgroups_serial_id_ref": None
        }]

        # proposal_ref_dict = {}
        # proposal_ref_dict["attribute_proposalid"] = None
        # proposal_ref_dict["inputdata_proposalgroups_serial_id_ref"] = id_ref

        dict_local = generic_extracting(etree, proposal_ref_dict)

        for s in dict_local["ProposalReference"]:
            s["inputdata_proposalgroups_serial_id_ref"] = id_ref

            if s["attribute_proposalid"] is not None:
                generate_sql_insert(tablename2, s, content, logging, esi, cur, conn, 'id')


       