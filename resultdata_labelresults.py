import os
import sys
from etree_helper import generic_extracting
from run_energy import get_root, handle_dicts
from utils import get_connection

def parse_resultdata_labelresults(esi, serial_id, logging, etree, cur, conn):
    
    #EnergyLabel_InputData_Label_Apartments_Apartment
    label_result_dict2 = {}
    label_result_dict2["Apartments"] = {"Apartment": {"CostForHeatingPerApartment": None}}
    
    #EnergyLabel_ResultData_LabelResults_ResultForAllProposals
    label_result_dict3 = {}
    label_result_dict3['EnergyLabelClassification'] = None
    label_result_dict3["FuelConsumption"] = {
        "EnergyLabelClassification": None,
        "Material": None,
        "Unit": None,
        "EnergyPerUnit": None,
        "CO2PerUnit": None,
        "CostPerUnit": None,
        "FixedCostPerYear": None,
        "SupplierCompanyName": None,
        "FuelConsumption": None,
        "IsForHeating": None,
    }

    #EnergyLabel_ResultData_LabelResults_ResultsForEachProposalGroup_ProposalGroupResult
    label_result_dict4 = {}
    label_result_dict4["ProposalGroupResult"] = {
            "Profitability": None, 
            "Category": None,
            "Investment": None,
            "InvestmentLifetime": None,
        }

    #EnergyLabel_ResultData_LabelResults_ResultForAllProfitableProposals
    label_result_dict5 = {}
    label_result_dict5["ResultForAllProfitableProposals"] = {
        "EnergyLabelClassification": None,
        "Material": None,
        "Unit": None,
        "EnergyPerUnit": None,
        "CO2PerUnit": None,
        "CostPerUnit": None,
        "FixedCostPerYear": None,
        "SupplierCompanyName": None,
        "FuelConsumption": None,
        "IsForHeating": None,
    }


    #EnergyLabel_ResultData_LabelResults_ResultsForEachProposalGroup_ProposalGroupResult_FuelSavings_FuelSaving
    label_result_dict5 = {}
    label_result_dict5["ProposalGroupResult"] = {"FuelSaving": {
        "Material": None,
        "Unit": None,
        "EnergyPerUnit": None,
        "CO2PerUnit": None,
        "CostPerUnit": None,
        "FixedCostPerYear": None,
        "SupplierCompanyName": None,
        "fuelSaved": None
        }
    }
    
    label_result_dict6 = {}
    label_result_dict6["ProposalResult"] = {"FuelSaving": 
        {
        "Material": None,
        "Unit": None,
        "EnergyPerUnit": None,
        "CO2PerUnit": None,
        "CostPerUnit": None,
        "FixedCostPerYear": None,
        "SupplierCompanyName": None,
        "fuelSaved": None
        }
    }

     #EnergyLabel_ResultData_LabelResults
    label_result_dict1 = {}
    label_result_dict1['EnergyLabelClassification'] = None
    label_result_dict1["AdjustedReportedConsumptions"] = None
    
    
    # label_result_dict1["Status"] = [{
    #     "EnergyLabelClassification": None,
    #     "Material": None,
    #     "Unit": None,
    #     "EnergyPerUnit": None,
    #     "CO2PerUnit": None,
    #     "CostPerUnit": None,
    #     "FixedCostPerYear": None,
    #     "SupplierCompanyName": None,
    #     "FuelConsumption": None,
    #     "IsForHeating": None,
    # }]
    
    dict_local = generic_extracting(etree, label_result_dict1)
    print("After generic extracting: ", dict_local)
    #label_result_id = generate_sql_insert("resultdata_labelresults", dict_local, logging, esi, cur, conn, 'id')
    
   

    # label_result_id = None
    # dict_local = generic_extracting(etree, label_result_dict2)
    # for s in label_result_dict2["Apartments"]["Apartment"]:
    #     s["label_result_id_ref"] = label_result_id
    #     generate_sql_insert("labelresults_apartment", s, logging, esi, cur, conn, 'null')



