import pandas as pd
from db_constants import *
from db_utils import *

DBNAME = "aurin_edu"
my_database = create_database(USERNAME, PASSWORD, URL, DBNAME)

edu_aurin = pd.read_csv('../tertiary_edu/tertiary_edu.csv')
(row_num, col_num) = edu_aurin.shape

for i in range(0, row_num):
    data_row = dict(edu_aurin.iloc[i])
    data_row['sa4_code16'] = int(data_row['sa4_code16'])
    data_row['uni_other_tert_instit_tot_p'] = int(data_row[' uni_other_tert_instit_tot_p'])
    del data_row[' uni_other_tert_instit_tot_p']
    data_row['sa4_name16'] = data_row[' sa4_name16']
    del data_row[' sa4_name16']
    my_database.create_document(data_row)










