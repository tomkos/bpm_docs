# Reimporting assets with content that contains environment-specific references

In IBM®
FileNet® Content Manager, a
document object's properties can be modified with a reimport, but the content elements cannot.
Solution application artifacts, such as pages that include a website widget or workflow definitions
that include URL references, might be affected. Similarly, if non-workflow assets that are
represented as documents with content are reimported into the same object store multiple times by
using FileNet Deployment
Manager, modifications
to environment-specific information by the FileNet Deployment
Manager data conversion feature might
not appear in the target system. This can occur with solution application artifacts such as form
templates and workflow definitions that include URL references.

- From the destination design object store, staging object store,
or target object store, delete the current version of the document
prior to the reimport. Deleting this version causes the document version
to be created, rather than modified, by the reimport.
- If the current document version cannot be deleted prior to the
reimport, modify the content manually by using the appropriate tools
in the destination object store after the reimport completes.

To find the current version of a document, use the IBM Administration Console for
Content Platform Engine to navigate to the destination
object store and browse to find the solution folder or the folder
that contains the asset. Locate the desired document and use the versions tab
on its details pane to view the versions.