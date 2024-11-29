# Installing IBM Business Automation
Machine Learning Server

## Before you begin

- Review hardware and software requirements. See IBM® Business Automation
Workflow
detailed system requirements.
- IBM Business Automation
Insights is configured to receive events
from your Business Automation Workflow installation. See Configuring event emitters with IBM Cloud Pak for Business Automation Business Automation Insights.
- Machine Learning Server retrieves data from Business Automation Insights through Elasticsearch queries. Go throughthe following items to ensure Machine Learning Server canaccess data from Business Automation Insights :
    - Make sure that the Elasticsearch port is exposed on the Business Automation Insights host by setting the
ELASTICSEARCH\_PORT variable in Business Automation Insights.
    - Make sure the following Business Automation Insights environmentvariables are available when you are installing Machine Learning Server . The variables canbe found in the Business Automation Insights .env file and are used by Machine Learning Server to access taskinformation stored in Business Automation Insights Elasticsearchindexes.
        - Make sure BAI\_HOSTNAME is the same as the Business Automation Insights hostname for
single-node deployment.
        - ELASTICSEARCH\_PORT
        - ES\_USERNAME
        - ES\_PASSWORD. Provide the actual password, not the base64-encoded string.
        - BAW\_TASK\_ALIAS=icp4ba-bai-process-summaries-completed-ibm-bai
- Access Elasticsearch by using the following
URL:https://BAI\_HOSTNAME:ELASTICSEARCH\_PORT/\_cat/healthIf
prompted, enter values for the ES\_USERNAME and ES\_PASSWORD
variables. Make sure that the Elasticsearch cluster health is either yellow or green. For more
information, see Cluster health API.

## About this task

- Passwords in the .env file are base64-encoded
and are stored in plain  text in configuration files. Therefore, make
sure to set permissions for access to the machine or to the top directory
of Machine Learning Server.
- Usernames and passwords are case-sensitive and only alphanumeric characters from A to Z and from
0 to 9 are allowed.

## Procedure

1. Download the Machine Learning Server archive
from IBM
Passport Advantage®.
2. Extract the files by running the following command:
tar -xzvf ba-ml-server-$VERSION.tar.gz
3. Go to the ba-ml-server-$VERSION directory.
4. Open the .env file and update the SERVICES
variable to include the nbt (Next Best Task) variable for the Intelligent Task Prioritization
service. For example: SERVICES="nbt"
5. Make sure ba-ml-server-start is set as an executable: 
sudo chmod a+x ./bin/ba-ml-server-start
6. Run the start script with the --acceptLicense flag.
If you are starting Machine Learning Server for the first time,
add the --init flag to check for missing values in the .env
file. You're prompted to enter any missing values. When all the values are entered, the script
launches the docker-compose.yml file by using the environment variables that
are defined in the .env file.Note: All the prompted values are stored in the
.env file, but passwords are base64 encoded.
./bin/ba-ml-server-start --acceptLicense --init
7. Call the status script to make sure that all launched containers are active: 
./bin/ba-ml-server-status
8. Test to ensure Machine Learning Server is
running: curl -k -u admin:NGINX\_AUTH\_PASSWORD "https://localhost/"