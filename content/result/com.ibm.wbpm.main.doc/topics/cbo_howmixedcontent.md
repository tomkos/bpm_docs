<!-- image -->

# How do I work with mixed content?

All other APIs work equally with text as they do with Properties. The getProperty(int) API will
return null for mixed content text data. The following example of mixed content code can be used to
print all the mixed content text from a DataObject:

```
DataObject mixedContent = ...
	Sequence seq = mixedContent.getSequence();

	for (int i=0; i < seq.size(); i++)
	{
	    Property prop = seq.getProperty(i);
	    Object value = seq.getValue(i);

	    if (prop == null)
	    {
	        System.out.println("Found mixed content text: "+value);
	    }
	    else
	    {
	        System.out.println("Found Property "+prop.getName()+": "+value);
	    }
	}
```