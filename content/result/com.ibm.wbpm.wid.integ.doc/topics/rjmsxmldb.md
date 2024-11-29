<!-- image -->

# Business object XML using JMS text message serialization

## Business object defined using an anonymous schema type

If
the business object is defined by a schema using an anonymous type such as
the following code:

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema"
	targetNamespace="http://ModuleTest">
	<xsd:element name="Employee">
		<xsd:complexType>
			<xsd:sequence>
				<xsd:element minOccurs="0" name="name"
					type="xsd:string" />
				<xsd:element minOccurs="0" name="empno"
					type="xsd:string" />
			</xsd:sequence>
		</xsd:complexType>
	</xsd:element>
</xsd:schema>
```

Then the contents of the JMS text message would
be the following code:

```
<?xml version="1.0" encoding="UTF-8"?>
<module:Employee xmlns:module="http://ModuleTest">
	<name>Name1</name>
	<empno>007</empno>
</module:Employee>
```

## Business object defined using a named schema type

If
the business object is defined by a schema using a named type such as the
following code:

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema"
	xmlns:tns="http://ModuleTest" targetNamespace="http://ModuleTest">
	<xsd:element name="Employee" type="tns:EmployeeType"></xsd:element>
	<xsd:complexType name="EmployeeType">
		<xsd:sequence>
			<xsd:element minOccurs="0" name="name" type="xsd:string" />
			<xsd:element minOccurs="0" name="empno" type="xsd:string" />
		</xsd:sequence>
	</xsd:complexType>
</xsd:schema>
```

Then the contents of the JMS text message would
be the following code:

```
<?xml version="1.0" encoding="UTF-8"?>
<module:Employee xmlns:module="http://ModuleTest">
	<name>Name1</name>
	<empno>007</empno>
</module:Employee>
```

## Related concepts

- Prepackaged JMS data format transformations
- JMS function selectors

## Related reference

- Overview of JMS, MQ JMS and generic JMS bindings
- Data handlers
- Working with the simple JMS data bindings
- Prepackaged JMS and MQ fault selectors