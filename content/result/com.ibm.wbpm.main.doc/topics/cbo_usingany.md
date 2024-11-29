<!-- image -->

# Using Any to set global elements for complex types

An occurrence of the any tag makes the DataObject Type isOpen() method and the isSequenced()
method return true. If the value for maxOccurs is > 1 on an any tag, it has no effect on the
structure of the DataObject; it is only used as information during validation. Similarly, the
occurrence of multiple any tags in a type does not change the structure of the DataObject; they are
used only for validating the location of open data that was set.

- How do I know if my DataObject has an any tag?

You can easily determine if instances of a DataObject have any values set within them by checking the instance properties to see if any of the open properties are attributes.
- How do I get/set any values?

Performing a get on data that was set in an any field can be done in the same manner as any other element value if the name is known.
- Valid mappings for data in an any attribute

An <any/> tag is a set of name/value pairs. The only valid mapping that can be determined at design time for <any/> is another <any/> or anyType that has the same maxOccurs value.