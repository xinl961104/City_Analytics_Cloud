#!/bin/bash

. ./openrc.sh; ansible-playbook -i hosts haproxy.yaml