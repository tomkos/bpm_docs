# Process Portal
limitations

## Security certificates must be accepted before logging in to Process Portal

```
The webpage at https://localhost:3001/Watson%20Translation?locale=en\_US might be temporarily down or 
it may have moved permanently to a new web address.
```

The error occurs because you are using a self-signed SSL certificate, but have not configured the
browser to allow the certificate yet. To fix the issue, you must accept all the security
certificates from all the systems (Process Federated Server, Process Portal, and the back-end
Business Automation Workflow) before the
login. For each of these systems, open another tab in your browser, call the URL for that system,
and then, when prompted, accept the self-signed certificate from that system. Then, refresh the
first browser tab where the error occurred.

## Truncated data field names in the Customize your view dialog

Containers: 
When you configure saved views in Workplace, you might
notice truncated data field names in the Customize your view dialog. The field
names come from aliases, which are generated from the data item names and have a maximum length. It
can be expected that data field names that exceed the maximum alias length show up truncated in the
dialog.

## Users added through Team Bindings in the Process Admin Console are not listed in the Team
Performance roster

Containers: 
Users defined in a group and individual users that are added on the
Team Bindings page in the Process Admin Console are missing from the roster in
the Team Performance dashboard.

## Process Portal is not
listed as a system application in Process Center

In Business Automation Workflow V21.0.2,
in Process Center, you might notice that Process Portal (SYSRP) is no longer
listed by default as a system application under Process Apps. Reach out to
IBM Support for workaround instructions to have the Process Portal (SYSRP) system
application displayed in Process Center in Business Automation Workflow V21.0.2.

## Task modifications are not instantly reflected in the Process Portal task list

In a federated Process Portal, after you modify a
task and immediately query the task list, you might not see the expected update in the task list.
Task list queries are based on the Process Federation Server index. By
default, the index takes 2000 ms (milliseconds) to update, which is reflected in the slight delay in
updating the task list. Wait for the next auto-refresh or refresh the task list manually to see your
update. For more information, see The Process Federation Server REST APIs.

## Functional IDs are listed in the Team Performance roster

In a federated Process Portal with multiple Business Automation Workflow systems, functional IDs
are included in the roster section of the Team Performance dashboard, typically
listed as Automation System Account. To avoid getting an error when you click an Automation System
Account name from a different Business Automation Workflow system, ignore the
Automation System Account users in the Process Portal
Team Performance dashboard. If necessary, you can access the functional ID user
from the Teams page in Workplace instead. See Managing work for teams with the Team Performance dashboard .

## No Heritage Process Portal
support in Business Automation Workflow
deployments with PostgreSQL

Heritage Process Portal
(deprecated) is not supported in Business Automation Workflow deployments with a
PostgreSQL database.

## Browser restrictions

Process Portal works
differently on some browser versions. For a list of the supported browsers, see the Detailed system requirements for a specific product.

## All browsers

## Google Chrome