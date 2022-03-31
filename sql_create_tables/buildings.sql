set
    search_path = test1;

CREATE Table "building" (
    "xml_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "attribute_building_id" text,
    "istenancy" text,
    "reportedconsumptions" text,
    "loggedconsumptions" text,
    "buildingregulation" text,
    "buildingregulationdate" text,
    "energypermitenergydemand" text,
    "br08buildingpermitclassification" text,
    "br18buildingpermitclassification" text,
    "br10buildingpermitclassification" text,
    "br15buildingpermitclassification" text
);

ALTER TABLE
    "building"
ADD
    FOREIGN KEY ("xml_id_ref") REFERENCES "xmldoc" ("id");

CREATE Table "building_address" (
    "building_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "name" text,
    "streetname" text,
    "housenumber" text,
    "floor" text,
    "sideordoor" text,
    "postalcode" text,
    "postalcity" text,
    "streetcode" text
);

ALTER TABLE
    "building_address"
ADD
    FOREIGN KEY ("building_id_ref") REFERENCES "building" ("id");

CREATE Table "bbr" (
    "building_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "buildingnumber" text,
    "usecode" text,
    "yearofconstruction" text,
    "dwellingarea" text,
    "commercialarea" text,
    "yearofrenovation" text
);

ALTER TABLE
    "bbr"
ADD
    FOREIGN KEY ("building_id_ref") REFERENCES "building" ("id");

CREATE Table "zones_zone" (
    "building_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
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
    "otherheatedbasementarea" text,
    "proposalgroups" text,
    "builtuparea" text,
    "buildingunits" text
);

ALTER TABLE
    "zones_zone"
ADD
    FOREIGN KEY ("building_id_ref") REFERENCES "building" ("id");

CREATE Table "buildingunits_status" (
    "zones_zone_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "shorttext" text,
    "longtext" text,
    "isbasedonseebstandardbuilding" text,
    "seebclassification" text,
    "proposals" text
);

ALTER TABLE
    "buildingunits_status"
ADD
    FOREIGN KEY ("zones_zone_id_ref") REFERENCES "zones_zone" ("id");