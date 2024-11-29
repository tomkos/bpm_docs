<!-- image -->

# Assemble the mediation module

## About this task

To assemble the mediation module:

## Procedure

1. The HelloWorldMediation component will ultimately
be implemented by a mediation flow, but first you need to give it
an interface so it can be invoked by other components. Select the
component, and notice the hover bar that comes up above it, as shown
here  Note: If you accidentally
double-click the component, an Open window will ask if you want to
create the implementation. If the window opens, click No to
close it.
Click the circled I from that hover bar
to create an interface (or right-click the component and select Add
> Interface). The Add Interface window opens. Select HelloWorld,
which is the interface that you recently created. Click OK.
You will now see a circled I on the left edge of the component,
and its hover help displays the interface type, as shown in the following
figure:
2. This mediation can now be invoked, but you also need to
identify what services it will invoke. Select the component again,
and this time select the right arrow from the hover bar to add a reference,
as shown in the following figure:  The Add
Reference window opens. In the Matching interfaces list,
select HelloService, which is the interface of the supplied
service that will be invoked. Click OK. You will now see a
little box on the right edge of the component, with "1..1" in it,
which represents a required service that this component has declared
it invokes, as shown in the following figure:
 You have not yet identified the actual
service to be invoked. At this point all you know is the interface
or shape of that service. (The "1..1" is the multiplicity of
the reference and it indicates that this reference must be satisfied
with exactly one wire to another component. It is possible to configure
the reference to allow multiple wires.) 
This is the elegance
of Service Component Architecture: regardless of the implementation
details, applications are defined as a series of components that expose
interfaces and consume other components or services through references.
3. Now you need to add an import component for the invocation
of the supplied HelloService web service whose endpoint WSDL
you copied into your library. In the Business Integration view, expand HelloWorldLibrary.
In the Web Service Ports category, drag the port (HelloService\_HelloServiceHttpPort)
anywhere in the assembly diagram canvas.
4. Click the name of the new import to enter edit mode, and
change the name to HelloServiceImport (that is, delete the
'1' suffix).
5. Hover over the reference box on the right border of the HelloWorldMediation component
until you see a yellow border and a yellow circle to the right, as
shown in the following figure:  Grab the circle with
your mouse and drag it to the circled I on the left edge of
the HelloServiceImport component to wire the two components
together, as shown in the figure below: Note: If
you right-click in the canvas you can toggle the Automatic
Layout setting to have nodes on the canvas automatically
aligned.
 You have just resolved the reference
of the first component with an actual provider of the service, which
in this case is an external web service. This means that when the
implementation of the first component invokes that reference, it will
really invoke the HelloService web service. (Soon, you will create
the implementation of the first component.)
Note: A quick way to
create a web service import is by dragging Import from the
palette to the assembly diagram and then configuring it. You would
create an import this way to invoke other types of services, such
as those invoked over the native SCA binding, or by sending a message
over HTTP, JMS or MQ, or by invoking remote enterprise JavaBeans.
Beyond these built-in import bindings, you can also use supplied adapters
to invoke external services by way of the J2EE Connector Architecture
(J2C) standard to do things like write to a file or send an email.
The services accessible by some of the adapters are referred to as
Enterprise Integration Services (EIS).
Optional:
In the palette, expand the Outbound Adapters and Outbound
Imports categories and see what external services are
available.
6. In addition to invoking a web service, you also want to
expose your mediation so it can be invoked from other modules in preparation
for Hello World Part 2. Because this is the only client you need to
support, you use the SCA export binding. (Other modules can invoke
an SCA export component by using a matching SCA import component in
their module.) In the assembly diagram canvas, right-click the HelloWorldMediation 
component and select Generate Export > SCA Binding, as shown
here:   This action
creates a new HelloWorldMediationExport export
component with an SCA binding that is wired to the HelloWorldMediation component.
Now your component can be accessed outside of this module.  
Note: SCA is only one way to expose a component
so that it can be invoked outside of the module. As you can see in
the Generate Export cascading menu, others
include HTTP, JMS, MQ and web services. As with imports, these are
all built-in bindings supported natively, but in addition there are
supplied adapters for invoking a module using the J2C standard. 
Optional:
In the palette, expand the Inbound Adapters and Inbound
Exports categories and see what other ways of invoking
the module are supported, such as receiving an email or contents appearing
in a flat file.
7. Press Ctrl-S to save your work in the assembly diagram.

## Results