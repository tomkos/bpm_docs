# Developing GDPR-ready process applications

## What personal data will be persisted?

If
you are developing a process application that handles personal data,
be aware that personal data stored in certain programming artifacts
are persisted. For example, parameters, variables, environment variables,
and process attachments are stored in the BPM database and caches.
When completed process instances and task instances are deleted the
personal data that is associated with those instances is deleted.
Use caution when using tracking events to avoid exposing personal
data, the same is true when using document attachments.

## Strategies for mitigating personal
data retention

You might need to consider
using an API to store all personal data in a separate data store in
a format like (data\_key, person\_key, field\_name, encrypted\_value),
so that BPM process applications only pass keys or encrypted data
rather than passing the data itself. When applications actually need
the unencrypted data, they must call an API to access the unencrypted
personal data. This approach would prevent unencrypted personal data
from being written to the BPM database, logging, and trace information.
By creating a centralized, encrypted store where all personal data
is stored, it will simplify implementing GDPR compliance actions such
as being able to retrieve all personal data about a particular individual,
and deleting or anonymizing their personal data.

## Protect sensitive
data in applications that contain human services

To protect
sensitive personal information, give special attention to BPM applications
that contain either client-side human services or heritage human services. 
Any
data provided in the input or output variables of the human service
is sent to the client browser. Also, all the incoming and outgoing
data from Ajax services or service flows with Ajax access is made
available on the client browser. In both cases, even though the information
is not visualized in the user interface, users can still access the
data through widely available debugging tools. For example, say you
have an application that has an Account business
object that has several properties, such as an email address, phone
number, and name. If you want the application to display the name
in a user interface but prevent the email address and phone number
from being exposed through the user interface, ensure that the input
variable for the human service does not include the Account business
object. If you use the Account business object
in its entirety as an input variable, all the authenticated users
of the human service will be able to view all the data specified in
the Account business object. To minimize the
risk of exposing sensitive data, use just the name as an input variable,
with the data being extracted in the mapping of the process task.

## Secure your BPM applications

- For more information about securing your applications, see Application security.
- For information about securing processes and tasks, see Authorization control for runtime REST API calls, which uses teams as described
in Creating a team.

<!-- image -->

## Protect personal data
in applications that contain BPEL processes

- Parameters, process variables, business objects, and environment
variables are stored in the BPM database and caches.
- SCA supports synchronous and asynchronous invocation of modules.
In a synchronous invocation, variables and business objects are not
persisted. In an asynchronous invocation, variables and business objects
are temporarily persisted in a queue and deleted after successful
completion of the invocation.
- If you enable events to be logged in the audit trail, the audit
log events are persisted in the audit trail tables of the BPM database.
- If you enable Common Event Infrastructure or Dynamic Event Framework
events to be emitted, these events are persisted.

- For a process template, setting the Automatically delete
the BPEL process after completion attribute causes process
instances to be deleted automatically when they complete.
- For a human task, setting the Auto deletion mode property
and the Duration until property cause human tasks
to be deleted automatically when they complete.
- If a problem occurs while processing a process instance or a human
task, the instance or the task is moved to the retention queue or
hold queue. The variables and business objects associated with the
message are also persisted in the queue. To remove a message from
a queue, use either the administrative console or scripting. The variables
and business objects remain persisted in the queue until you remove
the corresponding message.
- If a problem occurs while processing an SCA request or response
message, a failed SCA event is created. The variables and business
objects associated with the failed event are stored in the failed
event database. The data remains in the failed event database until
you successfully handle the failed event.