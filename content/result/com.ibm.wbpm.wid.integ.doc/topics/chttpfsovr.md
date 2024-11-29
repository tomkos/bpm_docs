<!-- image -->

# Overview of HTTP function selectors

When the HTTP export receives a request message, it uses the function
selector to determine the method name that it needs to invoke on the
interface based on the HTTP request information.

For a function selector, you can use one of the IBM-supplied function
selectors or use a custom function selector. In the second case, you
would supply a Java™ implementation
of the FunctionSelector interface.

The supplied HTTP function selectors are as follows:

- One function selector determines the function on the interface
to call based on the value of a special HTTP header (TargetFunctionName)
value from the request.
- The other function selector determines the function to call based
on the context path of the URL address and the HTTP method used in
the request.

## Related concepts

- Overview of HTTP data bindings
- Prepackaged HTTP data format transformations
- Prepackaged HTTP function selectors

## Related reference

- Data handlers
- Prepackaged HTTP fault selectors