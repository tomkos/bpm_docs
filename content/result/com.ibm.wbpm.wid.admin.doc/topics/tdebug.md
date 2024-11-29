<!-- image -->

# Using the integration debugger for problem determination

## About this task

- Component debugging

The integration debugger is an IBM Integration Designer tool that you can use to visually debug local or remote business integration components, such as business processes, business object data maps, mediation flows, and others.
- Integration debugger

In IBM Integration Designer, the integration debugger is the designated tool for debugging business integration components. The integration debugger features a sophisticated user interface that enables you to easily and precisely perform component debugging.
- Breakpoints in the integration debugger

In the integration debugger, you can add, disable, enable, or remove breakpoints. Breakpoints in the integration debugger are conceptually similar to breakpoints in the Java™ development tools (JDT) debugger. They are set at specific locations in a component where you want the component instance to pause so that you can determine the status of the component.
- Setting preferences for the integration test client

By default, the user-definable preferences for the integration test client are already optimized for testing modules. However, in the course of your testing activities, you may find that you want to change some preferences.
- Preparing for remote debugging

If you want to debug business integration components in a large application using the IBM Integration Designer integration debugger, you should consider deploying the application to a remote IBM Workflow Server machine and debugging it remotely from IBM Integration Designer. This can significantly enhance performance and minimize potential memory problems on your IBM Integration Designer machine
- Creating a component instance

Before you can work with the integration debugger, you must create an instance of the component that you want to debug. A component instance is a running component that can be run in parallel with other instances of the same component, such as a business process.
- Managing breakpoints in the integration debugger

In the component editors, you can add, disable, enable, or remove breakpoints on component elements and Java code. You can also use the Breakpoints view to manage the breakpoints.
- Stepping through component instances in the integration debugger

In the integration debugger, you can step into, step over, or step out of various elements in a component instance.
- Managing test variations

A test variation is a specific set of variable values for a test case. Although each test case is automatically assigned a default test variation, you can create multiple test variations for a test case that each contain a different set of variable values. When a test case is run, all of the test variations for the test case are run.
- Limitations for the integration debugger

From time to time, you may encounter some limitations when using the integration debugger. In most situations, you can work around these limitations and continue to successfully debug your business integration components.