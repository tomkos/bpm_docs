<!-- image -->

# Overriding a Service Data Object to Java conversion

## Before you begin

## About this task

## Procedure

1. Locate the generated component.
The component is named
java\_classMapper.component.
2. Edit the component using a text editor.
3. Comment out the generated code and provide your own method.

Do not change the file name that contains the component implementation.

## Example

```
private Object datatojava\_get\_customerAcct(DataObject myCustomerID, 
				String integer) 
{

		// You can override this code for custom mapping.
		// Comment out this code and write custom code.

		// You can also change the Java type that is passed to the 
		// converter, which the converter tries to create. 

		return SDOJavaObjectMediator.data2Java(customerID, integer) ; 
	
}
```

## What to do next

<!-- image -->