#!/bin/bash
while true; do
python3 multi_data_processing.py;
echo "processing done";
python3 map_reduce.py;
echo "map reduce done";
python3 web_db_data.py;
echo "data update done";
sleep 86400;
echo "slept for 86400 seconds";
done
