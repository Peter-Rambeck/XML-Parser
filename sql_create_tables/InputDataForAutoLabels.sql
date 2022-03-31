/* FB says (11/03): still need to decide how to handle references, xml_id_ref in everything acts as placeholder for now*/
/* FB says (14/03): The attribute id comes from the building tag, not from either address or bbr tag. Will need to handle.*/

/* EnergyLabel_InputDataForAutoLabels_Label_Address */
CREATE TABLE "inputdata_f_autolabels_address"(
    "id" SERIAL PRIMARY KEY,
    "xml_id_ref" bigint,
    "name" text,
    "streetname" text,
    "housenumber" text,
    "floor" text,
    "sideordoor" text,
    "postalcode" text,
    "postalcity" text,
    "streetcode" text
);
ALTER TABLE "inputdata_f_autolabels_address" ADD FOREIGN KEY ("xml_id_ref") REFERENCES "xmldoc" ("id");

/* EnergyLabel_InputDataForAutoLabels_Label_BBR */
CREATE TABLE "inputdata_f_autolabels_bbr"(
    "id" SERIAL PRIMARY KEY,
    "xml_id_ref" bigint,
    "municipalitynumber" text,
    "propertynumber" text,
    "bfenumber" text
);
ALTER TABLE "inputdata_f_autolabels_bbr" ADD FOREIGN KEY ("xml_id_ref") REFERENCES "xmldoc" ("id");

/* Reference middle table in case there are multiple addresses or BBR entries */
/* EnergyLabel_InputDataForAutoLabels_Label_Buildings */
CREATE TABLE "inputdata_f_autolabels_buildings"(
    "id" SERIAL PRIMARY KEY,
    "xml_id_ref" bigint,
    "attribute_id" text
);
ALTER TABLE "inputdata_f_autolabels_buildings" ADD FOREIGN KEY ("xml_id_ref") REFERENCES "xmldoc" ("id");

/* EnergyLabel_InputDataForAutoLabels_Label_Buildings_Building_Address */
CREATE TABLE "inputdata_f_autolabels_building_address"(
    "id" SERIAL PRIMARY KEY,
    "autolabel_building_id_ref" bigint,
    "name" text,
    "streetname" text,
    "housenumber" text,
    "floor" text,
    "sideordoor" text,
    "postalcode" text,
    "postalcity" text,
    "streetcode" text
);
ALTER TABLE "inputdata_f_autolabels_building_address" ADD FOREIGN KEY ("autolabel_building_id_ref") REFERENCES "inputdata_f_autolabels_building" ("id");

/* EnergyLabel_InputDataForAutoLabels_Label_Buildings_Building_BBR */
CREATE TABLE "inputdata_f_autolabels_building_bbr"(
    "id" SERIAL PRIMARY KEY,
    "autolabel_building_id_ref" bigint,
    "buildingnumber" text,
    "usecode" text,
    "yearofconstruction" text,
    "dwellingarea" text,
    "commercialarea" text,
    "yearofrenovation" text
);
ALTER TABLE "inputdata_f_autolabels_building_bbr" ADD FOREIGN KEY ("autolabel_building_id_ref") REFERENCES "inputdata_f_autolabels_building" ("id");