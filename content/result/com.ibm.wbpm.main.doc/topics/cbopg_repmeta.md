<!-- image -->

# Representing business object type metadata

The mechanism that is used to mix in the business object type metadata, is XML schema annotations
and the appInfo structure. This policy, although it requires modification of the
original schema definition, does so in a way that enables the annotations and
appinfo to be easily view toggled, or removed completely. This identification
scheme is done by using the source attribute on the xs:appinfo tag whose value is
the target namespace that defines the business object type metadata.

For example, assume that the following schema was imported into the runtime. The schema describes
a business object, named Product, that includes customer annotations.

```
<schema>
	targetNamespace="http://www.scm.com/ProductTypes"
	xmlns:p="http://www.scm.com/ProductTypes"
	xmlns:xs="http://www.w3.org/2001/XMLSchema"
	xmlns="http://www.w3.org/2001/XMLSchema"
	elementFormDefault="qualified

	<complexType name="Product">
		<annotation>
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