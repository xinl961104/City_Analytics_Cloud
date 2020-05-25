import pandas as pd
from db_constants import *
from db_utils import *

database_name = 'processed_data'
ddoc_id = 'ddoc001'
view_id = 'mapreduce'

income_aurin = pd.read_csv('../income_level/SA4_Personal_Income_2010-2015.csv')
senti_score_db = connect_database(USERNAME_LOCAL, PASSWORD_LOCAL, URL_LOCAL, database_name)
view = acess_view(senti_score_db, ddoc_id, view_id, True)

# each elem should contain a key and a value
# a key should be the region name classified by Statistical Area Level 4
# value should be the average of sentiment anaysis of that region
senti_by_region = {'code':[], 'senti_scores':[], 'tweet_count':[]}
with view as view:
    for row in view:
        senti_by_region['code'].append(int(row['key']))
        senti_by_region['senti_scores'].append(round(row['value']['sum'] / row['value']['count'], 3))
        senti_by_region['tweet_count'].append(row['value']['count'])
senti_by_region = pd.DataFrame(senti_by_region)
aurin_twitter = income_aurin.merge(senti_by_region, left_on=' sa4_code_2016', right_on = 'code')
print(aurin_twitter.iloc[:,[0,1,-1,-2]])
##print(aurin_twitter[['sa4_name16']])


##return render_template('home.html', vegan_map=document,
##form=form)