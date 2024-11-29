# Discovering and invoking a web service

## About this task

To invoke a web service in the designer, you discover the service and select the operations that
you want to use. Then, set the server that contains the configuration properties that are required
to invoke the service. An external service is generated containing the operations that you selected
in the discovered service and a reference to the server that you selected. Business objects are also
generated based on the WSDL definition.

Service providers update their services periodically, and you might want to rediscover the
updated service so that you can use it. When you discover a service, if an external service
discovered from the same URL already exists in the designer, you can either overwrite the existing
service or create a new one. To get the updated version of the web service, replace the external
service. If you have a service task that calls the external service, the operations and data
mappings are preserved, unless the operation or data is not included in the new version. If the
server connection information is unchanged, you can keep the reference to the server
information.

Complete the following steps to discover an existing web service with a WSDL definition and
generate an external service that you can use in a service flow.

## Procedure

1 Create an external service in one of the following ways:
    - Beside Services in the library navigation, click the plus sign (+).
Select External Service. In the New External Service 
page, choose Java, REST or Web service.
    - In the Service Flow editor, select a Service task.
In the Implementation tab for the service, click New.
2. Select one of the following: 

Web service from URL
Enter the URL or local filesystem path of the web service definition language (WDSL) file. For
example,
https://hostname:port/WebService.wsdl or
file://localhost/c:/WebService.wsdl. Where hostname is the
host name and port is the port number.
Web service from Web Service Server
Select the server that you created for the web service. 

If the WSDL is protected by HTTP basic authentication, specify user name and
password.
3. Each external service maps to a single port type. If the WSDL file has more than one port
type, you can select the port type that the generated external service will map to. Click
Next. 
Important:  Containers: 
Only operations that conform to the document literal wrapped style are supported. Any other
operations are not shown. Port types that do not contain at least one supported operation are also
not shown.
4. The discovered operations for the port type are listed. Select the operations that you
want to include in the external service, and click Next. 
The list of business objects that will be created is displayed, showing the XML type and the
corresponding workflow type.
Note: If a business object representing a discovered type already exists in the hierarchy of toolkit
dependencies (direct dependencies or toolkits dependent on toolkits), it is not re-created. However,
to refer to that business object, an application or toolkit must have a direct dependency on the
snapshot of the toolkit that contains the business object. You must add the direct dependency, if it
does not exist.
5. If the web service was already discovered, you can create a new external service or
replace the existing one. Click Next.
6. If you discovered the web service from a URL, you can set the server that contains the
properties used to invoke the web service. Either select an existing server, or create a new one
based on information in the WSDL definition. Click Finish.