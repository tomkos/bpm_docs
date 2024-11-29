# Uninstalling IBM® Business Automation
Machine Learning Server

## Procedure

1. From a command window, go to the directory where Machine Learning Server is installed. 
cd ba-ml-server-install-dir
2. Stop Machine Learning Server by using the
following command: 
./bin/ba-ml-server-stop
3. Delete the docker images in the local docker registry.

docker-compose rm --force --stop
4. Go up one level in the directory structure and remove the entire installation
directory. 
cd ..
rm -rf ba-ml-server-install-dir