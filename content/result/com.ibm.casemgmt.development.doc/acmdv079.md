# Content Platform Engine add-on
extensions

Using the Content Platform Engine APIs,
you can extend some of the custom classes to develop a customized solution. These custom classes
include the Case Folder and Case Activity classes, which are basic solution components. Both the
Case Folder and Case Activity classes are abstract classes and must be subclassed for a solution.
Other classes, such as Deployed Solution, Deployed Case Type, and Case Comment, can be used as-is or
can be subclassed. All of these custom classes are enabled to support case history and
analytics.

- Querying for cases
- Creating a case
- Updating case properties
- Retrieving the metadata for case classes and document classes
- Adding a folder in a case folder
- Adding a document to a case

- Design object store extensions

The design object store extensions include metadata that is required for design object store functions. The extensions provide property templates and implement custom classes, instances, and properties.
- Target object store extensions

The target object store extensions provide metadata that is required for target object store functions. The extensions provide property templates and implement custom classes, instances, and properties.
- History and analytics extensions

The history and analytics extensions include metadata that configures Content Platform Engine for auditing of analytical and historical information by workflow client applications.
- Subscriptions and events

The subscriptions, event actions, and code module are deployed to the target object store. You can use IBM® Administration Console for Content Platform Engine to view the metadata.