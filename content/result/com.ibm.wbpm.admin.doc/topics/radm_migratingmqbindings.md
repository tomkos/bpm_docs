<!-- image -->

# Migrating WebSphere MQ Bindings from version 6 to
later versions

Migration is only required for WebSphere® MQ
bindings that contain pre-configured resources.

## Specifying an activation specification

In WebSphere ESB version 7, the WebSphere MQ binding uses the WebSphere MQ resource adapter to receive messages, which requires an activation specification.
If a WebSphere MQ binding has pre-configured WebSphere MQ resources, define an additional activation
specification JNDI name in the end-point configuration of the binding. This JNDI name must refer to
an existing activation specification JMS resource on the server.

## Modifying connection factory properties

- SENDEXIT
- RECEXIT
- SENDEXITINIT
- RECEXITINIT

## Modifying destination properties

You must add these custom properties in the pre-configured destinations:

| Destination Type    | Property Name   | Property Value   | Property Type    |
|---------------------|-----------------|------------------|------------------|
| Send destination    | MDWRITE         | YES              | java.lang.String |
| Send destination    | MSGBODY         | MQ               | java.lang.String |
| Send destination    | MDMSGCTX        | SET\_ALL\_CONTEXT  | java.lang.String |
| Receive destination | MDREAD          | YES              | java.lang.String |
| Receive destination | MSGBODY         | MQ               | java.lang.String |
| Receive destination | MDMSGCTX        | SET\_ALL\_CONTEXT  | java.lang.String |