<!-- image -->

# Creating a new WSRR definition

## About this task

## Procedure

1. Expand Service integration > WSRR definitions, in the navigation pane.
The WSRR definitions page is displayed in the content pane, which shows a list of all
the WSRR definitions.
2. Click New.
The WSRR definitions configuration page displays.
3. Complete the following property fields:

WSRR definition name
This is required and must be unique inside the cell. It is the administrative name for this WSRR
definition.
Description
You have the option to enter a description for the definition.
Default WSRR definition
This indicates whether this definition is the default. If this is the first definition you have
created, it will automatically be set as the default. You cannot update the default from this
page.
Timeout of cache
The time (in seconds) after which the results in the WSRR cache expire and will be refreshed.
This can be changed from the default value. If you specify a value of 0 (zero), then results are
never cached. The cache is used for storing information about service endpoints and mediation
policies, retrieved from the registry. 
Connection type
Your only choice is Web service.
4. Click Apply to save these properties.
5. Click Connection properties, under Additional
properties in the content pane.
The Connection properties configuration page displays.
6 Complete the following property fields: Connection type This is set when the registry definition is created, and cannot be changed. Registry URL The URL to be used to connect to the WSRR instance. The default value is:http://localhost:9080/WSRRCoreSDO/services/WSRRCoreSDOPort If you want toretrieve endpoints from WSDL that has SOAP 1.2 bindings, you must use Version 7.0 or later versionsof the web service interface URL, which is generally:http://<server>:<port>/WSRR7\_0/services/WSRRCoreSDOPort . Note: If youcall the Version 7.0 URL from a client generated for a previous version of WSRR, the client mightfail if it cannot correctly process the data that is returned. You must use Version 7.0or later versions of the web service interface URL if you want to look up any of the followingendpoint types: In this case, the interface URL is generally:http://<server>:<port>/WSRR7\_0/services/WSRRCoreSDOPort , whereWSRR7\_0 is the version number. Authentication alias The alias to be used to authenticate with the WSRR instance. SSL Configuration The Secure Sockets Layer (SSL) configuration to be used to communicate with a secured WSRRinstance.
    - Manually defined MQ endpoints with associated interfaces
    - Manually defined JMS endpoints with associated interfaces
    - Manually defined HTTP endpoints with associated interfaces
7. Click Apply to save these properties.
8. Click Test Connection to test the connection to the WSRR instance that
has been defined.
If successful the following message is displayed:
The test connection operation for WSRR definition myWSRRDef  was successful
9. Click Save to apply your changes to the master configuration.
10. Click Save again to complete the procedure.

## Results