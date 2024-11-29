<!-- image -->

# Application design considerations for exceptions and faults

In order to create a comprehensive error handling strategy, solution
architects need to understand howIBM Workflow
Server represents
declared and undeclared exceptions.

The SCA programming model provides two types of exceptions:

- Service Business ExceptionsService Business Exceptions are
checked exceptions declared in a business method's function signature
(WSDL faults or Java™ throws).
Service Business Exceptions identify error conditions that are anticipated
by the application or service. These exceptions are sometimes referred
to as "checked exceptions"
An example is an InvalidSymbolException for
a stock quote service. Such exceptions are wrapped by ServiceBusinessException
and passed back to the client.
- Service Runtime ExceptionsAlso known as "system exceptions"
service runtime exceptions are not declared in the method signature.
In general, they represent error conditions that are not anticipated
by the application, such as a NullPointerException in
a Java Component. 
These
exceptions are wrapped by ServiceRuntimeException and
passed back to the client, which can interrogate the ServiceRuntimeException to
determine the cause. Note: When working at the SCA level these exceptions
are sometimes referred to as faults. However, when using Java code they are usually referred to as exceptions.

When
a ServiceRuntimeException is thrown from a component,
the current transaction will be rolled back.

- Service Business Exception handling

Service Business Exceptions represent known and declared exceptions anticipated by the application or service.
- Service Runtime Exception handling

Service Runtime Exceptions are undeclared exceptions. In general, they represent error conditions that are not anticipated by the application.