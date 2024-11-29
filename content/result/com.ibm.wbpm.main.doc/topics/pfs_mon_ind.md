# Monitoring and administering indexers with MBeans

- Monitor a running indexer to collect runtime metrics and status.
- Perform administrative tasks such as running unscheduled maintenance operations.

The MBeans are remotely accessible through the Liberty JMX REST Connector, which accepts only
secured SSL client connections with user authentication.

1. Add the restConnector-2.0 feature to the <featureManager>
section.
2. Define an existing user declared in LDAP or in the basic registry as a Liberty
administrator.

```
<featureManager>
   <feature>restConnector-2.0</feature>
</featureManager>

<administrator-role>
   <user>uid=admin,o=defaultWIMFileBasedRealm</user>
</administrator-role>
```

```
-XX:+DisableAttachMechanism,
-Dcom.ibm.tools.attach.enable=no
```

To view BPD and BPEL indexers MBean attributes, modify the attributes that are not in read-only
mode, and invoke operations, in addition to the curl command and the Administration scripts
mentioned in the following list, you can also use JConsole (for more information, see Using JConsole to interact with indexer MBeans).

- MBeans for BPD indexers

Each JMX MBean for BPD indexers has a specific Object Name, some attributes that you can access, and operations that you can invoke. There is no indexer MBean available if the BPD federated system is directly indexed by Business Automation Workflow, and not by Process Federation Server.
- MBeans for BPEL indexers

Each JMX MBean for BPEL indexers has a specific Object Name, some attributes that you can access, and operations that you can invoke.
- Using the curl command to access the indexers MBeans

You can use the curl command to view BPD and BPEL indexers MBean attributes, modify the attributes that are not in read-only mode, and invoke operations.
- Using the Administration scripts to access the indexers MBeans

You can access remotely the BPD or BPEL indexer MBeans using the administration scripts to monitor the values of the attributes and to execute a specific action on the indexer.