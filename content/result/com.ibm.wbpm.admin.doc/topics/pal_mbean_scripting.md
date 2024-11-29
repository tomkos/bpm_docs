# The Process Application LifeCycle (PAL) MBean

All of the methods exposed by the PALService MBean are listed in
the Javadoc: install\_root/web/mbeanDocs/PAL\_Service.html. Use
a Java Management Extensions (JMX) compliant console (for example,
JConsole) to work with MBeans.

## PALService MBean security considerations

You
can use the MBean to configure fine-grained security for the PAL administrative
actions with multiple security domains and administrative authorization
groups.

The PALService MBean runs on all cluster members of an Business Automation Workflow cluster. The MBean has
methods for each of the Business Automation Workflow wsadmin tasks. The MBean
methods are protected by administrative roles. For example, you can use administrative authorization
groups to make a user a deployer on DE1 but not on DE2. For more information on security roles and
groups, see Securing process applications.

In an environment with multiple
security domains, each security domain can have its own user registry.
Security domains can be attached to resources like servers, clusters,
and buses. In addition, global security settings apply to all administrative
functions and are the default security configuration for user applications.
Use security domains to define a customized configuration for user
applications. All administrative applications, such as the administrative
console, naming resources, and MBeans, use global security configurations.
If no security domains are configured, applications use information
from the global security configuration.

Several administrative
roles are defined to provide degrees of authority that are required
for certain administrative functions from either the administrative
console or the system management scripting interface, as described
in Administrative roles. Access can be granted
to each user per resource. For example, WebSphere Application Server
users can be granted configurator access to a specific instance of
a resource only (an application, an application server, or a node).
WebSphere Application Server users cannot access any other resources
outside of the resources that are assigned to them. The administrative
roles apply per resource and do not apply to the entire cell. However,
there is a cell-wide authorization group for compatibility with earlier
versions. WebSphere Application Server users that are assigned to
administrative roles in the cell-wide authorization group can still
access all of the resources within the cell. To achieve this instance-based
security, or fine-grained security, resources that require the same
privileges are placed in a group that is called the administrative
authorization group or authorization group. WebSphere Application
Server users are granted access to the authorization group by assigning
to them the required administrative role. See Fine-grained administrative security.

The Business Automation Workflow RunAs
role must be configured with a user ID that has the required privileges
to perform the requested function in the cluster security domain.
If the RunAs role is configured, the user ID that is defined as the
RunAs user role completes the actions. If the RunAs user is not configured,
the user ID that called the MBean completes the actions.

```
bpm.de.authenticationAlias.4.name=AdminJobAlias
bpm.de.authenticationAlias.4.user=
bpm.de.authenticationAlias.4.password=
bpm.de.roleMapping.3.name=BPMAdminJobUser
bpm.de.roleMapping.3.alias=AdminJobAlias
```

## Invoking PALService

```
profile\_root/bin/wsadmin.sh -lang jython -username username -password password
```

```
wsadmin>mbean = AdminControl.completeObjectName ("type=PALService,node=node,process=application\_cluster\_member,*")
```

```
AdminControl.invole\_jmx(mgmt.ObjectName(mbean),
"admin\_task\_name",[parameter\_list],[parameter\_type\_list])
```

- Examples: Using the PALService MBean for administrative tasks

 Traditional: 
Refer to the following examples to help you understand how to use the PALService MBean to complete common administrative tasks. All of the examples use the processInstancesPurge method available in the MBean.