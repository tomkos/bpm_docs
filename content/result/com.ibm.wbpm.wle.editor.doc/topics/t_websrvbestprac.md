# Using web services for inter-process application communication

## When you need to enable web services interoperability

By
default, type definitions in the WSDL of an exposed web service use
array wrappers for business objects with list-type properties, however
the XSD schema representation of the business object provided by Process Designer,
does not use array wrappers. This affects the runtime behavior of
the process application calling the web service.

```
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:tns="http://AFWSTK1" 
           targetNamespace="http://AFWSTK1" elementFormDefault="qualified" attributeFormDefault="unqualified">
  <xs:complexType name="MyBO\_3">
    <xs:sequence>
      <xs:element name="listOfMyBO\_2" nillable="false" type="tns:MyBO\_2" minOccurs="0" maxOccurs="unbounded" />
      <xs:element name="item" nillable="false" type="tns:MyBO\_2" minOccurs="0" maxOccurs="1" />
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="MyBO\_2">
    <xs:sequence>
      <xs:element name="myString" nillable="false" type="xs:string" minOccurs="0" maxOccurs="1" />
    </xs:sequence>
  </xs:complexType>
  <xs:element name="MyBO\_3" type="tns:MyBO\_3" />
</xs:schema>
```

```
<schema attributeFormDefault="unqualified" elementFormDefault="qualified" 
        targetNamespace="http://AFWSTK1" xmlns="http://www.w3.org/2001/XMLSchema" 
        xmlns:impl="http://AFWSPTK/MyWebService\_2.tws" xmlns:impl1="http://AFWSTK1" 
        xmlns:xsd="http://www.w3.org/2001/XMLSchema">
...
  <complexType name="MyBO\_3">
    <sequence>
      <element maxOccurs="1" minOccurs="0" name="listOfMyBO\_2" nillable="false" type="impl1:ArrayOf\_MyBO\_2"/>
      <element maxOccurs="1" minOccurs="0" name="item" nillable="false" type="impl1:MyBO\_2"/>
    </sequence>
  </complexType>
  <complexType name="MyBO\_2">
    <sequence>
      <element maxOccurs="1" minOccurs="0" name="myString" nillable="false" type="xsd:string"/>
    </sequence>
  </complexType>
  <complexType name="ArrayOf\_MyBO\_2">
    <sequence>
      <element maxOccurs="unbounded" minOccurs="0" name="item" nillable="true" type="impl1:MyBO\_2"/>
    </sequence>
  </complexType>
...
```

## Enabling web services interoperability and reuse of
the same business objects of a common toolkit

- Changing the way how WSDLs are generated
- Using advanced parameter properties for your business objects

```
<enable-advanced-parameter-properties-for-wsdl merge="replace">true
</enable-advanced-parameter-properties-for-wsdl>
```

```
<common merge="mergeChildren">
  ...
    <webservices merge="mergeChildren">
    ...
    </webservices>
  ...
</common>
```