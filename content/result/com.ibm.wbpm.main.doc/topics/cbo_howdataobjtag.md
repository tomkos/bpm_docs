<!-- image -->

# How do I know if my DataObject has an any tag?

DataObject does not provide a mechanism for determining if a DataObject Type has an any tag.
DataObjects only have the concept of "open" that applies to both any and anyAttribute and allows the
free additional of any properties. While the presence of an any tag causes a DataObject to have
isOpen() = true and isSequenced() = true, it might just have an anyAttribute tag and one of the
reasons for being sequenced discussed in the Sequences topics. The following example demonstrates
these concepts:

```
DataObject dobj = ...

	// Check to see if the type is open, if it isn't then it can't have
	// any values set in it.
	boolean isOpen = dobj.getType().isOpen();

	if (!isOpen) return false;  // Does not have any values set

	// Open Properties are added to the Instance Property list, but not
	// the Property list, so comparing their sizes can easily determine
	// if any open data is set
	int instancePropertyCount = dobj.getInstanceProperties().size();
	int definedPropertyCount = dobj.getType().getProperties().size();

	// If equal, does not have any open content set
	if (instancePropertyCount == definedPropertyCount) return false;

	// Check the open content Properties to determine if any are Elements
	for (int i=definedPropertyCount; i < instancePropertyCount; i++)
	{
	    Property prop = (Property)dobj.getInstanceProperties().get(i);
	    if (boXsdHelper.isElement(prop))
	    {
	        return true;  // Found an any value
	    }
	}

	return false;  // Does not have any values set
```