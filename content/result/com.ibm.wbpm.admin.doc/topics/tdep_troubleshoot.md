# Troubleshooting service module deployment failures

## Before you begin

- You have a basic understanding of debugging a module.
- Logging and tracing is active while the module is being deployed.

## About this task

## Procedure

1 Determine if the application installation failed. Examinethe SystemOut.log file for messages that specifythe cause of failure. Some of the reasons an application might notinstall include the following: Important: If the installationhas failed and the application contains services, you must removeany SIBus destinations or JCA activation specifications created beforethe failure before attempting to reinstall the application. The simplestway to remove these artifacts is to click Save > Discardall after the failure. If you inadvertently save the changes,you must manually remove the SIBus destinations and JCA activationspecifications (see Deleting SIBus destinations and Deleting JCA activationspecifications).
    - You are attempting to install an application on multiple servers
in the same Network Deployment cell.
    - An application has the same name as an existing module on the
Network Deployment cell to which you are installing the application.
    - You are attempting to deploy Java EE modules within an EAR file
to different target servers.
2 If the application is installed correctly, examine it todetermine if it started successfully. If the applicationdid not start successfully, the failure occurred when the server attemptedto initiate the resources for the application.

If the application
did not start successfully, the failure occurred when the server attempted
to initiate the resources for the application.

1. Examine the SystemOut.log file
for messages that will direct you on how to proceed.
2 Determine if resourcesrequired by the application are available or have started successfully. Resources that are not started prevent an application fromrunning. This protects against lost information. The reasons for aresource not starting include:
    - Bindings are specified incorrectly
    - Resources are not configured correctly
    - Resources are not included in the resource archive (RAR) file
    - Web resources not included in the web services archive (WAR) file
3. Determine if any components are missing. 
The reason for missing a component is an incorrectly built enterprise
archive (EAR) file. Make sure that the all of the components required
by the module are in the correct folders on the test system on which
you built the Java™ archive (JAR) file. Preparing
to deploy to a server contains additional information.
3 Examine the application to see if there is informationflowing through it. Even a running application can failto process information. Reasons for this are similar to those mentionedin step 2.b .

Even a running application can fail
to process information. Reasons for this are similar to those mentioned
in step 2.b.

1. Determine if the application uses any services contained
in another application. Make sure that the other application
is installed and has started successfully.
2. Determine if the import and export bindings for devices
contained in other applications used by the failing application are
configured correctly. Use the administrative console to
examine and correct the bindings.
4. Correct the problem and restart the application.

- Deleting JCA activation specifications

The system builds JCA application specifications when installing an application that contains services. There are occasions when you must delete these specifications before reinstalling the application.
- Deleting SIBus destinations

Service integration bus (SIBus) destinations are used to hold messages being processed by SCA modules. If a problem occurs, you might have to remove bus destinations to resolve the problem.