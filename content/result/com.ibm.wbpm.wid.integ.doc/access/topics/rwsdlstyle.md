<!-- image -->

# WSDL binding styles

## Introduction

A WSDL document describes a
web service. A WSDL binding describes how the service is bound to
a messaging protocol, particularly the SOAP messaging protocol. A
WSDL SOAP binding can be either a Remote Procedure Call (RPC) style
binding or a document style binding. A SOAP binding can also have
an encoded use or a literal use. This combination gives you four style
and use models:  RPC encoded,  RPC literal, document encoded, and
document literal. Add to this collection a pattern which is commonly
called the document literal wrapped pattern and you have five binding
styles to choose from when creating a WSDL file.

- The input message has a single part.
- The part is an element.
- The element has the same name as the operation.
- The element's complex type has no attributes.

The following tables illustrate the various WSDL patterns. For a more detailed discussion of this
topic, see Which style of WSDL should I use? .

## RPC styles

Table 1 uses one Java™ method and shows the approximate code that
would result if you run that method through a Java-to-WSDL tool specifying
that you want to generate RPC encoded and RPC literal WSDL files.
The Java method is public void myMethod(int
x, float y);. This method is invoked with 5 as the value
for parameter x and 5.0 for parameter y.

|                  | RPC encoded                                                                                                                                                                                                                                                                                                                                                        | RPC literal                                                                                                                                                                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WSDL Example     | <message name="myMethodRequest"> 	<part name="x" type="xsd:int"/> 		<part name="y" type="xsd:float"/> </message>  <message name="empty"/>  <portType name="PT"> 	<operation name="myMethod"> 		<input message="myMethodRequest"/> 		<output message="empty"/> 	</operation> </portType>  <binding .../>                                                            | <message name="myMethodRequest"> 	<part name="x" type="xsd:int"/> 		<part name="y" type="xsd:float"/> </message>  <message name="empty"/>  <portType name="PT"> 	<operation name="myMethod"> 		<input message="myMethodRequest"/> 		<output message="empty"/> 	</operation> </portType> <binding .../> |
| Instance Message | <soap:envelope> 	<soap:body> 		<myMethod> 			<x xsi:type="xsd:int">5</x> 			<y xsi:type="xsd:float">5.0</y> 		</myMethod> 	</soap:body> </soap:envelope>                                                                                                                                                                                                           | <soap:envelope> 	<soap:body> 		<myMethod> 			<x>5</x> 			<y>5.0</y> 		</myMethod> 	</soap:body> </soap:envelope>                                                                                                                                                                                       |
| Advantages       | The WSDL is about as straightforward as it is possible for a WSDL to be. The operation name appears in the message, so the receiver has an easy time dispatching this message to the implementation of the operation.                                                                                                                                              | The WSDL is still about as straightforward as it is possible for WSDL to be.  The operation name still appears in the message.  The type encoding info is eliminated.  RPC literal is WS-I compliant.                                                                                                  |
| Disadvantages    | You cannot easily validate this message since only the <x ...="">5</x> and <y ...="">5.0</y> lines contain things defined in a schema; the rest of the soap:body content comes from WSDL definitions. The type encoding information (such as xsi:type="xsd:int") can degrade throughput performance. Although it is legal WSDL, RPC encoded is not WS-I compliant. | You still cannot easily validate this message since only the <x ...="">5</x> and <y ...="">5.0</y> lines contain things defined in a schema; the rest of the soap:body content comes from WSDL definitions.                                                                                            |

## Document styles

Table 2 uses one Java method and shows the approximate code that
would result if you run that method through a Java-to-WSDL tool specifying
that you want to generate document literal and document literal wrapped
WSDL files. Again, the Java method
is public void myMethod(int x, float y);. Again,
this method is invoked with 5 as the value for parameter x and
5.0 for parameter y.

The document encoded
style is not WS-I compliant and is not useful, so it is not included
in this evaluation.

|                  | DOC literal *                                                                                                                                                                                                                                                                                                                                                                                                                          | DOC literal wrapped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WSDL Example     | <types> 	<schema> 		<element name="xElement" type="xsd:int"/> 		<element name="yElement" type="xsd:float"/> 	</schema> </types>  <message name="myMethodRequest"> 	<part name="x" element="xElement"/> 	<part name="y" element="yElement"/> </message>  <message name="empty"></message>  <portType name="PT"> 	<operation name="myMethod"> 		<input message="myMethodRequest"/> 		<output message="empty"/> 	</operation> </portType> | <types> 	<schema> 		<element name="myMethod"> 			<complexType> 				<sequence> 					<element name="x" type="xsd:int"></element> 					<element name="y" type="xsd:float"></element> 				</sequence> 			</complexType> 			</element>  			<element name="myMethodResponse"> 				<complexType></complexType> 			</element> 	</schema> </types>  <message name="myMethodRequest"> 	<part name="parameters" element="myMethod"/> </message>  <message name="empty"> 	<part name="parameters" element="myMethodResponse"/> </message> <portType name="PT"> 	<operation name="myMethod"> 		<input message="myMethodRequest"/> 		<output message="empty"/> 	</operation> </portType> |
| Instance Message | <soap:envelope> 	<soap:body> 		<xElement>5</xElement> 		<yElement>5.0</yElement> 	</soap:body> </soap:envelope>                                                                                                                                                                                                                                                                                                                        | <soap:envelope> 	<soap:body> 		<myMethod> 			<x>5</x> 			<y>5.0</y> 		</myMethod> 	</soap:body> </soap:envelope>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Advantages       | You can finally validate this message with any XML validator. Everything within soap:body is defined in a schema.  There is no type encoding information.   Document/literal is WS-I compliant, but with restrictions (see "Disadvantages").                                                                                                                                                                                           | Everything that appears in soap:body is defined by the schema, so you can easily validate this message.   The method name appears in the SOAP message. There is no type encoding information.   Document literal is WS-I compliant, and the wrapped pattern meets the WS-I restriction that the SOAP message's soap:body has only one child.                                                                                                                                                                                                                                                                                                                               |
| Disadvantages    | The operation name in the SOAP message is lost. Without the name, dispatching can be difficult, and sometimes impossible. WS-I only allows one child of soap:body in a SOAP message, but this example has two children.  The WSDL is more complicated.                                                                                                                                                                                 | The WSDL is more complicated still.  If you have overloaded operations, you cannot use the document literal wrapped style.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## Related tasks

- Interoperability with services from other vendors
- Importing WSDL or XSD files
- Exporting WSDL files