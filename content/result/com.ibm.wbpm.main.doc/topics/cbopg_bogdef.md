<!-- image -->

# Business graph model definition

The templated business graph is created by extending the business graph
complex type that is provided by the business object framework runtime and adding an element
delegating to the original business object. The diagram shows a UML model for the business graph.
The business graph is abstract, providing just the standard set of headers that are added to the
top-level business object.

Figure 1. Business graph complex type

<!-- image -->

The XML schema model for the abstract business graph XML schema complex type:

```
<schema
	targetNamespace="http://www.ibm.com/xmlns/prod/websphere/bo/6.0.0"
	xmlns:bo="http://www.ibm.com/xmlns/prod/websphere/bo/6.0.0"
	xmlns:sdo="commonj.sdo"
	xmlns:xs="http://www.w3.org/2001/XMLSchema"
	xmlns="http://www.w3.org/2001/XMLSchema"
	elementFormDefault="qualified">

	<import namespace="commonj.sdo" schemaLocation="DataGraph.xsd"/>

	<complexType name="BusinessGraph" abstract="true">
		<sequence>
			<element name="changeSummary" type="sdo:ChangeSummaryType"
				minOccurs="0" maxOccurs="1"/>
			<element name="eventSummary" type="bo:EventSummary"
				minOccurs="0" maxOccurs="1"/>
			<element name="property" type="bo:ValuesType"
				minOccurs="0"/>
		</sequence>
		<anyAttribute namespace="##other" processContents="lax"/>
	</complexType>

	<complexType name="EventSummary">
		<sequence>
			<any namespace="##any" processContents="lax"
				minOccurs="0" maxOccurs="unbounded"/>
		</sequence>
	</complexType>

	<complexType name="ValuesType">
		<complexContent>
			<extension base="ecore:EClass"/>
		</complexContent>
	</complexType>

	<attribute name="name" type="string"/>
</schema>
```

Business graphs are only a high-level concept because they exist to add a set of headers to an
existing top-level business object, and cannot be modeled in a recursive design pattern like
business objects can. Business graphs can be applied to any business object, but upon application,
that business object becomes a top-level business object.

This is an example of a business graph that wraps a business object named ProductCategory,
ProductCategory is a hierarchical business object that contains a child business object named
Product.

```
<schema
	targetNamespace="http://www.scm.com/ProductCategoryTypes/ProductCategoryBG"
	xmlns:pcbg="http://www.scm.com/ProductCategoryTypes/ProductCategoryBG"
	xmlns:pc="http://www.scm.com/ProductCategoryTypes"
	xmlns:bo="http://www.ibm.com/xmlns/prod/websphere/bo/6.0.0"
	xmlns:xs="http://www.w3.org/2001/XMLSchema"
	xmlns="http://www.w3.org/2001/XMLSchema"
	elementFormDefault="qualified">

	<import namespace="http://www.ibm.com/xmlns/prod/websphere/bo/6.0.0"
		schemaLocation="BusinessGraph.xsd"/>

	<import namespace="http://www.scm.com/ProductCategoryTypes"
		schemaLocation="ProductCategoryTypes.xsd"/>

	<complexType name="ProductCategoryBG">
		<complexContent>
			<extension base="bo:BusinessGraph">
				<sequence>
					<element name="verb" minOccurs="0" maxOccurs="1"/>
					<element name="productCategory"
						type="pc:ProductCategory"
						minOccurs="0" maxOccurs="1"/>
				</sequence>
			</extension>
		<complexContent>
	<complexType>
</schema>
```

- The templated business graph are defined using a named complex type that extends the
bo:BusinessGraph schema by restriction (this pattern provides restrictions on the
allowable Verb value).
- The name of the templated business graph is the name of the top-level business object, with the
string "BG" appended.
- The target namespace of the templated business graph is composed of the target namespace of the
business object being wrapped, followed by a "/", named by the complex type of the templated
business graph.
- The templated business graph complex type definition are placed in its own XML schema file whose
name corresponds to the name of the complex type.