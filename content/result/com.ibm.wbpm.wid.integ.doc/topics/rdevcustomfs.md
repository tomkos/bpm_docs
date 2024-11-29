<!-- image -->

# Developing a custom fault selector

## Implementing the FaultSelector interface

The
custom fault selector must implement the com.ibm.websphere.dhframework.faults.FaultSelector
interface.

```
package com.ibm.websphere.dhframework.faults; 

import commonj.connector.runtime.BindingContext; 

/** 
* A Fault Selector that determines if the input data is a business fault, 
* runtime fault or a normal response. It also determines the native fault name. 
*/ 

public interface FaultSelector 
extends BindingContext 
{ 
public static enum ResponseType { 
RESPONSE, BUSINESS\_FAULT, RUNTIME\_EXCEPTION 
}; 

/** 
* This method looks at the source object or headers from the context service to 
* determine if the response is fault or not. If the source data is read from the 
* input stream or reader, then this method should put this read data in the binding 
* context so it can be accessed by the data handler. 

* @param source 
* This can be of type InputStream, Reader or Java Object like an 
* Exception Object or the serialized object in case of JMS ObjectMessage. 
* @return Whether the response is a normal response, business fault or 
* runtime exception. 
*/ 
ResponseType getResponseType(Object source); 

/** 
* Gets the native fault name from the headers from the context service or from the 
* source object. 
* 
* @param source 
* This can be either InputStream, Reader or Java Object like an 
* Exception Object or the serialized object in case of JMS ObjectMessage. 
* @return The native fault name. 
*/ 
String getFaultName(Object source); 
}
```

The source data is shared between the fault selector
and the data handler. If the fault selector has read the data from
the input stream or reader, then the data handler will not be able
to read this data again. The fault selector has to put the read data
in the binding context so it can be used by the data handler.

## Binding context interface

The
binding context contains runtime contextual information passed from
the caller to the data handler. The BindingContext interface is used
to specify the runtime context of the data handler. The DataHandler
interface extends from BindingContext interface. Therefore, each data
handler implementation needs to implement the setBindingContext method
of the BindingContext interface.

```
public void setBindingContext( Map context)
	{
		this.context = context;
	}
```

The context is a Map. The key gives the name of the context
information and the value passed gives its value. Refer to the BindingContext
class for the information that bindings can provide in the context.
The following table contains the list of some of the relevant information
available in the context.

| Key                                  | Value                                                                                                                          | Description of value                                                                                                                                                                                                                                                                                                  |
|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BindingContext.BINDING\_COMMUNICATION | BindingContext.BINDING\_COMMUNICATION\_INBOUND BindingContext.BINDING\_COMMUNICATION\_OUTBOUND                                     | Indicates if the native data is coming into the module or going out of the module.                                                                                                                                                                                                                                    |
| BindingContext.BINDING\_CONFIGURATION | Configuration properties of the Java™ code.                                                                                    | This Java code provided by the data handler implementation contains the values for the properties that are set at design time. This information is set by the BindingRegistry which instantiated the data handler.See Accessing configuration properties for more details.                                            |
| BindingContext.BINDING\_INVOCATION    | BindingContext.BINDING\_INVOCATION\_REQUEST BindingContext.BINDING\_ INVOCATION\_RESPONSE BindingContext.BINDING\_ INVOCATION\_FAULT | Indicates whether the invocation to the data handler is in the context of a request, response or fault.                                                                                                                                                                                                               |
| BindingContext.BINDING\_NAME          | String                                                                                                                         | Name of the export or import                                                                                                                                                                                                                                                                                          |
| BindingContext.EXPECTED\_TYPE         | Qualified name (QName) of the business object.                                                                                 | The QName of the expected type of business object for native data to business object transformation. This information is set by the caller of the data handler.See Obtaining a business object type for more details.                                                                                                 |
| BindingContext .BINDING\_REGISTRY     | Runtime implementation of the Binding registry.                                                                                | The Binding registry maintains all the data handler, data binding and function selectors. This information is set by the BindingRegistry which instantiated the data handler.See Binding registry and invoking other data handlers for more details.                                                                  |
| WPSBindingContext.FAULT\_NAME         | String                                                                                                                         | Name of the business fault in case of export response                                                                                                                                                                                                                                                                 |
| WPSBindingContext.TRANSFORMED\_DATA   | Object                                                                                                                         | This allows context data sharing between the function selector and data handler, and fault selector and data handler. If the data is already parsed or read by the function selector or fault selector then it can be stored in the context and passed onto the data handler so the data handler does not re-read it. |

- Service Message Object (SMO) headers

Service Message Object headers provide protocol-specific and protocol-neutral headers to author data handlers.
- Example of a custom fault selector

This code sample shows how you might develop a custom fault selector.