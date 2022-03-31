import json
import os

file_dir = '../ciw_test/xml_schema_val.json'

# Main focus is returning a list of tags derived from the wanted tag.
def create_list_from_tag(wanted_tag) -> list:
    tag_list = []
    with open(file_dir, "r") as file:
        data = json.load(file)
        for key in data:
            if wanted_tag in key:
                tag_list.append(key)

        #file_text.close()
        return tag_list


'''
# Main focus is returning a list of tags derived from the wanted tag.
def create_list_from_tag(wanted_tag, file_name) -> list:
    tag_list = []
    with open(file_dir, "r") as file:
        data = json.load(file)
        for key in data:
            if wanted_tag in key:
                tag_list.append(key)

        # Also write the list to a file for manual inspection.
        for elem in tag_list:
            if not os.path.exists(file_name):
                file_text = open(file_name, "w+")
            else:
                file_text = open(file_name, "a+") 
            file_text.write('%s\n'  %(elem))

        #file_text.close()
        return tag_list
'''