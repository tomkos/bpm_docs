<!-- image -->

# Adding key attributes

## About this task

You can either edit the Display name of
the key attribute, or set another attribute of the referenced Data
Type by clicking Change which invokes the Add
key attribute window.

Adding a key attribute can be done several
ways:

- Using the menu of the relationship
- Using the Add key attribute button on the
Role Section Toolbar

After
clicking the Add key attribute button, the
Select key attributes table opens.

The Select key attributes
table shows the attributes available in the data type which is used
for the role. There is the option to choose either a single attribute
or to select multiple attributes. You also can select attributes from
a child data type. The table contains only the key attributes that
can be added to the role. Key attributes that are already assigned
to the role are not in the table. You can edit the entries in the
Index column if a data element is of type Field (Array).
In this case, it is possible to select a dedicated element of the
array (for example, /attribute2[4]/) with the
index. Additionally, it is possible to clear the index value meaning
that no dedicated element of the array is selected and value /attribute2/ 
is selected.

Even though the Select key attribute table displays
all elements of an object type, such as business objects, not all
can be selected as a key attribute.  In general, all elements of kind xsd:element or xsd:attribute (see
column Kind ) can be used. If a limiting rule
prevents an element to become a key attribute, then the row cannot
be selected and the reason will be displayed in the status line under
the table.

## Limitations for key attributes

- Fields of the following simple data types
    - xsd:date
    - xsd:dateTime
    - xsd:time
    - xsd:hexBinary
    - xsd:NMTOKENS
- Fields that are derived types of these data types

- xsd:date
- xsd:dateTime
- xsd:time
- xsd:hexBinary
- xsd:NMTOKENS
- Fields of anonymous data types (xsd:anytype, xsd:anySimpleType)
- xsd:any elements
- Fields that are defined inside an xsd:choice structure
- Business object attributes of anonymous data type (xsd:anyAttribute)
- Fields that are defined as soap:enc data
types in Interfaces (wsdl files)
- Fields that are included in doc-lit wrapped style wrapper elements
in Interfaces (wsdl files)
- Fields that are defined inside an xsd:list structure
are not handled as an array data type. The index value cannot be selected
for such a key attribute.