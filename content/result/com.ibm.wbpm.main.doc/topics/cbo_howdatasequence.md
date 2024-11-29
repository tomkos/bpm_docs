<!-- image -->

# How do I know if my DataObject has a sequence?

You would use DataObject noSequence and DataObject withSequence as shown in the following
example:

```
DataObject noSequence = ...
	DataObject withSequence = ...

	// Displays false
	System.out.println(noSequence.getType().isSequenced());

	// Displays true
	System.out.println(withSequence.getType().isSequenced());

	// Displays true
	System.out.println(noSequence.getSequence() == null);

	// Displays false
	System.out.println(withSequence.getSequence() == null);
```