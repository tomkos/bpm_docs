<!-- image -->

# EJB fault selector

If a fault is detected, the EJB fault selector returns the native
fault name to the binding runtime so the
JAX-WS data handler can convert the exception object into a fault
business object.

- The first element in the Object[] is the return value from the Java method invocation.
- The subsequent values represent the
input parameters for the method.

For exception scenarios, the binding assembles an Object[] and
the first element represents the exception thrown by the method.

| Type              | Return value          | Description                                                                                        |
|-------------------|-----------------------|----------------------------------------------------------------------------------------------------|
| Fault             | ResponseType.FAULT    | Returned when the passed Object[] contains an exception object.                                    |
| Runtime exception | ResponseType.RUNTIME  | Returned if the exception object does not match any of the declared exception types on the method. |
| Normal response   | ResponseType.RESPONSE | Returned in all other cases.                                                                       |

If the fault selector returns a value of ResponseType.FAULT, the native fault name is returned. This native
fault name is used by the binding to determine the corresponding WSDL
fault name from the model and to invoke the correct fault data handler.