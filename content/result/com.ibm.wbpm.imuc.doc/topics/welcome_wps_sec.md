# Securing your environment

The security of IBM® Business Automation
Workflow
depends on securing the runtime environment and securing applications.

Application security is turned on by default in IBM Business Automation Workflow and
cannot be turned off.

IBM Business Automation Workflow security is based on the WebSphere® Application
Server
8.5 security. For detailed information, see the
documentation for WebSphere Application
Server Network Deployment.

- Configuring IBM Business Automation Workflow without a file-based user registry

 If your security policy does not allow user accounts to be stored in a file-based user repository, the default setup is not suitable for your requirements.
- Configuring the user registry

 To use an external security provider, you must add the provider to the federated repository. Only the federated repositories configuration is supported. All other types of repositories are deprecated, including the local operating system registry, stand-alone Lightweight Directory Access Protocol (LDAP) registry, and stand-alone custom registry.
- Security roles and groups

Look up reference information related to IBM Business Automation Workflow security roles and groups.
- Configuring multiple deployment environments

You can isolate multiple deployment environments within a single cell in your IBM Business Automation Workflow configuration.
- Configuring Business Automation Workflow endpoints to match your topology

If the user's browser requests pass through a web server or load-balancing server before the request reaches the Business Automation Workflow server, you must configure the virtual host information that is used by Business Automation Workflow to generate URLs.
- Configuring third-party authentication products

To use a third-party authentication product, you must customize various configuration settings.
- Security configuration properties

Use the WebSphere command-line administration tool (wsadmin) AdminConfig commands to access and modify IBM Business Automation Workflow security properties as configuration objects.
- Configuring Secure Sockets Layer (SSL) for IBM Business Automation Workflow

You can enable Secure Sockets Layer (SSL) communication for IBM Business Automation Workflow. This process enables secure https communication between the Process Center and the Workflow Server.
- Enabling a NIST SP800-131a compliant environment

You can configure IBM Business Automation Workflow to support the National Institute of Standards and Technology (NIST) SP800-131a security standard. SP800-131a requires longer key lengths and stronger cryptography than other standards, such as FIPS 140-2. SP800-131a requires Transport Layer Security (TLS) V1.2.
- Configuring cross-cell security for IBM Workflow Center

Before registering a Workflow Center with another Process Center in different cell, you must complete security configuration. Once the security configuration between the cells is completed, a Workflow Center in one cell can register a Workflow Center in another cell with HTTPS protocol over Secure Sockets Layer (SSL).
- Configuring administrative and application security

The first step in securing your IBM Business Automation Workflow environment and your applications is to make sure that administrative security is enabled.
- Configuring security for case management solutions

In both the development and the production environments, you configure security on the case management objects that are controlled by Content Platform Engine. You must also configure security on Content Platform Engine process services queues, rosters, and application spaces. For Case Client, you configure view and edit access to pages.
- Setting up security for the Business Space component and Heritage Process Portal

If you are using Heritage Process Portal with your environment, you must consider security options for the Business Space component. If you want to turn on security, set up application security and designate a user repository. To define administrators, assign a Business Space superuser role.
- Security in human tasks and BPEL processes

There are a number of roles associated with human tasks and BPEL processes. These roles are unique to tasks and processes that run in Business Process Choreographer.
- Securing access to timetables in the Business Calendars widget

The Security Roles widget provides you with the ability to secure access to individual timetables in the Business Calendars widget. You use the Security Roles widget to assign roles to the members of an organization. It is these roles that determine the level of access to the timetables.
- Storing WebSphere Application Server credentials

As part of WebSphere Application Server configuration, IBM Business Automation Workflow persists many credentials in authentication aliases.
- Security-hardening properties

IBM Business Automation Workflow provides configuration settings at the deployment environment level. This is to harden security that mitigates web application threats, including cross-site request forgery (CSRF), network sniffing, clickjacking, and uploading malicious documents.