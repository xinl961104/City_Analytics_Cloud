import pandas as pd
from db_constants import *
from db_utils import *

DBNAME = "aurin_donation"
my_database = create_database(USERNAME, PASSWORD, URL, DBNAME)

edu_aurin = pd.read_csv('../donation/2014_donation.csv')
(row_num, col_num) = edu_aurin.shape

for i in range(0, row_num):
    data_row = dict(edu_aurin.iloc[i])
    data_row['sa4_code16'] = int(data_row['sa4_code16'])
    data_row['donation_med_aud'] = int(data_row['donation_med_aud'])
    data_row['sa4_name16'] = str(data_row[' sa4_name16'])
    del data_row[' sa4_name16']
    del data_row[' yr']
    my_database.create_document(data_row)