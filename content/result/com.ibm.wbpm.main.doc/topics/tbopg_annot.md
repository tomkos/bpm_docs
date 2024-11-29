<!-- image -->

# Annotating a business object definition

## About this task

To annotate the business object definition follow these
guidelines.

## Procedure

1. If the part of the business object definition that the instance metadata is to be attached to
does not already have an annotation, add one. If it already has an annotation, use the existing
one.
2. Create a separate xs:appinfo tag within the xs:annotation
tag, and define the source attribute to the namespace defined by the business object type metadata
being added.
3. Inside the xs:appinfo tag, define a QName, using a target namespace prefix,
followed by the name of the complex type definition. Append the attribute QName defined with
xmlns: followed by the previously used target namespace prefix. Set the value of
this QName attribute to the target namespace of the business object type metadata being used.
4. Add the structure and instance data mandated by the business object type metadata definition.
Close all tags as appropriate.

## Example

Once the object is imported in, it is identified to need a set of PeopleSoft annotations. This
example shows the same business object definition with the PeopleSoft metadata added.

```
<schema>
	targetNamespace="http://www.scm.com/ProductTypes"
	xmlns:p="http://www.scm.com/ProductTypes"
	xmlns:xs="http://www.w3.org/2001/XMLSchema"
	xmlns="http://www.w3.org/2001/XMLSchema"
	elementFormDefault="qualified

	<complexType name="Product">
		<annotation>
			<appinfo source="http://www.ibm.com/xmlns/prod/websphere/Adapter/PSFT">
				<psft:PSFTMetadata 
					xmlns:psft="http://www.ibm.com/xmlns/prod/websphere/Adapter/PSFT">
					<hostname>mumbai</hostname>
					<ipaddress>9.29.1.1</ipaddress>
				<psft:PSFTMetadata>
			</appInfo>
			<appInfo>
				<SCMEditor value="Bottom" type="Anchor"/>
			</appInfo>
			<documentation>
				Describes the SCM Product
			</documentation>
		</annotation>

		<sequence>
			<element name="id" type="ID"/>
			<element name="description" type="string" default="DefaultDescription"/>
			<element name="sku" type="p:Sku"/>
		</sequence>
	</complexType>

	<simpleType name="Sku">
		<restriction base="string">
			<pattern value="\d{3}-[A-Z]{2}"/>
		</restriction>
	</simpleType>
</schema>
```