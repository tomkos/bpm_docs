# Document start event

A document start event simplifies the starting
of a process that uses information from an ECM system.

You
can use a document start event to automatically start a process when
a document is created in an Enterprise Content Management (ECM) system.

Alternatively, you can use a document start event to launch a process
instance from an existing document in an ECM system.

## Why you would use a document start event

Enterprise
Content Management (ECM) systems store large amounts of information
for organizations. That information is in the form of documents like
reports, legal documents, invoices and proposals. In addition, ECM
systems perform tasks to manage those documents, such as determining
whether individual documents can be updated or deleted.

You
can use a document start event to automatically start a process when
a new document is created. This is useful when the process is associated
with a specific type of document, such as an insurance claim. For
example, a process might have a set of activities that are used for
an insurance claim investigation. The process can be automatically
started by the document start event as soon as an insurance claim
is submitted.

You can also use a document start event to launch a process instance from an existing document.
This is useful when you need to perform certain operations that are associated with the document,
such as having a team review it. For example, to enable a team to review the document, the process
would define an appropriate set of parallel or sequential tasks. You could then launch the process
from the document to initiate the team review. Currently, you can only launch a process this way by
using the Start Process REST API.

## How to create a document start event

1. In a process definition, select an existing Start Event icon or add a
Document Start Event icon from the palette.
2. In the Properties view, open the General tab.
3. In the Start Event section, ensure that Document
is selected.
4 In the Event Properties section, complete the following steps:
    1. In the Trigger button group, select
Document created to automatically start a process when a new document is
created or select Launched from document to launch a process instance from an
existing document. Note: To start a process from a document start event using a Launched
from document trigger, the process needs to be exposed to start. Also, a process can
only contain a maximum of one document start event with a Launched from
document trigger.
    2. In the Source drop-down list, select a server. The servers in the list
are the ECM servers that are listed in the Process Application Settings page
of your process application.
    3. In the Type drop-down list, select a document type. The document types
that are shown are the document types available in the source.
    4. If you want to include the document subtypes, select Include subtypes.
For example, a medical document type might contain a dental subtype that you want included.
5. Open the Data Mapping tab and map the document type properties to your
process variables. You can also select the + to show the additional technical
properties that you might also want to map. For example, you might select a property that indicates
who created the document and map that property to a process variable.
6. Click Save or Finish Editing.

The process is started in the default snapshot of a process application. In
Workflow Center, the tip is the default snapshot
unless another snapshot was explicitly configured to be the default. If the process is defined in a
toolkit, it is started only if a snapshot of that toolkit is referenced by a process application. If
multiple process applications reference the same toolkit that contains a process with a starting
document, multiple process instances are started.

A document start event that is configured to run when a document is created will not trigger for
the current (tip) snapshot of a toolkit application. This is because the engine looks at the current
(tip) snapshots of process applications and will not find artifacts in orphaned toolkits. To test
the event, your process application should include a snapshot of the toolkit that contains the event
definition.

## The JavaScript starting document system variable

The
identifier of the starting document is available in a JavaScript system
variable. For processes and server-side services, use tw.system.currentProcessInstance.startingDocumentId to
return the identifier. You can also use tw.system.currentProcessInstance.startingDocumentServerName to
return the server name of the document. You can use this identifier
and server name in activities, such as with Enterprise Content Management
operations.

For client-side human services, use tw.system.processInstance.startingDocumentId to
return the identifier. Use tw.system.processInstance.startingDocumentServerName to
return the server name of the document.