<!-- image -->

# Resolving property names that contain periods

Property names in Service Data Objects (SDOs) are based on the names of the elements and
attribute that are generated from in the XSD. Business objects will handle the "." character
properly, with one exception: if an XSD has a single cardinality property named "<name>.<#>"
and a multiple cardinality property named "<name>".

An XPath such as "foo.0" would not resolve properly if there is a single cardinality property
named "foo.0" and multiple cardinality property named "foo". In this case, the single cardinality
Property named "foo.0" would be the one resolved. Although this should be a rare occurrence, you can
avoid it entirely if you use the "foo[1]" syntax to access their multiple cardinality property. SDOs
will not support the "." syntax for indexing, so you should use the "[]" for indexing.

- Serializing and deserializing unions with xsi:type

In XSD, a union is a way to merge the lexical spaces of several simple datatypes known as members.