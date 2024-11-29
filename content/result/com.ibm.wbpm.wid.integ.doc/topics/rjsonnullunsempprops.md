<!-- image -->

# Handling JSON null and empty arrays and objects

JSON data has the concept of null and empty arrays and
objects. This section explains how each of these concepts is mapped
to the data object concepts of null and unset.

## Null values

JSON has a special value called
null which can be set on any type of data including arrays, objects,
number and boolean types.

```
34	{				        Schema types
35	    "id":null,				(integer)
36	    "firstName": null,			(string)
37	    "address": null,			(Address complex type with maxOccurs = 1)
38	    "homeAddresses":null		(Address complex type with maxOccurs > 1)
39	    "phoneNumbers": null		(string with maxOccurs > 1)
40	}
```

Considering the previous example where JSON data
with a null value is parsed into a data object, the following is true:

- id - If the property is defined as nillable in the schema, then
it will be set to null. If the property is not defined as nillable,
it will throw an exception.
- firstName - The null value is set on the property.
- address - If the property is defined as nillable in the schema,
then it will be set to null. If the property is not defined as nillable,
it will throw an exception.
- homeAddresses - Schema does not allow nillable for this property
hence it will be unset.
- phoneNumbers - This property has to be defined as nillable in
the schema or else it will throw an exception.

When serializing to JSON, if a value of a property in
the data object is null, then it will be serialized as a JSON null.

## Unset property

Non-existence of a property
from the JSON data maps to an unset attribute in the data object space.
If the property in the data object is not set (unset), then the property
will not appear in the JSON data.

## Empty property

The JSON empty concept applies
for arrays and objects as shown below.

```
41	{
42	    "address":{}
43	     "homeAddresses":[]
44	      "phoneNumbers":[]
45	}
```

In the case of address, an empty address data object
is created. Data object does not have a concept of empty lists. Hence,
no action is taken on the data object for those two properties.