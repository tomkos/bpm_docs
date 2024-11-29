# Configuring a Web Service Integration component in the desktop Process Designer (deprecated)

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

If the web service uses the SSL protocol, the certificate that is used by the target host must be
installed in the Business Automation Workflow
environment. If the certificate is not installed, you get a No trusted certificate is
found error when you try to discover the WSDL implementation properties.

Ensure
that you know whether the service that you are invoking requires any
additional SOAP headers in web service messages. Conversely, if the
web service has to process the request message, for example, for the
security information, contact the web service provider to ensure that
they can support your header.

If the web service uses X509 client
and server certificates for both encrypting and signing the request,
the certificates must be added to the IBM Business Automation Workflow keystore.
In addition, configuration changes must be made to the 100Custom.xml file
as described in Setting up message-level encryption.

## Procedure

1. In Process Designer, create
an integration service for the process application.
2. Drag a Web Service Integration component from the palette
to the diagram, and click the component to open the properties.
3 Specify the location and properties of the web serviceWSDL file by clicking the Implementation propertiestab. Select the Discovery Scheme you want fromthe drop-down list. You have two choices, which are explained in thisstep and the following step. From process application settings meansthat you select a configuration from the web service server configurationsas shown by the following sub steps.
    1. In the Web Service field, select
the web service from the web services available. If no web services
are available, click Use the Process Application Settings
editor to add a server. Then, configure a web service
type server with a WSDL URL, which references a web service.
    2. Select the operation that you want to use from the Operations field.
    3. Select the SOAP protocol version for your web service.
    4 Extract the input and output variables from the WSDLfile that are needed by the web service by clicking GenerateTypes . Note: If a business object representinga discovered type already exists in the hierarchy of toolkit dependencies(direct dependencies or toolkits dependent on toolkits), it is notre-created. However, to refer to that business object, an applicationor toolkit must have a direct dependency on the snapshot of the toolkitthat contains the business object. You must add the direct dependency,if it does not exist. You can map the inputand output variables in two ways. In the Properties view,select the Data Mapping tab and click the "Auto-mapweb service connector input (or output) parameters" icon. You canalso manually create the variables by using the functions in the Variables tab.Then, you can map these variables to the web service input and outputparameters in the Data Mapping section.Ifyour web service integration component calls an inbound web servicethat is created in Business Automation Workflow , youmust generate the types again in the following cases.
        - The inbound web service uses a business object that is defined
in the System Data Toolkit. The namespace of that business object
uses a host name and a port specification. The types must be generated
again for business objects (complex types) if the inbound web service's
host name or port is changed in this situation.
        - The Target namespace scheme field is changed
to the Per snapshot name value. The namespace
of the WSDL file uses the snapshot name once you select this option.
You must generate the types again for business objects (complex types)
each time you create a snapshot for the inbound web service.
4 Provide inline configuration , theother choice from the Discovery Scheme field,means that you specify your own web service configuration as shownin the following sub steps.

1 Enter a value in the WSDL URI field. You can enter a URL, or use the Registry Explorer to discoverit. If you use the Registry Explorer, the WSDLURL , Protected WSDL , Username ,and Password fields are populated automatically.If you enter the URL manually, you must also provide the other informationabout the WSDL file if needed.
    1. Click Browse to start the Registry Explorer,
and then select the registry type from the list.
    2. Select a registry URL or enter a new one.
    3. For protected web services, enable the Is Protected check
box, and provide the user name and password, and click Next.
    4. Enter the name of the web service and click Search
services. You can include wildcard characters in the name;
for a UDDI registry, use a percent sign (%), for a WebSphere Service
Registry and Repository registry use an asterisk (*).
    5. Select a web service, click Next to see
detailed information, and then Finish.
2. Click Discover to find the WSDL
file and obtain the list of operations. Then, select an operation
from the list.
3. Select the SOAP protocol version for your web service.
4. Optional: Specify that the endpoint address
URL can be overridden and provide an alternative endpoint address. 
 You might want to specify an alternative endpoint address.
For example, if you have different endpoints for development, test,
staging, and production environments. If your production environment
does not have direct internet access and requests are routed through
a proxy server or gateway, this alternative is also helpful. 
You
can enter the new address as a String value, for example, https://provider.com/services/myService,
or as a JavaScript expression that is wrapped by <#...#>.
5 Extract the input and output variables from the WSDLfile that are needed by the web service by clicking GenerateTypes . Note: If a business object representinga discovered type already exists in the hierarchy of toolkit dependencies(direct dependencies or toolkits dependent on toolkits), it is notre-created. However, to refer to that business object, an applicationor toolkit must have a direct dependency on the snapshot of the toolkitthat contains the business object. You must add the direct dependency,if it does not exist. You can map the inputand output variables in two ways. In the Properties view,select the Data Mapping tab and click the "Auto-mapweb service connector input (or output) parameters" icon. You canalso manually create the variables by using the functions in the Variables tab.Then, you can map these variables to the web service input and outputparameters in the Data Mapping section.Ifyour web service integration component calls an inbound web servicethat is created in Business Automation Workflow , youmust generate the types again in the following cases.

- The inbound web service uses a business object that is defined
in the System Data Toolkit. The namespace of that business object
uses a host name and a port specification. The types must be generated
again for business objects (complex types) if the inbound web service's
host name or port is changed in this situation.
- The Target namespace scheme field is changed
to the Per snapshot name value. The namespace
of the WSDL file uses the snapshot name once you select this option.
You must generate the types again for business objects (complex types)
each time you create a snapshot for the inbound web service.
5. Optional: Add a SOAP header by creating a new
variable in the Variables tab of type SOAPHeader or SOAPHeaders,
then map that variable in the Data Mapping tab
under Properties. For detailed instructions, see Creating implicit SOAP headers for outbound web service integrations. You can
add a SOAP header to a SOAP request, for example, to pass additional
context information to the web service.You can also add SOAP headers
using the Headers tab. This method of adding headers is deprecated.
However, if you have defined the SOAP header in the header section
of a web service integration components use the same type that is
defined in the WSDL file, or use the basic XML schema definition (XSD)
type. Otherwise, you cannot automatically map the SOAP header variable
or change its values from the data mappings section.
6 Click the Security properties tab.Specify the type of security by selecting Use Basic Security or UsePolicy Set . Restriction: If youcreate multiple Web Service integrations that share the same WSDLURI, you must use the same policy set and bindings for each of theintegrations.

1. If you select Use Basic Security,
specify the policy sets that are used by the web service, and provide
the user name and password. Specify the certificate, encryption, and
signature settings for both the client application and the web service
server. These settings ensure the integrity and confidentiality of
the messages that are exchanged with the web service.
2. If you select Use Policy Set,
select the policy set and the policy binding from the drop-down lists.
Policy Set: Specifies the name of the application policy
set. Click Select to choose the policy set.
The list you will see depends on the policies available on the server.
Some default application policy sets include: WSHTTPS default, WSAddressing
default, and Username WSSecurity default. You can also create additional
application policy sets in the WebSphere Application Server Administrative
Console. Deselecting a policy set also removes the policy binding.
More information on policy sets can be found in the WebSphere Application Server Web Services Guide IBM
Redbook.
Policy Binding: Specifies the name of the general client
policy set binding, which contains system-specific configuration parameters
like username and password information. Click Select to
choose the policy binding. The list you will see depends on the policy
set bindings available on the server. Default policy set bindings
include: Client sample and Client sample V2. You can also create additional
policy set bindings in the WebSphere Application Server Administrative
Console. Deselecting removes the policy binding.
7. Configure the input and output mappings for the parameters
in the WSDL file by clicking the Data Mapping properties
tab.