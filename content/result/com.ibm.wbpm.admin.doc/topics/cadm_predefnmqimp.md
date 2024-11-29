<!-- image -->

# Properties of WebSphere MQ
bindings

Typically, WebSphere MQ
import and export bindings are created in Integration Designer. You can
either create the connections and destinations required for the WebSphere MQ binding at the
time the component is installed on your server, or you can specify
the JNDI name of the resources on the server that you intend your WebSphere MQ binding to use.

Configuring the WebSphere MQ
binding depends upon which option was selected.

In the case
where new message provider resources are created (that
is, the resources are created on the server during installation),
the resources will exist and can be located and administered using
the administrative console.

| Resource                          | Module name   | Import name   | Resource global JNDI name         |
|-----------------------------------|---------------|---------------|-----------------------------------|
| Outbound Connection Factory       | mq.module     | my/import     | mq.module/my/import\_MQ\_CF         |
| Response Activation Specification | mq.module     | my/import     | mq.module/my/import\_AS            |
| Send                              | mq.module     | my/import     | mq.module/my/import\_MQ\_SEND\_D     |
| Receive                           | mq.module     | my/import     | mq.module/my/export\_MQ\_RECEIVE\_D  |
| SIB Callback Destination          | mq.module     | my/import     | mq.module/my/import\_MQ\_CALLBACK\_D |
| SIB Callback Connection Factory   | All modules   | my/import     | SCA.MQ/Callback\_CF                |

| Resource                         | Module name   | Export name   | Resource global JNDI name         |
|----------------------------------|---------------|---------------|-----------------------------------|
| Request Activation Specification | mq.module     | my/export     | mq.module/my/export\_AS            |
| Response Connection Factory      | mq.module     | my/export     | mq.module/my/export\_RESP\_CF       |
| Receive                          | mq.module     | my/export     | mq.module/my/export\_MQ\_RECEIVE\_D  |
| Send                             | mq.module     | my/export     | mq.module/my/export\_MQ\_SEND\_D     |
| SIB Callback Destination         | mq.module     | my/export     | mq.module/my/export\_MQ\_CALLBACK\_D |
| SIB Callback Connection Factory  | All modules   | my/export     | SCA.MQ/Callback\_CF                |

- The resources are created at the server
scope. The default scope
in the administrative console is cell. You must change the scope in
order to locate and administer the resources.
- The SIB Callback
Destination and SIB Callback Connection Factory
are SIB JMS resources. The other entries in the table are WebSphere MQ resources. The
two types of resources are administered separately from the administrative
console.

If you select the other option and
the WebSphere MQ binding
is expecting to find
resources on the server that it will use, you must have these resources
installed and the import or export file must contain their JNDI names.
The association between the WebSphere MQ
binding and the resources will then be made.