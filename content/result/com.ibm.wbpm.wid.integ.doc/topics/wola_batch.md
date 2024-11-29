<!-- image -->

# Transactions, security, and connection properties for batch
programs on z/OS

## Batch outbound calling

Outbound interactions
with batch programs on z/OS are achieved using the native WOLA APIs
(Host Service and Receive Request). WOLA does not support transactions
for batch programs.

## Batch security and connection properties

For
outbound calls to batch server programs, the user ID of the batch
job is used for requests from WebSphere Application Server for z/OS.
There is no identity propagation in this scenario.

In the New
External Service wizard, on the Security and
Configuration Properties page, specify the JNDI name of
the connection factory defined on WebSphere Application Server for z/OS or
specify the connection properties for the batch program in the binding.
If you choose to specify the connection properties, then the managed
connection factory is created during deployment with the specified
properties.

For batch programs on z/OS, you must specify the
following information in the New External Service wizard:

- Specify the target register name in the Security and
Configuration Properties page.
- Specify the name of external service to invoke in the InteractionSpec Service
name property for the selected operation in the New
External Service wizard.