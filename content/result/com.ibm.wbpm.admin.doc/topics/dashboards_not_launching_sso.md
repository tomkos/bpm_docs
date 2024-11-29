# Dashboards cannot be launched in some single sign-on environments

## About this task

## Procedure

- To use the WebSphere administrative console to set the com.ibm.bpm.dashboard.whitelist propertyfor your environment, complete the following steps:
    1. Log into the administrative console.
    2. In the tree view, expand Servers > Server
Types  and select WebSphere application
servers. The Application servers page opens.
    3. Click your server name to open the Configuration page, then expand Java
and Process management and select Process definition to
open the Process definition page.
    4. Select Java Virtual Machine to open the
Java Virtual Machine page and then select Custom properties to
open the Custom properties page.
    5. Click New to open the New page where you
will add the JVM custom property.
    6. In the Name field, type com.ibm.bpm.dashboard.whitelist.
    7. In the Value field, specify a comma-separated
list of acceptable host names or domains.
    8. In the Description field, type Whitelist
of SSO access gateway servers or referrers.
    9. Click OK and then click the Save link
to save the changes in the administrative console.
    10. In a clustered environment, repeat the previous steps for each
application cluster member.
    11. Restart the stand-alone server or the application cluster members
to activate the new property.
- To use the wsadmin scripting client to set the com.ibm.bpm.dashboard.whitelist property
for your environment, run the following commands (where cluster\_name is
the cluster name in your environment): for server in AdminUtilities.convertToList(AdminConfig.showAttribute(AdminConfig.getid("/Cell:/ServerCluster:cluster\_name/"), "members")):
    serverName = AdminConfig.showAttribute(server, "memberName")
    nodeName = AdminConfig.showAttribute(server, "nodeName")
    AdminTask.setJVMSystemProperties( [ '-serverName', serverName, '-nodeName', nodeName, '-propertyName', 'com.ibm.bpm.dashboard.whitelist', '-propertyValue', 'hostname.com' ] ')
    property = AdminConfig.getid("/Cell:/Node:%s/Server:%s/JavaProcessDef:/JavaVirtualMachine:/Property:com.ibm.bpm.dashboard.whitelist/" % (nodeName, serverName))
    AdminConfig.modify(property, [['description', 'Whitelist of SSO access gateway servers or referrers']])
AdminConfig.save()