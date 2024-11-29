# Integrating with IBM Enterprise Records

## About this task

- Documents in a case can be declared as records. The record is stored in the IBM Enterprise Records file plan object store.Important: When you manually
declare a record from the search results in IBM Content
Navigator and this
document is already attached to a case, you must search for the document and declare it as a record
from the search results. You cannot browse for the document.
- A source document that was declared as a record can be added to
a case because the record object store on the IBM Enterprise Records system is also configured
as the target object store on the IBM Business Automation
Workflow system.
- The IBM Enterprise Records and IBM Business Automation
Workflow applications can exist
on the same application server. However, coexistence is not required.
- The IBM Enterprise Records system
and the IBM Business Automation
Workflow system
must use the same object store.
- When you configure your IBM Enterprise Records system
and your IBM Business Automation
Workflow system
at the same time and connect to the same object store, all documents
that are added to the target object store can be declared as records.

## Procedure

To integrate IBM Enterprise Records with IBM Business Automation
Workflow:

1. Install and configure IBM Business Automation
Workflow.
2. Install and configure IBM Enterprise Records.
3. Create an object store that is configured as both a target
object store and a record object store.
4. Optional: 
Declare source documents in your cases on IBM Business Automation
Workflow as
records from the search results in IBM Content
Navigator.

- Known limitations for IBM Enterprise Records

Integrating IBM Business Automation Workflow with IBM Enterprise Records has several limitations.

## Related information

- IBM Enterprise Records Installation
and Upgrade
- Creating the IBM Enterprise Records Object store configuration
profile and running the profile tasks
- Declare records