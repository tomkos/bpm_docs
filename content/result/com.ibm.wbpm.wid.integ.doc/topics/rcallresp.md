<!-- image -->

# Callout response

There is one callout response node for each target operation.
Errors that are not defined as WSDL fault messages are propagated to the fail
terminal of the callout response node.

<!-- image -->

Select
the check box to include the original request message if you want to propagate
the complete message to the fail terminal in the event of a failure. If you
don't select the check box, the message information that is propagated includes
the failure information (in the failinfo element) and some context information.