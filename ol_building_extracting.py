from etree_helper import generic_extracting, generate_sql_insert

def parse_building(etree, content, serial_id, logging, esi, cur, conn):
    building_dict = {}
    building_dict["EnergyLabelClassification"] = None
    building_dict["Status"] = {"Name": None, "StreetName": None, "HouseNumber": None, "SideOrDoor": None, "PostalCode": None, "PostalCity": None, "StreetCode": None }
    building_dict["BBR"] = {"BuildingNumber": None, "UseCode": None, "YearOfConstruction": None, "DwellingArea": None, "CommercialArea": None}
   
   
    building_zones_dict = {}
    building_zones_dict["Name"] = None
    building_zones_dict["Usage"] = None
    building_zones_dict["SubtractWindowAreaFromOuterWalls"] = None
    building_zones_dict["BBRUseCode"] = None
    building_zones_dict["BuildingType"] = None
    building_zones_dict["HousingUnits"] = None
    building_zones_dict["FloorCount"] = None
    building_zones_dict["Height"] = None
    building_zones_dict["UsageDays"] = None
    building_zones_dict["UsageFrom"] = None
    building_zones_dict["UsageTo"] = None
    building_zones_dict["TotalHeatedFloorArea"] = None
    building_zones_dict["TopFloorAreaOfHeatedFloorArea"] = None
    building_zones_dict["BasementAreaOfHeatedFloorArea"] = None
    building_zones_dict["UnheatedBasementArea"] = None
    building_zones_dict["HeatCapacity"] = None
    building_zones_dict["Rotation"] = None
    building_zones_dict["AdditionToEnergyFrame"] = None
    building_zones_dict["SetPointHeatedTemperature"] = None
    building_zones_dict["SetPointWantedTemperature"] = None
    building_zones_dict["SetPointNaturalVentilationTemperature"] = None
    building_zones_dict["SetPointCoolingTemperature"] = None
    building_zones_dict["SetPointStoreTemperature"] = None
    building_zones_dict["DimensioningRoomTemperature"] = None
    building_zones_dict["DimensioningOuterTemperature"] = None
    building_zones_dict["DimensioningStoreTemperature"] = None
    building_zones_dict["ElectricityPriceForHeating"] = None
    building_zones_dict["ElectricityPriceForNonHeating"] = None
    building_zones_dict["ElectricityPriceForExcessProduction"] = None
    building_zones_dict["YearlyFeeForExcessProductionOfElectricity"] = None
    building_zones_dict["EstimatedElectricityConsumptionForNonHeating"] = None
    building_zones_dict["SunBurdenedRooms"] = None
    building_zones_dict["HeatedDwellingArea"] = None
    building_zones_dict["HeatedCommercialArea"] = None
    building_zones_dict["ElectricityPrice"] = None
    building_zones_dict["WaterPrice"] = None
    building_zones_dict["ElectricityForHeatingPrice"] = None
    building_zones_dict["ElectricityForNonHeatingPrice"] = None
    building_zones_dict["OtherHeatedBasementArea"] = None



    #dict_local1 = generic_extracting(etree, building_dict)
    dict_local = generic_extracting(etree, building_zones_dict)

    generate_sql_insert("building", dict_local, content, logging, esi, cur, conn, 'id')

    nested_searches = ["Zone", "Status"]


    for et in etree:
        dict_local = generic_extracting(et, building_dict)
        #husk logging:   esi, logging,
        building_id = generate_sql_insert(tablename, dict_local,logging, esi,cur,conn,'building_track_id')
        etree_l = et.findall('.//{*}' + nested_searches[0])
        for et1 in etree_l:
            dict_local = generic_extracting(et1, building_zones_dict)
            


                
