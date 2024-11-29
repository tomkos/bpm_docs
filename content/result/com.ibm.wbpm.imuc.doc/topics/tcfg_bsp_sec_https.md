<!-- image -->

# Allowing insecure access to Heritage Process Portal

The Business Space component is configured to be accessed by HTTPS
by default. 
You can change the protocol from the default or
back to the default by running a script.

You should require HTTPS communication from the browser to
the server when accessing any IBM® Business Automation Workflow user
interface. Typically, these user interfaces are available for authenticated users only and
authentication credentials are submitted with every request; for example, user IDs and passwords, or
the LTPA cookie. These authentication credentials should be protected from eavesdropping and
therefore never be transmitted over unencrypted connections. If you have an SSL offloading
requirement, see the httpsIndicatorHeader configuration in Web container customer properties in the WebSphere® Application
Server documentation.

## About this task

This task describes how to change the protocol by running the
configBSpaceTransport.py script.

Enforcement of HTTPS with
cumulative fix 2017.03 also enabled additional security configuration: setting the secure flag for
LTPA and HTTP session cookies. This new default configuration instructs browsers to send these
sensitive cookies over secure connections only. If you configure Business Space or Heritage Process Portal to be available over non-secure HTTP connections, these cookies must
not be marked with the secure flag. The configBSpaceTransport.py script has
been enhanced to disable the secure flag for these two cookies for the
allowhttp parameter and to enable the secure flag for these two cookies for the
httpsonly parameter.

```
AdminTask.setBPMProperty(['-de', 'De1', '-name', 'ProcessServer.MarkCookiesSecureOnSecureConnections', '-value', 'false'])"
```

## Procedure

- If you have a stand-alone server, run wsadmin.sh or wsadmin.bat fromthe stand-alone\_profile/bin/ directory on theserver. Tip: By default, the command applies to the currentserver and node. If you want to specify a different location, usethe optional -serverName and -nodeName parameters.

<!-- image -->

<!-- image -->

<!-- image -->

    - To allow only HTTPS connections to Heritage Process Portal, enter the following command:wsadmin -user user\_name -password password 
        -f install\_root/BusinessSpace/scripts/configBSpaceTransport.py -httpsonly
    - To allow HTTP connections to Heritage Process Portal, enter the following command:wsadmin -user user\_name -password password 
        -f install\_root/BusinessSpace/scripts/configBSpaceTransport.py -allowhttp
- If you have a network deployment environment, you must run wsadmin.sh or wsadmin.bat from thedmgr\_profile/bin/ directory on the server to update the cluster where theBSpaceEAR application is deployed. First, stop all the servers in your deployment environment, including the deployment manager and the node agents, then runthe command in disconnected mode by using the wsadmin -conntype none option. Where application\_cluster is the applicationcluster of your IBM Business Automation Workflow deployment environment.

<!-- image -->

<!-- image -->

<!-- image -->

- To allow only HTTPS connections to Heritage Process Portal, enter the following
command:wsadmin -user user\_name -password password 
        -f install\_root/BusinessSpace/scripts/configBSpaceTransport.py -httpsonly 
        -clusterName application\_cluster
- To allow HTTP connections to Heritage Process Portal, enter the following
command:wsadmin -user user\_name -password password 
        -f install\_root/BusinessSpace/scripts/configBSpaceTransport.py -allowhttp 
        -clusterName application\_cluster

Where application\_cluster is the application
cluster of your IBM Business Automation Workflow deployment environment.

## Results

## Related information

- configureBPMTransportSecurity command