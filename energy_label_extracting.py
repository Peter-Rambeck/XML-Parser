from etree_helper import generic_extracting, generate_sql_insert, place_on_disk
from pprint import pprint

def parse_energy_label(content, esi, serial_id, logging, etree, cur, conn):
    energy_label_dict = {}
    energy_label_dict["SchemaVersion"] = None
    energy_label_dict["EnergyLabelType"] = {"BasedOn": None, "IncludesVAT": None, "IsMixedUsage": None, "IsNewBuild": None, "Usage": None}
    energy_label_dict["EnergyLabelSoftware"] = {"Name": None, "Version": None}
    energy_label_dict["CalculationSoftware"] = {"Name": None, "Version": None}
    energy_label_dict["Company"] = {"Name": None, "Number": None, "PhoneNumber": None, "Email": None, "Address": {"StreetName": None, "HouseNumber":None, "SideOrDoor": None, "PostalCode": None, "PostalCity": None, "StreetCode": None}}
    energy_label_dict["Consultant"] = {"ID": None, "Name": None, "Email": None}
    energy_label_dict["ValidFrom"] = None
    energy_label_dict["ValidTo"] = None
    energy_label_dict["Label"] = {
        "ReviewDate": None, "Ownership": None,
        "Comments": {
            "Additional": None, "BBRinformation": None, "CalculationHolidayCottage": None, "Conclusion": None,"General": None,"InaccessibleRooms": None,
            "MonthlyReading": None,"OnApartments": None,"OnBuildingDescription": None,"OnBuildingPermit": None,"OnConsumption": None,"OnDestructiveInspections": None,
            "OnEnergyFrame": None,"OnEnergyPrices": None,"OnHeatLoss": None,"OnInstallation": None,"OnInsulation": None,"Properties": None,"StatedVersusCalculatedConsumption": None,
            },
        "Address": {"Floor": None,"Name": None, "StreetName": None, "HouseNumber": None, "SideOrDoor": None, "PostalCode": None, "PostalCity": None, "StreetCode": None},
        "BBR": {"MunicipalityNumber": None, "PropertyNumber": None, "BFENumber": None},
        "Image": None
        }
    energy_label_dict["xml_id_ref"] = serial_id
    dict_local = generic_extracting(etree, energy_label_dict)
    
    #also the PDF file
    image = dict_local["Label"]["Image"]
    del dict_local["Label"]["Image"]
    place_on_disk(image)
    #from pprint import pprint
    #pprint(dict_local)
    generate_sql_insert("energylabel", dict_local, content, logging, esi, cur, conn, 'null')

def parse_energy_label_apartments(content, esi, serial_id, logging, etree, cur, conn):
    energy_label_dict = {}
    energy_label_dict["Label"] = {"Apartment": [{"Name": None, "Buildings": None, "Addresses": None, "AreaPerApartmentOfType": None, "NumberOfApartmentsOfType": None}]}
    dict_local = generic_extracting(etree, energy_label_dict)
    #from pprint import pprint
    #pprint(dict_local)
    for s in energy_label_dict["Label"]["Apartment"]:
        s["xml_id_ref"] = serial_id
        generate_sql_insert("energy_label_apartments", s, content, logging, esi, cur, conn, 'null')


