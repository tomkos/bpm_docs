# Verifying the case applications in the development environment

## Procedure

To verify the case applications:

1 Log into the IBM Business AutomationWorkflow Case Client to check that the connections to therepositories are working correctly. If the error message The repository is notavailable is displayed for a repository, complete the following steps:
    1. Launch the IBM Content
Navigator
administration tool.
    2. In the client, click Repositories.
    3. Select the affected repository and click Edit.
    4. In the Protocol field, ensure that EJB is
specified.
    5. In the Server URL field, ensure that the correct server URL is specified
(and that it uses the EJB port and not the WSI port).
    6. Click Connect to test the connection. (If queried for your administrator
ID and password, specify them.)
    7. If the connection is successful, click Save and close.
    8. Log into the Case Client again to confirm that
the connection to the repositories are now working correctly and that the error message
The repository is not available is no longer displayed.
2. Verify the IBM Business Automation
Workflow API deployment by accessing the
following link from a browser:

Environment
Application URL

High availability
http://virtual\_server\_name/CaseManager/CASEREST/v1/info

Network deployment
http://server\_name:port/CaseManager/CASEREST/v1/info
3. Log in to the IBM Business Automation
Workflow
Case administration client by accessing the following link from
a browser:

Environment
Application URL

High availability
http://virtual\_server\_name.domain.com/navigator/?desktop=bawadmin

Network deployment
http://server\_name:port/navigator/?desktop=bawadmin
4. Log in to the Case Client by accessing the default IBM Business Automation
Workflow desktop from a browser:

Environment
Application URL

High availability
http://virtual\_server\_name.domain.com/navigator/?desktop=baw

Network deployment
http://server\_name:port/navigator/?desktop=baw

Verify that your specified Lightweight Directory Access Protocol (LDAP) users can log in to
the Case Client.
5. Click the help icon to test whether the Case Client help system displays
content.
6. Log in to the Case Builder by accessing the following link from
a browser:

Environment
Application URL

High availability
http://virtual\_server\_name/CaseBuilder

Network deployment
http://server\_name:port/CaseBuilder

Verify that your specified LDAP users can log in to the Case Builder.
7. Click the help icon to test whether the Case Builder help
system displays content.