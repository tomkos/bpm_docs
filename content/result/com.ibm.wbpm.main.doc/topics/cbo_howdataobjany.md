<!-- image -->

# How do I tell if my DataObject has an anyAttribute tag?

DataObject does not provide a mechanism for determining if a DataObject Type has an anyAttribute
tag. DataObjects only have the concept of "open" that applies to both any and <anyAttribute/> and
allows the free additional of any Properties. While it is true that if a DataObject has isOpen() =
true and isSequenced() = false, then it must have an anyAttribute tag, if isOpen() = true and
isSequenced() = true, the DataObject Type might or might not have an anyAttribute tag.

DataObject provides metadata query methods to programmatically answer this and other questions
about the XSD structure that was used to generate the DataObject. The InfoSet model can be queried
if it is necessary to know if the anyAttribute tag is present. Because anyAttribute is singular and
either is or is not true, business objects will also provide a BOXSDHelper hasAnyAttribute(Type)
method to allow determination as to if setting an open attribute on this DataObject would produce a
valid result. The following example code demonstrates these concepts:

```
DataObject dobj = ...

	// Check to see if the type is open, if it isn't then it can't have
	// anyAttribute values set in it.
	boolean isOpen = dobj.getType().isOpen();

	if (!isOpen) return false;  // Does not have anyAttribute values set

	// Open Properties are added to the Instance Property list, but not
	// the Property list, so comparing their sizes can easily determine
	// if any open data is set
	int instancePropertyCount = dobj.getInstanceProperties().size();
	int definedPropertyCount = dobj.getType().getProperties().size();

	// If equal, does not have any open content set
	if (instancePropertyCount == definedPropertyCount) return false;

	// Check the open content Properties to determine if any are Attributes
	for (int i=definedPropertyCount; i<instancePropertyCount; i++)
	{
	    Property prop = (Property)dobj.getInstanceProperties().get(i);
	    if (boXsdHelper.isAttribute(prop))
	    {
	        return true;  // Found an anyAttribute value
	    }
	}

	return false;  // Does not have anyAttribute values set
```