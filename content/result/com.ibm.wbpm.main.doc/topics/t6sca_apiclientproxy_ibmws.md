<!-- image -->

# Using the wsimport command-line tool to
generate a web service proxy for a web services application

## Before you begin

Before generating a web service proxy, you must
have previously exported the WSDL files that describe the BPEL process
or human task web services APIs from the WebSphere® environment, and copied them
to your client programming environment.

## About this task

- HTTP transport layer
- JMS transport layer

## Procedure

1. Generate a web service proxy for the Business Process Choreographer
web services API. You can merge both proxies into one common
directory (for example, proxy-bpc) and overwrite existing files if
you are prompted.The following example applies
to the HTTP transport layer. The myService1.wsdl and myService2.wsdl files
contain interface definitions of custom BPEL processes, or human tasks,
or both. In addition, <bfm\_location> and <htm\_location> can
be obtained from the WSDL <port> element in
the BFMJAXWSService.wsdl and HTMJAXWSService.wsdl files. wsimport.bat BFMJAXWSService.wsdl myService1.wsdl myService2.wsdl
 -d proxy-bfm 
 -wsdllocation <bfm\_location>

wsimport.bat HTMJAXWSService.wsdl myService1.wsdl myService2.wsdl
 -d proxy-htm 
 -wsdllocation <htm\_location>
The following example
applies to the JMS transport layer. The myService1.wsdl and myService2.wsdl files
contain interface definitions of custom BPEL processes. In addition, <bfm\_location> can
be obtained from the WSDL <port> element in
the files BFMJMSService.wsdl. wsimport.bat BFMJMSService.wsdl myService1.wsdl myService2.wsdl
 -d proxy-bfm 
 -wsdllocation <bfm\_location>
2. Include the generated class files in your project.