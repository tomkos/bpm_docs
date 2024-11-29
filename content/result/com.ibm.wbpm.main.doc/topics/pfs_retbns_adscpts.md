# Using the Administration scripts to access the retriever MBeans

These administration scripts are located in the
PFS\_INSTALL\_DIR/ibmProcessFederationServer/wlp-ext/adminScripts
directory.

## Preparing your environment for the Administration scripts

- JAVA\_HOME : A directory where the Java runtime environment is installed. If
this environment variable is not defined then the PATH is checked for a java
executable.
- WLP\_HOME : The Liberty wlp directory. This variable is
used to locate the restConnector.jar file in
WLP\_HOME/clients. If this environment variable is not defined, then it is
assumed that the restConnector.jar file is located in
./clients.
- PFS\_ADMIN\_HOME : The directory that contains the
PFS\_Admin\_Command.jar file. If this environment variable is not defined, then
it is assumed that this file is located in the current directory.

## Using the Administration scripts

- Using the listBpdRetrieverUniqueIDs script This script displays thelist of the unique retriever IDs of the running BPD retriever MBeans. Syntax Options The following table lists all the options available:Table 1. Options of the listBpdRetrieverUniqueIDs script Option Description Required -help Displays information about the options, the attributes that can be queried, and theproperties that must be set in the options file. No -file filename Specifies the absolute path name of the option file that must contain the followingproperties: Yes -verbose Verbose output of the script execution. No

This script displays the
list of the unique retriever IDs of the running BPD retriever MBeans.

    - Linux/Unix: listBpdRetrieverUniqueIDs.sh -file optionsFile
[-verbose]
    - Windows: listBpdRetrieverUniqueIDs.bat -file optionsFile
[-verbose]

Options

| Option         | Description                                                                                                                                                                                                                                                                                                                                                                                                           | Required   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| -help          | Displays information about the options, the attributes that can be queried, and the properties that must be set in the options file.                                                                                                                                                                                                                                                                                  | No         |
| -file filename | Specifies the absolute path name of the option file that must contain the following properties: host=<Process Federation Server host name> port=<HTTPS server port> user=<user with administrative role defined on the server> password=<user password> trustStoreFile=<name and path of the truststore for SSL connection with the server> trustStoreType=<truststore type> trustStorePassword=<truststore password> | Yes        |
| -verbose       | Verbose output of the script execution.                                                                                                                                                                                                                                                                                                                                                                               | No         |

- Using the listBpelRetrieverUniqueIDs script This script displays thelist of the unique retriever IDs of the running BPEL retriever MBeans. Syntax Options The following table lists all the options available:Table 2. Options of the listBpelRetrieverUniqueIDs script Option Description Required -help Displays information about the options, the attributes that can be queried, and theproperties that must be set in the options file. No -file filename Specifies the absolute path name of the option file that must contain the followingproperties: Yes -verbose Verbose output of the script execution. No

This script displays the
list of the unique retriever IDs of the running BPEL retriever MBeans.

- Linux/Unix: listBpelRetrieverUniqueIDs.sh -file optionsFile
[-verbose]
- Windows: listBpelRetrieverUniqueIDs.bat -file optionsFile
[-verbose]

Options

| Option         | Description                                                                                                                                                                                                                                                                                                                                                                                                           | Required   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| -help          | Displays information about the options, the attributes that can be queried, and the properties that must be set in the options file.                                                                                                                                                                                                                                                                                  | No         |
| -file filename | Specifies the absolute path name of the option file that must contain the following properties: host=<Process Federation Server host name> port=<HTTPS server port> user=<user with administrative role defined on the server> password=<user password> trustStoreFile=<name and path of the truststore for SSL connection with the server> trustStoreType=<truststore type> trustStorePassword=<truststore password> | Yes        |
| -verbose       | Verbose output of the script execution.                                                                                                                                                                                                                                                                                                                                                                               | No         |

- Using the listCaseRetrieverUniqueIDs script This script displays thelist of the unique retriever IDs of the running Case retriever MBeans. Syntax Options The following table lists all the options available:Table 3. Options of the listCaseRetrieverUniqueIDs script Option Description Required -help Displays information about the options, the attributes that can be queried, and theproperties that must be set in the options file. No -file filename Specifies the absolute path name of the option file that must contain the followingproperties: Yes -verbose Verbose output of the script execution. No

This script displays the
list of the unique retriever IDs of the running Case retriever MBeans.

- Linux/Unix: listCaseRetrieverUniqueIDs.sh -file optionsFile
[-verbose]
- Windows: listCaseRetrieverUniqueIDs.bat -file optionsFile
[-verbose]

Options

| Option         | Description                                                                                                                                                                                                                                                                                                                                                                                                           | Required   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| -help          | Displays information about the options, the attributes that can be queried, and the properties that must be set in the options file.                                                                                                                                                                                                                                                                                  | No         |
| -file filename | Specifies the absolute path name of the option file that must contain the following properties: host=<Process Federation Server host name> port=<HTTPS server port> user=<user with administrative role defined on the server> password=<user password> trustStoreFile=<name and path of the truststore for SSL connection with the server> trustStoreType=<truststore type> trustStorePassword=<truststore password> | Yes        |
| -verbose       | Verbose output of the script execution.                                                                                                                                                                                                                                                                                                                                                                               | No         |

- Using the monitorBpdRetriever script You can use this script toretrieve the attributes value of a running BPD retriever MBean. Syntax Options The following table lists all the options available:Table 4. Options of the monitorBpdRetriever script Option Description Required -help Displays information about the options, the attributes that can be queried, and theproperties that must be set in the options file. No -file filename Specifies the absolute path name of the option file that must contain the followingproperties: Yes -id Specifies the unique retriever ID of the BPD retriever MBean that this script accessesremotely. This unique retriever ID can be retrieved with scriptlistBpdRetrieverUniqueIDs . Yes -attribute One attribute among: Yes -verbose Verbose output of the script execution. No

You can use this script to
retrieve the attributes value of a running BPD retriever MBean.

- Linux/Unix: monitorBpdRetriever.sh -file optionsFile -id
BPD\_uniqueRetrieverID -attribute attributeName
[-verbose]
- Windows: monitorBpdRetriever.bat -file optionsFile -id
BPD\_uniqueRetrieverID -attribute attributeName
[-verbose]

Options

| Option         | Description                                                                                                                                                                                                                                                                                                                                                                                                                   | Required   |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| -help          | Displays information about the options, the attributes that can be queried, and the properties that must be set in the options file.                                                                                                                                                                                                                                                                                          | No         |
| -file filename | Specifies the absolute path name of the option file that must contain the following properties:  host=<Process Federation Server host name>  port=<HTTPS server port>  user=<user with administrative role defined on the server>  password=<user password>  trustStoreFile=<name and path of the truststore for SSL connection with the server>   trustStoreType=<truststore type>  trustStorePassword=<truststore password> | Yes        |
| -id            | Specifies the unique retriever ID of the BPD retriever MBean that this script accesses remotely.  This unique retriever ID can be retrieved with script listBpdRetrieverUniqueIDs.                                                                                                                                                                                                                                            | Yes        |
| -attribute     | One attribute among:  connectionTimeout readTimeout internalRestUrlPrefix federatedSystemInfo federatedSystemStatusInfo lastSavedSearch                                                                                                                                                                                                                                                                                       | Yes        |
| -verbose       | Verbose output of the script execution.                                                                                                                                                                                                                                                                                                                                                                                       | No         |

- Using the monitorBpelRetriever script You can use this script toretrieve the attributes value of a running BPEL retriever MBean. Syntax Options The following table lists all the options available:Table 5. Options of the monitorBpelRetriever script Option Description Required -help Displays information about the options, the attributes that can be queried, and theproperties that must be set in the options file. No -file filename Specifies the absolute path name of the option file that must contain the followingproperties: Yes -id Specifies the unique retriever ID of the BPEL retriever MBean that this script accessesremotely. This unique retriever ID can be retrieved with scriptlistBpelRetrieverUniqueIDs . Yes -attribute One attribute among: Yes -verbose Verbose output of the script execution. No

You can use this script to
retrieve the attributes value of a running BPEL retriever MBean.

- Linux/Unix: monitorBpelRetriever.sh -file optionsFile -id
BPEL\_uniqueRetrieverID -attribute attributeName
[-verbose]
- Windows: monitorBpelRetriever.bat -file optionsFile -id
BPEL\_uniqueRetrieverID -attribute attributeName
[-verbose]

Options

| Option         | Description                                                                                                                                                                                                                                                                                                                                                                                                                   | Required   |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| -help          | Displays information about the options, the attributes that can be queried, and the properties that must be set in the options file.                                                                                                                                                                                                                                                                                          | No         |
| -file filename | Specifies the absolute path name of the option file that must contain the following properties:  host=<Process Federation Server host name>  port=<HTTPS server port>  user=<user with administrative role defined on the server>  password=<user password>  trustStoreFile=<name and path of the truststore for SSL connection with the server>   trustStoreType=<truststore type>  trustStorePassword=<truststore password> | Yes        |
| -id            | Specifies the unique retriever ID of the BPEL retriever MBean that this script accesses remotely.  This unique retriever ID can be retrieved with script listBpelRetrieverUniqueIDs.                                                                                                                                                                                                                                          | Yes        |
| -attribute     | One attribute among:  connectionTimeout readTimeout internalRestUrlPrefix federatedSystemInfo federatedSystemStatusInfo lastSavedSearch                                                                                                                                                                                                                                                                                       | Yes        |
| -verbose       | Verbose output of the script execution.                                                                                                                                                                                                                                                                                                                                                                                       | No         |

- Using the monitorCaseRetriever script You can use this script toretrieve the attributes value of a running Case retriever MBean. Syntax Options The following table lists all the options available:Table 6. Options of the monitorCaseRetriever script Option Description Required -help Displays information about the options, the attributes that can be queried, and theproperties that must be set in the options file. No -file filename Specifies the absolute path name of the option file that must contain the followingproperties: Yes -id Specifies the unique retriever ID of the Case retriever MBean that this script accessesremotely. This unique retriever ID can be retrieved with scriptlistCaseRetrieverUniqueIDs . Yes -attribute One attribute among: Yes -verbose Verbose output of the script execution. No

You can use this script to
retrieve the attributes value of a running Case retriever MBean.

- Linux/Unix: monitorCaseRetriever.sh -file optionsFile -id
Case\_uniqueRetrieverID -attribute attributeName
[-verbose]
- Windows: monitorCaseRetriever.bat -file optionsFile -id
Case\_uniqueRetrieverID -attribute attributeName
[-verbose]

Options

| Option         | Description                                                                                                                                                                                                                                                                                                                                                                                                                   | Required   |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| -help          | Displays information about the options, the attributes that can be queried, and the properties that must be set in the options file.                                                                                                                                                                                                                                                                                          | No         |
| -file filename | Specifies the absolute path name of the option file that must contain the following properties:  host=<Process Federation Server host name>  port=<HTTPS server port>  user=<user with administrative role defined on the server>  password=<user password>  trustStoreFile=<name and path of the truststore for SSL connection with the server>   trustStoreType=<truststore type>  trustStorePassword=<truststore password> | Yes        |
| -id            | Specifies the unique retriever ID of the Case retriever MBean that this script accesses remotely.  This unique retriever ID can be retrieved with script listCaseRetrieverUniqueIDs.                                                                                                                                                                                                                                          | Yes        |
| -attribute     | One attribute among:  connectionTimeout readTimeout internalRestUrlPrefix federatedSystemInfo federatedSystemStatusInfo                                                                                                                                                                                                                                                                                                       | Yes        |
| -verbose       | Verbose output of the script execution.                                                                                                                                                                                                                                                                                                                                                                                       | No         |