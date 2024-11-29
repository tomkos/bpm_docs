# Troubleshooting and support for IBM Business Automation Workflow

Troubleshooting and support information
for IBM Business Automation Workflow helps
you understand, isolate, and resolve problems.

Troubleshooting
and support information contains instructions for using the problem-determination
resources that are provided with your IBM products.

To
resolve a problem on your own, you can find out how to identify the
source of a problem, how to gather diagnostic information, where to
get fixes, and which knowledge bases to search. If you need to contact IBM Support, you can find out what
diagnostic information the service technicians need to help you address
a problem.

Resources for troubleshooting IBM Business Automation Workflow include
a strategy for troubleshooting and diagnosing problems, a list of
error messages, specific troubleshooting documentation organized by
the tasks you are performing in IBM Business Automation Workflow, documentation
about tools that help you track and monitor errors in your deployed
applications, and links to technical support web sites.

Another troubleshooting resource is the IBM Community. Use the
forum to read or participate in technical discussions about the product with other customers.

- Overview of troubleshooting

Troubleshooting is a systematic approach to solving a problem. The goal is to determine why something does not work as expected and how to resolve the problem.
- Troubleshooting checklist for IBM Business Automation Workflow

Asking questions about hardware and software requirements, product fixes, specific problems, error messages, and diagnostic data can help you troubleshoot IBM Business Automation Workflow.
- Messages overview

When you receive a message from IBM Business Automation Workflow, you can often resolve the problem by reading the entire message text and the recovery actions that are associated with the message.
- IBM Business Automation Workflow log files

IBM Business Automation Workflow offers a comprehensive set of log files to help you identify and resolve problems during installation, configuration, and run time.
- Transaction log file

The transaction (tranlog) log file stores critical transactional data that is written to databases. It is an internal file that WebSphere® Application Server uses to manage in-flight transactions and attempt to recover them if the server locks up.
- Known limitations for translated Business Automation Workflow components

Consider the following known limitations for IBM Business Automation Workflow components translated into national languages.
- Troubleshooting installation and configuration

You can diagnose problems when the installation and configuration of IBM Business Automation Workflow is unsuccessful.
- Troubleshooting migration

If your deployment environment was not migrated successfully, you can take steps to resolve issues.
- Troubleshooting your deployment environment

When processing appears sluggish or requests fail, use a focused approach to determine the source of the problem in the environment. The approach described is for non-standalone server environments.
- Troubleshooting web services

If you have a problem using a web service, use the following troubleshooting resources.
- Troubleshooting high CPU loads on LDAP servers

In some situations, you may experience high CPU loads on a Lightweight Directory Access Protocol (LDAP) server connected to an Business Automation Workflow system. To help you identify the CPU-intensive requests, you can audit the information from the LDAP server. It is especially important to check the source IP address to identify the originator of the requests.
- Troubleshooting JVM issues

Best practices for troubleshooting JVM memory and CPU usage issues.
- Troubleshooting NIST SP800-131a environment configurations

If you are configuring IBM Business Automation Workflow to support the National Institute of Standards and Technology (NIST) SP800-131a security standard, you might observe one or more of the following configuration issues.
- Troubleshooting 100Custom configuration

The default values for the product with regard to teamworks configuration settings are set during installation. However, these values can be customized by the system administrator after installation. If there is a mistake in the 100custom.xml file, the customization is not applied and it is difficult to find where the problem is.
- Troubleshooting service module deployment failures

This topic describes the steps to take to determine the cause of a problem when deploying a service module. It also presents some possible solutions.
- Desktop Process Designer window is blank (deprecated)

After you log in to the desktop Process Designer, you might see a blank white desktop Process Designer window, a partially displayed view, or an HTTP error. Refresh your browser, or configure additional security in Internet Explorer V8 or V9.
- Logging into web Process Designer using a system ID may result in premature session timeout

If you log into web Process Designer using a system ID like "tw\_admin" or "deAdmin", your browser session may expire before the time limit set for the "LTPA timeout" parameter.
- On the Edge 42 browser, the process playback window blocks content

When using the Microsoft Edge 42 browser in an IBM Business Automation Workflow environment, the process playback window blocks content due to an invalid security certificate. The problem is restricted to processes in the process playback window and does not affect client-side human services.
- Existing Java integration implementations may throw exceptions when using the WebSphere Javamail library

In IBM Business Automation Workflow V18.0.0.1, a new Business Automation Workflow Javamail library was introduced to supplement the older WebSphere Javamail library. If you have an existing Java integration implementation that uses the older WebSphere Javamail library, the implementation may throw exceptions.
- Dashboards cannot be launched in some single sign-on environments

In some single sign-on environments that use a reverse proxy or a gateway server, the Business Automation Workflow dashboard does not render when you launch it. Instead, you see a blank screen. To resolve the problem, use the JVM custom property com.ibm.bpm.dashboard.whitelist to enable the custom dashboard allowlist.
- Troubleshooting a failure to access help topics

By default, IBM Business Automation Workflow is configured to access help topics from the online documentation. If you are working behind a firewall, you might find that links from the product to help files do not resolve. In that case, you need to either revise the proxy settings in the product or download and install the help contents to your local system.
- Troubleshooting problems in migrating a task to a new snapshot

During instance migration, the managers team information in a task is not migrated to a new snapshot if the managers team is provided by a team filter service that is specified in the task assignment. As a result, the snapshot deletion might be blocked.
- File Viewer overlaps Model dialog in Content Management Toolkit Views in Internet Explorer 11
- Troubleshooting on password match failed for the 'Admin' principal name

When the password entered does not match the password that is associated with the Admin principal name (reference CWWIM4513E), follow this topic for the workaround.
- Administration Console for Content Platform Engine is unable to get data from server

When you log in to the IBM Administration Console for Content Platform Engine, you see the message null serverName parameter is null or empty!
- Troubleshooting administration tasks and tools

Use the information in this group of topics to identify and resolve problems that can occur while you are administering the runtime environment.
- Troubleshooting runtime administration

If you encounter problems with your processes or resources during run time, use the information in these topics to help identify and resolve the issue.
- Troubleshooting WebSphere Application Server

Because IBM Business Automation Workflow is built on IBM WebSphere Application Server, the function that you are having problems with might be provided by the underlying WebSphere Application Server. You might want to consult troubleshooting information in the WebSphere Application Server documentation.
- Tools for troubleshooting your applications

IBM Business Automation Workflow and Integration Designer include several tools you can use to troubleshoot your applications that you develop and deploy on the server.
- Troubleshooting monitor models

These sections describe problems you might encounter while
you are using the Business Monitor development toolkit.
- Recovering from a failure

Recovering from a failure requires an understanding of standard system processing in the event of a failure, as well as an understanding of how to analyze problems that may be the cause of a failure.
- Disaster recovery

Disaster recovery consists of the policies and procedures that describe how to recover or continue the technology infrastructure critical to an organization after a natural or human-induced disaster.
- Searching knowledge bases

You can often find solutions to problems by searching IBM knowledge bases. Optimize your results by using available resources, support tools, and search methods.
- Getting fixes

A product fix might be available to resolve your problem.
- Contacting IBM Software Support

IBM Software Support provides assistance with product defects.