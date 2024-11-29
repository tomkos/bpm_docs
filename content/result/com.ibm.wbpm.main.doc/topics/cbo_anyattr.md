<!-- image -->

# Using AnyAttribute to set global attributes for complex types

Similar to the <any/> tag, the occurrence of the <anyAttribute/> tag makes the DataObject
Type isOpen() method return true. Unlike the <any/> tag, however, the
<anyAttribute/> tag does not cause a DataObject to be sequenced because attributes
in XSD are not ordered constructs.

- How do I tell if my DataObject has an anyAttribute tag?

You can easily determine if instances of a DataObject have anyAttribute values set within them by checking the instance properties to see if any of the open properties are attributes.
- How do I get or set anyAttribute values?

Setting an <anyAttribute/> value is done in the same way as setting an <any/> value, but instead of a global element a global attribute is used.
- Valid mappings for data in an anyAttribute

The AnyAttribute tag is similar to the any tag, and is a set of name/value pairs. Consequently, the only valid mapping for anyAttribute is another anyAttribute.