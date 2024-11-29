<!-- image -->

# Planning to configure Business
Process Choreographer

## About this task

## Procedure

1 Decide which configuration tool to use to create your deploymentenvironment:
    - If you want a default Business Process Choreographer configuration
that either uses the common database or a separate database, you can
use either the administrative console deployment environment wizard
or the BPMConfig command to create a network deployment
environment.
    - If you want a fully customized Business Process Choreographer
configuration, you must edit your requirements into a configuration
properties file and then run the BPMConfig command
to create your network deployment environment.
2 If you use the deployment environment wizard, decide whichdeployment environment pattern you want.

- Application, Remote Messaging, Remote Support
- Single Cluster
3 If you use the BPMConfig command tocreate your deployment environment, you must identify which propertiesfile to base your configuration on. The sample propertiesfiles are named according to the following format: product\_configuration -topology-environment\_type -database\_type . Tip: Thefollowing steps are intended only as a guide for creating a BusinessProcess Choreographer configuration. For more information about usingthe BPMConfig command, refer to BPMConfig command-line utility .

1. If you need to only run BPEL processes, you can use
one of the AdvancedOnly product configuration
properties files in the Install\_root/BPM/samples/config/advancedonly directory.
These configurations do not include support for BPMN processes, which
results in a smaller footprint.
2. If you need support for both BPMN processes and BPEL
processes, use one of the Advanced product configuration
properties files in the Install\_root/BPM/samples/config/advanced directory.
In this case, decide whether you are creating a Workflow Server (PS)
or Workflow Center (PC)
configuration.
3. Depending on your need for production performance, decide
between a single cluster (SingleCluster) or three
cluster (ThreeClusters) topology environment.
4. Identify which database system to use. For example, SQLServer, SQLServer-WinAuth, Oracle, DB2,
or DB2zOS.
5. Together, your choices for product configuration, topology
environment, and database type identify which properties file to copy
and, if necessary, customize. For example, Install\_root/BPM/samples/config/advancedonly/AdvancedOnly-ThreeClusters-DB2zOS.properties,
or Install\_root/BPM/samples/config/advanced/Advanced-PS-SingleCluster-Oracle.properties.
6. All the Advanced and AdvancedOnly configuration
files include a Business Process Choreographer configuration that
you can customize as necessary.
4 Ifyou do not have enough information or authority to create the wholeconfiguration on your own, consult and plan with the people who areresponsible for other parts of the system. For example:

- You might need to request information about your organization's
LDAP server, if it uses authentication you might need to request a
user ID, and authorization.
- If you are not authorized to create the database, your database
administrator (DBA) must be included in planning the databases. Your
DBA needs a copy of the database scripts to customize and run.
5. If you want the Human Task Manager to send email notifications
of escalation events, identify the host name or IP address where the
Simple Mail Transfer Protocol (SMTP) email server is located.
Plan what the sender address will be for email notifications.
If the email service requires authentication, make sure that you know
the user ID and password to use to connect to the service.
6 If you are going to use the Business ProcessChoreographer Explorer, Heritage Process Portal , ora client that uses the Representational State Transfer (REST) APIor the JAX web services API, decide on the context roots for the RESTAPI and the JAX web services API.

- The defaults for the Business Flow Manager are /rest/bpm/bfm and /BFMJAXWSAPI.
- The defaults for the Human Task Manager are /rest/bpm/htm and /HTMJAXWSAPI.

- When configured on a single cluster, or on multiple clusters that
are mapped to different web servers, you can use the default values.
- When configured in a network deployment environment on multiple
deployment targets that are mapped to the same web server, do not
use the default values. The context root for each Business Process
Choreographer configuration must be unique for each combination of
host name and port. You will have to set these values manually using
the administrative console after you have configured an environment
that includes Business Process Choreographer.
7. If you want to use people assignment, complete the steps
that are described in Planning for the people directory provider.