<!-- image -->

# Security considerations for recovery

FEM queries target different sources for different types of failed
events. BPC-type failed events are queried by API calls to the Business Flow Manager API. Only a
BPESystemAdministrator is allowed to run Business Flow Manager API queryAll()
calls, which are necessary to query BPC-type failed events without work item authorization.
Therefore, in an Business Automation Workflow environment, any
administrative user that works with FEM must be part of the BPEContainer's BPESystemAdministrator
role. To map users or groups to the BPESystemAdministrator role, open the administrative console and
go to Enterprise Applications > BPEContainer\_... > Security role to user/group
mapping.

For more information about implementing security, see Creating a secure environment.