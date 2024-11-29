# SMO body
structure

- The WSDL message has
a single message part that is defined
by an element: The SMO body has a single child element with a
name the same as the part element name, and the type is the same as
the part element type. This applies to WSDL operations that follow
the document literal wrapped style. The SMO body for the following
WSDL message example has one child element named operation1,
with a type the same as the type of the operation1 element
that is declared in or referred to from the WSDL: <wsdl:message name="operation1RequestMsg">
    <wsdl:part element="tns:operation1" name="operation1Parameters"/>
</wsdl:message>
- All other WSDL message
formats: The SMO body has one child
element for every WSDL message part. The element name is the same
as the part name, and the element type is the effective type of the
WSDL message part.The SMO body for the following WSDL message example
has two child elements, arg1 and arg2,
both of type string:<wsdl:message name="operation2RequestMsg">
    <wsdl:part type="xsd:string" name="arg1"/>
    <wsdl:part type="xsd:string" name="arg2"/>
</wsdl:message>