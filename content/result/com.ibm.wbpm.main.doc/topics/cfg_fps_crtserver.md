# Creating a process federation server

## Procedure

1 Create the server by using the ibmProcessFederationServertemplate. The following message indicates that the process federationserver was created successfully in the pfs\_install\_root /usr/servers directory.Server server\_name created
    1. Go to the command line and change the directory to the pfs\_install\_root/bin directory.
    2. Enter the following command. server create server\_name --template=ibmPfs:ibmProcessFederationServerserver\_name must
contain only Unicode alphanumeric characters, for example, 0-9, a-z,
A-Z), underscore (\_), dash (-), plus (+), and period (.). The name
cannot begin with a dash or period. Your file system, operating system,
or compressed file directory might impose additional restrictions.

```
Server server\_name created
```

2 Test Process Federation Server bystarting and stopping the server.

1. Start the server. Enter the following command
in the pfs\_install\_root/bin directory.server start server\_name 
The following messages indicate that the server started
successfully.Starting server server\_name
Server server\_name started
2. Check the server logs in the pfs\_install\_root/usr/servers/server\_name/logs directory.
Look for the following message in the messages.log file.[AUDIT   ] CWWKF0011I: The server server\_name is ready to run a smarter planet.
3. Stop the server. Enter the following command
in the pfs\_install\_root/bin directory.server stop server\_name 
The following messages indicate that the server stopped
successfully.Stopping server server\_name
Server server\_name stopped

## Results

## What to do next