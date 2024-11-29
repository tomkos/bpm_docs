<!-- image -->

# Converting annotation into DataObjects

## About this task

To convert an annotation into a
DataObject.

## Procedure

1. Obtain an annotation.
2. Use the BOTypeMetadata to convert that annotation into an SDO
DataObject.
The BOTypeMetadata implementation is available as a singleton using the
BOTypeMetadata.INSTANCE instance.

## Example

```
<schema>
	targetNamespace="http://www.ibm.com/xmlns/prod/websphere/botm/7.0.0"
	xmlns:xs="http://www.w3.org/2001/XMLSchema"
	xmlns="http://www.w3.org/2001/XMLSchema"
	elementFormDefault="qualified">

	<complexType name="VerbInfo">
		<sequence>
			<element name="verbInfo" type="string"/>
		</sequence>	
	</complexType>
</schema>
```

One of the capabilities of the business object framework is the ability to add additional
supported verbs and accompanying metadata to enable meta-driven capabilities at run time. The
capability is supported through the use of verbs and the VerbInfo metadata to annotate the verbs
with additional metadata. The following example demonstrates the places where the VerbInfo metadata
would be added for each of the possible Verb values.

```
<schema
	targetNamespace="http://www.scm.com/ProductCategoryTypes/ProductCategoryBG"
	xmlns:pcbg="http://www.scm.com/ProductCategoryTypes/ProductCategoryBG"
	xmlns:pc="http://www.scm.com/ProductCategoryTypes"
	xmlns:sdo="commonj.sdo"
	xmlns:bo="http://www.ibm.com/xmlns/prod/websphere/bo/7.0.0"
	xmlns:xs="http://www.w3.org/2001/XMLSchema"
	xmlns="http://www.w3.org/2001/XMLSchema"
	elementFormDefault="qualified">

	<import namespace="http://www.ibm.com/xmlns/prod/websphere/bo/7.0.0"
		schemaLocation="BusinessGraph.xsd"/>

	<import namespace="commonj.sdo"
		schemaLocation="DataGraph.xsd"/>

	<import namespace="http://www.scm.com/ProductCategoryTypes"
		schemaLocation="ProductCategoryTypes.xsd"/>

	<complexType name="ProductCategoryBG">
		<complexContent>
			<extension base="bo:BusinessGraph">
				<sequence>

					<element name="verb"
						minOccurs="0" maxOccurs="1">
						<simpleType>
							<restriction base="string">
								<enumeration value="Create">
									<annotation>
										<appinfo source="http://www.ibm.com/xmlns/prod/websphere/botm/7.0.0">
											<botm:VerbInfo 
												xmlns:botm="http://www.ibm.com/xmlns/prod/websphere/botm/7.0.0">
												<verbInfo>Metadata relating to Create</verbInfo>
											</botm:VerbInfo>
										</appinfo>
									</annotation>
								</enumeration>
								<enumeration value="Retrieve">
									<annotation>
										<appinfo source="http://www.ibm.com/xmlns/prod/websphere/botm/7.0.0">
											<botm:VerbInfo 
												xmlns:botm="http://www.ibm.com/xmlns/prod/websphere/botm/7.0.0">
												<verbInfo>Metadata relating to Retrieve</verbInfo>
											</botm:VerbInfo>
										</appinfo>
									</annotation>
								</enumeration>
							</restriction>
						</simpleType>
					</element>

					<element name="productCategory" type="pc:ProductCategory"
						minOccurs="0" maxOccurs="1"/> 

				</sequence>
			</extension>
		</complexContent>
	</complexType>
	
	<element name="productCategoryBG" type="pcbg:ProductCategoryBG"/>

</schema>
```