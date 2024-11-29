<!-- image -->

# Unit testing

## Testing components

- You have chosen to test an entire module and the integration test client has encountered a
component that has not been implemented.
- You have chosen to test a set of components or a single component in a module, which means that
any other unselected components in the module are automatically emulated regardless of whether they
are implemented or not.

## Example

The component HelloWorldMediation calls an external web service, which takes a string input and
returns the concatenated string. To test the operation callHello independently of the web service,
you can use an emulate event.

1. From the module assembly diagram, call the Test Component in Isolation.
2. In the integration test client, select an interface and an operation that you want to
test.Figure 1. Integration Test Client properties
3. Enter the input parameter values for the selected operation.
Figure 2. Input parameters
4. Click the Continue button to begin invoking the selected operation with
the specified parameter values.
5. If the selected component is referenced to another component or Import, then the integration
test client will pause at the point where the reference is used. It also allows you to emulate the
results returned by the reference, so that you can test your component even if the dependent
component is not implemented.
6. Once the values for emulation are specified, click the Continue button to continue.
7. If everything goes well, then the expected result is
returned.