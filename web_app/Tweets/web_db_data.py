import pandas as pd
from db_constants import *
from db_utils import *
pd.set_option('display.max_columns', None)

database_name = 'processed_data'
ddoc_id = 'ddoc001'
view_id = 'mapreduce'

db_aurin_edu = 'aurin_edu'
db_aurin_income = 'aurin_income'
db_aurin_donation = 'aurin_donation'

senti_score_db = connect_database(USERNAME, PASSWORD, URL, database_name)
view = acess_view(senti_score_db, ddoc_id, view_id, True)

edu_db = connect_database(USERNAME, PASSWORD, URL, db_aurin_edu)
map_fun_1 = '''function(doc) {
                emit(doc.sa4_code16, doc.uni_other_tert_instit_tot_p);
        }'''
create_view(edu_db, ddoc_id, view_id, map_fun_1)
view_edu = acess_view(edu_db, ddoc_id, view_id, False)
edu_table = {'code':[], 'tertiary_pop':[]}
with view_edu as view_edu:
    for row in view_edu:
        edu_table['code'].append(int(row['key']))
        edu_table['tertiary_pop'].append(int(row['value']))
edu_table = pd.DataFrame(edu_table)


income_db = connect_database(USERNAME, PASSWORD, URL, db_aurin_income)
map_fun_2 = '''function(doc) {
                emit(doc.sa4_code_2016, doc.earners_persons_2014_15);
        }'''
create_view(income_db, ddoc_id, view_id, map_fun_2)
view_income = acess_view(income_db, ddoc_id, view_id, False)
income_table = {'code':[], 'avg_income':[]}
with view_income as view_income:
    for row in view_income:
        income_table['code'].append(int(row['key']))
        income_table['avg_income'].append(int(row['value']))
income_table = pd.DataFrame(income_table)


life_db = connect_database(USERNAME, PASSWORD, URL, db_aurin_donation)
map_fun_3 = '''function(doc) {
                emit(doc.sa4_code16, doc.donation_med_aud);
        }'''
create_view(life_db, ddoc_id, view_id, map_fun_3)
view_life = acess_view(life_db, ddoc_id, view_id, False)
donation_table = {'code':[], 'med_donation':[]}
with view_life as view_life:
    for row in view_life:
        donation_table['code'].append(int(row['key']))
        donation_table['med_donation'].append(int(row['value']))
donation_table = pd.DataFrame(donation_table)


# each row should contain a key and a value
# a key should be the region name classified by Statistical Area Level 4
# value should be the average of sentiment anaysis of that region
senti_by_region = {'code':[], 'senti_scores':[], 'tweet_count':[]}
with view as view:
    for row in view:
        senti_by_region['code'].append(int(row['key']))
        senti_by_region['senti_scores'].append(round(row['value']['sum'] / row['value']['count'], 3))
        senti_by_region['tweet_count'].append(row['value']['count'])
senti_by_region = pd.DataFrame(senti_by_region)



code_name = {'code':[206, 207, 208, 209, 210, 211, 212, 213, 214], 'region_name':['Melbourne - Inner', 'Melbourne - Inner East', 'Melbourne - Inner South', 'Melbourne - North East', 'Melbourne - North West', 'Melbourne - Outer East', 'Melbourne - South East', 'Melbourne - West', 'Mornington Peninsula']}
code_name = pd.DataFrame(code_name)

edu_table = edu_table.merge(code_name, left_on='code', right_on='code')
income_table = income_table.merge(code_name, left_on='code', right_on='code')
donation_table = donation_table.merge(code_name, left_on='code', right_on='code')

edu_twitter = edu_table.merge(senti_by_region, left_on='code', right_on = 'code')
income_twitter = income_table.merge(senti_by_region, left_on='code', right_on = 'code')
donation_twitter = donation_table.merge(senti_by_region, left_on='code', right_on ='code')

print(edu_twitter)
print(income_twitter)
print(donation_twitter)


##use .iloc to query data in the table, e.g. aurin_twitter.iloc[row_index, col_index]
##print(aurin_twitter[['sa4_name16']])


##return render_template('home.html', vegan_map=document,
##form=form)