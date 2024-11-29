<!-- image -->

# EJB function selector

## Import function selector

- If the @WebMethod annotation is present, the function selector
uses the @WebMethod annotation to determine the correct Java method mapping for the WSDL method.
- If the @WebMethod annotation is missing, the function selector assumes that the Java method
name is the same as the invoked operation name.

The function selector returns a java.lang.reflect.Method
object that represents the method of the EJB interface.

The function selector uses a Java Object array (Object[]) to contain the
response from the target method. The  first element in the Object[]
is a Java method with the name
of the WSDL, and the second element in the Object[] is the input business
object.

## Export function selector

For inbound processing, the export function selector
derives the target method to be invoked from the Java method.

The export function selector
maps the Java operation name
invoked by the EJB client into the name of the operation in the interface
of the target component. The method name is returned as a String and
is resolved by the SCA runtime depending on the interface type of
the target component.