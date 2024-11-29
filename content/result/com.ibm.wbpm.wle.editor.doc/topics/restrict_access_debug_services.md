# Restricting access to debugging for services

You might need to limit access to debugging functions in the Inspector. For services
other than human services, you can control which users have the ability to debug services. To edit
the settings, copy the code snippet and then make the necessary changes.

The settings are checked by the server that runs the service. They need to be applied to the
configuration file of your IBM® Workflow
Center when you debug locally in your designer.

The following elements enable you to configure debugging functions for services.

| Element                                                       | Default setting   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------------------------------------------------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <enabled merge="replace">true</enabled>                       | true              | On Workflow Center: Establishes whether debugging of services is enabled. If set to false, when you attempt to debug a service in the Inspector, the service simply runs without any debugging feedback.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| <enforce-debug-role merge="replace">true</enforce-debug-role> | false             | Establishes whether users who don't belong to the Debug group (defined in the following setting) can access the debugging function. Only one user role can be defined. By default, this element is set to false, which allows users who don't belong to the Debug group to access debugging function. So, by default, all users have access to debugging for services. To limit access to users who are members of the Debug group, set this element to true. If enabled as false or enforce-debug-role is false, this setting has no effect. If enabled and debug-role is true, a user with this role has access to debugging functions. A user who isn't assigned this role won't have access to debugging functions and the service runs as it would normally. |
| <debug-role merge="replace">debug</debug-role>                | debug             | Specifies the group that users must be a member of so they can access the debugging function. Only one group can be defined. If one or both of the preceding settings is false (enabled and enforce-debug-role), then this setting has no effect. If both of the preceding settings are true, then  A user who belongs to this role will have access to debugging functionality. A user who does not belong to this role will not have access to debugging functionality. If you do not specify any value for debug-role , debugging functionality is disabled.                                                                                                                                                                                                   |

```
<server>
	<debug>
         <enabled merge="replace">true</enabled>
         <enforce-debug-role merge="replace">true</enforce-debug-role>
         <debug-role merge="replace">debug</debug-role>
	</debug>
</server>
```

For information about the 100Custom.xml file's location and how to create, modify, and deploy it,
see The 100Custom.xml file and configuration.