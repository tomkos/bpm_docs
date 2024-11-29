# Resolving user mismatch between the user information cache
and the database

## About this task

The
problem of user information mismatch between the cache and the database
only occurs in a few environments. As a result, the specified period
of time is set to the default value of 0 milliseconds,
which means that cache entries are always considered valid. You should
only change this value if you experience exceptions, such as a SqlIntegrityConstraintViolationException exception
in the SystemOut.log file that begins with the
following lines:

```
com.lombardisoftware.client.delegate.BusinessDelegateException:
 PreparedStatementCallback;
 SQL [insert into LSW\_USR\_GRP\_MEM\_XREF (USER\_ID, GROUP\_ID) values (?, ?)];
```

## Procedure

- Traditional: To add the configuration setting to the 100Custom.xml file, complete thefollowing steps:
    1. Stop the servers for Workflow Server or Workflow Center.
    2. Open each 100Custom.xml file. For information about the individual
100Custom.xml files that need to be updated and their locations, see the topic
Location of 100Custom configuration files.
    3. In each 100Custom.xml file, add the
user-info-cache-block-period setting. For example, to prevent administrators
from accessing task instance data, add the following elements under the
<properties> element:<server>
    <user-info-cache-block-period merge="replace">120000
    </user-info-cache-block-period>
</server>The period of time is specified in millisecond (ms). If you do not want
to use the default value of 0, the recommended time period is
120000 (2 minutes). If the setting is not set, the period of time defaults to
0. If a value of 0 is specified, the cache entries are
always considered valid.
    4. In each 100Custom.xml file, save your changes.
    5. In a browser, open each 100Custom.xml file to ensure that it contains no
special characters.
    6 Complete one of the following steps:
        - In a clustered environment, ensure that the changes are propagated to the nodes by forcing a
synchronization and restarting the deployment environment.
        - In a stand-alone server environment, restart the server.
- Containers: 
 If
you use containers, make changes to the 100Custom.xml file by following the
procedure described at Customizing Business Automation Workflow properties.