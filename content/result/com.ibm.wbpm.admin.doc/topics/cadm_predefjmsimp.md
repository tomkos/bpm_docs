<!-- image -->

# Properties of
JMS bindings

Typically, JMS import and export bindings are created
in Integration Designer. When
you configure the binding, you can either create the connections and
destinations required for the JMS binding (by selecting Configure
new messaging provider resources, which is the default),
or you can select Use pre-configured messaging provider
resources. If you choose pre-configured, you add the JNDI
names for the connection factory and the send destination (for a one-way
operation) or the send and receive destinations (for a request-response
operation).

Configuring the JMS binding depends upon which
option was selected.

```
moduleName/importName\_resourceAbbreviation
```

```
moduleName/exportName\_resourceAbbreviation
```

```
Inventory/Import1\_CF
```

| Property                          | Example                         |
|-----------------------------------|---------------------------------|
| JNDI name for connection factory  | moduleName/importName\_CF        |
| JNDI name for send destination    | moduleName/importName\_SEND\_D    |
| JNDI name for receive destination | moduleName/importName\_RECEIVE\_D |

| Property                               | Example                         |
|----------------------------------------|---------------------------------|
| JNDI name for activation specification | moduleName/exportName\_AS        |
| JNDI name for receive destination      | moduleName/exportName\_RECEIVE\_D |
| JNDI name for send destination         | moduleName/exportName\_SEND\_D    |