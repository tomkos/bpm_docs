# Adding an IBM Business Automation
Workflow server
(deprecated)

## About this task

To add a server, follow these steps.

## Procedure

1. Select the Servers tab from the Process App Settings editor. You will see the Process App Settings editor when you first click Open in Designer from a newly created process application
in the Workflow Center. Alternately you can select Process App Settings from the drop-down list on the toolbar in Process Designer.
2. Beneath the Servers heading click Add. Beneath the Server Details heading, enter a meaningful name for server. From the drop-down
list in the Type field, select IBM
Case Manager Server. Enter a description of what the server
does or provides in the Description field.
3 Beneath the Server Locations heading,enter the following information.
    - Environment Type : The environment of the IBM Business AutomationWorkflow server.Enter the server location information (hostname, port, if it willbe a secure service, target object store, connection userid and password)for each environment type. If you do not provide values for theseenvironments, the values from the default environment type will beused.
        - Default: A set of default values that are
used if you do not provide values for the following environment types.
        - Development: The environment where you
develop your services.
        - Test: The environment where you test your
services.
        - Staging: The environment where you deploy
your services for pre-production testing.
        - Production: The environment where your
services are deployed for use by your organization.
- Hostname: The hostname of the IBM Business Automation
Workflow server.
Specify an IP address or a hostname and domain (but do not specify http:// or another protocol). For example:myHost.labwide.ibm.com
- Port: The port number of the IBM Business Automation
Workflow server.
- Secure: Select if you want your service
to be secure, that is, use the Hypertext Transfer Protocol Secure
(HTTPS) protocol. If you are accessing a server using SSL security,
see Accessing an IBM Business Automation Workflow server using the Secure Sockets Layer (SSL) (deprecated).
- Target Object Store: The target object
store name for the IBM Business Automation
Workflow server.
A target object store is used to store runtime case solutions. If
you do not know the name, you should be able to get it from the IBM Business Automation
Workflow server
administrator.
- Connection Userid: The userid for connecting
to the IBM Business Automation
Workflow server.
- Password: The password of the userid connecting
to the IBM Business Automation
Workflow server.
4. Save your work. From the menu, select File > Save All.