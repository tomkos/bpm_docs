<!-- image -->

# Using Rational Application Developer to generate a web service
proxy for a web services application

## Before you begin

Before generating a web service proxy, you must have previously
exported the WSDL and XSD files that describe the BPEL process or
human task web services interfaces from the WebSphere environment
and copied them to your client programming environment.

## About this task

- HTTP transport layer
- JMS transport layer

## Procedure

1 Add the appropriate WSDL file to your project: A new wsdl directoryand subdirectory structure are created in your project.
    - For BPEL processes (HTTP and JMS transport layers):
        1 Extract the exported file BPEContainer\_nodename\_servername\_WSDLFiles.zip toa temporary directory. Do not change the contents of this directory,and be aware that only the following WSDL and XSD files are used forthe web service proxy generation for interactions with BPEL processes:
            - BFMJAXWSService.wsdl (HTTP) or BFMJMSService.wsdl (JMS)
            - BFMJAXWSInterface.wsdl
            - BFMJAXWSCallbackService.wsdl
            - BFMJAXWSCallbackInterface.wsdl
            - BFMDataTypes.xsd
            - BPCDataTypes.xsd
            - wsa.xsd
    2 Import the subdirectory META-INF from theextracted directory.
        - For HTTP, the directory is: BPEContainer\_nodename\_servername.ear/bfmjaxws.war
        - For JMS, the directory is: BPEContainer\_nodename\_servername.ear/bfmjaxwsjms.jar
- For human tasks (HTTP transport layer only):

1 Extract the exported file TaskContainer\_nodename\_servername\_WSDLFiles.zip toa temporary directory. Do not change the contents of this directory,and be aware that only the following WSDL and XSD files are used forthe web service proxy generation for interactions with human tasks:
    - HTMJAXWSService.wsdl
    - HTMJAXWSInterface.wsdl
    - HTMJAXWSCallbackService.wsdl
    - HTMJAXWSCallbackInterface.wsdl
    - HTMDataTypes.xsd
    - BPCDataTypes.xsd
    - wsa.xsd
2. Import the subdirectory META-INF from the
extracted directory: TaskContainer\_nodename\_servername.ear/htmjaxws.war.
2. Select the BFMJAXWSService.wsdl or
the BFMJMSService.wsdl file in the newly-created wsdl directory.
3. Right-click and choose Web services > Generate client. Before
continuing with the remaining steps, ensure that the server has started.
4. On the Web Services window, click Next to
accept all the defaults.
5. On the WebSphere JAX-WS Web Service Client Configuration window,
click Finish to accept all the defaults.
6. Optional: For the HTTP transport layer only:
Redo steps 2 to 5 of this procedure with HTMJAXWSService.wsdl and
overwrite all the files if you are prompted.

## Results