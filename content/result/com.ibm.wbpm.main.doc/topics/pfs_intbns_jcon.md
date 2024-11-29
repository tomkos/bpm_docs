# Using JConsole to access the MBeans

## About this task

Whatever your choice, you use the JConsole in the same way.

## Procedure

1 Launch JConsole using the following syntax. Example :jconsole -J-Djava.class.path=C:/IBM/Java/lib/jconsole.jar;C:/IBM/Java/lib/tools.jar;C:/IBM/wlp/clients/restConnector.jar -J-Djavax.net.ssl.trustStore=C:/IBM/wlp/usr/servers/pfs/resources/security/key.jks -J-Djavax.net.ssl.trustStorePassword=password -J-Djavax.net.ssl.trustStoreType=jks
    - On
Windows:jconsole -J-Djava.class.path=<JAVA\_HOME>/lib/jconsole.jar;                                                                
                                <JAVA\_HOME>/lib/tools.jar;
                                <PFS\_INSTALL\_DIR>/wlp/clients/restConnector.jar
           -J-Djavax.net.ssl.trustStore=trustStoreAbsoluteName
           -J-Djavax.net.ssl.trustStorePassword=trustStorePassword
           -J-Djavax.net.ssl.trustStoreType=keystoreType
    - On
UNIX:jconsole -J-Djava.class.path=<JAVA\_HOME>/lib/jconsole.jar:
                                <JAVA\_HOME>/lib/tools.jar:
                                <PFS\_INSTALL\_DIR>/wlp/clients/restConnector.jar
           -J-Djavax.net.ssl.trustStore=trustStoreAbsoluteName 
           -J-Djavax.net.ssl.trustStorePassword=trustStorePassword         
           -J-Djavax.net.ssl.trustStoreType=trustStoreType
    - trustStoreAbsoluteName is the name of a truststore prefixed with its absolute
path.
    - trustStoreType is the type of the truststore.
    - trustStorePassword is the password for accessing the content of the
truststore.

```
jconsole -J-Djava.class.path=C:/IBM/Java/lib/jconsole.jar;C:/IBM/Java/lib/tools.jar;C:/IBM/wlp/clients/restConnector.jar 
-J-Djavax.net.ssl.trustStore=C:/IBM/wlp/usr/servers/pfs/resources/security/key.jks 
-J-Djavax.net.ssl.trustStorePassword=password -J-Djavax.net.ssl.trustStoreType=jks
```

2 Provide authentication information for the connection: Example: url : service:jmx:rest://pfsHost.com:9443/IBMJMXConnectorRESTuser : uid=admin,o=defaultWIMFileBasedRealmpassword : admin

1. Select the Remote Process connection.
2. Type the following service URL to connect JConsole to the Liberty REST Connector
exposed by Process Federation Server, with the Process Federation Server host name for
hostname, and the HTTPS port for
port:service:jmx:rest://hostname:port/IBMJMXConnectorREST
3. Type the user name and the password.  The user must be declared as a
Liberty administrative user in the Liberty server.xml file.

```
url : service:jmx:rest://pfsHost.com:9443/IBMJMXConnectorREST
user : uid=admin,o=defaultWIMFileBasedRealm
password : admin
```

3 Go to the MBean tab:

- If you want to monitor a BPD indexer, go to
com.ibm.bpm.federation.server
 > Indexers > BpdIndexers.
- If you want to monitor a BPEL indexer, go to
com.ibm.bpm.federation.server
 > Indexers > BpelIndexers.
- If you want to monitor a BPD retriever, go to
com.ibm.bpm.federation.server
 > Retrievers > BpdRetrievers.
- If you want to monitor a BPEL retriever, go to
com.ibm.bpm.federation.server
 > Retrievers > BpelRetrievers.
- If you want to monitor a Case retriever, go to
com.ibm.bpm.federation.server
 > Retrievers > CaseRetrievers.
4 Click:

- Attributes to view or manage attributes.
- Operation to invoke operations.