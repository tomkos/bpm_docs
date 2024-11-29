<!-- image -->

# Component debugging

To perform debugging, you need:

- The test environment
- The integration debugger

The test environment and the integration debugger are described
in greater detail in the following sections.

## The test environment

The test environment
features runtime support for  IBM Workflow
Server,
and helps you to debug many of the business integration components
that can be created in IBM Integration
Designer,
including mediation flows.

## The integration debugger

The integration
debugger uses and extends the Java™ development
tools (JDT) debugger. However, unlike the JDT debugger, the integration
debugger features a graphical debugging environment for debugging
the following types of business integration components:

- Business processes
- Business object data maps
- Business rule sets and decision tables
- Business state machines
- Visual snippets
- Mediation flows
- XML maps

Note that you can only debug XML maps within the workspace
and not on a server, because debugging will only pause for breakpoints
set in the XML map when you are testing or debugging within the workspace.
Breakpoints will not cause the maps to pause when running on the server.

The
integration debugger documentation provides sufficient information
about the basic JDT debugger tools to enable you to work with the
integration debugger. However, if you want to learn more about the
JDT debugger, see http://www.eclipse.org/eclipse/debug.

In
the integration debugger, you can set breakpoints on component elements
and source code. For example, in business processes, you can set breakpoints
on activities and Java snippet code. You can then
step through the component, change the values of its variables or
messages, and step into elements or source code. These capabilities
enable you to debug a wide variety of problems in a component, such
as:

- Links that have incorrectly implemented transition conditions
- Infinite loops that are not intended to be infinite
- Improper Java conditions