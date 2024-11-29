<!-- image -->

# JAX-WS data handler

The JAX-WS data handler is used by default when the EJB binding
has a WSDL interface. This data handler cannot be used to transform
a SOAP message representing a JAX-WS invocation to a data object.

1. The EJB binding sets the expected type, expected element, and
targeted method name in the BindingContext to match those specified
in the WSDL.
2. The EJB binding invokes the transform method for the data object
requiring data transformation.
3. The data handler returns an Object[] representing the parameters
of the method (in the order of their definition within the method).
4. The EJB binding uses the Object[] to invoke the method on the
target EJB interface.

- The first element in the Object[] is the return value from the Java method invocation.
- The subsequent values represent the
input parameters for the method.

This is required to support the In/Out and Out types of parameters.

For parameters of type Out, the values must be returned in the
response data object.

The data handler processes and transforms values found in the Object[]
and then returns a response to the data object.

```
public class TestType {
	private Object[] object;

	@XmlAnyElement (lax=true)
	public Object[] getObject() {
		return object;
	)

	public void setObject (Object[] object) {
		this.object=object;
	)
)
```

- The data handler does not include support for the header attribute @WebParam annotation.
- The namespace for business object schema files (XSD files) does
not include default mapping from the Java package
name. The annotation @XMLSchema in package-info.java
also does not work. The only way to create an XSD with a namespace
is to use the @XmlType and @XmlRootElement annotations. @XmlRootElement defines
the target namespace for the global element in JavaBeans types.
- The EJB import wizard does not create XSD files for unrelated
classes. Version 2.0 does not support the @XmlSeeAlso annotation,
so if the child class is not referenced directly from the parent class,
an XSD is not created. The solution to this problem is to run SchemaGen
for such child classes. SchemaGen is a command line utility (located
in the WPS\_Install\_Home/bin directory) provided to create XSD
files for a given bean. These XSDs must be manually copied to the
module for the solution to work.