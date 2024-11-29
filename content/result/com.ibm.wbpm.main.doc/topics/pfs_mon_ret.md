# Monitoring and administering retrievers with MBeans

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

To view BPD and BPEL retrievers MBean attributes, modify the attributes that are not in read-only
mode, and invoke operations, in addition to the curl command and the Administration scripts
mentioned in the following list, you can also use JConsole (for more information, see Using JConsole to interact with indexer MBeans).

- MBeans for BPD retrievers

Each JMX MBean for BPD retrievers has a specific Object Name, some attributes that you can access, and operations that you can invoke.
- MBeans for BPEL retrievers

Each JMX MBean for BPEL retrievers has a specific Object Name, some attributes that you can access, and operations that you can invoke.
- MBeans for Case retrievers

Each JMX MBean associated with a Case retriever has an Object Name, some attributes that you can access, and operations that you can invoke.
- Using the curl command to access the retriever MBeans

You can use the curl command to view BPD and BPEL retriever MBean attributes that are in read-only mode.
- Using the Administration scripts to access the retriever MBeans

You can access remotely the BPD, BPEL or Case retriever MBeans using the administration scripts to monitor the values of the attributes.