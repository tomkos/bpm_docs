# Controlling authenticated user access to internal service types

## About this task

If
you want to accept the default behavior and prevent authenticated
users from invoking internal service types, you can still start human
services that are exposed to the logged-on user and also start AJAX
Services. However, you cannot start other services unless all of the
following requirements are met:

- The request is processed on Workflow Center.
- The request was issued by Process Designer in
a playback session.
- The user who issues the request is a member of the tw\_authors group.
- The user who issues the request is granted Read access
to the process application.

If there are any failing services, you should review them
to ensure that they are exposed as a URL and exposed to the current
user. If you need to revert to the old behavior while you fix your
applications, you can permit all authenticated users to invoke internal
service types by completing the steps in the following procedure:

## Procedure

1. Stop the server for IBM® Workflow
Server or Workflow Center.
2. Open each 100Custom.xml file. For
information about the individual 100Custom.xml files
that need to be updated and their locations, see the topic Location of 100Custom configuration files.
3. In each 100Custom.xml file, add the enforce-correct-service-type-for-execute-service-by-name setting
and associated elements under the <properties> element,
as shown in the following example: <server>
   <web-workflow-manager>
      <enforce-correct-service-type-for-execute-service-by-name merge="replace">false</enforce-correct-service-type-for-execute-service-by-name>
   </web-workflow-manager>
</server>(If
you want, you can later change the value to true to prevent authenticated
users from invoking internal service types.)
4. In each 100Custom.xml file, save your
changes.
5. In a browser, open each 100Custom.xml file
to ensure that it contains no special characters.
6 Complete one of the following steps:
    - In a clustered environment, ensure that the changes are propagated
to the nodes by forcing a synchronization and restarting the deployment
environment.
    - In a stand-alone server environment, restart the server.