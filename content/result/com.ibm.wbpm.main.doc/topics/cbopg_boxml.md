<!-- image -->

# Business object definition

There are essentially three different forms of XML schema that IBM Business Automation Workflow recognizes as a business object
definition:

- A top-level complex type definition
- A top-level anonymous complex type definition
- A top-level element that references a named complex type

## Top-level complex type definition

```
<complexType name="ProductType">
	<sequence>
		<element name="name" type="string"/>
		<element name="color" type="string" maxOccurs="unbounded"/>
	</sequence>
</complexType>
```

- First, new types can be created using the complex type derivation model (of extension or
restriction).
- Second, new aggregate types can be created using the existing complex types and available simple
types as primitives.
- Third, new complex document definitions can be created, like the aggregate complex types.

## Top-level anonymous complex type definition

```
<element name="Product">
	<complexType>	
		<sequence>
			<element name="name" type="string"/>
			<element name="color" type="string" maxOccurs="unbounded"/>
		</sequence>
	</complexType>
</element>
```

If the imported business objects are all anonymous element definitions, they are ready made to be
included in JService invocations. However, they are not inherently reusable.

## Top-level element referencing a named type

```
<element name="product" type="prod:ProdType"/>
```

- Elements can cohabitate with their complex type definitions in the same XML schema file.
- Elements can cohabitate with their complex type definitions embedded in a WSDL file.
- Elements can be defined in XML schema A.xsd, while their complex type
definition is defined in XML schema file B.xsd.
- Elements can be embedded in a WSDL file, referencing a complex type definition defined in an XML
schema file.

## Example

The example demonstrates all the mechanisms for defining a business object combined together.

```
<schema
	targetNamespace="http://www.app.com/Address"
	xmlns:addr="http://www.app.com/Address"
	xmlns:xs="http://www.w3.org/2001/XMLSchema"
	xmlns="http://www.w3.org/2001/XMLSchema">

	<complexType name="Address">
		<sequence>
			<element name="street1" type="string"/>
			<element name="street2" type="string"/>
			<element name="city" type="string"/>
			<element name="state" type="string"/>
			<element name="zip" type="string"/>
		</sequence>
	</complexType>

	<element name="homeAddress" type="addr:Address"/>
	<element name="workAddress" type="addr:Address"/>
	<element name="otherAddress" type="addr:Address"/>

	<element name="individualContact">
		<complexType>
			<sequence>
				<element name="firstName" type="string"/>
				<element name="lastName" type="string"/>
				<element ref="addr:HomeAddress"/>
				<element ref="addr:WorkAddress"/>
				<element ref="addr:OtherAddress"/>
			</sequence>
		</complexType>
	</element>

	<element name="businessContact">
		<complexType>
			<sequence>
				<element name="name" type="string"/>
				<element ref="addr:WorkAddress"/>
			</sequence>
		</complexType>
	</element>

	<element name="chairmanOfTheBoard">
		<complexType>
			<sequence>
				<element name="startDate" type="date"/>
				<element ref="addr:IndividualContact"/>
				<element ref="addr:BusinessContact"/>
			</sequence>
		</complexType>
	</element>	
</schema>
```

- Elements are defined using named types; anonymous types are discouraged.
- Elements and complex type definitions do not
cohabitate
the same XML schema or WSDL file. This practice discourages type reuse.
- Complex types are defined in XML schema files, not WSDL definitions, creating a type library
like concept. Again,
this
type of definition enables and encourages complex type reuse.
- Element definitions are built as necessary to reference a single complex type definition. For
example, the definition of an element inside the WSDL is a pattern that is encouraged.
- Element definitions typically use the same target namespace as their complex type
definition.