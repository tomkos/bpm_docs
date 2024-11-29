# XSD generation pattern for business objects

A type without a name is called an anonymous type. An anonymous type can be specified in the
Advanced Properties section when creating a business object. This property is
not honoured by the generator, which means that a named, complex type will be generated.

You should be careful when you use the properties in the Advanced
Properties and Advanced Parameter Properties sections as the
generated schema may not be as you expected. This may be true for the properties that were specified
as a result of an import of a WSDL or XSD file. These imports may result in compile errors on some
of the generated artifacts when they in turn are brought into Integration Designer. In particular, note that
the Advanced Parameter Properties
Type Name and Type Namespace will be used as opposed
to the values specified by the referenced business object.

The schema you see by clicking View XML Schema may not be an accurate
representation of the XSD as seen in Integration Designer.

For wrapper array types, specified in Advanced Parameter Properties using
the wrap list property, the generated code is inline with the business object. No synchronization
with Integration Designer is done.

In Process Designer, when
you import a web service that has a wrapped array element definition, a dummy business object for
the wrapped array element will be created in addition to the referencing business object having the
same definition in the Advanced Parameter Properties. For example, in the
following code the BenefitMessagesWrapper complex type when imported would create a dummy business
object that serves no purpose since the MemberBenefit business object has the declaration defined
for it under the BenefitMessages property. Although it can be present as a business object, for
clarity you may want to delete it. If you do not delete it, the Integration Designer user will see two complex
types, which could cause confusion.

```
<xsd:schema targetNamespace="http://member.ourgroup.com"
	xmlns:bons0="http://member.ourgroup.com" xmlns:tns="http://member.ourgroup.com">
	<xsd:complexType name="MemberBenefit">
		<xsd:sequence>

			<xsd:element minOccurs="0" name="BenefitMessages"
				type="bons1:BenefitMessagesWrapper">
			</xsd:element>

		</xsd:sequence>
	</xsd:complexType>
	<xsd:complexType name="BenefitMessagesWrapper">
		<xsd:sequence>
			<xsd:element maxOccurs="unbounded" minOccurs="0"
				name="BenefitMessageObject" type="bons1:BenefitMessageObject" />
		</xsd:sequence>
	</xsd:complexType>
	<xsd:complexType name="BenefitMessageObject">
		<xsd:sequence>
			<xsd:element minOccurs="0" name="field1" type="xsd:string" />
			<xsd:element minOccurs="0" name="field2" type="xsd:string" />
		</xsd:sequence>
	</xsd:comple
```