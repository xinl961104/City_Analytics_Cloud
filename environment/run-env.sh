#!/bin/bash

. ./pt-52783-openrc.sh; ansible-playbook -i hosts -u ubuntu --key-file=~/.ssh/demo.pem env.yaml