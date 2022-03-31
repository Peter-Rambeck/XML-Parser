from etree_helper import generic_extracting, generate_sql_insert

def parse_resultdata_building_result(esi, serial_id, logging, etree, cur, conn):
    building_result_dict = {}
    building_result_dict["EnergyLabelClassification"] = None 
    building_result_dict["Status"] = {"EnergyLabelClassification": None}
    building_result_dict["ResultForAllProposals"] = {"EnergyLabelClassification": None}
    building_result_dict["ResultForAllProfitableProposals"] = {"EnergyLabelClassification": None}
    building_result_dict["Material"] = None
    building_result_dict["Unit"] = None
    building_result_dict["EnergyPerUnit"] = None
    building_result_dict["CO2PerUnit"] = None
    building_result_dict["CostPerUnit"] = None
    building_result_dict["FixedCostPerYear"] = None
    building_result_dict["SupplierCompanyName"] = None
    building_result_dict["FuelConsumption"] = None
    building_result_dict["FuelConsumptionPrYear"] = None
    building_result_dict["IsForHeating"] = None
    building_result_dict["Profitability"] = None
    building_result_dict["Category"] = None
    building_result_dict["Investment"] = None
    building_result_dict["FuelSaved"] = None
    building_result_dict["AdjustedReportedConsumptions"] = None
    building_result_dict["AdjustedLoggedConsumptions"] = None
    building_result_dict["FuelSavings"] = None
    building_result_dict["xml_id_ref"] = serial_id

    dict_local = generic_extracting(etree, building_result_dict)
    generate_sql_insert("resultdata_buildingresult", dict_local, logging, esi, cur, conn, 'null')

