<!-- image -->

# Designing the WTX map and related artifacts

When defining the business object, the complex type definition needs to
have a corresponding element. Without an element, WTX creates an XML structure
which does not contain a document root. This XML is not valid and not deserializable
by the WTXDataBinding. Hence, when creating a business object, a corresponding
element definition needs to be created. Create the element based on the guidelines
as follows:

- The element name has to be the same as the business object name
- The element namespace is the business object namespace + "wtx"
- List the target namespace and a prefix for the element namespace in the
schema.

For the given complex type, Customer.xsd, as follows:

```
1	<?xml version="1.0" encoding="UTF-8"?>
2	<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
3	            targetNamespace="http://www.ibm.com/crm"
4	            xmlns:bons="http://www.ibm.com/crm">
5	  <xsd:complexType name="Customer">
6	    <xsd:sequence>
7	      <xsd:element minOccurs="0" name="id" type="xsd:string"/>
8	      <xsd:element minOccurs="0" name="firstName" type="xsd:string"/>
9	      <xsd:element minOccurs="0" name="lastName" type="xsd:string"/>
10	    </xsd:sequence>
11	  </xsd:complexType>
12	</xsd:schema>
```

The element is CustomerElement.xsd, as follows:

```
13	<?xml version="1.0" encoding="UTF-8"?>
14	<schema xmlns="http://www.w3.org/2001/XMLSchema" 
15	        xmlns:bons="http://www.ibm.com/crm" 
16	        targetNamespace="http://www.ibm.com/crm/wtx" 
17	        elementFormDefault="qualified"
18	        xmlns:p="http://www.ibm.com/crm/wtx" >
19	
20	  <import namespace="http://www.ibm.com/crm" schemaLocation="Customer.xsd"/>
21	  <element name="Customer" type="bons:Customer"/>
22	</schema>
```