#!/bin/bash

. ./openrc.sh; ansible-playbook -i hosts couchDB.yaml