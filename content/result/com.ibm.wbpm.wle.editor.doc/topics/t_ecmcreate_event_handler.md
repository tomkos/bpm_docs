# Creating an event handler for an Enterprise Content Management
system

## About this task

- If you use IBM
FileNet® Content Manager, you do not need to write your own event handler, you only need
to perform the actions described in Using the event handler for FileNet Content Manager.
- If you do not use FileNet Content
Manager you must write your own event handler for your ECM system. Familiarize
yourself with your ECM system and its framework for implementing and
configuring an event handler. Plan for the specific requirements of
your ECM system.

## Procedure

1. Identify which ECM events you need your event handler to
support.  The following table lists the Business Automation Workflow
names for the ECM events that are supported by Business Automation Workflow.
Table 1. ECM events supported by Business Automation Workflow

Supported ECM events
Object types that the event can apply to

CheckedIn
Document

CheckedOut
Document

CheckOutCanceled
Document

ClassChanged
Folder or Document

ClassifyCompleted
Document

Created
Folder or Document

Deleted
Folder or Document

Filed
Folder

Frozen
Document

Locked
Folder or Document

PublishCompleted
Document

PublishRequested
Document

SecurityUpdated
Folder or Document

StateChanged
Document

Unfiled
Folder

Unlocked
Folder or Document

Updated
Folder or Document

VersionDemoted
Document

VersionPromoted
Document

Tip: For more details about the event types, refer to the REST API ECM event
resource reference topic.
2. For each event that you need notifications of, identify
the corresponding event name that is used by your ECM system.
3. Plan how your ECM event handler will obtain the information
required to connect to the Business Automation Workflow system. 
For example, the FileNet Content
Manager event handler, BPMEventHandler, loads the connection
information defined in a properties file that is stored in FileNet Content
Manager.
4. Plan your code to receive event notifications in your ECM
system and translate them into the corresponding calls to the appropriate Business Automation Workflow system.
For example, in the FileNet Content
Manager event handler BPMEventHandler, the BPMEventType method translates the FileNet Content
Manager event types to the corresponding Business Automation Workflow event
notification API method names.
5. Write your event handler according to your requirements
and the event handling framework provided by your ECM system.
Refer to the documentation for your ECM system.
6. Deploy and configure your event handler on your ECM system.
7. Verify that your event handler is called for the required
events, and that it transmits the events to the appropriate Business Automation Workflow server.
8. Verify that you can create an Business Automation Workflow process that receives the event notifications from your ECM system. Perform Subscribing to document and folder events.