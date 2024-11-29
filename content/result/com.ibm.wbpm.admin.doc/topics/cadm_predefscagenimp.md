<!-- image -->

# Properties of Generic JMS
bindings

Typically, the Generic JMS bindings are created
in Integration Designer.
You can
either create the connections and destinations required for the JMS
binding at the time the component is installed on your server, or
you can specify the JNDI name of the resources on the server that
you intend your JMS import or export to use.

Configuring the Generic JMS
binding depends upon which
option was selected.

| Resource             | Generated resource JNDI name         |
|----------------------|--------------------------------------|
| Outbound Connection  | [moduleName]/[importName]\_CF         |
| Response Connection  | [moduleName]/[importName]\_RESP\_CF    |
| Send destination     | [moduleName]/[importName]\_SEND\_D     |
| Receive destination  | [moduleName]/[importName]\_RECEIVE\_D  |
| Callback destination | [moduleName]/[importName]\_CALLBACK\_D |

| Resource             | Generated resource JNDI name         |
|----------------------|--------------------------------------|
| Inbound Connection   | [moduleName]/[exportName]\_LIS\_CF     |
| Response Connection  | [moduleName]/[exportName]\_RESP\_CF    |
| Receive destination  | [moduleName]/[exportName]\_RECEIVE\_D  |
| Send destination     | [moduleName]/[exportName]\_SEND\_D     |
| Callback destination | [moduleName]/[exportName]\_CALLBACK\_D |

If you select the other option and the
JMS import is expecting
to find required resources on the server, you must have these resources
installed and the import and export files must contain the JNDI names.
The association between the JMS binding and the resources will then
be made.