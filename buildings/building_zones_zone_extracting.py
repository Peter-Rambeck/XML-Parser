from etree_helper import generic_extracting, generate_sql_insert

def parse_building_zones_zone(etree, content, serial_id, logging, esi, cur, conn, id_func):
    print("Zone id_func: ", id_func)
    zone_ids = []

    for id_ref in id_func:     
        print("zone id_ref in loop: ", id_ref)   
        zones_zone_dict={}
        zones_zone_dict["Zone"] = [{"Name":  None, "Usage": None, "SubtractWindowAreaFromOuterWalls": None, "BBRUseCode": None, "BuildingType": None,
            "HousingUnits": None, "FloorCount": None, "Height": None, "UsageDays": None, "UsageFrom": None, "UsageTo": None, "TotalHeatedFloorArea": None,
            "TopFloorAreaOfHeatedFloorArea": None, "BasementAreaOfHeatedFloorArea": None, "UnheatedBasementArea": None, "HeatCapacity": None, "Rotation": None,
            "AdditionToEnergyFrame": None, "SetPointHeatedTemperature": None, "SetPointWantedTemperature": None, "SetPointNaturalVentilationTemperature": None,
            "SetPointCoolingTemperature": None, "SetPointStoreTemperature": None, "DimensioningRoomTemperature": None, "DimensioningOuterTemperature": None,
            "DimensioningStoreTemperature": None, "ElectricityPriceForHeating": None, "ElectricityPriceForNonHeating": None, 
            "ElectricityPriceForExcessProduction": None, "YearlyFeeForExcessProductionOfElectricity": None, "EstimatedElectricityConsumptionForNonHeating": None,
            "SunBurdenedRooms": None, "HeatedDwellingArea": None, "HeatedCommercialArea": None, "ElectricityPrice": None, "WaterPrice": None, 
            "ElectricityForHeatingPrice": None, "ElectricityForNonHeatingPrice": None, "OtherHeatedBasementArea": None, "ProposalGroups": None, "BuiltUpArea": None,
            "BuildingUnits": None}]
        dict_local = generic_extracting(etree, zones_zone_dict)
        print('Zone dict_local len: ', len(dict_local["Zone"]))
        #print('id_func len: ', len(id_func))
        
        # for s in dict_local["Zone"]:
        #     s["building_id_ref"]= id_ref
        #     print('Zone - got building_id_ref: ', id_ref)
        #     zones_zone_id_ref = generate_sql_insert("zones_zone", s, content, logging, esi, cur, conn, 'id')
        #     zone_ids.append(zones_zone_id_ref)
        # print("Zone ids: ", zone_ids)
    return zone_ids
    #return zones_zone_id_ref


