# Configuring Business Automation Workflow to use IBM® Business Automation
Machine Learning Server

## Procedure

1. Create an authentication alias for Machine Learning Server by following the instructions in Managing Java 2 Connector Architecture authentication data entries for
JAAS.
2. Optional: Create SSL configuration aliases.
For information about administering SSL configurations, see Creating a Secure Sockets Layer configuration and Retrieving signers from a remote SSL port.
3. Import Machine Learning Server
certificates.
For information about adding a signer certificate to a trust store, see Retrieving signers from a remote SSL port.
4 Configure the 100Custom.xml file. For more informationabout this file, see The 100Custom.xml file and configuration .
    1. Add the following configuration properties to the <server>
element:

<ml-server name="ml-server">
    <!-- 
        ML-Server configurations.  
           
        Use <host> to specify ml-server external hostname.
        Use <port> to specify ml-server expose port.
        Use <auth-alias> for ML-Server authentication. Create the authentication alias on server with the user name and  password configured in the ML-Server then update <auth-alias>.      
        e.g. create MLServer\_Auth\_Alias on server and then update like below.
       	<auth-alias>MLServer\_Auth\_Alias</auth-alias>             
        Use <ssl-config-alias> to specify a custom Secure Sockets Layer (SSL) configuration alias. If one is not specified the default configuration is used.
    -->
    <host></host>
    <port></port>
    <auth-alias></auth-alias>
    <ssl-config-alias></ssl-config-alias>
</ml-server>
5 Configure the Intelligent Task Prioritization service.

1. Make sure that Business Automation Insights has sufficient task
history. Specifically, two or more workers must complete at least 30 task instances for each task
before they can be used as training data. You will get a warning if you do not have enough task
instances when installing Machine Learning Server.
2. Enable the task filter service for Process Portal and Workplace in the resource
provider for mashups by following the instructions in Prioritizing work.
3. Configure the Intelligent Task Prioritization feature in Business Automation Workflow by using the
100Custom.xml file.  Add the following configuration properties to
the <common> element: <common merge="mergeChildren">
        <search-execution merge="mergeChildren">
                <include-flow-object-id-save-search merge="replace">true</include-flow-object-id-save-search>
        </search-execution>
</common>For more information about this file, see The 100Custom.xml file and configuration.
4. Ensure that the .env file SERVICES variable
includes the value nbt (Next Best Task). For example:
SERVICES="nbt"