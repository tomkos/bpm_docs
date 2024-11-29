<!-- image -->

# Creating a component instance

## Before you begin

The integration test client is the recommended tool for
creating a component instance for debugging, especially if the module
that contains your component is not yet complete. The test client
can automatically deploy your module and components to the server
and start the server in Debug mode. However, if your module is complete
and capable of running on its own, you can also use other methods
to create a component instance for debugging without the use of the
integration test client, such as a JAX-RPC web service, JSP, the Business
Process Choreographer Explorer, or the IBM® Integration
Designer application
framework.

To create a component instance using the integration
test client, the module that contains the component must have one
of the following exports:

- An export with an SCA binding.
- An export with a JMS binding that is referenced by the import
of another module.

If you have an export with a JMS binding that is not referenced
by the import of another module, or if you have an export with a SOAP
binding, you can still use the integration test client to initiate
debugging. However, you would need to use the attach facility of the
integration test client to attach the test client to your module and
then use a client of your own to create a component instance.

## About this task

## Procedure

1. In the Business Integration perspective, open the component
that you want to debug in the component editor. For example, if you
want to debug a business process, you would open the process in the
business process editor.
2. In the component editor, right-click the first element
in the component where you can set a breakpoint and then use the 
 menu to add a breakpoint to the element. This will prevent the component
instance from immediately running to completion when it is started.
3. Save your changes and close the component editor.
4 If you are debugging an XML map, complete one of the followingsteps: The integration test client opens.
    - In the Business Integration view, right-click the map and
select Test.
    - In the mediation flow editor, right-click the Mapping primitive
that is associated with the map and select Test XML Map.
5. In the Business Integration view, right-click the module
that contains your component and select Test > Test Module.
The integration test client opens, as shown in the following figure:  Note that if you
are debugging an XML map, you can right-click the map in the Business
Integration view and select Test or you
can right-click the Mapping primitive (that is associated with the
map) in the mediation flow editor and select Test XML Map.
The test client will open. If you want to open the Debug perspective
before each transform in the map runs, you can select the Stop
for debug before transformations check box in the test
client.
6. In the Business Integration view,  In the Events
area of the integration test client, an Invoke event is automatically
generated whenever the test client is started. An Invoke event is
an interactive event, which means that you must manually select an
operation to test and specify some initial request parameters values
for the operation before the test can continue.
7 In the Detailed Properties areaof the integration test client, complete the following steps:

1. In the Component field, ensure
that the selected component is the component that you want to debug.
2. In the Interface field, ensure
that the component interface is selected that contains the operation
that you want to invoke.
3. In the Operation field, ensure
that the interface operation is selected that you want to invoke.
8. In the Initial request parameters value
editor, specify the input values for the selected operation in the Value column,
as shown in the figure below:
9. Click the Continue icon. The Deployment
Location wizard opens.
10. Ensure that the correct deployment location is selected
in the Deployment Location wizard.
11 In the Mode drop-down list, ensurethat Debug is selected and then click Finish .The following tasks are automatically performed:

- The interface operation selected in the test client is invoked.
- The component and the rest of the module are automatically
deployed to the server.
- The server is started in Debug mode.
- A moment or two after the server is started in Debug mode,
the Console view displays a message that indicates that the server
is ready for debugging the component.
- A component instance is created and started.
- The Debug perspective is opened.
- The component editor that contains the breakpoint is opened
in the Debug perspective and the component thread pauses at the breakpoint
that you set in the editor.

## Results

When you have finished creating the component instance,
you can repeat the steps to create additional instances of the same
component (or to create new instances of different components) in
the integration test client and then debug them simultaneously in
the integration debugger. If you want to learn more about the integration
test client, see the integration test client topic "Testing authentication using the integration test client."