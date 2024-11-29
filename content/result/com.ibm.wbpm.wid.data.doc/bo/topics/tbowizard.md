<!-- image -->

# Creating business objects in Integration Designer

## About this task

## Procedure

1. Click File > New > Business Object.
2 The New Business Object wizard windowopens. Choose an existing module or library or click New tocreate one. Restriction: Do not use the following keywords asvariable names for business objects: Using these keywords might cause errors that are difficultto diagnose.
    - childrenCache
    - declaredClass
    - inherited
    - items
    - listAllSelectedIndices
    - \_objectPath
    - \_systemCallbackHandle
3. Optional: By default, business objects are created
as global complex types. If your integration scenario requires a global
element in the schema file, select the option Create the
business object as an element. If you select this option,
the business object is created as a global element with an anonymous
type, for example <xsd:element name="MyBusinessObject">
		<xsd:complexType>
			<xsd:sequence />
		</xsd:complexType>
	</xsd:element>For more information about manually
creating a global element that is based business objects and why you
would want to do this, see IBM Technote 1399071.
4. To pre-populate your business objects, click Next instead
of Finish.
5. The Derived Business Object window
opens. If they are available, you might choose to populate the new
business object with fields from one or more existing business objects.
6. Click Finish. The
new business object is created and available in the Business Integration
view.

## Other business object creation options

- Creating private business objects

Private business objects are business objects that are contained within other business objects.  They are only visible to the containing business object, thereby making them "private". A business object field can have either a simple  type or a business object type. All business objects are indexed and therefore can be reused in numerous places as required. If you want to use a complex type (that is, a business object type) that will only ever be used once, a private business object can be used for this purpose. In XSD terms, a private business object is simply an element with an anonymous complex type defined in a business object (that is, a complex type definition).  Or more simply, it is a business object field that defines an anonymous complex type instead of referencing a named complex type.
- Creating abstract business objects

An abstract  business object is like an abstract java class. You cannot get an xml instance of an abstract business object at run time, however an abstract business object can be inherited by a regular business object. It is good practice to use an inherited business object rather than the abstract business object.