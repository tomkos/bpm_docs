<!-- image -->

# Client programming model

The SCA client programming model provides two primary functions
for clients. The programming model exposes an interface that allows
clients to locate services within the current module, and once a service
is located the client programming model provides a way for the client
to invoke operations on that service.

Clients locate services by using the ServiceManager class. There
are a few ways to instantiate the ServiceManager class, depending
on the wanted lookup scope for the service.

The key interface that clients should be aware of for locating
services is com.ibm.websphere.sca.ServiceManager.
This interface includes a locateService method that returns a reference
to the service implementation for the service requested. The string
parameter that is passed into the locateService method represents
the reference name for the service that the client wants to locate.

Once a client has located the appropriate service, there are two
types of invocation models that can be used to make a call to an operation
or method offered by the service. First, there is a dynamic invocation style
of interaction. The key interface for this style of interaction is com.ibm.websphere.sca.Service.
The invoke() method on this interface takes the name of the operation
that you are going to invoke, along with the parameters needed to
call that operation.

```
public Interface MyService {
public String someMethod(String input);

Service myService = (Service) serviceManager.locateService("myService");
DataObject input = ...
DataObject result = (DataObject) myService.invoke("someMethod", input);
```

Clients can also use a static (type-safe) invocation method
to call a particular operation associated with a service. This type
of invocation only works for interface definitions that are specified
as Java™. In this situation,
the client casts the return from the locateService() call to the appropriate
interface and can proceed calling the appropriate type safe method
calls on that interface.

```
public Interface MyService {
public String someMethod(String input);

MyService myService = (MyService) serviceManager.locateService("myService");
String input = ...
String result = myService.someMethod(input);
```