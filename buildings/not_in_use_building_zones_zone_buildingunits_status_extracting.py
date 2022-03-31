from etree_helper import generic_extracting, generate_sql_insert

def parse_building_zones_zone_buildingunits_status(etree, content, zones_zone_id_ref, logging, esi, cur, conn, id_func):
    for id_ref in id_func:
        zones_zone_status_dict={}
        zones_zone_status_dict["ShortText"]= None
        zones_zone_status_dict["LongText"]= None
        zones_zone_status_dict["IsBasedOnSeebStandardBuilding"]= None
        zones_zone_status_dict["SEEBClassification"]= None
        zones_zone_status_dict["Proposals"]= None
        zones_zone_status_dict["zones_zone_id_ref"]= id_ref
        print('building_units - zones_zone_id_ref: ', id_ref)
        dict_local = generic_extracting(etree, zones_zone_status_dict)
        generate_sql_insert("buildingunits_status", dict_local, content, logging, esi, cur, conn, 'null')
        print("BuildingUnits: ", id_ref)
    #return id_func
