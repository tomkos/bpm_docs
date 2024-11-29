<!-- image -->

# Calling business services

## About this task

The Invoke activity calls an operation from another service.
To use an Invoke activity, you must specify a reference partner. The
reference partner always points to the Interface of the service that
you are calling. Then you associate the Invoke with that reference
partner and select one operation that you want to call on that partner.
You can have multiple Invoke activities for one partner. When the
Invoke activity runs, it will invoke the specified operation. If the
operation has inputs or outputs you must specify variables for each
of those inputs and outputs. These variables hold the data that is
being sent to the service or received from the service.

An outline
of how to call a business service from your BPEL process is provided
below. See related links for more detailed information.

## Procedure

1. Create a reference partner that points to the interface
of the target service.
2 Create an Invoke activity and associate it with this referencepartner.
    - Drag the partner onto the canvas, which automatically creates
an Invoke activity, or
    - Manually create an Invoke activity and associate the referencepartner:
        1. Add an Invoke activity to your BPEL process.
        2. In the properties view of the Invoke, set the partner.
3. In the Details tab of the Properties view of the Invoke,
select one operation of the partner.
4. In the Details tab of the Properties view of the Invoke,
set the data for that operation by providing appropriate variables
for each input and output of the operation.
5. Drop both the process and the partner onto the assembly
diagram, and create a wire between them. If the partner is not a local
component, create an Import and wire the process to the Import.