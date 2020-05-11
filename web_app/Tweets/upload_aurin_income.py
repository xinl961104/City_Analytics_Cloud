import pandas as pd
from db_constants import *
from db_utils import *

DBNAME = "aurin_income"
my_database = create_database(USERNAME_LOCAL, PASSWORD_LOCAL, URL_LOCAL, DBNAME)

edu_aurin = pd.read_csv('../income_level/SA4_Personal_Income_2010-2015.csv')
(row_num, col_num) = edu_aurin.shape

for i in range(0, row_num):
    data_row = dict(edu_aurin.iloc[i])
    data_row['sa4_code_2016'] = int(data_row[' sa4_code_2016'])
    del data_row[' sa4_code_2016']
    data_row['earners_persons_2014_15'] = int(data_row[' earners_persons_2014_15'])
    del data_row[' earners_persons_2014_15']
    data_row['sa4_name16'] = data_row[' sa4_name16']
    del data_row[' sa4_name16']
    my_database.create_document(data_row)