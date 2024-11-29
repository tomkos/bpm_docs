# Business object advanced properties

The advanced properties used for serialization purposes
are automatically created with appropriate values when you create
a business object or import a WSDL file with business objects. It
is recommended that you leave these serialization values as they are.
Only change a value if you are an advanced user who has a need to
override a value. You should be very knowledgeable of all the standard
XML elements as defined by the W3C's XML Schema.
You should also have read the web services compatibility topic and
the XSD generation pattern for business objects topic which are linked
to at the end of this topic. These topics specify restrictions that
apply to XML schemas interacting with this product and within this
product.

A change will only affect this particular business
object. If you had a process application with 100 business objects
and you wanted to override an element such as the target namespace
in the XML representation for all business objects then you would
need to make 100 changes.

Any change to serialization values should be tested. If you are using the business object in
inbound or outbound web services, for example, this would mean testing those web services after your
change. If you are using Integration Designer and your business object
is used in an Advanced Integration service, you should test the Advanced Integration
service.

| Advanced properties                                                                | Advanced parameter properties                                                                                                                                                                   |
|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Anonymous type Element name Element namespace Exclude from XML Namespace Type name | Anonymous list type Exclude from XML List item name List type name Maximum occurrences Minimum occurrences Name Namespace Nillable Node Type Order Time zone Type name Type namespace Wrap list |

## Anonymous list type

This
property sets whether the type of the wrapper is named or anonymous.
The default value is false (named type). This property is available
only when the parameter is a list and the wrap list property is true.

## Anonymous type

Schemas
can be built with sets of named types, for example, an InvoiceType.
Then elements can be declared such as invoiceCanadian that reference
those types. However, if you only need to reference a type once then
there is considerable coding overhead. An anonymous type is used for
these cases of a single reference.

To specify the value for an anonymous type, select Anonymous Type and
select true or false. The default value is false. If
you have read the XSD generation pattern for business objects topic you will also know that the true
value is not honoured by the generator. Save your work. Click View XML
Schema. Your output should be similar to the following sample.

```
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:tns="http://EH" targetNamespace=http://EH" 
		elementFormDefault="qualified" attributeFormDefault="unqualified">
	<xs:element name="employee">
		<xs:complexType>
			<xs:sequence>        
				<xs:element name="employeeNumber" nillable="false" type="xs:string" minOccurs="0" maxOccurs="1" />
				<xs:element name="firstName" nillable="false" type="xs:string" minOccurs="0" maxOccurs="1" />
				<xs:element name="lastName" nillable="false" type="xs:string" minOccurs="0" maxOccurs="1" />
			</xs:sequence>
		</xs:complexType>
	</xs:element>
</xs:schema>
```

## Element name

If the anonymous
type property is set to true, this property places the anonymous type
under an element with the specified name.

Use the default value
unless it is strictly necessary to make a change.

## Element namespace

This
property sets the namespace of the container element.

Use
the default value unless it is strictly necessary to make a change.

## Exclude from XML

In
most cases you would leave this setting in its default value of false,
which will include your 				business object or parameter in the XML
representation. However a type could define 				some instance fields
that you might not want to serialize to an XML representation. 				For
example, an instance field that has no equivalent in XML as it refers
to an 				internal running process. You may also not want to serialize
a lot of data when you 				know the web service could take some of
the data and calculate values itself thus 				improving performance
by reducing the data transferred.

To exclude
a business object or parameter from the XML representation, select Exclude
from XML and select true. Save
your work. Click View XML Schema.

```
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:tns="http://EH" targetNamespace=http://EH" 
		elementFormDefault="qualified" attributeFormDefault="unqualified">
	<xs:element name="employee">
		<xs:complexType>
			<xs:sequence>        
				<xs:element name="firstName" nillable="false" type="xs:string" minOccurs="0" maxOccurs="1" />
				<xs:element name="lastName" nillable="false" type="xs:string" minOccurs="0" maxOccurs="1" />
			</xs:sequence>
		</xs:complexType>
	</xs:element>
</xs:schema>
```

## List item name

This property
sets the name for a wrapped list item. This property is available
only when the parameter is a list and the wrap list property is true.

Use
the default value unless it is strictly necessary to make a change.
The default value is the name of the type of the list elements.

## List type name

This property
sets the name of the complex type that encapsulates a wrapped list.
The property is therefore valid only for a wrapped list that is not
anonymous.

Use the default value unless it is strictly necessary
to make a change.

## Maximum occurrences

This
property sets the maximum number of times that the parameter occurs.
The default value is 1. This property corresponds to maxOccurs in
the XML schema.

Use the default value unless it is strictly
necessary to make a change.

## Minimum occurrences

This
property sets the minimum number of times that the parameter occurs.
The default value is 0. This property corresponds to minOccurs in
the XML schema.

Use the default value unless it is strictly
necessary to make a change.

## Name

This property overrides the
name of the serialized parameter with the name that you specify. The
default value is the name of the parameter. This property corresponds
to the name attribute in the XML schema.

Use
the default value unless it is strictly necessary to make a change.

## Namespace

If you set the
namespace for the business object, this property changes the target
namespace. The target namespace defines explicitly the elements that
belong to this instance of the namespace. You might want to change
the target namespace if you imported a WSDL file and the target namespace
for your business object was changed on importation. If you set the
property for a parameter, it overrides the serialized element namespace
for that parameter.

To rename the target namespace, select Namespace and
enter the target namespace you prefer. For example: http://www.mycorporation.com/employees.
Save your work. Click View XML Schema. Your
output should be similar to the following sample.

```
<xs:schema targetNamespace="http://www.mycorporation.com/employees"
	elementFormDefault="qualified" attributeFormDefault="unqualified">
	<xs:complexType name="employee">
		<xs:sequence>
			<xs:element name="employeeNumber" type="xs:int" minOccurs="0"
				maxOccurs="1" nillable="false" />
			<xs:element name="firstName" type="xs:string" minOccurs="0"
				maxOccurs="1" nillable="false" />
			<xs:element name="lastName" type="xs:string" minOccurs="0"
				maxOccurs="1" nillable="false" />
		</xs:sequence>
	</xs:complexType>
	<xs:element name="employee" type="tns:employee" />
</xs:schema>
```

## Nillable

This property determines
whether the parameter can have a null value.

Use the default
value unless it is strictly necessary to make a change.

## Node Type

Nodes in an XML document can be defined as elements or attributes. In most cases, an element type
is used which is the default, so you do not need to set it explicitly. However, you can set it to
use an attribute.

To change the type to an attribute,
select Node Type and select Attribute.
Save your work. Click View XML Schema. Your
output should be similar to the following sample.

```
<xs:schema targetNamespace="http://EH" elementFormDefault="qualified"
	attributeFormDefault="unqualified">
	<xs:complexType name="employee">
		<xs:sequence>
			<xs:element name="firstName" type="xs:string" minOccurs="0"
				maxOccurs="1" nillable="false" />
			<xs:element name="lastName" type="xs:string" minOccurs="0"
				maxOccurs="1" nillable="false" />
		</xs:sequence>
		<xs:attribute name="employeeNumber" type="xs:int" />
	</xs:complexType>
	<xs:element name="employee" type="tns:employee" />
</xs:schema>
```

## Order

Order explicitly sets the
order of the complex type's elements. Usually you would leave the
order in the XML representation of the business object exactly as
it is in the business object editor. However, you might want to change
the order if the external web service changed and required the elements
to be presented in a specific way.

To change the order of a
complex type's elements, select each element and add a number to the Order field
to specify the order you want in the XML representation. For example,
suppose the order of an employee complex type is employeeNumber, firstName
and lastName and you needed to change it to accommodate a web service
order of lastName, firstName and then employeeNumber. You would set
employeeNumber to 2, firstName to 1 and lastName to 0. Save your work.
Click View XML Schema. Your output should be
similar to the following sample.

```
<xs:schema targetNamespace="http://EH" elementFormDefault="qualified"
	attributeFormDefault="unqualified">
	<xs:complexType name="employee">
		<xs:sequence>
			<xs:element name="lastName" type="xs:string" minOccurs="0"
				maxOccurs="1" nillable="false" />
			<xs:element name="firstName" type="xs:string" minOccurs="0"
				maxOccurs="1" nillable="false" />
			<xs:element name="employeeNumber" type="xs:int" minOccurs="0"
				maxOccurs="1" nillable="false" />
		</xs:sequence>
	</xs:complexType>
	<xs:element name="employee" type="tns:employee" />
</xs:schema>
```

## Time zone

This property sets
the time zone to use when serializing a date parameter. The property
is not used in WSDL generation or schema creation but it is used to
display date and time values. The default value is CLIENT. The other
valid values are SERVER and UTC.

Use the default value unless
it is strictly necessary to make a change.

## Type name

This property sets
the qualified name of the type for the business object or parameter.

Use
the default value unless it is strictly necessary to make a change.

## Type namespace

This property
overrides the type namespace of the serialized XSD type with the namespace
that you specify.

Use the default value unless it is strictly
necessary to make a change.

## Wrap list

This property determines
whether to create an array wrapper type to contain a list. The default
value is false, which means that the list is not wrapped. A list is
an array and it is specified when List is selected
as an attribute. You might use this field if you wanted to encapsulate
the array. A wrapper type can be anonymous and the name of the list
items can be overridden. If you have not selected List for
a variable, this field and other fields with list in their name are
disabled.

## Related reference

- Web services compatibility
- XSD generation pattern for business objects