import pandas as pd
import json

with open('nationwide_SEID_2011.json', 'r') as file1:
    data1 = json.loads(file1.read())

lga_name1 = []
state1 = []
SEID_score = []
population = []
for feature in data1['features']:
    lga_name1.append(feature['properties']['lga_name'].split()[0])
    state1.append(feature['properties']['ste_name'])
    SEID_score.append(feature['properties']['index_score'])
    population.append(feature['properties']['res_pop_count'])

SEID_2011 = pd.DataFrame(data =
                         {'lga_name':lga_name1, 'state':state1,
                          'SEID_score':SEID_score, 'population':population})

filtered_SEID_2011 = SEID_2011[
    (SEID_2011['lga_name'] == 'Melbourne') |
    (SEID_2011['lga_name'] == 'Sydney') |
    (SEID_2011['lga_name'] == 'Brisbane') |
    (SEID_2011['lga_name'] == 'Perth') |
    (SEID_2011['lga_name'] == 'Adelaide') |
    (SEID_2011['lga_name'] == 'Cairns') |
    (SEID_2011['lga_name'] == 'Darwin')]

filtered_SEID_2011 = filtered_SEID_2011.reset_index(drop=True)
filtered_SEID_2011.to_json('filtered_SEID_2011.json')

with open('nationwide_education_level_2016.json', 'r') as file2:
    data2 = json.loads(file2.read())

lga_name2 = []
no_attendence = []
not_stated = []
yr8  = []
yr9  = []
yr10 = []
yr11 = []
yr12 = []
post_school = []
for feature in data2['features']:

    lga_name2.append(feature['properties']['lga_name18'].split()[0])
    no_attendence.append(feature['properties']['hi_yr_scl_completed_p15_yrs_ov_no_scl_pr100'])
    not_stated.append(feature['properties']['hi_yr_scl_completed_p15_yrs_ov_ns_pr100'])
    yr8.append(feature['properties']['hi_yr_scl_completed_p15_yrs_ov_completed_yr_8_belo_pr100'])
    yr9.append(feature['properties']['hi_yr_scl_completed_p15_yrs_ov_completed_yr_9_equivalent_pr100'])
    yr10.append(feature['properties']['hi_yr_scl_completed_p15_yrs_ov_completed_yr_10_equivalent_pr100'])
    yr11.append(feature['properties']['hi_yr_scl_completed_p15_yrs_ov_completed_yr_11_equivalent_pr100'])
    yr12.append(feature['properties']['hi_yr_scl_completed_p15_yrs_ov_completed_yr_12_equivalent_pr100'])
    post_school.append(feature['properties']['p_post_scl_qualf_p_post_scl_qualification_pr100'])

edu_level_2016 = pd.DataFrame(data =
                          {'lga_name':lga_name2, 'no_attendence':no_attendence,
                           'not_stated':not_stated,
                          'yr8':yr8, 'yr9':yr9,
                         'yr10':yr10, 'yr11':yr11,
                         'yr12':yr12, 'post_school':post_school})

edu_level_2016['yr9-12'] = edu_level_2016['yr9'] + edu_level_2016['yr10'] +\
                            edu_level_2016['yr11']+edu_level_2016['yr12']

edu_level_2016 = edu_level_2016.drop(['yr9', 'yr10', 'yr11', 'yr12'], axis=1)

edu_level_2016 = edu_level_2016[
    (edu_level_2016['lga_name'] == 'Melbourne') |
    (edu_level_2016['lga_name'] == 'Sydney') |
    (edu_level_2016['lga_name'] == 'Brisbane') |
    (edu_level_2016['lga_name'] == 'Perth') |
    (edu_level_2016['lga_name'] == 'Adelaide') |
    (edu_level_2016['lga_name'] == 'Cairns') |
    (edu_level_2016['lga_name'] == 'Darwin')]

edu_level_2016 = edu_level_2016.reset_index(drop=True)
edu_level_2016.to_json('edu_level_2016.json')

with open('age_dist_2015.json', 'r') as file3:
    data3 = json.loads(file3.read())

lga_name3 = []
_0_4, _5_9, _10_14, _15_19, _20_24, _25_29, _30_34, _35_39, _40_44, _45_49, \
_50_54, _55_59, _60_64, _65_69, _70_74, _75_79, _80_84, _85_and_over \
        = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]

for feature in data3['features']:

    lga_name3.append(feature['properties']['lga_name'].split()[0])
    _0_4.append(feature['properties']['_0_4_years_percent'])
    _5_9.append(feature['properties']['_5_9_years_percent'])
    _10_14.append(feature['properties']['_10_14_years_percent'])
    _15_19.append(feature['properties']['_15_19_years_percent'])
    _20_24.append(feature['properties']['_20_24_years_percent'])
    _25_29.append(feature['properties']['_25_29_years_percent'])
    _30_34.append(feature['properties']['_30_34_years_percent'])
    _35_39.append(feature['properties']['_35_39_years_percent'])
    _40_44.append(feature['properties']['_40_44_years_percent'])
    _45_49.append(feature['properties']['_45_49_years_percent'])
    _50_54.append(feature['properties']['_50_54_years_percent'])
    _55_59.append(feature['properties']['_55_59_years_percent'])
    _60_64.append(feature['properties']['_60_64_years_percent'])
    _65_69.append(feature['properties']['_65_69_years_percent'])
    _70_74.append(feature['properties']['_70_74_years_percent'])
    _75_79.append(feature['properties']['_75_79_years_percent'])
    _80_84.append(feature['properties']['_80_84_years_percent'])
    _85_and_over.append(feature['properties']['_85_years_over_percent'])

age_group = pd.DataFrame(data = {'lga_name':lga_name3, '_0_4':_0_4,
                               '_5_9':_5_9, '_10_14':_10_14,
                              '_15_19':_15_19, '_20_24':_20_24,
                             '_25_29':_25_29, '_30_34':_30_34,
                             '_35_39':_35_39, '_40_44':_40_44,
                             '_45_49':_45_49, '_50_54':_50_54,
                             '_55_59':_55_59, '_60_64':_60_64,
                             '_65_69':_65_69, '_70_74':_70_74,
                             '_75_79':_75_79, '_80_84':_80_84,
                             '_85_and_over':_85_and_over})

age_group['_0_19'] = age_group['_0_4'] + age_group['_5_9'] + age_group['_10_14'] + age_group['_15_19']
age_group['_20_39'] = age_group['_20_24'] + age_group['_25_29'] + age_group['_30_34'] + age_group['_35_39']
age_group['_40_59'] = age_group['_40_44'] + age_group['_45_49'] + age_group['_50_54'] + age_group['_55_59']
age_group['_60_and_over'] = age_group['_60_64'] + age_group['_65_69'] + \
         age_group['_70_74'] + age_group['_75_79'] + age_group['_80_84'] + age_group['_85_and_over']
age_group = age_group.drop(['_0_4', '_5_9', '_10_14', '_15_19', '_20_24',
                         '_25_29', '_30_34', '_35_39', '_40_44', '_45_49',
                         '_50_54', '_55_59', '_60_64', '_65_69', '_70_74',
                         '_75_79', '_80_84', '_85_and_over'], axis=1)

age_group = age_group[
 (age_group['lga_name'] == 'Melbourne') |
 (age_group['lga_name'] == 'Sydney') |
 (age_group['lga_name'] == 'Brisbane') |
 (age_group['lga_name'] == 'Perth') |
 (age_group['lga_name'] == 'Adelaide') |
 (age_group['lga_name'] == 'Cairns') |
 (age_group['lga_name'] == 'Darwin')]

age_group = age_group.reset_index(drop=True)
age_group.to_json('age_group_2015.json')
