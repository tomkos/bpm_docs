<!-- image -->

# Designing business object type metadata

## About this task

## Procedure

1. Create an XML schema file with a valid target namespace. This step is used when the instance
metadata is added to the business object definition.
2. Define a named complex type to define each separate piece of metadata that can be added to a
business object. The complex type definition is used to define the structure of the dynamically
typed DataObject that is used to read the instance metadata. The name of the
complex type is used when the instance metadata is added to the business object definition.

## Example

```
<schema>
	targetNamespace="http://www.ibm.com/xmlns/prod/websphere/adapter/psft/
		PSFTBODefinitionASI/7.0.0"
	xmlns:psft="http://www.ibm.com/xmlns/prod/websphere/adapter/psft/
		PSFTBODefinitionASI/7.0.0"
	xmlns:xs="http://www.w3.org/2001/XMLSchema"
	xmlns="http://www.w3.org/2001/XMLSchema"
	elementFormDefault="qualified">

	<complexType name="PSFTBODefinitionASI">
		<sequence>
			<element name="hostname" type="string"/>
			<element name="ipaddress" type="string"/>
		</sequence>
	</complexType>
</schema>
```