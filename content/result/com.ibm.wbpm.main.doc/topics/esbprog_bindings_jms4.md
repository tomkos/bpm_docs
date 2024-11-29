<!-- image -->

# Using dynamic JMS endpoints

Figure 1. Mediation module with an unwired import which is configured to use service provider 1

<!-- image -->

- /headers/SMOHeader/Target/address
- /headers/SMOHeader/Target/@bindingType
- /headers/SMOHeader/Target/@import
- /headers/SMOHeader/AlternateTarget/address
- /headers/SMOHeader/AlternateTarget/@bindingType
- /headers/SMOHeader/AlternateTarget/@import

The address field includes the dynamic invocation target service URI for
requests. When requests are routed, the @bindingType field provides further
details about the URI. It indicates the type of binding that is used during a dynamic invocation.
When requests are routed, the @import field provides the name of a target
import that is used for dynamic invocation.

```
>>-scheme--:--jms-variant--:--jms-dest--?--parameter-----------><
```

- The scheme for a JMS URI must be jms.
- The jms-variant provides more information about the JMS connection (for example
by using the variant jndi).
- jms-dest identifies the JMS destination object, and must correspond to the
jms-variant.
- parameter is a key value pair separated by =. The only key supported is
jndiConnectionFactoryName. The value of this key must be the JNDI name of the connection
factory. Usage of this parameter is optional.

```
jms:jndi:MyTargetQueueName?jndiConnectionFactoryName=MyConnectionFactoryName
```