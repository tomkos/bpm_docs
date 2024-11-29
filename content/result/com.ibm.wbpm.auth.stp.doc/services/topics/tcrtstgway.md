<!-- image -->

# Creating a static service gateway

## About this task

This topic describes how to use the pattern to create
a service gateway. The pattern provides a starting point to create
common service gateway scenarios. You can also create a service gateway
by creating all the artifacts yourself. For more information, see Creating a service gateway

To
create a static service gateway from the pattern, follow these instructions:

## Procedure

1. In the main toolbar, click Open Patterns Explorer.
2. Select Static Service Gateway, right
click and select Create a Pattern Instance.
3. Enter a name in the Pattern instance name field.
This name will be used for the integration solution and referenced
projects that are created for the pattern.
4. Click OK. The Configure
Pattern Parameters page opens.
5. In a static gateway, you must specify the interfaces of
the service providers. Click Add to see the
list of available service provider interfaces. Select an interface
from the list of interfaces, and click OK.
Note: The interface must exist in a library in order to be available
in the list.
6. If you want to log request and response messages, choose
an option from the list of logging options.
7. Select a transport protocol for the export from the list
of supported protocols.
8. Choose the native data format for the message payload (or
body) .
9. Select a transport protocol for the imports from the list
of supported protocols.
10. Click Generate. The business integration
view opens showing the generated projects.
11. Click Summary to see the details
of the generated artifacts, and to determine your next steps to finish
implementing the gateway.

## What to do next