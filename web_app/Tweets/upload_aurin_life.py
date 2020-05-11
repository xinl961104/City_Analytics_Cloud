import pandas as pd
from db_constants import *
from db_utils import *

DBNAME = "aurin_life"
my_database = create_database(USERNAME_LOCAL, PASSWORD_LOCAL, URL_LOCAL, DBNAME)

edu_aurin = pd.read_csv('../life_expectancy/life_expectancy.csv')
(row_num, col_num) = edu_aurin.shape

for i in range(0, row_num):
    data_row = dict(edu_aurin.iloc[i])
    data_row['sa4_code'] = int(data_row[' sa4_code'])
    del data_row[' sa4_code']
    data_row['life_expectancy_p_2013_15'] = float(data_row['life_expectancy_p_2013_15'])
    data_row['sa4_name'] = data_row[' sa4_name']
    del data_row[' sa4_name']
    my_database.create_document(data_row)