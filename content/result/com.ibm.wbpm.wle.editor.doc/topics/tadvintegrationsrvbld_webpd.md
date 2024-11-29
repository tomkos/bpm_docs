# Invoking an Advanced Integration Service in the Process Designer

## Procedure

To invoke an existing AIS, perform one of the following
steps.

- To invoke the AIS from a process:
    1. Add the toolkit that was provided by the integration
developer to your process application as dependency.
    2. From the palette of the process editor, choose System
Task.
    3. On the Implementation tab of
the system task under Properties, click Select and
select the Advanced Integration Service provided by the toolkit.
    4. On the Data Mapping tab, provide
the mappings for the inputs and outputs. The integration developer
should provide you with information about what type of objects are
required.
- To invoke the AIS from a service flow

1. Add the toolkit that was provided by the integration
developer to your process application or toolkit as a dependency.
2. From the palette of the service flow, choose Linked
Service Flow and drop it into the diagram.
3. On the Implementation tab of
the linked service flow under Properties, click Select and
select the Advanced Integration Service that is provided by the toolkit.
4. On the Data Mapping tab, provide
the mappings for the inputs and outputs. The integration developer
should provide you with information about what type of objects are
required.

## Results

The Advanced Integration Service is invoked from a service
flow or a process.

## What to do next