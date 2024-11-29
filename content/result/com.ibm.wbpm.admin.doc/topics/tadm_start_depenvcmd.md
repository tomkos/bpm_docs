# Starting and stopping the deployment environment using the
command line

## Before you begin

To start or stop the deployment environment, you can run
the BPMConfig command with the -start or -stop parameter.
For both parameters, you can either specify a configuration properties
file that contains all of the required deployment environment information or you
can specify the profile and deployment environment name. If you choose
to specify the profile and deployment environment name for the -start parameter,
you do not need to specify the -username and -password options.
By comparison, if you choose to specify the profile and deployment
environment name for the -stop parameter, you
must specify the -username and -password options.
You can use the user name and password for the administrator of the
deployment environment.

## About this task

To start the deployment environment with the BPMConfig command,
perform the following steps.

## Procedure

- To start your deployment environment,you have two options:
    - Run the BPMConfig command passing it the name
of the configuration properties file that contains the configuration
properties for your deployment environment. For example: BPM\_home\bin\BPMConfig -start my\_environment.propertiesBPM\_home/bin/BPMConfig.sh -start my\_environment.properties
    - Run the BPMConfig command specifying the profile
and deployment environment name. For example: BPM\_home\bin\BPMConfig -start -profile DmgrProfile [-de De1]BPM\_home/bin/BPMConfig.sh -start -profile DmgrProfile [-de De1]If
there is only one deployment environment in the WebSphere cell, you
can omit the -de option.
- To stop your deployment environment, you have two options:

- Run the BPMConfig command passing it the name of the configuration properties
file that contains the configuration properties for your deployment environment. For example: 
BPM\_home\bin\BPMConfig -stop my\_environment.properties
BPM\_home/bin/BPMConfig.sh -stop my\_environment.properties
- Run the BPMConfig command specifying the profile, deployment environment
name, user name and password with the command. For example:
BPM\_home\bin\BPMConfig -stop -profile DmgrProfile [-de De1] -username DmgrAdmin -password mypasswordBPM\_home/bin/BPMConfig.sh -stop -profile DmgrProfile [-de De1] -username DmgrAdmin -password mypasswordIf
there is only one deployment environment in the WebSphere cell, you can omit the
-de option.