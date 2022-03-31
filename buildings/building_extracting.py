from etree_helper import generic_extracting, generate_sql_insert
import pprint

def parse_building(etree, content, serial_id, logging, esi, cur, conn, id_func):
    building_dict={}
    building_dict["Building"]= [{"IsTenancy" : None, "ReportedConsumptions": None, "LoggedConsumptions": None,
        'BuildingRegulation': None, 'BuildingRegulationDate': None, 'EnergyPermitEnergyDemand': None, 'BR08BuildingPermitClassification': None,
        'BR18BuildingPermitClassification': None, 'BR10BuildingPermitClassification': None, 'BR15BuildingPermitClassification': None}]
    dict_local = generic_extracting(etree, building_dict)
    print("Building doct_local: ", dict_local)
    id_list = []
    for s in dict_local["Building"]:
        s["xml_id_ref"] = serial_id
        building_id_ref = generate_sql_insert("building", s, content, logging, esi, cur, conn, 'id')
        id_list.append(building_id_ref)
    print("id_list building: ", id_list)
    return id_list

    #return building_id_ref

def parse_building_address(etree, content, serial_id, logging, esi, cur, conn, id_func):
    for id_ref in id_func:
        building_address_dict={}
        building_address_dict["Name"]= None
        building_address_dict["StreetName"]= None
        building_address_dict["HouseNumber"]= None
        building_address_dict["Floor"]= None
        building_address_dict["SideOrDoor"]= None
        building_address_dict["PostalCode"]= None
        building_address_dict["PostalCity"]= None
        building_address_dict["StreetCode"]= None
        building_address_dict["building_id_ref"] = id_ref
        print('Adress - got building_id_ref: ', id_ref)
        dict_local = generic_extracting(etree, building_address_dict)
        generate_sql_insert("building_address", dict_local, content, logging, esi, cur, conn, 'null')
        print(dict_local)

