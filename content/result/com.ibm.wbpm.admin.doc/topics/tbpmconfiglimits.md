# Limitations in administering the BPM document store

The following list contains some known limitations of
the BPM document store:

- You receive an FNRAC1008E error if Java 2 Security is enabled
- The document store must be enabled at configuration time for an Business Automation Workflow installation that is configured to use DB2 on z/OS
- The document store is only available when Federated Repositories is used as the user registry
- An exception occurs when you are logging or tracing document store operations
- Defining too many properties can exceed the table row size limit
- You cannot use IBM Content Navigator to view the BPM document store

Although
the BPM document store is
not available in these situations, you can continue to work with your
document attachments in the Business Automation Workflow database.
Alternatively, you can configure an external Enterprise Content Manager
(ECM) system for storing your documents. In either situation, the
legacy document APIs continue to be used. Any ECM operations that
specify the BPM document store as
a server will fail.

## You receive an FNRAC1008E error if
Java 2 Security is enabled

## The document store must be enabled at configuration
time for an Business Automation Workflow installation
that is configured to use DB2 on z/OS

## The document store is only available
when Federated Repositories is used as the user registry

To
use the document store with your LDAP users and groups, configure
LDAP as a repository in Federated Repositories instead of using stand-alone
LDAP as the user registry. Additional information is found in Configuring the user registry.

## An exception occurs when you are logging
or tracing document store operations

```
[3/19/13 23:31:12:548 PDT] 00000084 SystemErr     R log4j:WARN No appenders could be found for logger (filenet\_error.api.com.filenet.apiimpl.util.ConfigValueLookup).
[3/19/13 23:31:12:548 PDT] 00000084 SystemErr     R log4j:WARN Please initialize the log4j system properly.
[3/19/13 23:31:14:482 PDT] 00000084 SystemErr     R log4j:WARN Configuring default logging to the file E:\IBM\WebSphere\AppServer\profiles\Custom01\FileNet\
testDE1.AppCluster.WIN-E6GDL89KDJDNode01.0\p8\_server\_error.log
[3/19/13 23:31:49:536 PDT] 00000084 SystemErr     R log4j:WARN No appenders could be found for logger (filenet\_error.api.com.filenet.apiimpl.util.ConfigValueLookup).
[3/19/13 23:31:49:536 PDT] 00000084 SystemErr     R log4j:WARN Please initialize the log4j system properly.
[3/19/13 23:33:25:867 PDT] 00000108 SystemErr     R SLF4J: Class path contains multiple SLF4J bindings.
```

## Defining
too many properties can exceed the table row size limit

## You cannot use IBM Content
Navigator to
view the BPM document store