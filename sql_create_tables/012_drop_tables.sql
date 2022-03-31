BEGIN;
    drop schema if exists test1 cascade;
    create schema if not exists test1;


CREATE TABLE "xmldoc" (
  "id" SERIAL PRIMARY KEY,
  "energylabel_serial_identifier" bigint,
  "xml_name" text NOT NULL,
  "xml_insert_time" timestamp
);

/*---------------------------------------------------------------*/
/*ResultData*/

/*EnergyLabel_ResultData_LabelResults*/
CREATE TABLE "resultdata_labelresults" (
  "xml_id_ref" bigint,
  "id" SERIAL PRIMARY KEY,
  "adjustedreportedconsumptions" text,
  "status_energylabelclassification" text,
);
ALTER TABLE "resultdata_labelresults" ADD FOREIGN KEY ("xml_id_ref") REFERENCES "xmldoc" ("id");


/*EnergyLabel_ResultData_LabelResults_Status_FuelConsumption*/
CREATE TABLE "labelresults_status_fuelconsumption"(
  "resultdata_labelresults_id_ref" bigint
  "id" SERIAL PRIMARY KEY,
  "material" text,
  "unit" text,
  "energyperunit" text,
  "co2perunit" text,
  "costperunit" text,
  "fixedcostperyear" text,
  "suppliercompanyname" text,
  "fuelconsumption" text,
  "isforheating" text
)

/*EnergyLabel_ResultData_LabelResults_Apartments*/
CREATE TABLE "labelresults_apartment" (
  "id" SERIAL PRIMARY KEY,
  "labelresults_id_ref" bigint,
  "costforheatingperapartment" text
);
ALTER TABLE "labelresults_apartment" ADD FOREIGN KEY ("labelresults_id_ref") REFERENCES "resultdata_labelresults" ("id");

/*EnergyLabel_ResultData_LabelResults_ResultForAllProposals*/
CREATE TABLE "labelresults_resultforallproposals"(
  "xml_id_ref" bigint,
  "id" SERIAL PRIMARY KEY,
  "energylabelclassification" text,
  "material" text,
  "unit" text,
  "energyperunit" text,
  "co2perunit" text,
  "costperunit" text,
  "fixedcostperyear" text,
  "suppliercompanyname" text,
  "fuelconsumption" text,
  "isforheating" text
);
ALTER TABLE "labelresults_resultforallproposals" ADD FOREIGN KEY ("xml_id_ref") REFERENCES "xmldoc" ("id");


/*EnergyLabel_ResultData_LabelResults_ResultsForEachProposalGroup_ProposalGroupResult*/
CREATE TABLE "labelresults_rfepg_proposalgroupresult" (
  "labelresults_id_ref" bigint,
  "id" SERIAL PRIMARY KEY,
  "attribute_id" text,
  "profitability" text,
  "category" text,
  "investment" text,
  "investmentLifetime" text
);
ALTER TABLE "labelresults_rfepg_proposalgroupresult" ADD FOREIGN KEY ("labelresults_id_ref") REFERENCES "resultdata_labelresults" ("id");


/*EnergyLabel_ResultData_LabelResults_ResultsForEachProposalGroup_ProposalGroupResult_FuelSavings*/
CREATE TABLE "proposalgroupresult_fuelsavings" (
  "id" SERIAL PRIMARY KEY,
  "proposalgroupresult_id_ref" bigint,
  "material" text,
  "unit" text,
  "energyperunit" text,
  "co2perunit" text,
  "costperunit" text,
  "fixedcostperyear" text,
  "suppliercompanyname" text,
  "fuelsaved" text
);
ALTER TABLE "proposalgroupresult_fuelsavings" ADD FOREIGN KEY ("proposalgroupresult_id_ref") REFERENCES "labelresults_rfepg_proposalgroupresult" ("id");

/*EnergyLabel_ResultData_LabelResults_ResultForAllProfitableProposals*/
CREATE TABLE "labelresults_rfapp"(
  "xml_id_ref" bigint,
  "id" SERIAL PRIMARY KEY,
  "energylabelclassification" text,
  "material" text,
  "unit" text,
  "energyperunit" text,
  "co2perunit" text,
  "costperunit" text,
  "fixedcostperyear" text,
  "suppliercompanyname" text,
  "fuelconsumption" text,
  "isforheating" text
);
ALTER TABLE "labelresults_rfapp" ADD FOREIGN KEY ("xml_id_ref") REFERENCES "xmldoc" ("id");


/*EnergyLabel_ResultData_LabelResults_ResultForAllProfitableProposals_ProposalResult*/
CREATE TABLE "labelresults_rfapp_proposalresult"(
  "id" SERIAL PRIMARY KEY,
  "rfapp_id_ref" bigint,
  "profitability" text,
  "category" text,
  "investment" text
);
ALTER TABLE "labelresults_rfapp_proposalresult" ADD FOREIGN KEY ("rfapp_id_ref") REFERENCES "labelresults_rfapp" ("id");

/*EnergyLabel_ResultData_LabelResults_ResultForAllProfitableProposals_ProposalResult_FuelSavings*/
CREATE TABLE "rfapp_proposalresult_fuelsavings" (
  "id" SERIAL PRIMARY KEY,
  "rfapp_proposalresult_id_ref" bigint,
  "material" text,
  "unit" text,
  "energyperunit" text,
  "co2perunit" text,
  "costperunit" text,
  "fixedcostperyear" text,
  "suppliercompanyname" text,
  "fuelsaved" text
);
ALTER TABLE "rfapp_proposalresult_fuelsavings" ADD FOREIGN KEY ("rfapp_proposalresult_id_ref") REFERENCES "labelresults_rfapp_proposalresult" ("id");

/*---------------------------------------------------------------*/
/*Inputdata*/
CREATE TABLE "inputdata_label" (
  "xml_id_ref" bigint,
  "id" SERIAL PRIMARY KEY,
  "bbr_municipalitynumber" text,
  "bbr_propertynumber" text,
  "reviewdate" text,
  "ownership" text,
  "bbr_bfenumber" text,
  "owner_name" text,
  "realestatebroker_name" text,
  "realestatebroker_address_streetname" text,
  "realestatebroker_address_housenumber" text,
  "realestatebroker_address_postalcode" text,
  "realestatebroker_address_postalcity" text,
  "realestatebroker_phonenumber" text,
  "realestatebroker_email" text,
  "administrator_name" text,
  "administrator_address_streetname" text,
  "administrator_address_housenumber" text,
  "administrator_address_postalcode" text,
  "administrator_address_postalcity" text,
  "administrator_phonenumber" text
);

CREATE TABLE "energylabel" (
  "xml_id_ref" bigint,
  "id" SERIAL PRIMARY KEY,
  "schemaversion" text,
  "energylabeltype_basedon" text,
  "energylabeltype_usage" text,
  "energylabeltype_isnewbuild" text,
  "energylabeltype_includesvat" text,
  "energylabeltype_ismixedusage" text,
  "energylabelsoftware_name" text,
  "energylabelsoftware_version" text,
  "calculationsoftware_name" text,
  "calculationsoftware_version" text,
  "company_name" text,
  "company_number" text,
  "company_email" text,
  "company_phonenumber" text,
  "company_address_streetname" text,
  "company_address_housenumber" text,
  "company_address_sideordoor" text,
  "company_address_postalcode" text,
  "company_address_postalcity" text,
  "company_address_streetcode" text,
  "validfrom" text,
  "validto" text,
  "consultant_id" text,
  "consultant_name" text,
  "consultant_email" text,
  "image_upload_time" timestamp,
  "pdf_upload_time" timestamp
);
ALTER TABLE "energylabel" ADD FOREIGN KEY ("xml_id_ref") REFERENCES "xmldoc" ("id");

CREATE TABLE "resultdata_buildingresult" (
  "xml_id_ref" bigint,
  "energylabelclassification" text,
  "status_energylabelclassification" text,
  "resultforallproposals_energylabelclassification" text,
  "resultforallprofitableproposals_energylabelclassification" text,
  "material" text,
  "unit" text,
  "energyperunit" text,
  "co2perunit" text,
  "costperunit" text,
  "fixedcostperyear" text,
  "suppliercompanyname" text,
  "fuelconsumption" text,
  "isforheating" text,
  "profitability" text,
  "category" text,
  "investment" text,
  "investmentlifetime" text,
  "fuelsaved" text,
  "apartments" text,
  "adjustedreportedconsumptions" text,
  "adjustedloggedconsumptions" text,
  "resultsforeachproposalgroup" text,
  "fuelsavings" text,
  "costforheatingperapartment" text,
  "fuelconsumptionpryear" text
);

/*obs. inputdata*/
CREATE TABLE "energylabel_apartments" (
  "xml_id_ref" bigint,
  "name" text,
  "buildings" text,
  "addresses" text,
  "areaperapartmentoftype" text,
  "numberofapartmentsoftype" text
);

CREATE TABLE "buildings" (
  "xml_serial_id" bigint,
  "building_track_id" SERIAL PRIMARY KEY,
  "address_name" text,
  "address_streetname" text,
  "address_housenumber" text,
  "address_floor" text,
  "address_sideordoor" text,
  "address_postalcode" text,
  "address_postalcity" text,
  "address_streetcode" text,
  "bbr_buildingnumber" text,
  "bbr_usecode" text,
  "bbr_yearofconstruction" text,
  "bbr_dwellingarea" text,
  "bbr_commercialarea" text,
  "istenancy" text,
  "reportedconsumptions" text,
  "loggedconsumptions" text,
  "yearofrenovation" text
);

CREATE TABLE "building_zones" (
  "building_ref_id" bigint,
  "zone_track_id" SERIAL PRIMARY KEY,
  "id" text,
  "name" text,
  "usage" text,
  "subtractwindowareafromouterwalls" text,
  "bbrusecode" text,
  "buildingtype" text,
  "housingunits" text,
  "floorcount" text,
  "height" text,
  "usagedays" text,
  "usagefrom" text,
  "usageto" text,
  "totalheatedfloorarea" text,
  "topfloorareaofheatedfloorarea" text,
  "basementareaofheatedfloorarea" text,
  "unheatedbasementarea" text,
  "heatcapacity" text,
  "rotation" text,
  "additiontoenergyframe" text,
  "setpointheatedtemperature" text,
  "setpointwantedtemperature" text,
  "setpointnaturalventilationtemperature" text,
  "setpointcoolingtemperature" text,
  "setpointstoretemperature" text,
  "dimensioningroomtemperature" text,
  "dimensioningoutertemperature" text,
  "dimensioningstoretemperature" text,
  "electricitypriceforheating" text,
  "electricitypricefornonheating" text,
  "electricitypriceforexcessproduction" text,
  "yearlyfeeforexcessproductionofelectricity" text,
  "estimatedelectricityconsumptionfornonheating" text,
  "sunburdenedrooms" text,
  "heateddwellingarea" text,
  "heatedcommercialarea" text,
  "electricityprice" text,
  "waterprice" text,
  "electricityforheatingprice" text,
  "electricityfornonheatingprice" text,
  "otherheatedbasementarea" text
);

CREATE TABLE "zone_statuses" (
  "zone_ref_id" bigint,
  "status_track_id" SERIAL PRIMARY KEY,
  "status_id" text,
  "shorttext" text,
  "longtext" text,
  "isbasedonseebstandardbuilding" text,
  "seebclassification" text,
  "biclassification" text
);

CREATE TABLE "proposalgroups" (
  "proposalgroups_serial_id" SERIAL PRIMARY KEY,
  "building_zone_ref" bigint,
  "proposal_group_id" text,
  "shorttext" text,
  "longtext" text,
  "is_investment_overridden" text,
  "proposal_group_category" text,
  "proposal_group_s_e_e_b_classification" text,
  "proposal_group_proposal_reference_id" text,
  "biclassification" text
);

CREATE TABLE "status_building_units" (
  "status_ref_id" bigint,
  "building_unit_track_id" SERIAL PRIMARY KEY,
  "building_unit_qnumber" text,
  "area" text,
  "usagefactor" text,
  "natural_ventilation_winter" text,
  "natural_ventilation_summer" text,
  "natural_ventilation_summer_sideusaghrs" text,
  "mechanical_ventilation_winter" text,
  "mechanical_ventilation_summer" text,
  "mechanical_ventilation_summer_sideusaghrs" text,
  "infiltration_side_usaghrs" text,
  "temperature_efficiency" text,
  "injection_temperature" text,
  "special_powerusage" text,
  "has_heat_coils" text,
  "ventilation_system_number" text,
  "numberof_windows" text,
  "orientation" text,
  "inclination" text,
  "glassshare" text,
  "solarheat_transmittance" text,
  "solar_screening" text,
  "outer_wall_id" text,
  "short_text" text,
  "horizon" text,
  "eaves" text,
  "shade_left" text,
  "shade_right" text,
  "window_hole" text,
  "uvalue" text,
  "bfactor" text,
  "dimensioningoutertemperature" text,
  "dimensioninginnertemperature" text,
  "stove_isprimary" text,
  "stove_fuel_material" text,
  "stove_fuel_unit" text,
  "stove_fuel_energyperunit" text,
  "stove_fuel_co2perunit" text,
  "stove_fuelprice_costperunit" text,
  "stove_fuelprice_fixedcostperyear" text,
  "stove_fuelprice_suppliercompanyname" text,
  "stove_shareoffloorarea" text,
  "stove_efficiency" text,
  "stove_airflowrequirement" text
);

CREATE TABLE "proposals" (
  "id" SERIAL PRIMARY KEY,
  "proposal_ref" bigint,
  "proposal_ref_group" bigint,
  "proposal_ID" text,
  "shorttext" text,
  "longtext" text,
  "lifetime" text,
  "investment" text,
  "proposetoteardown" text,
  "seebclassification" text,
  "biclassification" text
);

/* EnergyLabel_InputData_Label_ProposalGroups_ProposalGroup */
CREATE TABLE "inputdata_proposalgroups" (
  "id" SERIAL PRIMARY KEY,
  "inputdata_label_id_ref" bigint,
  "shorttext" text,
  "longtext" text,
  "investment" text,
  "isinvestmentoverridden" text,
  "seebclassification" text,
  "isrecommended" text,
  "biclassification" text,
  "implementationreferencetext" text,
  "implementationreferencelink" text,
  "renovationtime" text,
  "alternativeimplementationtext" text,
  "attribute_id" text
);

/* EnergyLabel_InputData_Label_ProposalGroups_ProposalGroup_ProposalReferences_ProposalReference */
CREATE TABLE "inputdata_proposalreferences"(
"id" SERIAL PRIMARY KEY,
"inputdata_proposalgroups_serial_id_ref" bigint,
"attribute_proposalid" text
);


CREATE TABLE "run_logger" (
  "id" SERIAL PRIMARY KEY,
  "run_id" integer NOT NULL,
  "energylabel_serial_identifier" bigint,
  "log_level" integer NOT NULL,
  "log_leveltext" varchar NOT NULL,
  "message" varchar NOT NULL,
  "created_on" timestamp
);


ALTER TABLE "inputdata_label" ADD FOREIGN KEY ("xml_id_ref") REFERENCES "xmldoc" ("id");

ALTER TABLE "resultdata_buildingresult" ADD FOREIGN KEY ("xml_id_ref") REFERENCES "xmldoc" ("id");



ALTER TABLE "buildings" ADD FOREIGN KEY ("xml_serial_id") REFERENCES "xmldoc" ("id");

ALTER TABLE "building_zones" ADD FOREIGN KEY ("building_ref_id") REFERENCES "buildings" ("building_track_id");

ALTER TABLE "zone_statuses" ADD FOREIGN KEY ("zone_ref_id") REFERENCES "building_zones" ("zone_track_id");

ALTER TABLE "proposalgroups" ADD FOREIGN KEY ("building_zone_ref") REFERENCES "building_zones" ("zone_track_id");

ALTER TABLE "status_building_units" ADD FOREIGN KEY ("status_ref_id") REFERENCES "zone_statuses" ("status_track_id");

ALTER TABLE "proposals" ADD FOREIGN KEY ("proposal_ref") REFERENCES "zone_statuses" ("status_track_id");

ALTER TABLE "proposals" ADD FOREIGN KEY ("proposal_ref_group") REFERENCES "proposalgroups" ("proposalgroups_serial_id");

ALTER TABLE "energylabel_apartments" ADD FOREIGN KEY ("xml_id_ref") REFERENCES "xmldoc" ("id");

ALTER TABLE "inputdata_proposalgroups" ADD FOREIGN KEY ("inputdata_label_id_ref") REFERENCES "inputdata_label" ("id");

ALTER TABLE "inputdata_proposalreferences" ADD FOREIGN KEY ("inputdata_proposalgroups_serial_id_ref") REFERENCES "inputdata_proposalgroups" ("id");

CREATE INDEX ON "run_logger" ("id");

CREATE INDEX ON "run_logger" ("energylabel_serial_identifier");

    COMMIT;