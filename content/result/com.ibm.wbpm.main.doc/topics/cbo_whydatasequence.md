<!-- image -->

# Why do I need to know a DataObject has a Sequence?

A DataObject that is not sequenced allows random order set access. This functions like a Map
where all the keys are set to the same values. It does not matter in what order the keys were set,
the data in the map is the same, and would be serialized to XML identically.

When a DataObject is sequenced, the order in which the data was set is recorded in the Sequence,
much like adding data to a List. This provides two ways to access the data, by name/value pairs (the
DataObject APIs) and by order in which it was set (the Sequence APIs). You can use the DataObject
set(...) or Sequence add(...) APIs to preserve the structure. This ordering affects the way that the
XML is serialized.

Take for example, the <all/> tag XSD. When the set methods are called in the following order
it produces the following XML when serialized:

```
DataObject all = ...
	all.set("element1", "foo");
	all.set("element2", "bar");

<?xml version="1.0" encoding="UTF-8"?>
<p:All xsi:type="p:All" 
 xmlns:xsi=http://www.w3.org/2001/XMLSchema-instance 
 xmlns:p="http://All">
  <element1>foo</element1>
  <element2>bar</element2>
</p:All>
```

If instead, the set methods are called in the opposite order, then the following XML is produced
when the business object is serialized:

```
DataObject all = ...
	all.set("element2", "bar");
	all.set("element1", "foo");

<?xml version="1.0" encoding="UTF-8"?>
<p:All xsi:type="p:All" 
 xmlns:xsi=http://www.w3.org/2001/XMLSchema-instance 
 xmlns:p="http://All">
  <element2>bar</element2>
  <element1>foo</element1>
</p:All>
```

If the order of the Sequence is ever changed, then the Sequence class has basic add, remove, and
move methods to allow the user to alter the order of Sequence.