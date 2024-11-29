# Accessing SOAP header information in the SMO

## Introduction

Messages received from a web
services import or export might include
SOAP headers from the original SOAP message. The SOAP headers are
placed in the /headers/SOAPHeader element in
the headers section of the service message object (SMO).

A SOAPHeader element
is a wrapper that contains the original SOAP header as its value element. The element can have zero or more occurrences. The
XML namespace-qualified name of the SOAP header type appears in the name and nameSpace elements
of the SOAPHeader .

## SDO paths for accessing SOAP headers in custom mediations

- To access all SOAP headers present in the SMO:import commonj.sdo.DataObject;
import java.util.List;

DataObject smo = ...
List soapHeaders = smo.getList ("/headers/SOAPHeader");
Iterator it = soapHeaders.iterator ();

while (it.hasNext ())
{
	DataObject wrapper = (DataObject) it.next ();
	Object header = wrapper.get ("value");

	// do something with the header
}The list of SOAP headers might be an empty list.
- To access a SOAP header with a particular name (global element
or type name): import commonj.sdo.DataObject;
import java.util.List;

String headerName = ...
DataObject smo = ...
Object header = smo.get ("/headers/SOAPHeader[name='" + headerName + "']/value");

## Conditions under which SOAP headers are present in
a request or response flow

- The message has been received from a web service import or export.
- The import or export has been configured to
propagate protocol headers.
- The sending application included SOAP headers when creating the
original request.
- An XML schema or WSDL description of the header structures is
present in the mediation module or in the associated
library.Note: The XML schema for WS-Addressing
headers is automatically available.

- If the SOAP binding used by the client maps WSDL message parts
to SOAP headers, the corresponding content appears in the SMO body
rather than in the SOAPHeader element.
- WS-Addressing headers appear in the SMO
WSAHeader and not the SOAPHeader. These headers are read-only and
are not used when sending messages..