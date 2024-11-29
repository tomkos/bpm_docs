# Whether process instances run in deactivated snapshots

- Web service integrations
- Web services
- JavaScript APIs
- REST APIs
- UCA processes

- block-deactivated-snapshot-task-progression: When set to
true, this property prevents task-based services, like process activities,
from starting or progressing. Running process instances will not be able to finish.
- block-deactivated-snapshot-favorite-progression: When set to
true, this property prevents services from starting or progressing if they do
not have tasks and are associated with exposed favorites (startable services, URLs, project pages,
and dashboards).

```
<server>
        <block-deactivated-snapshot-favorite-progression merge="replace">false</block-deactivated-snapshot-favorite-progression>         
        <block-deactivated-snapshot-task-progression merge="replace">false</block-deactivated-snapshot-task-progression>
</server>
```

For more information about modifying XML configuration settings,
see the topic The 100Custom.xml file and configuration.