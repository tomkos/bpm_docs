<!-- image -->

# Generic JMS headers

A JMS message contains two types of headers-the JMS system header
and multiple JMS properties. Both types of headers can be accessed
either in a mediation module in the Service Message Object (SMO) or
by using the ContextService API.

- JMSType
- JMSCorrelationID
- JMSDeliveryMode
- JMSPriority

The Generic JMS binding also supports dynamic modification
of JMS headers and properties in the same manner as the JMS and MQ
JMS bindings.

Some Generic JMS providers place restrictions on which
properties can be set by the application and in what combinations.
You must consult your third-party product documentation for more information.
However, an additional property has been added to the methodBinding,
ignoreInvalidOutboundJMSProperties, which allows any exceptions to
be propagated.

The Generic JMS headers and message properties are used
only when the base service component architecture SCDL binding switch
is turned on. When the switch is turned on, context information is
propagated. By default, this switch is on. To prevent context information
propagation, change the value to false.

```
<esbBinding xsi:type="eis:JMSImportBinding" contextProgagationEnabled="true">
```