<!-- image -->

# Example of an XSD file

The following code fragment shows the contents
of an example XSD file:

```
<?xml version="1.0" encoding="UTF-8"?><xsd:schema targetNamespace="http://com.ibm.wbit.comptest.controller" 
		xmlns:Q1="http://com.ibm.wbit.comptest.controller" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
<xsd:complexType name="TestResults">
		<xsd:sequence>
			<xsd:element maxOccurs="unbounded" minOccurs="0" name="testSuites" type="Q1:TestSuiteRun"/>
		</xsd:sequence>
		<xsd:attribute name="testProject" type="xsd:string"/>
	</xsd:complexType>

	<xsd:complexType name="TestSuiteRun">
		<xsd:complexContent>
			<xsd:extension base="Q1:TestRun">
				<xsd:sequence>
					<xsd:element maxOccurs="unbounded" minOccurs="0" name="testCases" type="Q1:TestCaseRun">
					</xsd:element>
				</xsd:sequence>

				<xsd:attribute name="tests" type="xsd:int"/>

			</xsd:extension>
		</xsd:complexContent>
	</xsd:complexType>

	<xsd:complexType name="TestCaseRun">
		<xsd:complexContent>
			<xsd:extension base="Q1:TestRun">
				<xsd:sequence>
     	<xsd:element name="result" type="Q1:Severity"/>
      <xsd:element maxOccurs="unbounded" minOccurs="0" name="variations" type="Q1:VariationRun">
					</xsd:element>
				</xsd:sequence>
				<xsd:attribute name="variationCount" type="xsd:int"/>
			</xsd:extension>
		</xsd:complexContent>
	</xsd:complexType>

	<xsd:complexType name="VariationRun">
		<xsd:complexContent>
			<xsd:extension base="Q1:TestRun">
				<xsd:sequence>
     	<xsd:element name="result" type="Q1:Severity"/>
      <xsd:element name="exception" nillable="true" type="xsd:string">
						<xsd:annotation>
							<xsd:documentation>
								This element is used to display the exception of a failure or error.
							</xsd:documentation>
						</xsd:annotation>
					</xsd:element>
				</xsd:sequence>				
			</xsd:extension>
		</xsd:complexContent>
	</xsd:complexType>

	<xsd:simpleType name="Severity">
		<xsd:restriction base="xsd:string">
			<xsd:enumeration value="pass"/>
			<xsd:enumeration value="fail"/>
			<xsd:enumeration value="error"/>
		</xsd:restriction>
	</xsd:simpleType>

    <xsd:complexType name="TestRun">
      	<xsd:attribute name="name" type="xsd:string"/>
	  	<xsd:attribute name="startTime" type="xsd:dateTime"/>
	  	<xsd:attribute name="endTime" type="xsd:dateTime"/>
	  	<xsd:attribute name="result" type="xsd:string"/>
    </xsd:complexType>
</xsd:schema>
```