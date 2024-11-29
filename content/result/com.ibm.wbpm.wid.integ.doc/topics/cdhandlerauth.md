<!-- image -->

# Data handler authoring

Creating a data handler involves knowledge of the following elements.

- Data handler interface
- Binding context interface
- Data handler transformations
- Native data format to DataObject transformations
- DataObject to native data format transformations
- ServiceRuntimeException to native data transformations
- Native data to
ServiceRuntimeException transformations
- Data handler configuration
- Specifying configuration properties
- Accessing configuration properties
- Obtaining a business object type
- Binding registry and invoking other data handlers
- Data handler implementation outline

## Data handler interface

The
data handler provides the transformation function for transforming
from one form (source) to another (target). The result of the transformation
is mapped into either a provided target type or a new instance of
a specified target. All data handlers must implement the DataHandler
interface which has methods that map into a provided target type or
into a new instance of a specified target.

```
package commonj.connector.runtime;

public interface DataHandler extends commonj.connector.runtime.BindingContext
{
    public Object transform(Object source,
                            Class targetClass,
                            Object options)
        throws DataHandlerException;

    public void transformInto(Object source,
                              Object target,
                              Object options)
        throws DataHandlerException;
}
```

Let us first explore the transformation that maps into
a provided target type.

```
public Object transform(Object source, Class targetClass, Object options)
        throws DataHandlerException;
```

In the implementation of this method, the data handler
is expected to transform data from the source object
to a new instance of the targetClass. options provides
additional hints for the transformation. The signature of this method
is very generic. It allows both the source object
to be of any type and the targetClass to be of any
type. This method requires the data handler implementation to construct
the target object type, which is given by targetClass.
If there is any error during the transformation, the data handler
implementation is expected to throw a DataHandlerException.

There
are scenarios where the target object instance is available to the
caller. For such scenarios, the DataHandler interface
provides a transformInto method.

```
public void transformInto(Object, Object target, Object options)
       throws DataHandlerException;
```

In this method implementation the data handler is expected
to transform data from the source object to the target object. options provides
additional hints for the transformation. The signature of this method
is very generic. It allows the source object to be
of any type and the target object to be of any type.
If there is any error during the transformation data handler implementation
is expected to throw a DataHandlerException.

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
| BindingContext.BINDING\_CONFIGURATION | Configuration properties for a JavaBean.                                                                                       | This JavaBean provided by the data handler implementation contains the values for the properties that are set at design time. This information is set by the BindingRegistry which instantiated the data handler.See Accessing configuration properties for more details.                                             |
| BindingContext.BINDING\_INVOCATION    | BindingContext.BINDING\_INVOCATION\_REQUEST BindingContext.BINDING\_ INVOCATION\_RESPONSE BindingContext.BINDING\_ INVOCATION\_FAULT | Indicates whether the invocation to the data handler is in the context of a request, response or fault.                                                                                                                                                                                                               |
| BindingContext.BINDING\_NAME          | String                                                                                                                         | Name of the export or import                                                                                                                                                                                                                                                                                          |
| BindingContext.EXPECTED\_TYPE         | Qualified name (QName) of the business object.                                                                                 | The QName of the expected type of business object for native data to business object transformation. This information is set by the caller of the data handler.See Obtaining a business object type for more details.                                                                                                 |
| BindingContext .BINDING\_REGISTRY     | Runtime implementation of the Binding registry.                                                                                | The Binding registry maintains all the data handler, data binding and function selectors. This information is set by the BindingRegistry which instantiated the data handler.See Binding registry and invoking other data handlers for more details.                                                                  |
| WPSBindingContext.FAULT\_NAME         | String                                                                                                                         | Name of the business fault in case of export response                                                                                                                                                                                                                                                                 |
| WPSBindingContext.TRANSFORMED\_DATA   | Object                                                                                                                         | This allows context data sharing between the function selector and data handler, and fault selector and data handler. If the data is already parsed or read by the function selector or fault selector then it can be stored in the context and passed onto the data handler so the data handler does not re-read it. |

## Data handler transformations

As
mentioned previously, data handler interface signatures are very generic.
The data handler can allow transformation between source of any type
and target of any type. A generic interface enables data handler implementations
to support transformations between multiple types of objects. While
the interface is generic, there are limited transformations that are
relevant from the IBM® Workflow
Server perspective;
these are the transformations with are described in this section.
. If you decide to implement a data handler, you may decide to support
some or all of these transformations. call data handler describes how
various transformations can be used from different export and import
bindings.

- Native data format to DataObject transformations
- DataObject to native data format transformations

## Native data format to DataObject
transformations

In IBM Workflow
Server,
the binding (HTTP, MQ, JMS and EIS) receives business data in native
format inside a protocol envelope. The binding then invokes the data
binding to obtain the data object from the transport envelope. Depending
on the transport and type of transport envelope, the business data
in native transport envelope can be obtained as characters or bytes
or as java.lang.Object. call data handler describes
how this can be done. Therefore to be usable across these bindings,
it is sufficient for data handlers to support the source object as
java.io.InputStream, java.io.Reader and java.lang.Object.

| Source object       | Description                                                                                                                                                                                                                                                                                                                                                                       |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| java.io.InputStream | If the business data in native format is byte stream, then either it is in the form of an input stream which can be passed directly to the data handler or it is in the form of raw bytes from which an input stream can be constructed. This input stream can be used to invoke the data handler.dataObject = (DataObject) dh.transform(inputStream, DataObject.class, options); |
| Java.io.Reader      | If the business data in native format is characters, then either it is in the form of a reader which can be passed directly to the data handler or it is in the form of raw characters from which a reader can be constructed.  This reader can be used to invoke the data handler.dataObject = (DataObject) dh.transform(reader, DataObject.class, options);                     |
| Java.lang.Object    | If the business data in native format is received as Java™ object, data handlers for such protocols should support Java object to DataObject transformations.dataObject = (DataObject) dh.transform(object, DataObject.class, options);                                                                                                                                           |

## DataObject to native data
format transformations

In IBM Workflow
Server,
the binding (HTTP, MQ, JMS and EIS) sends business data in native
format inside a protocol envelope. The binding then invokes the data
binding to obtain the transport envelope from the data object. Depending
on the transport and type of transport envelope, the business data
in the native transport envelope can be as sent as characters or bytes
or as java.lang.Object. call data handler describes
how this can be done. To be usable across these bindings, it is sufficient
for data handlers to support target objects as one or more of the
following types: java.io.Writer, java.io.OutputStream, java.lang.Object
and java.io.InputStream.

| Target object        | Description                                                                                                                                                                                                                                                                                                                                                                                                               |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| java.io.Writer       | If the caller wants the data handler to write native data as character type on the protocol character stream, the caller can invoke the transformInto method with a target object of type java.io.Writer. Some protocols require java.lang.String (for example, JMS TextMessage). For such protocols, the caller can invoke the data handler with java.io.StringWriter.dh.transformInto(dataObject, writer, options);     |
| java.io.OutputStream | If the caller wants the data handler to write the native data as bytes on the protocol byte stream, the caller can invoke the transformInto method with a target object of type java.io.OutputStream. Some protocols require byte[] (for example, JMS ByteMessage). For such protocols, the caller can invoke the data handler with the in-memory byte output stream.dh.transformInto(dataObject, outputStream, options); |
| java.io.InputStream  | If the caller wants the data handler to provide a byte stream from which the caller can read the transformed native data, the caller can invoke the transform method requesting a target object of type java.io.InputStream. InputStream is = (InputStream) dh.transform(dataObject, java.io.InputStream.class, options);                                                                                                 |
| java.lang.Object     | If the caller wants the data handler to transform the business object into an object, the caller can invoke the transform method requesting a target object of type java.lang.Object. Object o = dh.transform(dataObject, Object.class, options);                                                                                                                                                                         |

## ServiceRuntimeException to
native data transformations

If you are authoring a data
handler to transform a ServiceRuntimeException to native data, then
there are additional transformations that you have to code in your
data handler.

| Source object           | Target object   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ServiceRuntimeException | OutputStream    | If the caller wants the data handler to convert the ServiceRuntimeException object to the native data as bytes on the protocol byte stream, the caller can invoke the transformInto method with a target object of type java.io.OutputStream. Some protocols require byte[] (for example, JMS ByteMessage). For such protocols, the caller can invoke the data handler with the in-memory byte output stream:  dh.transformInto(serviceRuntimeException, outputStream, options); |
| ServiceRuntimeException | Writer          | If the caller wants the data handler to convert the ServiceRuntimeException object to the native data as string on the protocol stream, the caller can invoke the transformInto method with a target object of type java.io.Writer. Some protocols require string (for example, JMS TextMessage). For such protocols, the caller can invoke the data handler with the in-memory writer:  dh.transformInto(serviceRuntimeException, writer, options);                             |
| ServiceRuntimeException | Object.class    | If the caller wants the data handler to convert the ServiceRuntimeException object to the native data as serialized object on the protocol stream, the caller can invoke the transform method with a target class of type java.io.Object. For such protocols, the caller can invoke the data handler as follows: dh.transform(serviceRuntimeException, Object.class, options);                                                                                                   |

## Native data to ServiceRuntimeException
transformations

If you are authoring a data handler to transform
native data to ServiceRuntimeException, then there are additional
transformations that you have to code.

| Source object   | Target class                  | Description                                                                                                                                                                                                                                                                                                                            |
|-----------------|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| InputStream     | ServiceRuntimeException.class | If the business data in native format is byte stream, then the data handler gets an input stream which is constructed from the byte stream. The data handler is expected to convert this native data to a ServiceRuntimeException object: dataObject = (DataObject) dh.transform(inputStream, ServiceRuntimeException.class, options); |
| Reader          | ServiceRuntimeException.class | If the business data in native format is a string, then the data handler gets a reader which is constructed from the String. The data handler is expected to convert this native  data to a ServiceRuntimeException object: dataObject = (DataObject) dh.transform(reader, ServiceRuntimeException.class, options);                    |
| Object          | ServiceRuntimeException.class | If the business data in native format is a simple type object or a seriliazed object, then the data handler gets an object. The data handler is expected to convert this native  data to a ServiceRuntimeException object: dataObject = (DataObject) dh.transform(object, ServiceRuntimeException.class, options);                     |

## Data handler configuration

- Specifying configuration properties
- Accessing configuration properties

## Specifying configuration properties

The
data handler implementation can have configuration properties. For
example, a delimited data handler can have a configuration for delimiter.
Data handlers are configured at authoring time from IBM Integration
Designer.

- The data handler implementation provides a JavaBean class for
its configuration.
- This class is required to be in the same package as the data handler
implementation class.
- This class should implement the java.io.Serializable interface.
- The name of this class should have Properties appended to the
data handler implementation class name.
- There has to be a set and get method for every configuration property
in this class.

For example if the data handler implementation class is
com.example.DelimitedDataHandler, the configuration class is com.example.DelimitedDataHandlerProperties.

```
1	import java.io.Serializable;
2	
3	public class DelimitedDataHandlerProperties
4	    implements Serializable
5	{
6	    protected String delimiter = ","; 
7	    
8	    
9	    public String getDelimiter(){
10	        return delimiter;
11	    }
12	
13	    public void setDelimiter (String delimiter){
14	        this.delimiter = delimiter;
15	    }
	}
```

In this example, delimiter is a property of String
type. The other types that are supported for the properties are boolean,
Boolean, byte, Byte, char, Character, double, Double, float, Float,
int, Integer, JavaBeans,
long, Long, short, Short, String, BindingTypeBeanProperty.

BindingTypeBeanProperty
is a type used when the type is a configuration namespace and name.
This is used when there is a data handler calling another data handler
and the called data handler is configured as a property. Arrays are
also supported, but only the default user interface rendering (no
configuration) is supported for simple arrays.

Before the data
handler can be invoked, the data handler needs to be configured in IBM Integration
Designer.
There can be multiple configurations for the same data handler. Configuring
data handler instances describes how resource configurations are created
for data handlers in IBM Integration
Designer.
In  Integration Designer each
data handler configuration has a QName. For example, delimited data
handler can have following two configurations:

```
http://configtns:configuration\_1: 
		delimiter = !
http://configtns:configuration\_2: 
		delimiter = *
```

## Accessing configuration properties

The
values for the configuration properties set at author time are accessed
by the data handler implementation at run time from the binding context
class. The binding context contains runtime contextual information
passed from the caller to the data handler. The BindingContext interface
is used to specify the runtime context of the data handler. The DataHandler
interface extends from the BindingContext interface. Therefore each
data handler implementation needs to implement the setBindingContext
method of the BindingContext interface.

```
public void setBindingContext( Map context)
{
	this.context = context;
          // get information from context
          // ... 
}
```

The context is a Map. The key gives the name of the
context information and the value for the key gives its value.  The
properties are accessed from the binding context using BindingContext.BINDING\_CONFIGURATION.
The following example illustrates how the Delimited data handler can
access its properties:

```
DelimitedDataHandlerProperties properties = null;
if(context != null)
     properties = 
    	 (DelimitedDataHandlerProperties)context.get(BindingContext.BINDING
			\_CONFIGURATION);
if(properties != null)
      delimiter = properties.getDelimiter();
```

## Obtaining a business object type

For
native to business object transformations, if the caller has advanced
knowledge of the type of business object in the native data, the caller
can specify that type in the binding context to the data handler.
The key name is BindingContext.EXPECTED\_TYPE and the value is the
QName of the expected type. The data handler implementation can use
BindingContext.EXPECTED\_TYPE  to construct the business object from
the native data. Some data handlers may require BindingContext.EXPECTED\_TYPE
be supplied to them in the binding context. However, for some formats,
type information is available in the native business data. Such data
handlers may not require BindingContext.EXPECTED\_TYPE in the context.
If the caller supplied BindingContext.EXPECTED\_TYPE, the data handler
implementation may obtain it from the context as follows:

```
QName expectedType = (QName) context.get(BindingContext.EXPECTED\_TYPE);
```

## Binding registry and invoking other
data handlers

The binding registry provides the means of
retrieving configured DataBinding, DataHandler or FunctionSelector
instances. The binding registry can be obtained from the BindingRegistryFactory
class. BindingRegistryFactory provides a static method to get an instance
of BindingRegistry. the following code snippet illustrates how the
binding registry can be used to obtain configured instances of data
handler. This code snippet assumes the user has configured the data
handler instance with a QName of "http://ProcessCustomerWPS, DelimitedDataHandlerConfig".

```
QName config = new QName("http://ProcessCustomerWPS",
			"DelimitedDataHandlerConfig");
BindingRegistry bindingRegistry = BindingRegistryFactory.getInstance();
DataHandler dataHandler =
	(DataHandler) bindingRegistry.locateBinding( config, 
	bindingContext);
```

A data handler implementation, a data
binding implementation, and a Java component
implementation can use the binding registry to obtain the configured
data handler instance. The required transformation method can then
be called on the data handler instance.

```
dataHandler.transformInto(dataObject, outputStream, options);
```

- Multi-layer native format: A native data format can require multiple
transformation layers. For example, the business data is delimited,
compressed and encrypted. The native data first needs decryption,
followed by decompression to obtain delimited data. Delimited data
can then be converted into a business object. Similarly, business
object to native format can require multiple transformation layers.
For example, the first business object needs to be converted to a
delimited format, followed by compression and encryption.
- Multi-part native format: In this case, each part of the message
is in a different format. An Email message with multiple attachments
is one such example. To compose a wrapper business object from native
data requires transforming each part with a data handler which can
then handle the format for that part. Similarly, to compose a native
message requires transforming each child business object of the wrapper
business object with a data handler which can transform that child
business object into the required native format for that part.

- Native data format to DataObject transformation: Compress data
handler de-compresses native data and then calls the configured delimited
data handler instance to obtain the business object.
- DataObject to native data format transformation: Compress data
handler calls the configured delimited data handler instance to transform
the business object into delimited data. It then compresses the delimited
data.

## Data handler implementation outline

Following
code snippet provides outline for data handler implementation. It
provides outline for all the transformations described in Data handler transformations.

```
1	public class DataHandlerOutline
2	    implements DataHandler
3	{
4	
5	    private DataHandlerOutlineProperties config;
6	    private Map context;
7	
8	    public void setBindingContext(Map context)
9	    {
10	        this.context = context;
11	        config = (DataHandlerOutlineProperties) context.get(BindingContext.BINDING\_CONFIGURATION);
12	    }
13	
14	    public Object transform(Object source,
15	                            Class target,
16	                            Object options)
17	        throws DataHandlerException
18	    {
19	        if ((source == null) || (target == null))
20	            return null;
21	
22	        // native data format to DataObject transformations
23	        if (target == DataObject.class) {
24	            if (source instanceof InputStream) {
25	                // TODO: Transform InputStream to DataObject
26	            }
27	            else if (source instanceof Reader) {
28	                // TODO: Transform Reader to DataObject
29	            }
30	            else {
31	                // TODO: Transform Object to DataObject
32	            }
33	        }
34	
35	        // DataObject to native data format transformations
36	        if (source instanceof DataObject) {
37	            if (target == InputStream.class) {
38	                // TODO: Transform DataObject to InputStream
39	            }
40	            else {
41	                // TODO: Transform DataObject to Object
42	            }
43	        }
44	        throw new DataHandlerException("Transformation not supported");
45	    }
46	
47	    public void transformInto(Object source,
48	                              Object target,
49	                              Object options)
50	        throws DataHandlerException
51	    {
52	        if ((source == null) || (target == null))
53	            return;
54	
55	        if (source instanceof DataObject)
56	            if (target instanceof OutputStream) {
57	                // TODO: Transform DataObject into given OutputStream
58	            }
59	        throw new DataHandlerException("Transformation not supported");
60	    }
61	
}
```

- Service Message Object (SMO) headers

Service Message Object headers provide protocol-specific and protocol-neutral headers to author data handlers.