<!-- image -->

# JAXB and EJBs

A valid generated XML Schema Definition (XSD) is not necessarily
valid in the context of generated Java beans based on it.

## How XSD and JAXB differ

Because an XSD is
consists of valid XML code, you should not assume that you can generate
JavaBeans from it, which could be your goal if you work with the Java
Architecture for XML Binding (JAXB). For example, you can have an
element and an attribute with the same name and at the same level
in XSD code. But converting this code to a Java bean, which has different
rules governing its behavior, will result in an error.

## How to modify an XSD to be acceptable to JAXB

If
you are facing the previous problem, there are four ways you could
modify the generated code to make it acceptable to the JAXB standard:

- Change the name of the element
- Change the name of the attribute
- Use JAXB annotations to change the Java property that the element
maps to
- Use JAXB annotations to change the Java property that the attribute
maps to.

For example, suppose there is some XSD code containing
an element and attribute with the same name, field2.
You could use JAXB annotations to modify the Java property for the
attribute to field4 as shown below.

```
<?xml version="1.0" encoding="UTF-8"?> 
   <xsd:schema targetNamespace="http://JAXBExport" 
    xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
    xmlns:jaxb="http://java.sun.com/xml/ns/jaxb" 
    jaxb:version="2.0"> 
    <xsd:complexType name="Test"> 
     <xsd:sequence> 
      <xsd:element minOccurs="0" name="field1" type="xsd:string"> 
      </xsd:element> 
      <xsd:element minOccurs="0" name="field2" type="xsd:string" /> 
     </xsd:sequence> 
     <xsd:attribute name="field2" type="xsd:string"> 
      <xsd:annotation> 
       <xsd:appinfo> 
        <jaxb:property name="field4"/> 
       </xsd:appinfo> 
      </xsd:annotation> 
     </xsd:attribute> 
    </xsd:complexType> 
   </xsd:schema>
```