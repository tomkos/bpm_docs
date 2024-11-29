<!-- image -->

# Create a mediation module project that references the library

## About this task

You will use a mediation module to access the supplied HelloService web
service and expose it as a service to other modules. Because the interface
of the service you invoke (HelloService) is different than the interface
of the service you expose (HelloWorld), you will need to map between
them.

## Procedure

1. Right-click the HelloWorldLibrary library and select New
> Project > Mediation Module. The New Mediation Module wizard
is displayed.
2. In the Module name field, enter HelloWorldMediation and
click Next. The Select required libraries page
opens.
3. Ensure that the HelloWorldLibrary project is selected.
This selection associates the library with this new module so that
this module can use any artifacts in that library. Click Finish.
The assembly editor opens for the new module and it contains a mediation
flow component, as shown here:

## Results