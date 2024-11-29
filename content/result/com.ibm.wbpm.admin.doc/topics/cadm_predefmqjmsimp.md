<!-- image -->

# Properties of
MQ JMS bindings

Typically, MQ JMS bindings are created in Integration Designer. You can
either create the connections and destinations required for the JMS
binding at the time the component is installed on your server, or
you can specify the JNDI name of the resources on the server that
you intend your MQ JMS import or export to use.

Configuring
the MQ JMS binding depends upon which option was selected.

In
the case where new message provider resources are created (that
is, the resources are created on the server during installation),
the resources will exist and can be located and administered using
the administrative console.

| Resource                               | Module name   | Import name   | Resource global JNDI name            |
|----------------------------------------|---------------|---------------|--------------------------------------|
| Outbound Connection Factory            | mqjms.module  | my/import     | mqjms.module/my/import\_MQ\_CF         |
| Response Activation Specification      | mqjms.module  | my/import     | mqjms.module/my/import\_AS            |
| Failed Event Replay Connection Factory | mqjms.module  | my/import     | mqjms.module/my/import\_RESP\_CF       |
| Send                                   | mqjms.module  | my/import     | mqjms.module/my/import\_MQ\_SEND\_D     |
| Receive                                | mqjms.module  | my/import     | mqjms.module/my/export\_MQ\_RECEIVE\_D  |
| SIB Callback Destination               | mqjms.module  | my/import     | mqjms.module/my/import\_MQ\_CALLBACK\_D |
| SIB Callback Connection Factory        | All modules   | my/import     | SCA.MQJMS/Callback\_CF                |

| Resource                               | Module name   | Export name   | Resource global JNDI name            |
|----------------------------------------|---------------|---------------|--------------------------------------|
| Request Activation Specification       | mqjms.module  | my/export     | mqjms.module/my/export\_AS            |
| Failed Event Replay Connection Factory | mqjms.module  | my/export     | mqjms.module/my/export\_LIS\_CF        |
| Response Connection Factory            | mqjms.module  | my/export     | mqjms.module/my/export\_RESP\_CF       |
| Receive                                | mqjms.module  | my/export     | mqjms.module/my/export\_MQ\_RECEIVE\_D  |
| Send                                   | mqjms.module  | my/export     | mqjms.module/my/export\_MQ\_SEND\_D     |
| SIB Callback Destination               | mqjms.module  | my/export     | mqjms.module/my/export\_MQ\_CALLBACK\_D |
| SIB Callback Connection Factory        | All modules   | my/export     | SCA.MQJMS/Callback\_CF                |

- The resources are created at the
server scope. The default scope
in the administrative console is cell. You must change the scope in
order to locate and administer the resources.
- The SIB callback
destination and SIB callback connection factory
are SIB JMS resources. The other entries in the table are MQ JMS resources.
The two types of resources are administered separately in the
administrative console.

If you select the
other option and the MQ JMS import or export binding is
expecting to find on the server resources that it will use, you must
have these resources installed and the import file must contain their
JNDI names. The association between the MQ JMS import and the resources
will then be made.