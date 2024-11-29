<!-- image -->

# Deploying a generated client to a test environment

## About this task

## Procedure

1. Click the Server tab in the properties
view.  If this is not open yet, then click Window >  Show View > Servers.
2. Right-click the server that you intend to deploy your client
to and select Add and Remove Projects from
the list.
3. In the Add and Remove Projects window,
select the generated Client EAR project that you created, and click Add.
4. Click Finish.
5 Invoke the client. You can start the clientin either of the following ways:
    1 With an external browser:
        - If the security is disabled, go to: http://localhost:9080/webProjectName (the
hostname and port number might vary depending on your server configuration).
        - If the security is enabled, go to https://localhost:9443/webProjectName.
2 Using IBM® IntegrationDesigner : A browser window opens.
    1. Change to the Web perspective
    2. Open the folder with the name of your web project, and then open
the folder WebContent.
    3. Right-click Index.jsp, and select Run > Run on Server