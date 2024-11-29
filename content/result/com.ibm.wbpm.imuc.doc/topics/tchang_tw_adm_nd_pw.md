# Changing the tw\_admin password in an ND cluster
environment

To change the tw\_admin password in an
ND cluster environment that you specified when you installed IBM® Business Automation Workflow, use
the WebSphere® Application
Server administrative
console to change the password.

## Before you begin

## Procedure

1. Log in to the WebSphere Application
Server administrative
console.
2. Navigate to Users and Groups > Manage Users and locate the tw\_admin user
account.
3. Change the password for the tw\_admin user
account.
4 Change the BPMAdmin\_Auth\_Alias password.
    1. In the WebSphere Application
Server administrative
console, click Security > Global
security.
    2. Under Authentication, click JAASConfiguration > J2C Authentication
data.
    3. Navigate to BPMAdmin\_Auth\_Alias.
    4. Change the BPMAdmin\_Auth\_Alias password.
5 Modify the tw\_admin password for the rolesassociated with the tw\_admin administrative username using one of the following methods:

- Go to Enterprise Applications > IBM\_BPM\_Teamworks\_<node and server location> > User RunAs roles, for example: Enterprise Applications > IBM\_BPM\_Teamworks\_Node01\_Server01 > User RunAs roles. Change the
password for the roles with which the tw\_admin administrative
user name is associated and apply the change. For example, if the twem and twuser roles
are associated with the tw\_admin user name, change
the password for those roles.
- Run the util\Security\bpmModifyMapRunAsRole.py utility
to update the password for the administrative user for the system
applications. See Defining RunAs roles user assignments for system applications for more information.Important: You
must run the bpmModifyMapRunAsRole.py utility twice
in a clustered environment. For example,wsadmin.bat -port port number -lang jython -user username -password admin -f C:\WAS\_INSTALL\_LOCATION\util\Security\bpmModifyMapRunAsRole.py -usr  username -pwd admin -clusterName BPM.AppTarget -applicationName Teamworkswsadmin.bat -port port number -lang jython -user username -password admin -f C:\WAS\_INSTALL\_LOCATION\util\Security\bpmModifyMapRunAsRole.py -usr  username -pwd admin -clusterName BPM.Support -applicationName PerformanceDW
6 In a network deployment environment, you must synchronizethe nodes that contain Workflow Center , Workflow Server , or PerformanceData Warehouse cluster members.

1. In the administrative console, click System administration > Nodes.
2. Select all of the nodes and click Full Resynchronize.
3. Stop and restart all of the clusters and servers.
7. Restart the cluster members.

## Related information

- Changing passwords after installation in IBM BPM version 7.5.1