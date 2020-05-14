#!/bin/bash

. ./pt-52783-openrc.sh; ansible-playbook -vvv -i hosts -u ubuntu --key-file=~/.ssh/demo.pem web.yaml