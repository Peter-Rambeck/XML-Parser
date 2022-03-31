

shortend column paths

energy_label tables:

BuildingResults_BuildingResult_ResultForAllProfitableProposals_EnergyLabelClassification ->
buildrels_resallprofitproposals_energylblclass text null, --shortened

ZoneResul_ResultForAllProfitableProposals_EnergyLabelClassification: ->
zoneresult_resallprofitproposals_energylblclass text null, --shortened


Unikke tabeller
1. xml_doc : unique
2. energy_label : alle tags i documentet med en instans
3. buildings : all 'building-data'
4. proposals
5: proposalgroup
6: zone_statuses
7: building_zones


zone_results tables:
zone_result_resultforallprofitableproposals:

All sub-tables with ref. to zone_result_resultforallprofitableproposals is shortened.
    resultforallprofitableproposals -> becomes: 'result_f_a_p_proposals'
