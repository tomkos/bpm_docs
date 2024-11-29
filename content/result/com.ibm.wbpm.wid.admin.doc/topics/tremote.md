<!-- image -->

# Preparing for remote debugging

## Before you begin

## About this task

## Procedure

1 On your remote machine, open a command window and navigateto one of the following directories (where installDir is theinstallation path of standalone IBM Business AutomationWorkflow or IBM IntegrationDesigner ):
    - On standalone IBM Business Automation
Workflow (where profileName is
the name of the profile that you want to use for the server): installDir/profiles/profileName/bin
    - On IBM Integration
Designer: installDir/pf/wps/bin
2. Assuming that server1 is the name of your remote IBM Business Automation
Workflow server,
run the command startServer server1 on Windows or ./startServer.sh
server1 on Linux.
3. When the server has finished starting, open a browser window
and load the URL for the IBM Business Automation
Workflow administrative
console on the remote machine; for example, http://localhost:9060/ibm/console or http://remote\_host\_name:9060/ibm/console.
4. In the User ID and Password fields
of the administrative console Login page, specify your user ID and
password and then click Log in.
5 Ensure that the server starts up in debug mode by completingthe following steps:

1. In the left frame of the administrative console, expand Servers and
then click the Application Servers link. The
Application Servers page opens in the right frame.
2. In the Application Servers page, click the server1 link.
The server1 page opens.
3. Scroll down to the Additional Properties section and
click the Debugging Service link. The Debugging
Service page opens.
4. Ensure that the Enable service at server
startup check box is selected.
5. In the JVM debug port field,
type a port number of your choice. For example, 7777.
(On Linux, the value must be greater than 1024.)
6. In the JVM debug arguments field,
specify all of the following arguments (including the -Xj9 argument);
however, for the address argument, replace 7777 with whatever
port number you specified in the JVM debug port field: -Dcom.ibm.ws.classloader.j9enabled=true
-Xj9 -Xdebug -Xnoagent -Xrunjdwp:transport=dt\_socket,server=y,suspend=n,address=7777
7. Click Apply to save the changes
so that they are picked up the next time the server is started.
8. Click the Save link to save the
changes.
6 Disable the transaction timeout values by completing thefollowing steps:

1. In the left frame of the administrative console, click
the Application Servers link. The Application
Servers page opens in the right frame.
2. In the right frame, click the server1 link.
The server1 page opens.
3. Scroll down to the Container Settings section and expand Container
Services, then click the Transaction Service link.
The Transaction Service page opens.
4. In the Total transaction lifetime timeout field,
type 0 to indicate that there should be no
timeout.
5. In the Client inactivity timeout field,
type 0 to indicate that there should be no
timeout.
6. Click Apply.
7. Click the Save link to save the
changes.
7 For multiprocessor systems, you should know that othertransaction limits may impact performance. Any transaction limit witha nonzero value can cause a running component instance to time outif the debugging time exceeds the allocated resources. If you experiencetimeout problems in your distributed applications, disable the ORBtimeout values by completing the following steps:

1. In the left frame of the administrative console, click
the Application Servers link. The Application
Servers page opens in the right frame.
2. In the right frame, click the server1 link.
The server1 page opens.
3. Scroll down to the Container Settings section and expand Container
Services, then click the ORB Service link.
The ORB Service page opens.
4. In the Request timeout field,
type 0.
5. In the Locate request timeout field,
type 0.
6. Click Apply.
7. Click the Save link and then
click the Save button to save the changes.
8. At the top of the administrative console, click the Logout link
to log out of the administrative console.
9 On your local IBM IntegrationDesigner machine,complete the following steps:

1. Set the integration debugger timeout values by following
the instructions in the debugger topic "Changing timeout values".
2. Open the component that you want to debug in the component
editor, then right-click the first element in the component where
you can set a breakpoint and use the   menu to add a breakpoint
to the element. This will prevent the component instance from immediately
running to completion when it is started.
3. Create a server instance for your remote IBM Business Automation
Workflow by
following the instructions in the deployment topic "Creating test environment servers".
4. In the Servers view, ensure that the status of your
new server is Started. (If it is not started,
then start or restart IBM Business Automation
Workflow directly
on the remote machine.)
5. In the Servers view, right-click your new server and
select Restart > Debug to restart your remote IBM Business Automation
Workflow in
debug mode.
6. When you have finished restarting the server in Debug
mode, use the integration test client to both deploy your module to
the new server and create a running instance of a component for remote
debugging, much like you would for local debugging. This is described
in the debugger topic "Creating a component instance". (Alternatively,
you can manually deploy your module to the new server and then use
a different means of creating a running instance of a component for
debugging, such as a JSP.)