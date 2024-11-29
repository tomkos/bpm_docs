# Declaring and passing variables

The variables are local to a process or service. You cannot reference a variable from another
process or service. Variables contain the values or references to business data. To propagate the
business data values and references, you must properly declare the variables and pass them to the
linked processes, services, and message events.

1. Declare variables at the process level.
2. For each linked process and service, declare variables and business
objects to receive the values of the variables of the main process.
3. Pass those variables as inputs to the linked processes and services
that require them for their implementation.
4. Pass the variables from the linked processes and services back
up to the main process as outputs when you want the main process to
be aware of changes made to the variables in the linked processes
or services.

When passing variables from a process to a linked process, their
types should be compatible. For example, a string variable
in a process can only be passed to a linked process if this linked
process has a string variable declared as an input variable.

- How variables are passed between process components at run time

Using variables, business data is passed between process application components at run time. Depending on the components that are involved, the data is passed either by value or by reference.
- Declaring variables for a process or a service

For each process or service flow that you create, you must declare variables to capture the data that activities in the process or service flow use.
- Mapping input and output data for an activity in processes

To pass variables to an activity, you must set the input and output data mapping.
- Mapping input and output data for an activity in a service flow

To pass variables to an activity, you must set the input and output data mapping.
- Declaring variables for a subprocess

Subprocesses and event subprocesses can access the variables of the process they are contained in. They can also have their own variables that are only relevant within the context of the subprocess or event subprocess and any subprocesses or event subprocesses they might contain.
- Testing declared variables and data mapping with coaches

When you declare and map variables in your process, you can test the mapping between activities by using coaches and running your process in the Inspector.