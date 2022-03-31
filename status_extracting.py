from etree_helper import generic_extracting, generate_sql_insert

def parse_status(esi, logging, etree, cur):
    status_dict = {}
    status_dict["ShortText"] = None
    status_dict["LongText"] = None
    status_dict["IsBasedOnSeebStandardBuilding"] = None
    status_dict["SEEBClassification"] = None
    list_of_dicts = []
    tablename = "zone_statuses"

    for et in etree:
        status_dict = generic_extracting(et, status_dict)
        #generic_inserting(status_dict, tablename, esi, logging, cur)
        list_of_dicts.append(status_dict)
    return list_of_dicts


    

    

