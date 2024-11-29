<!-- image -->

# Customizing Business Process
Choreographer

## Procedure

1. Optional: Verify that the basic
Business Process Choreographer configuration works: Perform Verifying that Business Process Choreographer works.
2. Optional: The Business Process Choreographer
configuration includes a Business Process Choreographer Explorer configuration.
To view or modify the Business Process Choreographer Explorer settings
using the administrative console, click Servers > Clusters > WebSphere application server clusters > cluster\_name,
then on the Configuration tab, in the Business Process Manager section, expand Business Process Choreographer, and click Business Process Choreographer Explorer.
3 If you want to the Human Task Managerto be able to send escalation emails, you must use the administrativeconsole to configure the settings for the Human Task Manager.
    - Set the email sender address and email URL link prefixes, click Servers > Clusters > WebSphere application server clusters > cluster\_name,
then on the Configuration tab, in the Business Process Manager section, expand Business Process Choreographer, and click Human Task Manager,
and complete the settings for the sender address and the prefixes
for link URLs that are included in escalation emails.
    - To set the email server address, port number, the user ID, and
password for the email server, click Resources > Mail > Mail sessions,
select Cell scope, then click HTM
mail session\_suffix, where suffix is
either node\_name\_server\_name or cluster\_name,
depending on where Business Process Choreographer is configured. Enter
your settings.
4 Set the context roots and endpoints.

1 If you will use the Business Process Choreographer Explorer,Business Process Archive Manager, the Business Space, or a clientthat uses the Representational State Transfer (REST) API, you mustchange the default context roots for the REST API so that they areunique for each combination of host name and port. Toset the context roots perform the following actions:
    1 To set the context roots for the Business Flow Manager, click Applications > Application Types > WebSphere enterprise applications then application \_suffix > Context Root for Web Modules ,where application is BPEContainer fora Business Process Choreographer configuration or BPArchiveMgr fora Business Process Archive Manager configuration, and suffix isthe name of the cluster where Business Process Choreographer or BusinessProcess Archive Manager is configured. Then make sure that the contextroots for the following web modules and are correct and unique.
        - BFMIF\_scopeWeb
        - BFMJAXWSAPI
        - BFMRESTAPI
2 To set the context roots for the Human Task Manager, click Applications > Application Types > WebSphere enterprise applications then application \_suffix > Context Root for Web Modules ,where application is TaskContainer fora Business Process Choreographer configuration or TaskArchiveMgr fora Business Process Archive Manager configuration, and suffix isthe name of the cluster where Business Process Choreographer is configured.Then make sure that the context roots for the following web modulesand are correct and unique.
    - HTMIF\_scopeWeb
    - HTMJAXWSAPI
    - HTMRESTAPI
3 To change the REST URLs that the Business Process ChoreographerExplorer uses: .

1. Click Servers > Clusters > WebSphere application server clusters >  cluster\_name . On the Configuration
tab, in the Business Process Manager section, expand Business
Process Choreographer and click Business Process
Choreographer Explorer.  Update the Business Flow Manager
and Human Task Manager REST API URLs.
2. Update the endpoints in config-rest.xml using a command similar
to the following example, which uses PS.AppTarget as
the cluster name:wsadmin>AdminTask.updateRESTServiceProvider(['-clusterName',  'PS.AppTarget', '-appName', 'BPEContainer\_PS.AppTarget', '-webModuleName','bfmrestapi.war', '-contextRoot', '/rest/bpm/bfmPS2/'])

wsadmin>AdminTask.updateRESTServiceProvider(['-clusterName',  'PS.AppTarget', '-appName', 'TaskContainer\_PS.AppTarget', '-webModuleName','taskrestapi.war', '-contextRoot', '/rest /bpm/htmPS2/'])
2 If you changed any of the context roots for the BusinessFlow Manager or Human Task Manager you must also modify the correspondingendpoints:

1. If you use the Business Process Choreographer Explorer or
Business Process Archive Explorer: Change
the REST endpoint to match the new context roots by clicking Servers > Clusters > WebSphere application server clusters > cluster\_name,
then on the Configuration tab, in the Business Process Manager section, expand Business Process Choreographer, and click Business Process Choreographer Explorer, select
the BPCExplorer\_scope or BPCArchiveExplorer\_scope instance
that you want to modify, and set the new value. For example,
if the context root for the Business Flow Manager REST API is /rest/bpm/bfm then
the full URL might be something like http://system7.mycompany.com:9080/rest/bpm/bfm.Note: If you
mapped the modules to an HTTP server, proxy server, IP sprayer, load
balancer, or similar server, the URL should be based on the hostname
and port number for that server.
2. If you use the Business Space: Change
the REST endpoints to match the new context roots by clicking Servers > Clusters > WebSphere application server clusters > cluster\_name,
then on the Configuration tab, in the Business Process Manager section, expand Business Process Choreographer,
and either Business Flow Manager or Human
Task Manager, then under Additional Properties click REST
Service Endpoint, and set the new value.Note: If
you mapped the modules to an HTTP server, proxy server, IP sprayer,
load balancer, or similar server, the URL should be based on the hostname
and port number for that server.
5. Optional: Update your virtual host configuration. By
default, the web modules of the Business Process Choreographer applications are configured for the
default\_host virtual host. Make sure that the ports associated with the host alias
are correct.  You might need to add host aliases for the host names and ports of
additional cluster members or for the web server that is used. For more details about virtual hosts,
refer to Virtual hosts.
6 Depending on the typeof people directory provider that you use for people assignment, youmight need to configure it:

- The system and user registry people directory providers can be
used without configuring them.
- If you are using Lightweight Directory Access Protocol (LDAP),
perform Configuring the LDAP people directory provider.
- If you are using the Virtual Member Manager (VMM), perform Configuring the Virtual Member Manager people directory provider.
7. Optional: If you configured
VMM, and you want to use people substitution, perform Configuring people substitution.
8. Optional: If you
want to use group work items, use the administrative console to enable
them. Click Servers > Clusters > WebSphere application server clusters > cluster\_name,
then on the Configuration tab, in the Business Process Manager section, expand Business Process Choreographer, and click Human Task Manager,
then select Enable group work items.
9. If you have WebSphere® application
security enabled and you have a long-running process that calls a
remote EJB method, make sure that your Common Secure Interoperability
Version 2 (CSIv2)  inbound authentication configuration has CSIv2
identity assertion enabled. For
more information about this, refer to Configuring Common Secure Interoperability Version
2 inbound communications.

## Results

- Configuring the people directory provider

Business Process Choreographer can use one of four people directory providers to determine who can start processes or claim activities or tasks. Two providers can be used in their default configurations (Local operating system user registry, WebSphere Application Server user registry). The Virtual Member Manager and LDAP people directory providers can usually be used in its default configuration, but in some cases, it must be configured.
- Configuring people substitution

This topic describes how to configure people substitution for Business Process Choreographer.
- Verifying that Business Process Choreographer works

Run the Business Process Choreographer installation verification application.

## Related tasks

- Configuring Business Process Archive Manager

## Related information

- Business Process Choreographer overview
- Troubleshooting the Business Process Choreographer configuration