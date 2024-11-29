# Authentication scenarios

The workflow system and the Enterprise Content Management system are separate systems. If shared
security is not configured, the workflow system does not recognize Enterprise Content Management
users and vice versa. Being authenticated on one system does not mean that a user or user group is
also authenticated on the other system. Consider the way you want to share Enterprise Content
Management information with workflow users before you design your application.

In some scenarios, you want to project the user identity of the currently acting human user from
the workflow system to the ECM system. This approach allows users to create and access private
documents, provides records for audits, and allows fine-grained access control on the Enterprise
Content Management server. In other scenarios, the actual user identity of the human user in the
workflow system does not matter in the Enterprise Content Management system. In such cases, it might
be enough to use a static system identity that represents the workflow system. For example, the
process might generate public documents or perhaps all workflow users need to see the same
collection of documents in a user interface.

When you configure access to an Enterprise Content Management server in the designer, you set a
user ID and password (see the related links for more information about this task). If you use the
default setting, the ID and password do not need to be valid on the workflow system, but they must
be valid for the Enterprise Content Management server. At the end of the settings, there is a check
box labeled Always use connection information specified here. When that check
box is selected, which it is by default, that user ID and password are attached to all calls made
from that process application to the ECM server. The advantage of this method is that the Enterprise Content
Management server is immediately available for use by the actions in the process application. However, do not use this
option if you want to restrict which documents or folders individual users can see and use. Using
this method, a static user name and password as defined in the process
application settings is the only credential that
can be submitted from the workflow system to the Enterprise Content Management server. There is no
way of telling the ECM system who the current "real" user is. Therefore, even if you set up single
sign-on (SSO), there is no way of fine-grained access control and gathering auditing data by
individual user.

1. The option "Always use this connection information" is checked.
2. A service credential in the SaaS tenant is created and specified. For more
information on how to create a service credential in the SaaS tenant, see:
 Creating and managing service accounts.
3. The newly created service credential in the SaaS tenant is given the
appropriate roles and permissions. For more information on how to assign roles and permissions for
the service credential, see:  Assigning roles and permissions.

Clear the Always use connection information specified here check box if
you want to restrict which documents or folders individual users or specific user groups can see and
use. When that check box is clear, the workflow system uses individual user names and IDs for
authentication and projects the identity to the Enterprise Content Management server. Now you can
assign specific tasks to users who can see only the documents and folders that they need to complete
those tasks. A service that is started by a user task in a process runs under the security context
of the user who claimed and started the task.

You can design a process to use both authentication methods, depending on the context. If the
Always use connection information specified here check box is not
selected, authorization depends on how you model your process. By choosing the context from
which the call is made, you can restrict access to the Enterprise Content Management server to a
user ID specified in the process application server settings or to a task owner. If the Enterprise Content Management
service is called by a system task in a process, the user that is identified in the process application settings
is used. If the Enterprise Content Management service is called by a human task, by a coach, or by
an integration service within a user task, the task owner identity is propagated to the ECM system.
In this latter case, the user ID and password set on the process
application are ignored. Calls that use the task
owner identity fail if the workflow and ECM systems do not have shared security.