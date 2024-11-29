# Calling a web service using a SOAP connector

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## About this task

These steps show you how to test your web service.

You
can see the following steps with screen captures from a previous version
in this technote.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a process application in the Designer view.
3. Click the plus sign next to the Implementation category
and select Implementation Service.
4. In the dialog that opens, enter a name and click Finish.
5. Beneath TOOLKITS, expand SystemData and
select Implementation. Locate the Call
WebService via SOAP component and drag it onto the diagram.
6. Drag a Server Scriplet from the
right-side palette to your diagram. Place it to the left of Call
WebService via SOAP.
7. Connect the lines. Start should
connect to the Untitled server scriptlet. The Untitled server
scriptlet should connect to Call WebService via SOAP. Call
WebService via SOAP should connect to End.
8 Select the Call WebService via SOAP component.Select the Data Mapping tab in the Properties view.You should be able to identify all of the inputs required except forthe request input.
    - wsdlURL maps to the URL address.
    - serviceNS maps to the targetNamespace value.
    - serviceName maps to the service
name value.
    - destinationAddress maps to the soap:address
location value.
    - soapAction maps to the soap:operation
soapAction value.
9 The request input includes yourvariable inputs. In this example, we use the server scriptlet to createthe XML input.

1. Open the variables tab and create a new private variable
called request with an XMLElement type.
2. Return to the diagram view and rename the server scriptlet
to Set Request.
3. Select the Implementation tab
from the Properties view for the server scriptlet
and bind the implementation to your request variable. Click Select and
click the request variable from the menu.
4. Copy your entire XML input from soapUI and paste it
into the server scriptlet implementation.
5. Bind your request variable to
the request input of the SOAP Connector. Return to the Data
Mapping section of the Call Web Service via
SOAP component and, using Select,
map request (XMLElement) to the request variable
you just created.
10. In a similar manner, create a variable called response of
type XMLElement, and bind it to the output
of the SOAP Connector; that is, the Call Web Service via
SOAP component. At this point, you should be able to test
your service using hard-coded values.
11 Run the service in debug mode to see the response placedinto your response variable. If it worked correctly, you are readyto add input variables to your service and map them into your requestvariable in the server scriptlet. The following example only has oneinput:

1. Add an input variable to your service.
2. Use the <#= #> notation to include JavaScript in
your server scriptlet, as described in Using scriptlets in script tasks.
For example if your input variable is degreesF, the
implementation code to refer to it would be <#= tw.local.degreesF
#>. Now your service input will determine the input to the
SOAP Connector.
12 Use Xpath to map your response variable into proper outputs.This example uses a single output variable (\_degreesC).

1. Add a Server Script to the end
of your service
2 Use Xpath to map the XML response into the output variables.For example:
    1. This Xpath expression returns a node list of all 'Page' nodes
until the VisioDocument/Pages node:xml.xpath("VisioDocument/Pages/Page");
You might need to experiment with having or not having
a slash at the beginning depending on the structure of the XML.
    2. This Xpath expression returns a node list of all 'Master' nodes
that have the NameU attribute equal to 'Horizontal holder':   xml.xpath("VisioDocument/Masters/Master[@NameU='Horizontal holder']");
    3. In either case, you need to know the node path and namespace.
The following Xpath expression ignores the depth and ignores namespaces.
It is the same as i, except it ignores namespace and depth of 'Page'
node: xml.xpath = "//*[local-name()='Page']";

In any case, the result is a nodelist that can
be used something like: var nodeList = xml.xpath(...);
tw.local.objArray = new tw.object.listOf.myObj();
for (var i=0;i<nodeList.length;i++) {
 var obj = new tw.object.myObj();
 //If name node always exists as a child
 obj.name = nodeList[i].name[0].getText();
 tw.local.objArray[tw.local.objArray.listLength] = obj;
}