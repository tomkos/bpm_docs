# exportWASConfig.py script

- Data sources
- JDBC providers
- JMS providers
- Connection factories
- JMS activation specifications
- JMS queue and topic specifications
- Namespace bindings
- Authentication aliases
- Secure Sockets Layer (SSL)
- Service integration buses (SIBs) and messaging engines

The exportWASConfig.py script
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
log file is named exportWASConfig\_yyyyMMdd\_hhmmss.log.

Start the wsadmin scripting client from the profile\_root/bin directory.

## Syntax

```
deployment\_manager\_profile/bin/wsadmin -conntype NONE -lang jython -f exportWASConfig.py
[-listDataSources  | -exportAllDataSources | -exportDataSource jndi\_name | 
  -listJDBCProviders  | -exportAllJDBCProviders  | 
  -listJMSProviders  | -exportAllJMSProviders  | 
  -listConnectionFactories  | -exportAllConnectionFactories  | -exportConnectionFactory jndi\_name |
  -listActivationSpecs | -exportAllActivationSpecs  | -exportActivationSpec jndi\_name |
  -listQueuesAndTopics | -exportAllQueuesAndTopics  | -exportQueueOrTopic jndi\_name |
  -listNameSpaceBindings | -exportAllNameSpaceBindings | -exportNameSpaceBinding namespace\_ID |
  -listAuthAliases | exportAllAuthAliases | -exportAuthAlias alias\_name |
  -exportSSLSettings | 
  -exportJavaSecurityFile |
  -exportSIBusConfig bus\_name ]
output\_directory
[-cell cell\_name]
[-node node\_name -server server\_name]  | [-cluster cluster\_name]
```

## Parameters

The
configuration for each data source is exported to
output\_directory/datasource\_id.obj. A
summary file output\_directory/exportDS.properties is also
created.

The
configuration for the data source with the specified JNDI name is exported to
output\_directory/datasource\_id.obj. A
summary file output\_directory/exportDS.properties is also
created.

- forwardRoutingPath
- reverseRoutingPath

The configuration for each authentication alias is exported to
output\_directory/auth\_alias\_id.obj. A
summary file output\_directory/exportAlias.properties is also
created.

The
configuration for the authentication alias with the specified name is exported to
output\_directory/auth\_alias\_id.obj. A
summary file output\_directory/exportAlias.properties is also
created.

Each SSL
setting is exported to
output\_directory/SSL\_Alias\_Name.obj. A
summary file output\_directory/exportSSL.properties is also
created.

- Bus
- Bus members
- Messagine engines
- Foreign buses
- Destinations
- Security

## Examples

```
wsadmin -conntype NONE -f /tmp/exportWASConfig.py -exportAllDataSources /tmp/exportedDataSources -cell Cell01 -cluster AppCluster
```

```
wsadmin -conntype NONE -f /tmp/exportWASConfig.py -exportDataSource /tmp/exportedDataSources jdbc/WPSDB -cell Cell01
```

```
wsadmin -conntype NONE -f /tmp/exportWASConfig.py -exportAllJDBCProviders /tmp/exportedJDBCProviders -cell Cell01
```

```
wsadmin -conntype NONE -f /tmp/exportWASConfig.py -exportSSLSettings /tmp/exportedSSLSettings
```

```
wsadmin -conntype NONE -f exportWASConfig.py -exportJavaSecurityFile /tmp/exportedJavaSecurityFile
```

```
wsadmin -conntype NONE -f /tmp/exportWASConfig.py -exportAllAuthAliases /tmp/exportedAuthAliases
```

```
wsadmin -conntype NONE -f /tmp/exportWASConfig.py -exportAuthAlias SCA\_Auth\_Alias /tmp/exportedAuthAliases
```

```
wsadmin -conntype NONE -f exportWASConfig.py -listDataSources
```

```
wsadmin -conntype NONE -f exportWASConfig.py -listAuthAliases
```