# Art Melbourne 

This is the repository of assignment 2 for the course COMP90024

Team 30:
Xingjian Zhang – Tweets Analysis, Views of CouchDB
Xin Li – Automatic Deployment, Django Web
Yuxian Wang – Automatic Deployment
Yue Bao – Data Harvesting, Error Handling

User Manual:

Web Interface Link: http://172.26.132.50:8080/
CouchDB cluster Link: http://172.26.132.50:4000/_utils/#
couchdb username: admin
couchdb password: password

How to automatic deploy with Anisble:





Ansible Playbook Structure and Explaination

 - The main.yaml file in the host_vars folder sets the variables for creating instances including volume, security groups, instances, the Ubuntu image for instances, the key used to create instances and the flavor.
 - To customize the instances, we need to install openstacksdk, set up the image, create the instances, add security groups and volume onto the instances. All of these tasks have been put in the roles folder.
 - The nectar.yaml file defines the tasks that would be executed on which host and the variables that need to be used.
 - The run-nectar.sh file specifies the playbook running with the openrc file.


Docker
- Same as main.yaml in nectar, the docker.yaml in host_vars folder stores the path of device and mount point for volume as variables.
- The tasks for docker contain setting proxy, installing independencies and docker and creating volume directory. More importantly, manager node and worker nodes should also be defined in this task
- More importantly, a manager node and worker nodes should also be defined as well. The two files, swarm manager and swarmworks, aim to initial the manager node, add the given token to hosts and join the worker nodes to it, so that the swarm mode could be created successfully.
- All the running tasks and sequences have been arranged in docker.yaml under the docker file. And the function of run-docker.sh is to execute the playbook with a key file.

Couchdb
After the environment has been set, a database is necessary for us to store the data crawled through Twitter API and from AURIN. Our processed data would be saved in the database after finishing the analysis as well. For this project, we use CouchDB as our database for the Couch Replication Protocol provides the high performance and strong reliability on data flow between cluster servers and web browsers. Moreover, CouchDB also provides MapReduce for comprehensive and efficient data retrieval.
Like the structure in Docker playbook, host_vars folder, roles folder, couchdb.yaml file and run-couchdb.sh file are included.
The couchDBManager file under the roles folder is to create the CouchDB service on four instances and cluster the service on manager node.

Three Service
This playbook mainly focuses on automatic deployment on Tweet_Collect, Tweet_Process and Web server. 
- Images of Tweet_Collect, Tweet_Process and Web have been built and pushed to Docker Hub in advance. In the roles folder, functions of setting up three services have been executed respectively.
- The functions of web.yaml and run-web.sh files are the same as those in the other three playbooks.

Haproxy
HAProxy is a load-balancer to direct users to available application servers.
We set the proxy on master node for CouchDB so that if CouchDB container is down on any node, users could still visit it on port 4000. 
We set the proxy on master node for Web so that if Web container is down on any node, users could visit it on port 8080. 





