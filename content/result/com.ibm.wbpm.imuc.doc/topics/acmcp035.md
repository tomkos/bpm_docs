# Known limitations for IBM Enterprise Records

## Limitations

- You cannot declare
a record directly from IBM Business Automation
Workflow.
- There is no support for configuring a file plan object store as
a target object store or a source object store.
- You must configure
a single object store for both applications
as a place to store the source documents. You must create a single
object store and configure it as a target object store on IBM Business Automation
Workflow and as a record-enabled
object store (ROS) on IBM Enterprise Records.
- When a source document is declared as a record, the security of
the record is controlled by IBM Enterprise Records,
overriding any security settings in your case.
- You cannot
determine whether a source document has been declared
as a record from the IBM Business Automation
Workflow user
interface.
- To declare a document that is already attached to a case as record, you must search
for the document in IBM Content
Navigator and then declare it as a record
from the search results. You cannot browse for the document.Tip: If you use the
traditional IBM Enterprise Records client, search for the record in Workplace XT.