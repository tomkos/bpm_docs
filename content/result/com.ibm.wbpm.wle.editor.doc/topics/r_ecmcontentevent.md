# The ECMContentEvent business object

When an event subscription is triggered, an ECMContentEvent business object is passed to the
service that is attached to the event subscription. The ECMContentEvent business object can contain
related data such as a document or folder that is added or removed from the base folder. In addition
to the data included in the ECMContentEvent business object, you can use a content integration step
in the service to retrieve more information about the object in the ECM server, such as additional
properties for the specified document or folder.

The
properties for the ECMContentEvent business object are described in
the following list:

- String serverName: The name of the ECM
server.
- ECMID repositoryId: The object ID of the
repository.
- ECMEventClass eventClass: The class of
the event, which is either "document" or "folder".
- ECMID objectTypeId: The object ID of the
folder type or the document type.
- ECMEventType eventType: The type of event
that occurred on the folder or document.
- ECMID objectId: The object ID of the folder
or document on which the event occurred.
- ECMEventClass relatedObjectClass: The class of a related event, which is
either Document or Folder.
- ECMID relatedObjectTypeId: The object ID of the related folder type or
document type.
- ECMID relatedObjectId: The object ID of the related folder or
document.