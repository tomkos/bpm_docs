<!-- image -->

# ElementFormDefault definition

```
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema  xmlns:xs="http://www.w3.org/2001/XMLSchema" targetNamespace="uri:my\_namespace">
	<xs:element name="myDoc"> 
		<xs:complexType> 
			<xs:sequence>
				<xs:element name="subnode" type="xs:string" maxOccurs="1" />
			</xs:sequence>
		</xs:complexType> 
	</xs:element>
</xs:schema>
```

```
<ns0:mydoc xmlns:ns0="uri:my-namespace">
	<ns0:subnode/>
</ns0:mydoc>
```

```
<ns0:mydoc xmlns:ns0="uri:my-namespace">
	 <subnode/>
</ns0:mydoc>
```

```
<xs:schema  xmlns:xs="http:// www.w3.org/2001/XMLSchema" targetNamespace="uri:my-namespace" elementFormDefault="qualified">
```

```
<xs:element name="subnode" maxOccurs="1"  form="qualified"/>
```