#from etree_helper import generic_extracting, generate_sql_insert
from asyncio import DefaultEventLoopPolicy
from operator import contains
from tag_iterator import create_list_from_tag
import os
import json
from pprint import pprint

#def zone_results(esi, logging, etree, serial_id, cur, conn):



# Zone_Results_Status_
#Sub groups to 'Status'
fuelconsumption = ['fuelconsumption_fuel_material', 'fuelconsumption_fuel_unit', 'fuelconsumption_fuel_energyperunit', 'fuelconsumption_fuel_co2perunit', 'fuelconsumption_fuelprice_costperunit', 'fuelconsumption_fuelprice_fixedcostperyear', 'fuelconsumption_fuelprice_suppliercompanyname', 'fuelconsumption_fuelconsumption', 'fuelconsumption_isforheating', 'fuelconsumption_fuelconsumptionpryear']
calculatedsbiresult = ['calculatedsbiresult_resultfigures_heatingrequirementforcentralheating', 'calculatedsbiresult_resultfigures_heatingrequirementforstoves', 'calculatedsbiresult_resultfigures_heatingrequirementforcentralheatingdegreedayindependent', 'calculatedsbiresult_resultfigures_electricityrequirementforheating', 'calculatedsbiresult_resultfigures_electricityrequirementfornonheating', 'calculatedsbiresult_resultfigures_electricityrequirementforlighting', 'calculatedsbiresult_resultfigures_electricityrequirementforventilation', 'calculatedsbiresult_resultfigures_electricityrequirementforheatpump', 'calculatedsbiresult_resultfigures_electricityrequirementforpumps', 'calculatedsbiresult_resultfigures_heatpumpheatingtotalperformance', 'calculatedsbiresult_resultfigures_solarheatingplantheatingtotalperformance', 'calculatedsbiresult_resultfigures_solarcellstotalperformance', 'calculatedsbiresult_resultfigures_fulfilmentheatinghotwater', 'calculatedsbiresult_resultfigures_fulfilmentelectricityhotwater', 'calculatedsbiresult_resultfigures_boilerefficiency', 'calculatedsbiresult_keyfigures_transmissionlossthroughenvelopeexcludingwindowsanddoors', 'calculatedsbiresult_keyfigures_energyframeinbrnoaddition', 'calculatedsbiresult_keyfigures_additiontoenergyframeduetomechanicalexhaust', 'calculatedsbiresult_keyfigures_additiontoenergyframeduetospecialconditions', 'calculatedsbiresult_keyfigures_totalenergyrequirement', 'calculatedsbiresult_keyfigures_contributiontoenergyrequirementheating', 'calculatedsbiresult_keyfigures_contributiontoenergyrequirementelectricity', 'calculatedsbiresult_keyfigures_contributiontoenergyrequirementexcesstemprature']
calculatedbe15result = ['calculatedbe15result_resultfigures_heatingrequirementforcentralheating', 'calculatedbe15result_resultfigures_heatingrequirementforstoves', 'calculatedbe15result_resultfigures_heatingrequirementforcentralheatingdegreedayindependent', 'calculatedbe15result_resultfigures_electricityrequirementforheating', 'calculatedbe15result_resultfigures_electricityrequirementfornonheating', 'calculatedbe15result_resultfigures_electricityrequirementforlighting', 'calculatedbe15result_resultfigures_electricityrequirementforventilation', 'calculatedbe15result_resultfigures_electricityrequirementforheatpump', 'calculatedbe15result_resultfigures_electricityrequirementforpumps', 'calculatedbe15result_resultfigures_heatpumpheatingtotalperformance', 'calculatedbe15result_resultfigures_solarheatingplantheatingtotalperformance', 'calculatedbe15result_resultfigures_solarcellstotalperformance', 'calculatedbe15result_resultfigures_windmillstotalperformance', 'calculatedbe15result_resultfigures_fulfilmentheatinghotwater', 'calculatedbe15result_resultfigures_fulfilmentelectricityhotwater', 'calculatedbe15result_resultfigures_boilerefficiency', 'calculatedbe15result_keyfigures_transmissionlossthroughenvelopeexcludingwindowsanddoors', 'calculatedbe15result_keyfigures_renovationclass2_energyframeinbrnoaddition', 'calculatedbe15result_keyfigures_renovationclass2_additiontoenergyframeduetospecialconditions', 'calculatedbe15result_keyfigures_renovationclass2_totalenergyrequirement', 'calculatedbe15result_keyfigures_renovationclass2_contributiontoenergyrequirementheating', 'calculatedbe15result_keyfigures_renovationclass1_energyframeinbrnoaddition', 'calculatedbe15result_keyfigures_renovationclass1_additiontoenergyframeduetospecialconditions', 'calculatedbe15result_keyfigures_renovationclass1_totalenergyrequirement', 'calculatedbe15result_keyfigures_renovationclass1_contributiontoenergyrequirementheating', 'calculatedbe15result_keyfigures_energyframe2015_energyframeinbrnoaddition', 'calculatedbe15result_keyfigures_energyframe2015_additiontoenergyframeduetospecialconditions', 'calculatedbe15result_keyfigures_energyframe2015_totalenergyrequirement', 'calculatedbe15result_keyfigures_energyframe2015_contributiontoenergyrequirementheating', 'calculatedbe15result_keyfigures_energyframe2015_contributiontoenergyrequirementelectricity', 'calculatedbe15result_keyfigures_energyframe2015_contributiontoenergyrequirementexcesstemprature', 'calculatedbe15result_keyfigures_energyframe2020_energyframeinbrnoaddition', 'calculatedbe15result_keyfigures_energyframe2020_additiontoenergyframeduetospecialconditions', 'calculatedbe15result_keyfigures_energyframe2020_totalenergyrequirement', 'calculatedbe15result_keyfigures_energyframe2020_contributiontoenergyrequirementheating', 'calculatedbe15result_keyfigures_energyframe2020_contributiontoenergyrequirementelectricity', 'calculatedbe15result_keyfigures_energyframe2020_contributiontoenergyrequirementexcesstemprature', 'calculatedbe15result_keyfigures_energyframe2015_contributiontoenergyrequirementexcesstemperature', 'calculatedbe15result_keyfigures_energyframe2020_contributiontoenergyrequirementexcesstemperature']
calculatedbe10result = ['calculatedbe10result_resultfigures_heatingrequirementforcentralheating', 'calculatedbe10result_resultfigures_heatingrequirementforstoves', 'calculatedbe10result_resultfigures_heatingrequirementforcentralheatingdegreedayindependent', 'calculatedbe10result_resultfigures_electricityrequirementforheating', 'calculatedbe10result_resultfigures_electricityrequirementfornonheating', 'calculatedbe10result_resultfigures_electricityrequirementforlighting', 'calculatedbe10result_resultfigures_electricityrequirementforventilation', 'calculatedbe10result_resultfigures_electricityrequirementforheatpump', 'calculatedbe10result_resultfigures_electricityrequirementforpumps', 'calculatedbe10result_resultfigures_heatpumpheatingtotalperformance', 'calculatedbe10result_resultfigures_solarheatingplantheatingtotalperformance', 'calculatedbe10result_resultfigures_solarcellstotalperformance', 'calculatedbe10result_resultfigures_windmillstotalperformance', 'calculatedbe10result_resultfigures_fulfilmentheatinghotwater', 'calculatedbe10result_resultfigures_fulfilmentelectricityhotwater', 'calculatedbe10result_resultfigures_boilerefficiency', 'calculatedbe10result_keyfigures_transmissionlossthroughenvelopeexcludingwindowsanddoors', 'calculatedbe10result_keyfigures_energyframe2010_energyframeinbrnoaddition', 'calculatedbe10result_keyfigures_energyframe2010_additiontoenergyframeduetospecialconditions', 'calculatedbe10result_keyfigures_energyframe2010_totalenergyrequirement', 'calculatedbe10result_keyfigures_energyframe2010_contributiontoenergyrequirementheating', 'calculatedbe10result_keyfigures_energyframe2010_contributiontoenergyrequirementelectricity', 'calculatedbe10result_keyfigures_energyframe2010_contributiontoenergyrequirementexcesstemprature', 'calculatedbe10result_keyfigures_energyframe2015_energyframeinbrnoaddition', 'calculatedbe10result_keyfigures_energyframe2015_additiontoenergyframeduetospecialconditions', 'calculatedbe10result_keyfigures_energyframe2015_totalenergyrequirement', 'calculatedbe10result_keyfigures_energyframe2015_contributiontoenergyrequirementheating', 'calculatedbe10result_keyfigures_energyframe2015_contributiontoenergyrequirementelectricity', 'calculatedbe10result_keyfigures_energyframe2015_contributiontoenergyrequirementexcesstemprature', 'calculatedbe10result_keyfigures_energyframe2020_energyframeinbrnoaddition', 'calculatedbe10result_keyfigures_energyframe2020_additiontoenergyframeduetospecialconditions', 'calculatedbe10result_keyfigures_energyframe2020_totalenergyrequirement', 'calculatedbe10result_keyfigures_energyframe2020_contributiontoenergyrequirementheating', 'calculatedbe10result_keyfigures_energyframe2020_contributiontoenergyrequirementelectricity', 'calculatedbe10result_keyfigures_energyframe2020_contributiontoenergyrequirementexcesstemprature', 'calculatedbe10result_keyfigures_energyframe2010_contributiontoenergyrequirementexcesstemperature', 'calculatedbe10result_keyfigures_energyframe2015_contributiontoenergyrequirementexcesstemperature', 'calculatedbe10result_keyfigures_energyframe2020_contributiontoenergyrequirementexcesstemperature']
calculatedbe06result = ['calculatedbe06result_resultfigures_heatingrequirementforcentralheating', 'calculatedbe06result_resultfigures_heatingrequirementforstoves', 'calculatedbe06result_resultfigures_heatingrequirementforcentralheatingdegreedayindependent', 'calculatedbe06result_resultfigures_electricityrequirementforheating', 'calculatedbe06result_resultfigures_electricityrequirementfornonheating', 'calculatedbe06result_resultfigures_electricityrequirementforlighting', 'calculatedbe06result_resultfigures_electricityrequirementforventilation', 'calculatedbe06result_resultfigures_electricityrequirementforheatpump', 'calculatedbe06result_resultfigures_electricityrequirementforpumps', 'calculatedbe06result_resultfigures_heatpumpheatingtotalperformance', 'calculatedbe06result_resultfigures_solarheatingplantheatingtotalperformance', 'calculatedbe06result_resultfigures_solarcellstotalperformance', 'calculatedbe06result_resultfigures_fulfilmentheatinghotwater', 'calculatedbe06result_resultfigures_fulfilmentelectricityhotwater', 'calculatedbe06result_resultfigures_boilerefficiency', 'calculatedbe06result_keyfigures_transmissionlossthroughenvelopeexcludingwindowsanddoors', 'calculatedbe06result_keyfigures_energyframeinbrnoaddition', 'calculatedbe06result_keyfigures_additiontoenergyframeduetomechanicalexhaust', 'calculatedbe06result_keyfigures_additiontoenergyframeduetospecialconditions', 'calculatedbe06result_keyfigures_totalenergyrequirement', 'calculatedbe06result_keyfigures_contributiontoenergyrequirementheating', 'calculatedbe06result_keyfigures_contributiontoenergyrequirementelectricity', 'calculatedbe06result_keyfigures_contributiontoenergyrequirementexcesstemprature']

# Zone_Results_
# Main groups
resultforallprofitableproposals = ['EnergyLabelClassification', 'FuelConsumption', 'CalculatedSolarCellUtilization', 'CalculatedBe18Result', 'CalculatedSBIResult', 'CalculatedBe15Result', 'CalculatedBe10Result', 'CalculatedBe06Result']


# Zone_Results_
# Main groups
resultforallproposals =['EnergyLabelClassification', 'FuelConsumption', 'CalculatedSolarCellUtilization', 'CalculatedBe18Result', 'CalculatedBe15Result', 'CalculatedBe10Result', 'CalculatedBe06Result']

# Main groups is 'Buildings
main_groups = ['Address', 'BBR', 'Zones']
main_groups_zones_zone = ['Statuses', 'ProposalGroups', 'BuildingUnits']

pre_tag = "EnergyLabel_InputData_Label_Buildings_Building"
tag = "Zones_Zone_BuildingUnits" #resultforallprofitableproposals[4]
sub_tags_to_main_group = "Status" # main_groups_zones_zone[1] # main_groups[2]

def create_first_list_of_main_groups():
    first_main_list = []
    first_main_list_with_values = []

    with open("testfiles/all_tags.json", "r") as file:
        data = json.load(file)
        for key in data:
            if (pre_tag + "_" + tag) in key:
                key = key.split(tag + "_")[1]
                if "_" not in key:
                    first_main_list_with_values.append(key)
                key = key.split("_")[0]
                if key not in first_main_list and key not in first_main_list_with_values:
                    print("Key1: ", key)
                    first_main_list.append(key)
        return first_main_list_with_values, first_main_list


def create_sub_tag_list_from_main_group():
    tag_list = [] 
    last_tag_list = []
    with open("testfiles/all_tags.json", "r") as file:
        data = json.load(file)
        try:
            for key in data:
                if (pre_tag + "_" + tag + "_" + sub_tags_to_main_group ) in key: #  
                    # print('Key: ', key)
                    key1 = key.split(pre_tag + "_" + tag + "_" + sub_tags_to_main_group + "_")[1] #   
                    tag_list.append(key1)
                    if "_" not in key1:
                        last_tag_list.append(key1)
                    
            for elem in tag_list:
                print(elem)
        except:
            print(key)
            pass
        return tag_list, last_tag_list 

tag_list = create_sub_tag_list_from_main_group()


def sorting_tag_list():
    sorted_tag_list = []
    for elem in tag_list:
        if "_" not in elem:
            sorted_tag_list.append(elem)
    return sorted_tag_list



foreign_key = "zones_zone_id_ref" 
foreign_key_table_id = "zonez_zone"


tag_list, last_tag_list = create_sub_tag_list_from_main_group()
print(last_tag_list)
#sorting_tag_list()

def create_table(ref_list):
    new_fields = []
    print("--")
    print("CREATE Table" + " " + '"' + tag.lower() + '_' + sub_tags_to_main_group.lower() + '"' + " " + "(")
    print('"' + foreign_key + '"' + " bigint,")
    print('"id"' + " SERIAL PRIMARY KEY,")
    for elem in ref_list:
        # elem = elem.split(tag)[0]
        elem = '"' + elem.lower() + '"' + " text,"
        print(elem)
        new_fields.append(elem)
    print(");")
    print("ALTER TABLE")
    print('"' + tag.lower() + '_' + sub_tags_to_main_group + '"')
    print("ADD")
    print("FOREIGN KEY " + "( " + '"' + foreign_key + '"' + " )" + " REFERENCES " + '"' + foreign_key_table_id + '"' + ' ("id");')
    print("--")

    return new_fields

sub_tag = sub_tags_to_main_group

def create_component():
    new_dict = []
    print("--")
    local_dict = tag.lower() + '_' + sub_tag.lower() + "_" + "dict"
    
    # Initialize dict
    print(local_dict + "=" + '{' + '}')
    
    # Loop over field names
    for elem in tag_list: # tag_list
        print(local_dict + '[' +'"' + elem + '"' + ']' + "= None")
    
    # Instantiate serial_id
    print(local_dict + '[' + '"' + foreign_key + '"' + ']' + "= serial_id")



    # print('"' + foreign_key + '"' + " bigint,")
    # print('"id"' + " SERIAL PRIMARY KEY,")
    # for elem in tag_list:
    #     # elem = elem.split(tag)[0]
    #     elem = '"' + elem + '"' + " text,"
    #     print(elem)
    #     new_fields.append(elem)
    # print(");")
    # print("ALTER TABLE")
    # print('"' + tag.lower() + '_' + sub_tags_to_main_group + '"')
    # print("ADD")
    # print("FOREIGN KEY " + "( " + '"' + foreign_key + '"' + " )" + " REFERENCES " + '"' + foreign_key_table_id + '"' + ' ("id");')
    # print("--")

    return new_dict




# help toe xtract columns

def print_copy_tags():
    counter = 0
    str_list = copy_tags.splitlines()	
    for elem in str_list:
        elem = str(elem.replace(": null", " text"))
        elem = elem.split("Status")[1].lower()
        contains = ("_").lower()
        if contains in elem:
            counter += 1
            elem = elem.split(contains)[1]	
            print(len(elem), elem)
        print( "Counter: ", counter)
        print(len(str_list))

# end

def create_dict_from_tag(wanted_tag) -> dict:
    tag_dict = {}
    with open(file_dir, "r") as file:
        data = json.load(file)
        for elem in data:
            if wanted_tag in elem:
                if elem is not None:
                    tag_dict[wanted_tag] = None
        return tag_dict


wanted_tag = "EnergyLabel_ResultData_ZoneResults_ZoneResult_"


# Create the main list of inter-connecting-tables
def create_zone_results_main_list():
    main_tables_list = []
    tags = create_list_from_tag(wanted_tag)
    for elem in tags:
        elem_name = elem.split(wanted_tag)[1]
        elem_name = elem_name.split('_')[0]
        if elem_name not in main_tables_list:
            main_tables_list.append(elem_name)
    return main_tables_list


def create_sub_list_from_main(main_list):
    sub_main_tables_list = []
    print(wanted_tag + main_list[0])

    sub_tags = create_list_from_tag(wanted_tag + main_list[0])
    #print(sub_tags)
    for elem in sub_tags:
        elem_name = elem.split(wanted_tag)[1]
        #elem_name = elem.split('_')[0]
        if elem_name not in sub_main_tables_list:
            sub_main_tables_list.append(elem_name)
    #return sub_main_tables_list



def create_sub_tables_dict_from_main(main_list) -> dict:
    sub_tables_dict = {}
    tag = wanted_tag + main_list[0]
    tags = create_list_from_tag(tag)
    print(tags[:5])



def create_zone_results_dict():
    zone_result_dict = {}
    tags = create_list_from_tag(wanted_tag)

    for elem in tags:
        elem_name = elem.split(wanted_tag)[1]
        zone_result_dict[elem_name] = None
    return zone_result_dict


def create_sub_tables_name_list(result_dict)->list:
    sub_tables_list = []
    for key in result_dict:
        table_name = key.split('_')[0]
        if table_name not in sub_tables_list:
            sub_tables_list.append(table_name)
    return sub_tables_list


def create_sub_tables_dict(create_sub_tables_name_list) -> list:
    sub_tags = []
    for elem in create_sub_tables_name_list:
        sub_tags.append(wanted_tag + elem + "_")
    list_of_sub_tables = []
    for elem in sub_tags:
        list_of_sub_tables.append(create_sub_result_dict(elem))
    return list_of_sub_tables
        

def create_parent_table():
    split_name_list = wanted_tag.split('_')
    table_name = split_name_list[len(split_name_list)-2]
    return table_name



def create_sub_result_dict(given_tag):
    sub_result_dict = {}
    tags = create_list_from_tag(given_tag)
    for elem in tags:
        elem_name = elem.split(given_tag)[1]
        sub_result_dict[elem_name] = None
    return sub_result_dict


string = """ "transmissionlossthroughenvelopeexcludingwindowsanddoors" text,
    "energyframe2010_energyframeinbrnoaddition" text,
    "energyframe2010_additiontoenergyframeduetospecialconditions" text,
    "energyframe2010_totalenergyrequirement" text,
    "energyframe2010_contributiontoenergyrequirementheating" text,
    "energyframe2010_contributiontoenergyrequirementelectricity" text,
    "energyframe2010_contributiontoenergyrequirementexcesstemprature" text,
    "energyframe2015_energyframeinbrnoaddition" text,
    "energyframe2015_additiontoenergyframeduetospecialconditions" text,
    "energyframe2015_totalenergyrequirement" text,
    "energyframe2015_contributiontoenergyrequirementheating" text,
    "energyframe2015_contributiontoenergyrequirementelectricity" text,
    "energyframe2015_contributiontoenergyrequirementexcesstemprature" text,
    "energyframe2020_energyframeinbrnoaddition" text,
    "energyframe2020_additiontoenergyframeduetospecialconditions" text,
    "energyframe2020_totalenergyrequirement" text,
    "energyframe2020_contributiontoenergyrequirementheating" text,
    "energyframe2020_contributiontoenergyrequirementelectricity" text,
    "energyframe2020_contributiontoenergyrequirementexcesstemprature" text,
    "energyframe2010_contributiontoenergyrequirementexcesstemperature" text,
    "energyframe2015_contributiontoenergyrequirementexcesstemperature" text,
    "energyframe2020_contributiontoenergyrequirementexcesstemperature" text"""


gumle = 'status_calculatedbe10result_keyfigures_dict'

def create_columns():
    #print(string)
    så = string.replace(",", "")
    der = så.replace("\n", "")
    nå = der.strip()
    x = nå.split("text")
    print(x)
    for elem in x:
        elem = elem.strip()
        print(gumle + "[" + elem + "]" + " = None")

