# Configuring the Business Space Ajax proxy

## About this task

The Ajax proxy file, proxy-config.xml,
is located in the following location if you are using the environment
that is shipped with IBM® Business Automation Workflow:

profile\_root/BusinessSpace/node\_name/server\_name/mm.runtime.prof/config/proxy-config.xml.

For
issues with the Ajax proxy, see IBM Mashups tech notes at http://www-01.ibm.com/support/search.wss?tc=SSWP9P.

## Procedure

1. Modify the proxy-config.xml file as
needed. For example, if you are changing the timeout
settings for the Business Space Ajax proxy, you modify the proxy:value for socket-timeout.
2. Run the updateBlobConfig command using
the wsadmin scripting client, designating the -serverName and -nodeName parameters
for a stand-alone server or -clusterName for
a cluster, -propertyFileName with the value of
the path for the proxy-config.xml file, and -prefix with
the value Mashups\_. The following example
uses Jython:  
AdminTask.updateBlobConfig('[-serverName server\_name -nodeName node\_name -propertyFileName
"profile\_root/BusinessSpace/node\_name/server\_name/mm.runtime.prof/config/proxy-config.xml"
-prefix "Mashups\_"]')
AdminConfig.save()

The following example uses Jacl: 
$AdminTask
updateBlobConfig {-serverName server\_name -nodeName node\_name -propertyFileName
"profile\_root/BusinessSpace/node\_name/server\_name/mm.runtime.prof/config/proxy-config.xml"
-prefix "Mashups\_"}
$AdminConfig save

- Adding proxy policies to the Business Space Ajax proxy

Add additional proxy policies to the proxy-config.xml file so that Heritage Process Portal works properly in a distributed environment.
- Changing the timeout settings for the Business Space Ajax proxy

Heritage Process Portal uses a proxy component to connect to your Representational State Transfer (REST) services. If REST services are not responsive, update the connection timeout settings to your REST services, depending on the performance of the REST service servers.
- Blocking IP addresses using the Business Space Ajax proxy

The Ajax proxy forwards requests from widgets to your product and target servers, if the servers are remote from the IBM Business Automation Workflow server. The Ajax proxy is configured to be closed by default but provides a default policy that allows access to all endpoints. You can configure the Ajax proxy to restrict access to specific IP addresses.