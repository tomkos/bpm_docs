# importWASConfig.py script

- Authentication aliases, JDBC providers, JMS providers, and resource
adapters
- Data sources (which refer to authentication aliases and JDBC providers)
- Namespace bindings
- Bus and messaging engines, bus links, bus destinations (which
refer to namespace bindings)
- Connection factories (which refer to authentication aliases, JMS
providers, and bus names)
- JMS queue and topic specifications (which refer to bus names)
- Activation specifications (which refer to authentication aliases,
JMS providers, bus and messaging engine names, and JMS queues)

After you run the importWASConfig.py command,
restart the IBM® Business Automation Workflow environment.

The importWASConfig.py script
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- Run the command in disconnected mode; that is,
with the server stopped. Use the -conntype none option.

## Location

The script is in install\_root/util/migration/scripts.
If you installed the new version of the product on a different computer
and copied the migration files to the source environment, the script
is in remote\_migration\_utility/util/migration/scripts.

A
log file is created in the directory where you run the command. The
log file is named importWASConfig\_yyyyMMdd\_hhmmss.log.

Start the wsadmin scripting client from the profile\_root/bin directory.

## Syntax

```
deployment\_manager\_profile/bin/wsadmin -conntype NONE -lang jython -f importWASConfig.py
[-importAllAuthAliases | -importAuthAlias alias\_name |
  -importAllJDBCProviders  | 
  -importAllJMSProviders  |
  -importAllDataSources | -importDataSource jndi\_name | 
  -importAllNameSpaceBindings | -importNameSpaceBinding namespace\_ID | 
  -importSIBusConfig bus\_name | 
  -importAllConnectionFactories  | -importConnectionFactory jndi\_name | 
  -importAllQueuesAndTopics  | -importQueueOrTopic jndi\_name | 
  -importAllActivationSpecs  | -importActivationSpec jndi\_name | 
  -importAllSSLSettings | -importSSLSetting alias\_name | 
  -importJavaSecurityFile ]
input\_directory
```

## Parameters

The configuration for each authentication alias is imported to the target environment. If an
authentication alias with that name exists, it is skipped.

The configuration for the authentication alias with the specified name is
imported to the target environment, unless an authentication alias with that name exists. If it
exists, you are asked if you want to update it.

If the JNDI name of the data source exists in the
target environment, the configuration is updated. Otherwise, a new data source is created and you
are prompted for the scope and JDBC provider.

- Bus
- Bus members
- Messagine engines
- Foreign buses
- Destinations
- Security

- forwardRoutingPath
- reverseRoutingPath

```
#Exported SLL Setting
CellDefaultSSLSettings.ObjectFileName=CellDefaultSSLSettings.obj
CellDefaultSSLSettings.ScopeName=(cell):bxv9v447Cell01
#Exported SLL Setting
NodeDefaultSSLSettings.ObjectFileName=NodeDefaultSSLSettings.obj
NodeDefaultSSLSettings.ScopeName=(cell):bxv9v447Cell01:(node):bxv9v447Node01
```

The SSL setting with the
specified alias is imported to the target environment.

## Examples

```
wsadmin -conntype NONE -f /tmp/importWASConfig.py -importAllAuthAliases  /tmp/exportedAuthAliases
```

```
wsadmin -conntype NONE -f /tmp/importWASConfig.py -importAuthAlias tmp/SCA\_Auth\_Alias /tmp/exportedAuthAliases
```

```
wsadmin -conntype NONE -f /tmp/importWASConfig.py -importAllDataSources /tmp/exportedDataSources
```

```
wsadmin -conntype NONE -f /tmp/importWASConfig.py -importDataSource jdbc/WPSDB /tmp/exportedDataSources
```

```
wsadmin -conntype NONE -f /tmp/importWASConfig.py -importAllJDBCProviders /tmp/exportedJDBCProviders
```

```
wsadmin -conntype NONE -f /tmp/importWASConfig.py -importAllSSLSettings /tmp/exportedSSLSettings
```

```
wsadmin -conntype NONE -f /tmp/importWASConfig.py -importSSLSetting CellDefaultSSLSettings /tmp/exportedSSLSettings
```

```
wsadmin -conntype NONE -f /tmp/importWASConfig.py -importJavaSecurityFile /tmp/exportedJavaSecurityFile
```