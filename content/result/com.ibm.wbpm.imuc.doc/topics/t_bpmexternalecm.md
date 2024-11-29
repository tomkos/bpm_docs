# Configuring Business Automation Workflow with a new external Content Platform Engine

You might be currently working with the BPM content store to store Enterprise
Content Manager (ECM) information in IBM® Business Automation
Workflow. But you might want
to work instead with a new external ECM system. You can configure Business Automation Workflow to work with a new
Content Platform Engine. This
configuration continues to use the existing domain and object store without migrating the data from
the BPM content store.

## About this task

You cannot reverse this configuration and return to using the BPM content store. Once configured,
you must always use the external Content Platform Engine.

To use an external server, the host name must have a domain name suffix, for example
MyDmgrHost.my\_domain.com.

In addition to the topics that explain the configuration, see Configuring Content Platform
Engine into a new application server instance with a new profile. Configuring with a
new profile, which is necessary for this configuration, is discussed. Details on the steps that
follow are also provided.

- Installing Content Platform Engine

Begin your configuration by installing Content Platform Engine.
- Preparing Business Automation Workflow for an external Content Platform Engine

Preparing IBM Business Automation Workflow for an external Content Platform Engine requires authentication and authorization updates.
- Configuring Content Platform Engine for the Business Automation Workflow content store

Content Platform Engine must be configured by using the FileNet Configuration Manager to work with the BPM content store (deprecated).
- Configuring single sign-on with LTPA for an external Content Platform Engine

To allow access to case information on an external ECM system for an IBM Business Automation Workflow user, you must configure cross-cell single sign-on (SSO) access control. Unless you are using User Management Service (UMS), use Lightweight Third-Party Authentication (LTPA). This configuration is for the Business Automation Workflow cell and the external Content Platform Engine cell. The configuration includes the configuration of the user registry and trusted realm.
- Configuring Business Automation Workflow to use the external Content Platform Engine

IBM Business Automation Workflow must be configured to allow the interaction between Business Automation Workflow and Content Platform Engine.