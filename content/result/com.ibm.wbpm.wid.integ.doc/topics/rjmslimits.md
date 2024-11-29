<!-- image -->

# Limitations of the JMS, MQ JMS and generic JMS bindings

The limitations of using the JMS, MQ JMS and generic JMS
bindings are discussed in the following sections.

- Implications of generating default bindings
- Response correlation scheme
- Bidirectional support
- Adapters using JMS RAR files

## Implications of generating default
bindings

When you generate a binding, several fields will
be filled in for you as defaults, if you do not choose to enter the
values yourself. For example, a connection factory name will be created
for you. If you know that you will be putting your application on
a server and accessing it remotely with a client, you should at binding
creation time enter JNDI names rather than take the defaults since
you will likely want to control these values through the administrative
console at run time.

However, if you did accept the defaults
and then find later that you cannot access your application from a
remote client, you can use the administrative console to explicitly
set the connection factory value. Locate the provider endpoints field
in the connection factory settings and add a value such as <server\_hostname>:7276
(if using the default port number).

## Response correlation
scheme

If you use the Request Correlation ID to Correlation
ID value in the Response correlation scheme field, which is used to
correlate messages in a request-response operation, you must have
a dynamic correlation ID in the message.

To create a dynamic
correlation ID in a mediation module using the mediation flow editor,
add an XSLT node before the import with the JMS binding. Open the
XSLT map editor. The known service component architecture headers
will be available in the target message. Drag a field containing a
unique ID in the source message onto the correlation ID in the JMS
header in the target message.

## Bidirectional support

Only
ASCII characters are supported for Java™ Naming
and Directory Interface (JNDI) names at run time.

## Adapters using JMS RAR files

1. When you import the project interchange file do not select  websphere\_default\_messaging\_provider.
2. Import all your SCA modules except the JMS connector into the
workspace.
3. Once the migration is complete, open the assembly editor for any
one of the modules.
4. Select a JMS binding component on the assembly editor and open
any binding configuration tab in the Properties view. After a few
moments you will see that the new JMS connector appears in the workspace
and the binding properties are available for editing.