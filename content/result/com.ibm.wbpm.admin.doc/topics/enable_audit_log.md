# Enabling the audit log

## Procedure

- audit-file-location: The full path name to an existing directory where the logs
will be stored. This parameter must be set.
- audit-file-name: Name of the audit file to use, ending in
.log. The default is bawaudit.log.
- audit-rollover-size: Size (in MB) at which the audit file will roll over. The
default is 100.
- audit-enabled: Enable auditing. The default is false.
- verbose: Add additional information to the log message. This additional
information requires database queries, for example originalData to see the previous
value. The default is true.
- max-historical-files: Maximum number of rolled-over files to keep before the
old ones get removed. Use -1 for no cleanup. The default is
5.

```
<server>
   <audit-config>
      <audit-file-location merge="replace">C:/BAW/AppServer/profiles/StandAloneProfile/logs/server1</audit-file-location>
      <audit-file-name merge="replace">bawaudit.log</audit-file-name>
      <audit-rollover-size merge="replace">100</audit-rollover-size>
      <audit-enabled merge="replace">false</audit-enabled>
      <verbose merge="replace">true</verbose>
      <max-historical-files merge="replace">5</max-historical-files>
    </audit-config>
</server>
```