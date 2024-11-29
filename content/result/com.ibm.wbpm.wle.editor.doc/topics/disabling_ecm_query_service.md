# Disabling the ECM Query Authorization Service

## About this task

This configuration disables the default mandatory requirement to validate the CMIS query for all
process applications. This is meant to avoid breaking existing process applications during a
transition period, in which new snapshots that include the ECM Query Authorization
Service for ECM server with static credentials are developed.

## Procedure

1. Add the following configuration settings to the 100Custom.xml file
in IBM® Workflow
Center or
IBM IBM Workflow
Server. 
Note: Disabling the authorization service can lead to security vulnerabilities.
<server>
<!-- enable/disable the enable query authorization security service . This is enabled by default (true) and can be disabled by setting it to false -->
<enable-query-authorization-security-service merge="replace">false</enable-query-authorization-security-service>
</server>
2 To enable or disable the ECM Query Authorization SecurityService , perform one of the following options:
    - For external ECM Server definitions within your process applications and toolkits, clear the
Always use this connection information option, which causes IBM Business Automation
Workflow (IBM BPM) to
propagate each user's context to the ECM server.
Not all ECM systems can share security context with Business Automation Workflow. To determine whether you
can use this option, see Authentication scenarios.
    - For external ECM Server definitions within your process applications and toolkits that has
the Always use this connection information option enabled, create a service
that helps in validating the CMIS query. Then, associate this service with the ECM server
definition. One could create unique service per each ECM server definition, that can contain
validation logic for that ECM server, or could create a single service that can have validation
logic per each ECM server.
3 Open the settings page for a process application or toolkit that contains an ECM serverdefinition, and go to the Servers tab. Select the ECMserver from the list, and scroll to the ECM Query Authorization Service property. Thenselect New to generate an empty service with the proper interface, or selectan existing service. The interface for this service must have the following signature in the Variables tab: Input parameters Output parameter

The interface for this service must have the following signature in the Variables tab:

- inCmisQuery (String)
- servername (String)
- serverName (String)

- outCmisQuery (Boolean)
4. Define the logic that uses one or more of the input parameters to help in validating the
incoming CMIS query for the respective server. The service must return a validated
CMIS query.
5. Click Save or Finish Editing.
6. Run a test to confirm the authorization logic that you developed is working as you
expect.
7. Create a snapshot for your changes when you are ready to deploy them.