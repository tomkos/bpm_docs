# Verifying the IBM Business Automation
Workflow applications
in the production environment

## Procedure

To verify the IBM Business Automation
Workflow
applications:

1. Verify the IBM Business Automation
Workflow API
deployment by accessing the following link from a browser:

Environment
Application URL

High availability
http://virtual\_server\_name/CaseManager/CASEREST/v1/info

Network deployment
http://server\_name:port/CaseManager/CASEREST/v1/info
2. Log in to the IBM Business Automation
Workflow administration
client by accessing the following link from a browser:

Environment
Application URL

High availability
http://virtual\_server\_name.domain.com/navigator/?desktop=bawadmin

Network deployment
http://server\_name:port/navigator/?desktop=bawadmin
3. Log in to the Case Client by
accessing the default IBM Business Automation
Workflow desktop
from a browser:

Environment
Application URL

High availability
http://virtual\_server\_name.domain.com/navigator/?desktop=baw

Network deployment
http://server\_name:port/navigator/?desktop=baw

Verify that your specified Lightweight Directory Access Protocol
(LDAP) users can log in to the Case Client.
4. Click the help icon to test whether the Case Client help system displays
content.