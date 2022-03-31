#set
#search_path = test1;
#CREATE TABLE "xmldoc" ("id" SERIAL PRIMARY KEY);
# Start: ZoneResult_Status
CREATE Table "zone_result_status" (
    "xml_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "calculatedsolarcellutilization_solarcellshare" text,
    "calculatedsolarcellutilization_totalutilizationpercent" text,
    "energylabelclassification" text
);

ALTER TABLE
    "zone_result_status"
ADD
    FOREIGN KEY ("xml_id_ref") REFERENCES "xmldoc" ("id");

CREATE Table "status_fuelconsumption" (
    "zone_result_status_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "fuel_material" text,
    "fuel_unit" text,
    "fuel_energyperunit" text,
    "fuel_co2perunit" text,
    "fuelprice_costperunit" text,
    "fuelprice_fixedcostperyear" text,
    "fuelconsumption" text,
    "isforheating" text
);

ALTER TABLE
    "status_fuelconsumption"
ADD
    FOREIGN KEY ("zone_result_status_id_ref") REFERENCES "zone_result_status" ("id");

CREATE Table "status_calculatedsbiresults_resultfigures" (
    "zone_result_status_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "heatingrequirementforcentralheating" text,
    "heatingrequirementforstoves" text,
    "heatingrequirementforcentralheatingdegreedayindependent" text,
    "electricityrequirementforheating" text,
    "electricityrequirementfornonheating" text,
    "electricityrequirementforlighting" text,
    "electricityrequirementforventilation" text,
    "electricityrequirementforheatpump" text,
    "electricityrequirementforpumps" text,
    "heatpumpheatingtotalperformance" text,
    "solarheatingplantheatingtotalperformance" text,
    "solarcellstotalperformance" text,
    "fulfilmentheatinghotwater" text,
    "fulfilmentelectricityhotwater" text,
    "boilerefficiency" text
);

ALTER TABLE
    "status_calculatedsbiresults_resultfigures"
ADD
    FOREIGN KEY ("zone_result_status_id_ref") REFERENCES "zone_result_status" ("id");

CREATE Table "status_calculatedsbiresults_keyfigures" (
    "zone_result_status_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "transmissionlossthroughenvelopeexcludingwindowsanddoors" text,
    "energyframeinbrnoaddition" text,
    "additiontoenergyframeduetomechanicalexhaust" text,
    "additiontoenergyframeduetospecialconditions" text,
    "totalenergyrequirement" text,
    "contributiontoenergyrequirementheating" text,
    "contributiontoenergyrequirementelectricity" text,
    "contributiontoenergyrequirementexcesstemprature" text
);

ALTER TABLE
    "status_calculatedsbiresults_keyfigures"
ADD
    FOREIGN KEY ("zone_result_status_id_ref") REFERENCES "zone_result_status" ("id");

CREATE Table "status_calculatedbe15result_keyfigures" (
    "zone_result_status_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "transmissionlossthroughenvelopeexcludingwindowsanddoors" text,
    "renovationclass2_energyframeinbrnoaddition" text,
    "renovationclass2_additiontoenergyframeduetospecialconditions" text,
    "renovationclass2_totalenergyrequirement" text,
    "renovationclass2_contributiontoenergyrequirementheating" text,
    "renovationclass1_energyframeinbrnoaddition" text,
    "renovationclass1_additiontoenergyframeduetospecialconditions" text,
    "renovationclass1_totalenergyrequirement" text,
    "renovationclass1_contributiontoenergyrequirementheating" text,
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
    "energyframe2015_contributiontoenergyrequirementexcesstemperature" text,
    "energyframe2020_contributiontoenergyrequirementexcesstemperature" text
);

ALTER TABLE
    "status_calculatedbe15result_keyfigures"
ADD
    FOREIGN KEY ("zone_result_status_id_ref") REFERENCES "zone_result_status" ("id");

CREATE Table "status_calculatedbe15result_resultfigures" (
    "zone_result_status_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "heatingrequirementforcentralheating" text,
    "heatingrequirementforstoves" text,
    "heatingrequirementforcentralheatingdegreedayindependent" text,
    "electricityrequirementforheating" text,
    "electricityrequirementfornonheating" text,
    "electricityrequirementforlighting" text,
    "electricityrequirementforventilation" text,
    "electricityrequirementforheatpump" text,
    "electricityrequirementforpumps" text,
    "heatpumpheatingtotalperformance" text,
    "solarheatingplantheatingtotalperformance" text,
    "solarcellstotalperformance" text,
    "windmillstotalperformance" text,
    "fulfilmentheatinghotwater" text,
    "fulfilmentelectricityhotwater" text,
    "boilerefficiency" text
);

ALTER TABLE
    "status_calculatedbe15result_resultfigures"
ADD
    FOREIGN KEY ("zone_result_status_id_ref") REFERENCES "zone_result_status" ("id");

CREATE Table "status_calculatedbe18result_resultfigures" (
    "zone_result_status_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "heatingrequirementforcentralheating" text,
    "heatingrequirementforstoves" text,
    "heatingrequirementforcentralheatingdegreedayindependent" text,
    "electricityrequirementforheating" text,
    "electricityrequirementfornonheating" text,
    "electricityrequirementforlighting" text,
    "electricityrequirementforventilation" text,
    "electricityrequirementforheatpump" text,
    "electricityrequirementforpumps" text,
    "heatpumpheatingtotalperformance" text,
    "solarheatingplantheatingtotalperformance" text,
    "solarcellstotalperformance" text,
    "windmillstotalperformance" text,
    "fulfilmentheatinghotwater" text,
    "fulfilmentelectricityhotwater" text,
    "boilerefficiency" text
);

ALTER TABLE
    "status_calculatedbe18result_resultfigures"
ADD
    FOREIGN KEY ("zone_result_status_id_ref") REFERENCES "zone_result_status" ("id");

CREATE Table "status_calculatedbe18result_keyfigures" (
    "zone_result_status_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "transmissionlossthroughenvelopeexcludingwindowsanddoors" text,
    "renovationclass2_energyframeinbrnoaddition" text,
    "renovationclass2_additiontoenergyframeduetospecialconditions" text,
    "renovationclass2_totalenergyrequirement" text,
    "renovationclass2_contributiontoenergyrequirementheating" text,
    "renovationclass1_energyframeinbrnoaddition" text,
    "renovationclass1_additiontoenergyframeduetospecialconditions" text,
    "renovationclass1_totalenergyrequirement" text,
    "renovationclass1_contributiontoenergyrequirementheating" text,
    "energyframe2018_energyframeinbrnoaddition" text
);

ALTER TABLE
    "status_calculatedbe18result_keyfigures"
ADD
    FOREIGN KEY ("zone_result_status_id_ref") REFERENCES "zone_result_status" ("id");

CREATE Table "status_calculatedbe10result_resultfigures" (
    "zone_result_status_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "heatingrequirementforcentralheating" text,
    "heatingrequirementforstoves" text,
    "heatingrequirementforcentralheatingdegreedayindependent" text,
    "electricityrequirementforheating" text,
    "electricityrequirementfornonheating" text,
    "electricityrequirementforlighting" text,
    "electricityrequirementforventilation" text,
    "electricityrequirementforheatpump" text,
    "electricityrequirementforpumps" text,
    "heatpumpheatingtotalperformance" text,
    "solarheatingplantheatingtotalperformance" text,
    "solarcellstotalperformance" text,
    "windmillstotalperformance" text,
    "fulfilmentheatinghotwater" text,
    "fulfilmentelectricityhotwater" text,
    "boilerefficiency" text
);

ALTER TABLE
    "status_calculatedbe10result_resultfigures"
ADD
    FOREIGN KEY ("zone_result_status_id_ref") REFERENCES "zone_result_status" ("id");

CREATE Table "status_calculatedbe10result_keyfigures" (
    "zone_result_status_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "transmissionlossthroughenvelopeexcludingwindowsanddoors" text,
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
    "energyframe2020_contributiontoenergyrequirementexcesstemperature" text
);

ALTER TABLE
    "status_calculatedbe10result_keyfigures"
ADD
    FOREIGN KEY ("zone_result_status_id_ref") REFERENCES "zone_result_status" ("id");

CREATE Table "status_calculatedbe06result_resultfigures" (
    "zone_result_status_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "heatingrequirementforcentralheating" text,
    "heatingrequirementforstoves" text,
    "heatingrequirementforcentralheatingdegreedayindependent" text,
    "electricityrequirementforheating" text,
    "electricityrequirementfornonheating" text,
    "electricityrequirementforlighting" text,
    "electricityrequirementforventilation" text,
    "electricityrequirementforheatpump" text,
    "electricityrequirementforpumps" text,
    "heatpumpheatingtotalperformance" text,
    "solarheatingplantheatingtotalperformance" text,
    "solarcellstotalperformance" text,
    "fulfilmentheatinghotwater" text,
    "fulfilmentelectricityhotwater" text,
    "boilerefficiency" text
);

ALTER TABLE
    "status_calculatedbe06result_resultfigures"
ADD
    FOREIGN KEY ("zone_result_status_id_ref") REFERENCES "zone_result_status" ("id");

CREATE Table "status_calculatedbe06result_keyfigures" (
    "zone_result_status_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "transmissionlossthroughenvelopeexcludingwindowsanddoors" text,
    "energyframeinbrnoaddition" text,
    "additiontoenergyframeduetomechanicalexhaust" text,
    "additiontoenergyframeduetospecialconditions" text,
    "totalenergyrequirement" text,
    "contributiontoenergyrequirementheating" text,
    "contributiontoenergyrequirementelectricity" text,
    "contributiontoenergyrequirementexcesstemprature" text
);

ALTER TABLE
    "status_calculatedbe06result_keyfigures"
ADD
    FOREIGN KEY ("zone_result_status_id_ref") REFERENCES "zone_result_status" ("id");

# End: ZoneResult_Status
# Start: ZoneResult_ResultForAllProfitableProposals
CREATE Table "zone_result_resultforallprofitableproposals" (
    "xml_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "energylabelclassification" text
);

ALTER TABLE
    "zone_result_resultforallprofitableproposals"
ADD
    FOREIGN KEY ("xml_id_ref") REFERENCES "xmldoc" ("id");

CREATE Table "result_f_a_p_proposals_calculatedbe06result_resultfigures" (
    "zone_result_resultforallprofitableproposals_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "heatingrequirementforcentralheating" text,
    "heatingrequirementforstoves" text,
    "heatingrequirementforcentralheatingdegreedayindependent" text,
    "electricityrequirementforheating" text,
    "electricityrequirementfornonheating" text,
    "electricityrequirementforlighting" text,
    "electricityrequirementforventilation" text,
    "electricityrequirementforheatpump" text,
    "electricityrequirementforpumps" text,
    "heatpumpheatingtotalperformance" text,
    "solarheatingplantheatingtotalperformance" text,
    "solarcellstotalperformance" text,
    "fulfilmentheatinghotwater" text,
    "fulfilmentelectricityhotwater" text,
    "boilerefficiency" text
);

ALTER TABLE
    "result_f_a_p_proposals_calculatedbe06result_resultfigures"
ADD
    FOREIGN KEY (
        "zone_result_resultforallprofitableproposals_id_ref"
    ) REFERENCES "zone_result_resultforallprofitableproposals" ("id");

CREATE Table "result_f_a_p_proposals_calculatedbe06result_keyfigures" (
    "zone_result_resultforallprofitableproposals_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "transmissionlossthroughenvelopeexcludingwindowsanddoors" text,
    "energyframeinbrnoaddition" text,
    "additiontoenergyframeduetomechanicalexhaust" text,
    "additiontoenergyframeduetospecialconditions" text,
    "totalenergyrequirement" text,
    "contributiontoenergyrequirementheating" text,
    "contributiontoenergyrequirementelectricity" text,
    "contributiontoenergyrequirementexcesstemprature" text
);

ALTER TABLE
    "result_f_a_p_proposals_calculatedbe06result_keyfigures"
ADD
    FOREIGN KEY (
        "zone_result_resultforallprofitableproposals_id_ref"
    ) REFERENCES "zone_result_resultforallprofitableproposals" ("id");

CREATE Table "result_f_a_p_proposals_calculatedbe10result_resultfigures" (
    "zone_result_resultforallprofitableproposals_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "heatingrequirementforcentralheating" text,
    "heatingrequirementforstoves" text,
    "heatingrequirementforcentralheatingdegreedayindependent" text,
    "electricityrequirementforheating" text,
    "electricityrequirementfornonheating" text,
    "electricityrequirementforlighting" text,
    "electricityrequirementforventilation" text,
    "electricityrequirementforheatpump" text,
    "electricityrequirementforpumps" text,
    "heatpumpheatingtotalperformance" text,
    "solarheatingplantheatingtotalperformance" text,
    "solarcellstotalperformance" text,
    "windmillstotalperformance" text,
    "fulfilmentheatinghotwater" text,
    "fulfilmentelectricityhotwater" text,
    "boilerefficiency" text
);

ALTER TABLE
    "result_f_a_p_proposals_calculatedbe10result_resultfigures"
ADD
    FOREIGN KEY (
        "zone_result_resultforallprofitableproposals_id_ref"
    ) REFERENCES "zone_result_resultforallprofitableproposals" ("id");

CREATE Table "result_f_a_p_proposals_calculatedbe10result_keyfigures" (
    "zone_result_resultforallprofitableproposals_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "transmissionlossthroughenvelopeexcludingwindowsanddoors" text,
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
    "energyframe2020_contributiontoenergyrequirementexcesstemperature" text
);

ALTER TABLE
    "result_f_a_p_proposals_calculatedbe10result_keyfigures"
ADD
    FOREIGN KEY (
        "zone_result_resultforallprofitableproposals_id_ref"
    ) REFERENCES "zone_result_resultforallprofitableproposals" ("id");

CREATE Table "result_f_a_p_proposals_calculatedbe15result_resultfigures" (
    "zone_result_resultforallprofitableproposals_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "heatingrequirementforcentralheating" text,
    "heatingrequirementforstoves" text,
    "heatingrequirementforcentralheatingdegreedayindependent" text,
    "electricityrequirementforheating" text,
    "electricityrequirementfornonheating" text,
    "electricityrequirementforlighting" text,
    "electricityrequirementforventilation" text,
    "electricityrequirementforheatpump" text,
    "electricityrequirementforpumps" text,
    "heatpumpheatingtotalperformance" text,
    "solarheatingplantheatingtotalperformance" text,
    "solarcellstotalperformance" text,
    "windmillstotalperformance" text,
    "fulfilmentheatinghotwater" text,
    "fulfilmentelectricityhotwater" text,
    "boilerefficiency" text
);

ALTER TABLE
    "result_f_a_p_proposals_calculatedbe15result_resultfigures"
ADD
    FOREIGN KEY (
        "zone_result_resultforallprofitableproposals_id_ref"
    ) REFERENCES "zone_result_resultforallprofitableproposals" ("id");

CREATE Table "result_f_a_p_proposals_calculatedbe15result_keyfigures" (
    "zone_result_resultforallprofitableproposals_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "transmissionlossthroughenvelopeexcludingwindowsanddoors" text,
    "renovationclass2_energyframeinbrnoaddition" text,
    "renovationclass2_additiontoenergyframeduetospecialconditions" text,
    "renovationclass2_totalenergyrequirement" text,
    "renovationclass2_contributiontoenergyrequirementheating" text,
    "renovationclass1_energyframeinbrnoaddition" text,
    "renovationclass1_additiontoenergyframeduetospecialconditions" text,
    "renovationclass1_totalenergyrequirement" text,
    "renovationclass1_contributiontoenergyrequirementheating" text,
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
    "energyframe2015_contributiontoenergyrequirementexcesstemperature" text,
    "energyframe2020_contributiontoenergyrequirementexcesstemperature" text
);

ALTER TABLE
    "result_f_a_p_proposals_calculatedbe15result_keyfigures"
ADD
    FOREIGN KEY (
        "zone_result_resultforallprofitableproposals_id_ref"
    ) REFERENCES "zone_result_resultforallprofitableproposals" ("id");

CREATE Table "result_f_a_p_proposals_calculatedsbiresult_resultfigures" (
    "zone_result_resultforallprofitableproposals_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "heatingrequirementforcentralheating" text,
    "heatingrequirementforstoves" text,
    "heatingrequirementforcentralheatingdegreedayindependent" text,
    "electricityrequirementforheating" text,
    "electricityrequirementfornonheating" text,
    "electricityrequirementforlighting" text,
    "electricityrequirementforventilation" text,
    "electricityrequirementforheatpump" text,
    "electricityrequirementforpumps" text,
    "heatpumpheatingtotalperformance" text,
    "solarheatingplantheatingtotalperformance" text,
    "solarcellstotalperformance" text,
    "fulfilmentheatinghotwater" text,
    "fulfilmentelectricityhotwater" text,
    "boilerefficiency" text
);

ALTER TABLE
    "result_f_a_p_proposals_calculatedsbiresult_resultfigures"
ADD
    FOREIGN KEY (
        "zone_result_resultforallprofitableproposals_id_ref"
    ) REFERENCES "zone_result_resultforallprofitableproposals" ("id");

CREATE Table "result_f_a_p_proposals_calculatedsbiresult_keyfigures" (
    "zone_result_resultforallprofitableproposals_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "transmissionlossthroughenvelopeexcludingwindowsanddoors" text,
    "energyframeinbrnoaddition" text,
    "additiontoenergyframeduetomechanicalexhaust" text,
    "additiontoenergyframeduetospecialconditions" text,
    "totalenergyrequirement" text,
    "contributiontoenergyrequirementheating" text,
    "contributiontoenergyrequirementelectricity" text,
    "contributiontoenergyrequirementexcesstemprature" text
);

ALTER TABLE
    "result_f_a_p_proposals_calculatedsbiresult_keyfigures"
ADD
    FOREIGN KEY (
        "zone_result_resultforallprofitableproposals_id_ref"
    ) REFERENCES "zone_result_resultforallprofitableproposals" ("id");

CREATE Table "result_f_a_p_proposals_calculatedbe18result_resultfigures" (
    "zone_result_resultforallprofitableproposals_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "heatingrequirementforcentralheating" text,
    "heatingrequirementforstoves" text,
    "heatingrequirementforcentralheatingdegreedayindependent" text,
    "electricityrequirementforheating" text,
    "electricityrequirementfornonheating" text,
    "electricityrequirementforlighting" text,
    "electricityrequirementforventilation" text,
    "electricityrequirementforheatpump" text,
    "electricityrequirementforpumps" text,
    "heatpumpheatingtotalperformance" text,
    "solarheatingplantheatingtotalperformance" text,
    "solarcellstotalperformance" text,
    "windmillstotalperformance" text,
    "fulfilmentheatinghotwater" text,
    "fulfilmentelectricityhotwater" text,
    "boilerefficiency" text
);

ALTER TABLE
    "result_f_a_p_proposals_calculatedbe18result_resultfigures"
ADD
    FOREIGN KEY (
        "zone_result_resultforallprofitableproposals_id_ref"
    ) REFERENCES "zone_result_resultforallprofitableproposals" ("id");

CREATE Table "result_f_a_p_proposals_calculatedbe18result_keyfigures" (
    "zone_result_resultforallprofitableproposals_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "transmissionlossthroughenvelopeexcludingwindowsanddoors" text,
    "renovationclass2_energyframeinbrnoaddition" text,
    "renovationclass2_additiontoenergyframeduetospecialconditions" text,
    "renovationclass2_totalenergyrequirement" text,
    "renovationclass2_contributiontoenergyrequirementheating" text,
    "renovationclass1_energyframeinbrnoaddition" text,
    "renovationclass1_additiontoenergyframeduetospecialconditions" text,
    "renovationclass1_totalenergyrequirement" text,
    "renovationclass1_contributiontoenergyrequirementheating" text,
    "energyframe2018_energyframeinbrnoaddition" text,
    "energyframe2018_additiontoenergyframeduetospecialconditions" text,
    "energyframe2018_totalenergyrequirement" text,
    "energyframe2018_contributiontoenergyrequirementheating" text,
    "energyframe2018_contributiontoenergyrequirementelectricity" text,
    "energyframe2018_contributiontoenergyrequirementexcesstemperature" text,
    "lowenergyframe_energyframeinbrnoaddition" text,
    "lowenergyframe_additiontoenergyframeduetospecialconditions" text,
    "lowenergyframe_totalenergyrequirement" text,
    "lowenergyframe_contributiontoenergyrequirementheating" text,
    "lowenergyframe_contributiontoenergyrequirementelectricity" text,
    "lowenergyframe_contributiontoenergyrequirementexcesstemperature" text
);

ALTER TABLE
    "result_f_a_p_proposals_calculatedbe18result_keyfigures"
ADD
    FOREIGN KEY (
        "zone_result_resultforallprofitableproposals_id_ref"
    ) REFERENCES "zone_result_resultforallprofitableproposals" ("id");

CREATE Table "result_f_a_p_proposals_calculatedsolarcellutilization" (
    "zone_result_resultforallprofitableproposals_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "solarcellshare" text,
    "totalutilizationpercent" text
);

ALTER TABLE
    "result_f_a_p_proposals_calculatedsolarcellutilization"
ADD
    FOREIGN KEY (
        "zone_result_resultforallprofitableproposals_id_ref"
    ) REFERENCES "zone_result_resultforallprofitableproposals" ("id");

CREATE Table "result_f_a_p_proposals_fuelconsumption" (
    "zone_result_resultforallprofitableproposals_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "fuel_material" text,
    "fuel_unit" text,
    "fuel_energyperunit" text,
    "fuel_co2perunit" text,
    "fuelprice_costperunit" text,
    "fuelprice_fixedcostperyear" text,
    "fuelprice_suppliercompanyname" text,
    "fuelconsumption" text,
    "isforheating" text
);

ALTER TABLE
    "result_f_a_p_proposals_fuelconsumption"
ADD
    FOREIGN KEY (
        "zone_result_resultforallprofitableproposals_id_ref"
    ) REFERENCES "zone_result_resultforallprofitableproposals" ("id");

# End: ZoneResult__ResultForAllProfitableProposals
# Start: ZoneResult__ResultForAllProposals
CREATE Table "zone_result_resultforallproposals" (
    "xml_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "energylabelclassification" text
);

ALTER TABLE
    "zone_result_resultforallproposals"
ADD
    FOREIGN KEY ("xml_id_ref") REFERENCES "xmldoc" ("id");

CREATE Table "resultforallproposals_fuelconsumption" (
    "zone_result_resultforallproposals_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "fuel_material" text,
    "fuel_unit" text,
    "fuel_energyperunit" text,
    "fuel_co2perunit" text,
    "fuelprice_costperunit" text,
    "fuelprice_fixedcostperyear" text,
    "fuelprice_suppliercompanyname" text,
    "fuelconsumption" text,
    "isforheating" text
);

ALTER TABLE
    "resultforallproposals_fuelconsumption"
ADD
    FOREIGN KEY (
        "zone_result_resultforallproposals_id_ref"
    ) REFERENCES "zone_result_resultforallproposals" ("id");

CREATE Table "resultforallproposals_calculatedsolarcellutilization" (
    "zone_result_resultforallproposals_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "solarcellshare" text,
    "totalutilizationpercent" text
);

ALTER TABLE
    "resultforallproposals_calculatedsolarcellutilization"
ADD
    FOREIGN KEY (
        "zone_result_resultforallproposals_id_ref"
    ) REFERENCES "zone_result_resultforallproposals" ("id");

CREATE Table "resultforallproposals_calculatedbe18result_resultfigures" (
    "zone_result_resultforallproposals_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "heatingrequirementforcentralheating" text,
    "heatingrequirementforstoves" text,
    "heatingrequirementforcentralheatingdegreedayindependent" text,
    "electricityrequirementforheating" text,
    "electricityrequirementfornonheating" text,
    "electricityrequirementforlighting" text,
    "electricityrequirementforventilation" text,
    "electricityrequirementforheatpump" text,
    "electricityrequirementforpumps" text,
    "heatpumpheatingtotalperformance" text,
    "solarheatingplantheatingtotalperformance" text,
    "solarcellstotalperformance" text,
    "windmillstotalperformance" text,
    "fulfilmentheatinghotwater" text,
    "fulfilmentelectricityhotwater" text,
    "boilerefficiency" text
);

ALTER TABLE
    "resultforallproposals_calculatedbe18result_resultfigures"
ADD
    FOREIGN KEY (
        "zone_result_resultforallproposals_id_ref"
    ) REFERENCES "zone_result_resultforallproposals" ("id");

CREATE Table "resultforallproposals_calculatedbe18result_keyfigures" (
    "zone_result_resultforallproposals_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "transmissionlossthroughenvelopeexcludingwindowsanddoors" text,
    "renovationclass2_energyframeinbrnoaddition" text,
    "renovationclass2_additiontoenergyframeduetospecialconditions" text,
    "renovationclass2_totalenergyrequirement" text,
    "renovationclass2_contributiontoenergyrequirementheating" text,
    "renovationclass1_energyframeinbrnoaddition" text,
    "renovationclass1_additiontoenergyframeduetospecialconditions" text,
    "renovationclass1_totalenergyrequirement" text,
    "renovationclass1_contributiontoenergyrequirementheating" text,
    "energyframe2018_energyframeinbrnoaddition" text,
    "energyframe2018_additiontoenergyframeduetospecialconditions" text,
    "energyframe2018_totalenergyrequirement" text,
    "energyframe2018_contributiontoenergyrequirementheating" text,
    "energyframe2018_contributiontoenergyrequirementelectricity" text,
    "energyframe2018_contributiontoenergyrequirementexcesstemperature" text,
    "lowenergyframe_energyframeinbrnoaddition" text,
    "lowenergyframe_additiontoenergyframeduetospecialconditions" text,
    "lowenergyframe_totalenergyrequirement" text,
    "lowenergyframe_contributiontoenergyrequirementheating" text,
    "lowenergyframe_contributiontoenergyrequirementelectricity" text,
    "lowenergyframe_contributiontoenergyrequirementexcesstemperature" text
);

ALTER TABLE
    "resultforallproposals_calculatedbe18result_keyfigures"
ADD
    FOREIGN KEY (
        "zone_result_resultforallproposals_id_ref"
    ) REFERENCES "zone_result_resultforallproposals" ("id");

CREATE Table "resultforallproposals_calculatedbe15result_resultfigures" (
    "zone_result_resultforallproposals_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "heatingrequirementforcentralheating" text,
    "heatingrequirementforstoves" text,
    "heatingrequirementforcentralheatingdegreedayindependent" text,
    "electricityrequirementforheating" text,
    "electricityrequirementfornonheating" text,
    "electricityrequirementforlighting" text,
    "electricityrequirementforventilation" text,
    "electricityrequirementforheatpump" text,
    "electricityrequirementforpumps" text,
    "heatpumpheatingtotalperformance" text,
    "solarheatingplantheatingtotalperformance" text,
    "solarcellstotalperformance" text,
    "windmillstotalperformance" text,
    "fulfilmentheatinghotwater" text,
    "fulfilmentelectricityhotwater" text,
    "boilerefficiency" text
);

ALTER TABLE
    "resultforallproposals_calculatedbe15result_resultfigures"
ADD
    FOREIGN KEY (
        "zone_result_resultforallproposals_id_ref"
    ) REFERENCES "zone_result_resultforallproposals" ("id");

CREATE Table "resultforallproposals_calculatedbe15result_keyfigures" (
    "zone_result_resultforallproposals_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "transmissionlossthroughenvelopeexcludingwindowsanddoors" text,
    "renovationclass2_energyframeinbrnoaddition" text,
    "renovationclass2_additiontoenergyframeduetospecialconditions" text,
    "renovationclass2_totalenergyrequirement" text,
    "renovationclass2_contributiontoenergyrequirementheating" text,
    "renovationclass1_energyframeinbrnoaddition" text,
    "renovationclass1_additiontoenergyframeduetospecialconditions" text,
    "renovationclass1_totalenergyrequirement" text,
    "renovationclass1_contributiontoenergyrequirementheating" text,
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
    "energyframe2015_contributiontoenergyrequirementexcesstemperature" text,
    "energyframe2020_contributiontoenergyrequirementexcesstemperature" text
);

ALTER TABLE
    "resultforallproposals_calculatedbe15result_keyfigures"
ADD
    FOREIGN KEY (
        "zone_result_resultforallproposals_id_ref"
    ) REFERENCES "zone_result_resultforallproposals" ("id");

CREATE Table "resultforallproposals_calculatedbe10result_resultfigures" (
    "zone_result_resultforallproposals_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "heatingrequirementforcentralheating" text,
    "heatingrequirementforstoves" text,
    "heatingrequirementforcentralheatingdegreedayindependent" text,
    "electricityrequirementforheating" text,
    "electricityrequirementfornonheating" text,
    "electricityrequirementforlighting" text,
    "electricityrequirementforventilation" text,
    "electricityrequirementforheatpump" text,
    "electricityrequirementforpumps" text,
    "heatpumpheatingtotalperformance" text,
    "solarheatingplantheatingtotalperformance" text,
    "solarcellstotalperformance" text,
    "windmillstotalperformance" text,
    "fulfilmentheatinghotwater" text,
    "fulfilmentelectricityhotwater" text,
    "boilerefficiency" text
);

ALTER TABLE
    "resultforallproposals_calculatedbe10result_resultfigures"
ADD
    FOREIGN KEY (
        "zone_result_resultforallproposals_id_ref"
    ) REFERENCES "zone_result_resultforallproposals" ("id");

CREATE Table "resultforallproposals_calculatedbe10result_keyfigures" (
    "zone_result_resultforallproposals_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "transmissionlossthroughenvelopeexcludingwindowsanddoors" text,
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
    "energyframe2020_contributiontoenergyrequirementexcesstemperature" text
);

ALTER TABLE
    "resultforallproposals_calculatedbe10result_keyfigures"
ADD
    FOREIGN KEY (
        "zone_result_resultforallproposals_id_ref"
    ) REFERENCES "zone_result_resultforallproposals" ("id");

CREATE Table "resultforallproposals_calculatedbe06result_resultfigures" (
    "zone_result_resultforallproposals_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "heatingrequirementforcentralheating" text,
    "heatingrequirementforstoves" text,
    "heatingrequirementforcentralheatingdegreedayindependent" text,
    "electricityrequirementforheating" text,
    "electricityrequirementfornonheating" text,
    "electricityrequirementforlighting" text,
    "electricityrequirementforventilation" text,
    "electricityrequirementforheatpump" text,
    "electricityrequirementforpumps" text,
    "heatpumpheatingtotalperformance" text,
    "solarheatingplantheatingtotalperformance" text,
    "solarcellstotalperformance" text,
    "fulfilmentheatinghotwater" text,
    "fulfilmentelectricityhotwater" text,
    "boilerefficiency" text
);

ALTER TABLE
    "resultforallproposals_calculatedbe06result_resultfigures"
ADD
    FOREIGN KEY (
        "zone_result_resultforallproposals_id_ref"
    ) REFERENCES "zone_result_resultforallproposals" ("id");

CREATE Table "resultforallproposals_calculatedbe06result_keyfigures" (
    "zone_result_resultforallproposals_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "transmissionlossthroughenvelopeexcludingwindowsanddoors" text,
    "energyframeinbrnoaddition" text,
    "additiontoenergyframeduetomechanicalexhaust" text,
    "additiontoenergyframeduetospecialconditions" text,
    "totalenergyrequirement" text,
    "contributiontoenergyrequirementheating" text,
    "contributiontoenergyrequirementelectricity" text,
    "contributiontoenergyrequirementexcesstemprature" text
);

ALTER TABLE
    "resultforallproposals_calculatedbe06result_keyfigures"
ADD
    FOREIGN KEY (
        "zone_result_resultforallproposals_id_ref"
    ) REFERENCES "zone_result_resultforallproposals" ("id");

# End: ZoneResult__ResultForAllProposals
CREATE Table "zone_result" (
    "xml_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "energylabelclassification" text
);

ALTER TABLE
    "zone_result"
ADD
    FOREIGN KEY ("xml_id_ref") REFERENCES "xmldoc" ("id");

# Start: ZoneResult__resultsforeachproposalgroup
CREATE Table "zone_result_resultsforeachproposalgroup" (
    "xml_id_ref" bigint,
    "id" SERIAL PRIMARY KEY
);

ALTER TABLE
    "zone_result_resultsforeachproposalgroup"
ADD
    FOREIGN KEY ("xml_id_ref") REFERENCES "xmldoc" ("id");

CREATE Table "resultforeachproposalgroup_proposalresult" (
    "zone_result_resultsforeachproposalgroup_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "profitability" text,
    "category" text,
    "investment" text,
    "fuelsavings" text
);

ALTER TABLE
    "resultforeachproposalgroup_proposalresult"
ADD
    FOREIGN KEY (
        "zone_result_resultsforeachproposalgroup_id_ref"
    ) REFERENCES "zone_result_resultsforeachproposalgroup" ("id");

CREATE Table "resultforeachproposalgroup_fuelsavings" (
    "zone_result_resultsforeachproposalgroup_id_ref" bigint,
    "id" SERIAL PRIMARY KEY,
    "fuelsaving_fuel_material" text,
    "fuelsaving_fuel_unit" text,
    "fuelsaving_fuel_energyperunit" text,
    "fuelsaving_fuel_co2perunit" text,
    "fuelsaving_fuelprice_costperunit" text,
    "fuelsaving_fuelprice_fixedcostperyear" text,
    "fuelsaving_fuelprice_suppliercompanyname" text,
    "fuelsaving_fuelsaved" text
);

ALTER TABLE
    "resultforeachproposalgroup_fuelsavings"
ADD
    FOREIGN KEY (
        "zone_result_resultsforeachproposalgroup_id_ref"
    ) REFERENCES "zone_result_resultsforeachproposalgroup" ("id");

# End: ZoneResult__resultsforeachproposalgroup