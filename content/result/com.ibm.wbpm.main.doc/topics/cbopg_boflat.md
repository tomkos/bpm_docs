<!-- image -->

# Flat and hierarchical business objects

## Flat business object

A flat business object contains one or more simple attributes and a list of supported
verbs. A simple attribute represents one value, such as a String or Integer or Date. All simple
attributes have single cardinality. If the business object is an application-specific business
object, a flat business object can represent one entity in an application or in a technology
standard.

## Hierarchical business object

Hierarchical business object definitions define the structure of multiple related
entities, encapsulating not only each individual entity but also aspects of the relationship between
entities.
In
addition to containing at least one simple attribute, a hierarchical business object has one or more
attributes that are complex (that is, the attribute itself contains one or more business objects,
called child business
objects).
The business object that contains the complex attribute is called the parent business
object.

- Single cardinality - When an attribute in a parent business object represents a single child
business
object.
The type of the attribute is set to the name of the child business object, and the cardinality is
set to one.
- Multiple cardinality - When an attribute in the parent business object represents an array of
child business objects. The type of the attribute is set to the name of the child business object,
and the cardinality is set to n.

In turn, each child business object can contain attributes that contain a child business object,
or an array of business objects, and so on. The business object at the top of the hierarchy, which
itself does not have a parent, is called the top-level business object. Any single business
object, independent of its child business objects that it might contain (or that might contain it),
is called an individual business object.

## Example

The following example helps illustrate the difference between a flat business object and
hierarchical business object. The diagram contains a flat business object, named Product. The
business object is represented in memory with the Service Data Object type
commonj.sdo.DataObject (unless it was statically generated).
This
flat business object has a set of attributes that are modeled as XML schema simple types as well as
an attribute that is modeled as a list of simple types.

The diagram also illustrates a Product business object, in combination with the ProductCategory
business object, to create a more complex hierarchical business object. This business object has
both a top-level business object (ProductCategory), as well as a contained business object
(Product).

Figure 1. Comparison of flat and hierarchical business objects

<!-- image -->

Here is example of the flat business object definition for the Product business object. The
Product business object defines two properties, Name and
Inventory, that are typed by the XML schema simple types
xs:string and xs:int. In addition, Product also demonstrates the
definition of List property Color, which is a List of xs:string
simple types.

```
<schema>
	targetNamespace="http://www.scm.com/ProductTypes"
	xmlns:xs="http://www.w3.org/2001/XMLSchema"
	xmlns="http://www.w3.org/2001/XMLSchema">

	<complexType name="Product">
		<sequence>
			<element name="name" type="string"/>
			<element name="inventory" type="int"/>
			<element name="color" type="string" maxOccurs="unbounded"/>
		</sequence>
	</complexType>
</schema>
```

Here is example of the hierarchical business object ProductCategory. The definition defines two
different business objects, ProductCategory and Product. The hierarchical ProductCategory business
object defines the property, Name and also defines a List of business objects of
type Product or ProductCategory.

```
<schema>
	targetNamespace="http://www.scm.com/ProductCategoryTypes"
	xmlns:pc="http://www.scm.com/ProductCategoryTypes"
	xmlns:xs="http://www.w3.org/2001/XMLSchema"
	xmlns="http://www.w3.org/2001/XMLSchema">
	elementFormDefault="qualified">

	<complexType name="ProductCategory">
		<sequence>
			<element name="name" type="string"/>
			<choice>
				<element name=="productCategory" 
					type="pc:ProductCategory"
					maxOccurs="unbounded"/>
				<element name=="product" 
					type="pc:Product"
					maxOccurs="unbounded"/>
			</choice>
		</sequence>
	</complexType>

	<complexType name="Product">
		<sequence>
			<element name="name" type="string"/>
			<element name=="inventory" type="int"/> 
			<element name=="color" type="string" maxOccurs="unbounded"/>
		</sequence>
	</complexType>

</schema>
```