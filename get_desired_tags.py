import json
from utils import get_connection
from pprint import pprint

def get_tags(tag_desired, num_underscores=4, unddesired_tags=[]):
    count = 0
    name_dt = {}
    with open("testfiles/all_tags.json") as d:
        data = json.load(d)

    #and 'ResultForAllProposals' not in key and 'EnergyLabelSoftwareSpecificData' not in key and 'InputDataForAutoLabels' not in key
    for key in data.keys():
        if tag_desired in key and 'PDFReportData' not in key and 'InputData' not in key and 'EnergyLabelSoftwareSpecificData' not in key and 'InputDataForAutoLabels' not in key and key.count('_') <= num_underscores:       
            print(key)
            #print("\""+key.split("_",3)[-1].lower()+ "\"" + " text" )    
            count +=1   

            #key_list = key.split('_')
            #key_list = [key.lower() for key in key_list]
            #if key_list[-2] != 'resultdata':
                #name_dt['_'.join(key_list[-2:])] = 'text'
            #else: name_dt[key_list[-1]] = 'text'
    print(count)
    print("end")
    #pprint(name_dt)
    #return name_dt

def get_tags2(tag_desired, num_underscores=4, unddesired_tags=[]):
    count = 0
    name_dt = {}
    with open("testfiles/all_tags.json") as d:
        data = json.load(d)
    for key in data.keys():
        if tag_desired in key and 'PDFReportData' not in key  and 'InputData' not in key and key.count('_') <= num_underscores:   
            if key.split('_')[3].endswith('s') and key.split('_')[3] != 'Status':pass 
            else: 
                print(key)
                #print("\""+key.split("_",3)[-1].lower()+ "\"" + " text" )    
                count +=1   
   
            #key_list = key.split('_')
            #key_list = [key.lower() for key in key_list]
            #if key_list[-2] != 'resultdata':
                #name_dt['_'.join(key_list[-2:])] = 'text'
            #else: name_dt[key_list[-1]] = 'text'
    print(count)
    print("end")
    #pprint(name_dt)
    #return name_dt


    
## så vi ikke roder i den samme ;)
def get_count(tag_desired):
    name_dt = {}
    with open("xml_schema_val.json") as d:
        data = json.load(d)
    for key in data.keys():
        if key.count('_') <= 10 and tag_desired in key and 'ResultData' not in key and 'PDFReportData' not in key and list(key)[-1] != 's':
            print(key)
            key = key.split('_')[-1]
            name_dt[key.lower()] = 'text'
    return name_dt




def create_table(tag):
    name_dt = get_tags(tag)
    print(len(name_dt))
    pprint(name_dt)
    with get_connection() as conn:
        with conn.cursor() as cursor:

            sql_statement = ["create table test ("]

            for key, value in name_dt.items():
                sql_statement.append(f'{key} {value},')
            sql_statement.append(');')
            
            print("".join(sql_statement))

