# Changing the IBM® Business Automation
Machine Learning Server configuration

## About this task

| Variable name       | Description                                                               |
|---------------------|---------------------------------------------------------------------------|
| NGINX\_AUTH\_PASSWORD | The Nginx basic authentication password to access Machine Learning Server |
| BAI\_HOSTNAME        | Host name of the Business Automation Workflow environment                 |
| ELASTICSEARCH\_PORT  | Exposed port for Elasticsearch on the Business Automation Workflow host   |
| ES\_USERNAME         | User name for accessing Elasticsearch                                     |
| ES\_PASSWORD         | Password for accessing Elasticsearch                                      |

## Procedure

1. Stop Machine Learning Server by
using the following command: ./bin/ba-ml-server-stop
2. To change the value of a variable, overwrite its value
in the .env file. Note: To change
a password (values that are base64 encoded), delete the password and
the base64 tag in the .env file.
3. Restart Machine Learning Server by
using the following command and enter the prompted variables:
./bin/ba-ml-server-start --init --acceptLicense