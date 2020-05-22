#!/bin/bash

. ./openrc.sh; ansible-playbook -vvv -i hosts -u ubuntu --key-file=~/.ssh/id_Cassie.pem web.yaml