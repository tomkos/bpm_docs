# Disable automatic schema management

## About this task

```
<load-tracking-definition>
<max-attempts>2</max-attempts>
<loader-factory-class-name ="com.lombardisoftware.server.tracking.definitionloader.BasicDefinitionLoaderFactory" />
<validate queued="true"/>
<store queued="false"/>
<automatic-schema-management>true</automatic-schema-management>
</load-tracking-definition>
```

## Procedure

1. Copy the following content from 00Static.xml to
your custom configuration file (typically, 100Custom.xml).
<load-tracking-definition>
<max-attempts>2</max-attempts>
<loader-factory-class-name ="com.lombardisoftware.server.tracking. 
definitionloader.BasicDefinitionLoaderFactory" />
<validate queued="true"/>
<store queued="false"/>
<automatic-schema-management>true</automatic-schema-management>
</load-tracking-definition>
2. Change the value of <automatic-schema-management> to false and
save the file.
3. Restart the server.
4. After you create a tracking group and update the tracking
definitions for your process application, use the perfDWTool to run
the following commands against the default profile. install\_root/profiles/profile\_name/bin/perfDWTool.sh 
-u userName -p password pending -preview pending.sql

install\_root/profiles/profile\_name/bin/perfDWTool.sh 
-u userName -p password pending -execute