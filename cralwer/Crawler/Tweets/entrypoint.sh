#!/usr/bin/env bash
 
pip install CouchDB:2.1.0
pip install tweepy:3.8.0

python3 ./stream_listener.py

